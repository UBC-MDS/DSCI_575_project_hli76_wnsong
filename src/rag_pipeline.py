import os
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

from src.bm25 import BM25Search
from src.semantic import SemanticSearch
from src.hybrid import HybridSearch

TOP_K = 10

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
- You must answer the question using ONLY the following context (real product reviews with helpful votes and the metadata for the products).
- Always cite the product ASIN when possible.
- If the answer is present, extract and summarize it clearly.
- Do NOT say "I don't know" if the answer exists in the context.
- Only say "I don't know" if the context truly does not contain the answer.
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
    if isinstance(retriever, HybridSearch):
        raw_results = retriever.search(query, top_k=top_k)
        results = [(idx, score) for idx, score, _details in raw_results]
    else:
        results = retriever.search(query, top_k=top_k)
    context = build_context(results, documents, doc_ids)
    prompt = build_prompt(query, context, system_prompt=DEFAULT_SYSTEM_PROMPT)
    response = llm.invoke(prompt).content
    return response
