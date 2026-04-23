import os
from pathlib import Path

# Tool-specific imports
from tavily import TavilyClient
from langchain.tools import tool
from langchain_classic.agents import (
    AgentExecutor,
    create_tool_calling_agent,
    tool,
)
from langchain_core.prompts import ChatPromptTemplate
# from langchain.pydantic_v1 import BaseModel, Field  # Note: if this throws an error, use `from pydantic import BaseModel, Field`
from pydantic import BaseModel, Field

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

from src.bm25 import BM25Search
from src.semantic import SemanticSearch
from src.hybrid import HybridSearch

TOP_K = 10

# ---------------------------------------------------------
# Tool Definition
# ---------------------------------------------------------
class WebSearchInput(BaseModel):
    query: str = Field(description="The specific search term or question to look up on the internet.")


@tool(args_schema=WebSearchInput)
def web_search(query: str) -> str:
    """
    Search the web for current, up-to-date information about an Amazon product.
    Use this tool ONLY when the provided context does not contain enough information
    to answer the user's question, such as current market pricing, recent news, 
    competitor comparisons, or updated technical specifications.
    """
    tavily_api_key = os.getenv("TAVILY_API_KEY")
    if not tavily_api_key:
        return "Error: TAVILY_API_KEY is not set."
        
    tavily_client = TavilyClient(api_key=tavily_api_key)
    # hardcode max_results here to simplify the LLM's job
    results = tavily_client.search(query, max_results=5) 
    snippets = [r["content"] for r in results.get("results", [])]
    return "\n".join(snippets)

# @tool
# def web_search(query: str, max_results: int = 3) -> str:
#     """
#     Search the web for current, up-to-date information about an Amazon product.
#     Use this tool ONLY when the provided context does not contain enough information
#     to answer the user's question, such as current market pricing, recent news, 
#     competitor comparisons, or updated technical specifications.
#     """
#     tavily_api_key = os.getenv("TAVILY_API_KEY")
#     if not tavily_api_key:
#         return "Error: TAVILY_API_KEY is not set."
        
#     tavily_client = TavilyClient(api_key=tavily_api_key)
#     results = tavily_client.search(query, max_results=max_results)
#     snippets = [r["content"] for r in results.get("results", [])]
#     return "\n".join(snippets)

# List of tools available to the agent
tools = [web_search]


def load_retrievers(documents):
    """
    Initialize all retrieval systems.

    Parameters
    ----------
    documents : list
        List of documents used to build BM25, semantic, and hybrid retrievers.

    Returns
    -------
    dict
        Dictionary containing initialized retrievers:
        - "bm25"
        - "semantic"
        - "hybrid"
    """
    retrievers = {
        "bm25": BM25Search(documents), 
        "semantic": SemanticSearch(documents)
    }
    retrievers["hybrid"] = HybridSearch(
        bm25=retrievers["bm25"],
        semantic=retrievers["semantic"],
        alpha=0.5,
        top_k_candidates=TOP_K + 100,
    )
    return retrievers


def build_context(results, documents, doc_ids):
    """
    Build a formatted context string from retrieval results.

    Parameters
    ----------
    results : list of tuple
        List of (document_index, score) pairs returned by a retriever.
    documents : list of str
        List of document texts corresponding to indices.
    doc_ids : list of str
        List of product identifiers (product_asin) aligned with documents.

    Returns
    -------
    str
        Formatted context string combining product metadata and text.
    """
    context = ""
    for i, (index, score) in enumerate(results):
        product_asin = doc_ids[index]
        product_context = documents[index]
        # print(f"{i+1}. ({score:.3f}) {product.product_title.values[0]}")
        context += f"""
parent_asin: {product_asin}
{product_context}

"""
    return context


DEFAULT_SYSTEM_PROMPT = """
You are a helpful Amazon shopping assistant.
You have been provided with context containing product reviews and metadata.
If the provided context does not contain enough information to answer the user's question, you can use the `web_search` tool to look up current pricing, news, or specifications.
Always try to be helpful and cite the ASIN when possible.
"""

def build_prompt(query, context, system_prompt=DEFAULT_SYSTEM_PROMPT):
    """
    Construct the final prompt for the LLM.

    Parameters
    ----------
    query : str
        User query.
    context : str
        Retrieved context string from search results.
    system_prompt : str, optional
        System instructions defining model behavior.

    Returns
    -------
    str
        Fully formatted prompt for the language model.
    """
    return f"""
{system_prompt}

---------

Context: 
{context}

---------

Question:
{query}

"""


def RAG_pipeline(retriever, documents, doc_ids, query, llm, top_k=TOP_K):
    """
    Run a Retrieval-Augmented Generation (RAG) pipeline.

    Parameters
    ----------
    retriever : BM25Search or SemanticSearch or HybridSearch
        custom retriever object
    documents : list
        Corpus of documents to search over.
    doc_ids : list
        Document identifiers (e.g., ASINs).
    query : str
        User input question.
    llm : (ChatGroq)
        Language model used for generation.
    top_k : int, optional
        Number of top results to retrieve.

    Returns
    -------
    str
        Generated answer from the language model.
    """
    # if isinstance(retriever, HybridSearch):
    #     raw_results = retriever.search(query, top_k=top_k)
    #     results = [(idx, score) for idx, score, _details in raw_results]
    # else:
    #     results = retriever.search(query, top_k=top_k)
    # context = build_context(results, documents, doc_ids)
    # prompt = build_prompt(query, context, system_prompt=DEFAULT_SYSTEM_PROMPT)
    # response = llm.invoke(prompt).content
    # return response

    # Retrieve local context
    if isinstance(retriever, HybridSearch):
        raw_results = retriever.search(query, top_k=top_k)
        results = [(idx, score) for idx, score, _details in raw_results]
    else:
        results = retriever.search(query, top_k=top_k)
        
    context = build_context(results, documents, doc_ids)
    
    # Build the Agent Prompt Template
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", DEFAULT_SYSTEM_PROMPT + "\n\nContext:\n{context}"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    # Create and invoke the agent
    agent = create_tool_calling_agent(llm, tools, prompt_template)
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True, 
        handle_parsing_errors=True
    )
    
    response = agent_executor.invoke({
        "input": query,
        "context": context
    })
    
    return response["output"]