import os
from tavily import TavilyClient
from langchain_core.tools import tool

@tool
def web_search(query: str, max_results: int = 3) -> str:
    """
    Search the web for up-to-date information about a product.
    
    Use this tool ONLY when:
    - The user asks for current pricing, availability, or recent news.
    - The user asks for technical specifications not found in the review context.
    - The information in the historical review corpus is insufficient to answer the query.
    """
    api_key = os.getenv("TAVILY_API_KEY")
    if not api_key:
        return "Error: TAVILY_API_KEY environment variable not set."
    
    client = TavilyClient(api_key=api_key)
    try:
        # We use 'basic' search depth for speed, which is ideal for RAG tools
        results = client.search(query, search_depth="basic", max_results=max_results)
        snippets = [r["content"] for r in results.get("results", [])]
        return "\n".join(snippets)
    except Exception as e:
        return f"Error performing web search: {e}"