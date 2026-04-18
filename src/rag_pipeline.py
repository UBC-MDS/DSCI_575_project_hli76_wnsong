import os
import pickle
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from langchain_groq import ChatGroq

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
load_dotenv()
from src.bm25 import BM25Search
from src.semantic import SemanticSearch
from src.hybrid import HybridSearch

TOP_K = 10


def build_context(results, documents, doc_ids):
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
    retrievers = {"bm25": BM25Search(documents), "semantic": SemanticSearch(documents)}
    retrievers["hybrid"] = HybridSearch(
        bm25=retrievers["bm25"],
        semantic=retrievers["semantic"],
        alpha=0.5,
        top_k_candidates=TOP_K + 100,
    )
    return retrievers


llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))


def RAG_pipeline(retriever, documents, query, llm, top_k=TOP_K):
    retriever = load_retrievers(documents)[retriever]
    if isinstance(retriever, HybridSearch):
        raw_results = retriever.search(query, top_k=top_k)
        results = [(idx, score) for idx, score, _details in raw_results]
    else:
        results = retriever.search(query, top_k=top_k)
    context = build_context(results)
    prompt = build_prompt(query, context, system_prompt=DEFAULT_SYSTEM_PROMPT)
    response = llm.invoke(prompt).content
    return response
