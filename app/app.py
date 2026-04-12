import os
import duckdb
import pickle
import pandas as pd
import streamlit as st
from pathlib import Path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bm25 import BM25Search
from src.semantic import SemanticSearch
from src.download_data import download_data

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


# Initialize search systems (replace with real ones)
bm25 = BM25Search(documents)
semantic = SemanticSearch(documents)


# output text for reviews
def review_text(reviews, max_len=200):
    output_text = ""
    while len(output_text) < 200 or len(output_text) != len(reviews):
        for r in reviews:
            output_text += r + "\n"
    return output_text


# log feedback
FEEDBACK_FILE = f"{PROCESSED_DATA_DIR}/feedback.csv"


def log_feedback(query, doc, score, feedback):
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


st.title("Smart Amazon Product Query Assistant")

# model
mode = st.radio("Search Mode", ["BM25", "Semantic", "Hybrid"], horizontal=True)

# query
query = st.text_input("Enter your query")

# display results
if query and mode != "Hybrid":
    if mode == "BM25":
        results = bm25.search(query)
    elif mode == "Semantic":
        results = semantic.search(query)

    st.subheader("Results")

    for i, (idx, score) in enumerate(results):
        product_asin = doc_ids[idx]
        product = products.loc[products["parent_asin"] == product_asin]

        with st.container():
            st.markdown(f"### {product.product_title.values[0]}")

            st.write(review_text(product.reviews.values[0]))

            # rating
            st.write(f"⭐ Rating: {product.average_rating.values[0]}")

            # score
            st.write(f"Score: {score:.3f}")

            # feedback buttons
            col1, col2 = st.columns(2)

            with col1:
                if st.button("👍", key=f"up_{i}"):
                    log_feedback(query, product["parent_asin"], score, 1)
                    st.success("Feedback saved")

            with col2:
                if st.button("👎", key=f"down_{i}"):
                    log_feedback(query, product["parent_asin"], score, 0)
                    st.success("Feedback saved")

            st.divider()
elif mode == "Hybrid":
    st.write("not implemented yet")
