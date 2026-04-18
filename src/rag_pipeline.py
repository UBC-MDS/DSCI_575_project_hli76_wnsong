import os
from pathlib import Path
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

from src.bm25 import BM25Search
from src.semantic import SemanticSearch
from src.hybrid import HybridSearch
from src.tools import web_search

TOP_K = 10


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
Instructions:
- You are a helpful Amazon shopping assistant.
- You have access to historical product reviews and metadata provided in the Context below.
- Always cite the product ASIN when possible.
- If the question requires up-to-date pricing, live availability, or specs missing from the context, use your `web_search` tool to find it.
- Do NOT say "I don't know" if the answer exists in the context or can be found via web search.

Context:
{context}
"""

# build_prompt becomes absolete if we use a tool-calling agent, but we keep it for now since we are not fully implementing the agent in this codebase. 
# The agent implementation is more complex and would require changes to how we structure the prompt and handle tool calls, so we will leave that as a future enhancement.
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
    Execute a Retrieval-Augmented Generation (RAG) pipeline utilizing an LLM agent 
    with tool-calling capabilities.

    This pipeline first retrieves relevant historical product reviews and metadata using the 
    specified retrieval system. It then constructs a LangChain Agent equipped with a web search 
    tool, allowing the LLM to dynamically fetch up-to-date information if the historical context 
    is insufficient to answer the user's query.

    Parameters
    ----------
    retriever : BM25Search, SemanticSearch, or HybridSearch
        The initialized search system used to retrieve relevant local documents.
    documents : list of str
        The full corpus of product documents/reviews.
    doc_ids : list of str
        The unique identifiers (e.g., parent ASINs) corresponding to the documents.
    query : str
        The question or search input provided by the user.
    llm : BaseChatModel
        The initialized LangChain chat model (e.g., ChatGroq) capable of tool calling.
    top_k : int, optional
        The number of top document candidates to retrieve for context. Defaults to TOP_K.

    Returns
    -------
    str
        The final generated response from the agent, synthesizing both the local historical 
        review context and any live web data retrieved during execution.

    Notes
    -----
    - The function utilizes `create_tool_calling_agent` and `AgentExecutor` to handle 
      multi-step reasoning.
    - The `agent_scratchpad` in the prompt template is required for the LLM to store 
      and read the outputs of its tool calls before formulating the final answer.
    - Currently provisions the `web_search` tool (powered by Tavily) to handle live 
      pricing, availability, and specs queries.
    """
    if isinstance(retriever, HybridSearch):
        raw_results = retriever.search(query, top_k=top_k)
        results = [(idx, score) for idx, score, _details in raw_results]
    else:
        results = retriever.search(query, top_k=top_k)
        
    context = build_context(results, documents, doc_ids)

    tools = [web_search]

    agent_prompt = ChatPromptTemplate.from_messages([
        ("system", DEFAULT_SYSTEM_PROMPT),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"), # Required for the agent to track tool calls
    ])

    agent = create_tool_calling_agent(llm, tools, agent_prompt)
    
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    response = agent_executor.invoke({
        "input": query,
        "context": context
    })
    
    return response["output"]
