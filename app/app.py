import os
import sys
import duckdb
import pickle
import pandas as pd
import streamlit as st
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bm25 import BM25Search
from src.semantic import SemanticSearch
from src.hybrid import HybridSearch
from src.download_data import download_data
from src.rag_pipeline import RAG_pipeline


FILE_PATH = os.path.dirname(os.path.abspath("."))
print(FILE_PATH, os.listdir())

download_data()

CATEGORY = "Appliances"
PROCESSED_DATA_DIR = Path("../data/processed")

with open(f"{PROCESSED_DATA_DIR}/{CATEGORY}_product_documents.pkl", "rb") as f:
    documents = pickle.load(f)
with open(f"{PROCESSED_DATA_DIR}/{CATEGORY}_doc_ids.pkl", "rb") as f:
    doc_ids = pickle.load(f)

product_data_file = "Appliances_products.parquet"

c2 = duckdb.connect()
products = c2.execute(
    f"SELECT * FROM read_parquet('{PROCESSED_DATA_DIR}/{product_data_file}')"
).df()


# output text for reviews
def review_text(reviews, max_len=200):
    """
    Concatenate a list of review strings into a single formatted text block.

    Parameters
    ----------
    reviews : list of str
        A list containing individual review texts.
    max_len : int, optional
        Maximum character length of the output text. Default is 200.

    Returns
    -------
    str
        A single string containing concatenated reviews separated by newlines.
        The output is truncated based on the specified maximum length.

    Notes
    -----
    The function appends reviews sequentially until the output length
    exceeds `max_len` or all reviews are processed. The logic may allow
    slight overflow beyond `max_len` due to per-review concatenation.
    """
    output_text = ""
    for r in reviews:
        if len(output_text) < 200 or len(output_text) <= len(reviews):
            output_text += f"""
{r}
"""
    return output_text


# log feedback
FEEDBACK_FILE = f"{PROCESSED_DATA_DIR}/feedback.csv"


def log_feedback(query, doc, score, feedback):
    """
    Log user feedback for a search result into a CSV file.

    Parameters
    ----------
    query : str
        The search query entered by the user.
    doc : str
        Identifier of the retrieved document (e.g., parent ASIN).
    score : float
        Relevance score assigned to the document by the search system.
    feedback : int
        User feedback indicator (e.g., 1 for helpful, 0 for not helpful).

    Returns
    -------
    None
        This function does not return any value. It writes data to a CSV file.

    Notes
    -----
    - If the feedback file already exists, the new feedback entry is appended.
    - The CSV file is stored at the path defined by `FEEDBACK_FILE`.
    """
    row = {
        "query": query,
        "document": doc,
        "score": score,
        "feedback": feedback,
    }

    new_row = pd.DataFrame([row])

    if os.path.exists(FEEDBACK_FILE):
        logfile = pd.read_csv(FEEDBACK_FILE)
        logfile = pd.concat([logfile, new_row], ignore_index=True)
    else:
        logfile = new_row

    logfile.to_csv(FEEDBACK_FILE, index=False)


st.set_page_config(
    page_title="Smart Amazon Assistant",
    layout="wide"
)
st.title(f"Smart Amazon Product Query Assistant for {CATEGORY}")

st.markdown("""<style>
/* Global font size */
html, body, [class*="css"]  {
    font-size: 20px;
}

st.set_page_config(
    page_title="Smart Amazon Assistant",
    layout="wide"
)

/* Text input styling */
.stTextInput > div > div > input {
    font-size: 20px;
    padding: 12px 14px;
    border-radius: 10px;
    border: 1px solid #3B82F6;
    background-color: #111827;
    color: #E5E7EB;
}

/* Input focus effect */
.stTextInput > div > div > input:focus {
    border: 1px solid #60A5FA;
    box-shadow: 0 0 0 2px rgba(59,130,246,0.3);
}

/* Labels */
label {
    font-size: 20px !important;
    font-weight: 500;
}

/* Slider and radio */
.stSlider, .stRadio {
    font-size: 20px;
}

/* Card container */
.result-card {
    background-color: #172036;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 18px;
    border: 1px solid rgba(59,130,246,0.35); /* stronger border */
    box-shadow: 0 4px 16px rgba(0,0,0,0.5); /* depth */
    transition: all 0.2s ease-in-out;
}

/* Hover effect: slightly brighter on hover */
.result-card:hover {
    background-color: #1E2A44; 
    border: 1px solid rgba(96,165,250,0.8);
    box-shadow: 0 8px 28px rgba(0,0,0,0.7);
}

/* Title */
.result-title {
    font-size: 24px;
    font-weight: 600;
    margin-bottom: 8px;
}

/* Rating and score */
.result-meta {
    font-size: 20px;
    color: #9CA3AF;
    margin-bottom: 10px;
}

/* Review text */
.result-text {
    font-size: 20px;
    line-height: 1.5;
    margin-bottom: 12px;
}
</style>""",
    unsafe_allow_html=True,
)

@st.cache_resource
def load_retrievers(documents, TOP_K=10):
    """
    Cache retrievers so they are built only once per session.

    Parameters
    ----------
    documents : list
        List of documents used for retrieval.

    Returns
    -------
    dict
        Dictionary with BM25, Semantic, and Hybrid retrievers.
    """
    bm25 = BM25Search(documents)
    semantic = SemanticSearch(documents)

    hybrid = HybridSearch(
        bm25=bm25,
        semantic=semantic,
        alpha=0.5,
        top_k_candidates=TOP_K + 100,
    )

    return {
        "bm25": bm25,
        "semantic": semantic,
        "hybrid": hybrid
    }


retrievers = load_retrievers(documents)

tab1, tab2 = st.tabs(["Search", "RAG Assistant"])
with tab1:
    # model
    mode = st.radio("Search Mode", ["BM25", "Semantic", "Hybrid"], horizontal=True)

    # display top k results
    top_k = st.slider(
        "Number of Results", 
        min_value=5, 
        max_value=100, 
        value=5, 
        step=5, 
        format="plain"
    )

    # query
    query = st.text_input("Enter your query")

    # Initialize search systems
    bm25 = BM25Search(documents)
    semantic = SemanticSearch(documents)
    hybrid = HybridSearch(
        bm25=bm25, semantic=semantic, alpha=0.5, top_k_candidates=top_k + 100
    )

    # display results
    if query:
        with st.spinner("Generating answer..."):
            if mode == "BM25":
                results = retrievers["bm25"].search(query, top_k=top_k)
            elif mode == "Semantic":
                results = retrievers["semantic"].search(query, top_k=top_k)
            elif mode == "Hybrid":
                raw_results = retrievers["hybrid"].search(
                    query, top_k=top_k
                )  # list of (idx, hybrid_score, details)
                # convert to same format as BM25/Semantic: list of (idx, score)
                results = [(idx, score) for idx, score, _details in raw_results]

        st.subheader("Results")

        for i, (idx, score) in enumerate(results):
            parent_asin = doc_ids[idx]
            product = products.loc[products.parent_asin == parent_asin]

            title = product.product_title.values[0]
            reviews = review_text(product.reviews.values[0])
            rating = product.avg_rating.values[0]
            price = product.price.values[0]

            st.markdown(
                f"""
            <div class="result-card">
                <div class="result-title">{title}</div>
                <div class="result-meta">⭐ Rating: {rating} | Score: {score:.3f} | Price: {price}</div>
                <div class="result-text">{reviews}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # 👍 👎 buttons under each card
            col1, col2 = st.columns(2)

            with col1:
                if st.button("👍 Helpful", key=f"up_{i}"):
                    log_feedback(query, parent_asin, score, 1)
                    st.success("Feedback saved")

            with col2:
                if st.button("👎 Not Helpful", key=f"down_{i}"):
                    log_feedback(query, parent_asin, score, 0)
                    st.success("Feedback saved")

            st.divider()

with tab2:
    rag_mode = st.radio("Retriever", ["bm25", "semantic", "hybrid"], horizontal=True)
    llm_mode = st.radio("LLM Model", ["llama-versatile-70b", "gpt-oss-20b"], horizontal=True)
    
    if llm_mode == "llama-versatile-70b":
        llm = ChatGroq(
            model="llama-3.3-70b-versatile", 
            api_key=os.getenv("GROQ_API_KEY")
        )
    else:
        llm = ChatGroq(
            model="openai/gpt-oss-20b", 
            api_key=os.getenv("GROQ_API_KEY")
        )

    top_k_rag = st.slider(
        "Context size",
        min_value=3,
        max_value=20,
        value=5,
        step=1,
        format="plain",
        key="rag_topk",
    )

    rag_query = st.text_input("Ask a question about products", key="rag_query")
    if rag_query:
        with st.spinner("Generating answer..."):
            retriever = retrievers[rag_mode]
            answer = RAG_pipeline(
                retriever=retriever,
                documents=documents,
                doc_ids=doc_ids,
                query=rag_query,
                llm=llm,
                top_k=top_k_rag
            )
        st.markdown("### Recommendation")
        st.markdown(
                f"""
            <div class="result-card">
                <div class="result-text">{answer}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )
        # st.write(answer)
