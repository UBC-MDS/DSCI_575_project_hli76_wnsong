import os
import duckdb
import pickle
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
print("Working directory:", os.getcwd())

RAW_DATA_DIR = Path("../data/raw")
PROCESSED_DATA_DIR = Path("../data/processed")
CATEGORY = "Appliances"
BASE_URL = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw"
REVIEWS_URL = f"{BASE_URL}/review_categories/{CATEGORY}.jsonl.gz"
META_URL = f"{BASE_URL}/meta_categories/meta_{CATEGORY}.jsonl.gz"
REVIEWS_FILE = RAW_DATA_DIR / f"{CATEGORY}.jsonl.gz"
META_FILE = RAW_DATA_DIR / f"meta_{CATEGORY}.jsonl.gz"
OUTPUT_FILE = RAW_DATA_DIR / f"{CATEGORY}_merged.parquet"
os.makedirs(RAW_DATA_DIR, exist_ok=True)
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)


c2 = duckdb.connect()

review_data_file = f"{CATEGORY}_reviews_raw.parquet"
meta_data_file = f"{CATEGORY}_meta_raw.parquet"

# save reviews data
if review_data_file not in os.listdir(RAW_DATA_DIR):
    print("Downloading Review Data\nCategory: {}".format(CATEGORY))
    c2.execute(
        f"""
          COPY (SELECT rating, title, text, parent_asin, helpful_vote FROM read_json_auto('{REVIEWS_URL}'))
          TO '{RAW_DATA_DIR}/{review_data_file}'
          (FORMAT PARQUET, COMPRESSION ZSTD)
      """
    )
    print("Done")
else:
    print("Review data for {} already downloaded".format(CATEGORY))

# save meta data
if meta_data_file not in os.listdir(RAW_DATA_DIR):
    print("Downloading Meta Data\nCategory: {}".format(CATEGORY))
    c2.execute(
        f"""
    COPY (SELECT * EXCLUDE (images, videos) FROM read_json_auto('{META_URL}', union_by_name=true))
    TO '{RAW_DATA_DIR}/{meta_data_file}'
    (FORMAT PARQUET, COMPRESSION ZSTD)
    """
    )
    print("Done")
else:
    print("Meta data for {} already downloaded".format(CATEGORY))


# merge meta data and reviews and save
merged_data_file = f"{CATEGORY}_merged.parquet"

if merged_data_file not in os.listdir(PROCESSED_DATA_DIR):
    print("Merging Review/Meta Data\nCategory: {}".format(CATEGORY))
    c2.execute(
        f"""
        COPY (
            SELECT r.*, m.title AS product_title, m.price,
                        m.average_rating, m.main_category, m.store
            FROM read_parquet('{RAW_DATA_DIR}/{review_data_file}') r
            LEFT JOIN read_parquet('{RAW_DATA_DIR}/{meta_data_file}') m USING (parent_asin)
        )
        TO '{PROCESSED_DATA_DIR}/{merged_data_file}' (FORMAT PARQUET, COMPRESSION ZSTD)
    """
    )
    print("Done")
else:
    print("Merged data for {} is ready".format(CATEGORY))


products = c2.execute(
    f"""
    SELECT 
        parent_asin,
        ANY_VALUE(product_title) AS product_title,
        ANY_VALUE(main_category) AS main_category,
        ANY_VALUE(store) AS store,
        ANY_VALUE(price) AS price,
        ANY_VALUE(average_rating) AS avg_rating,
        LIST(text) AS reviews,
        LIST(title) AS review_titles,
        LIST(helpful_vote) AS helpful_votes
    FROM read_parquet('{PROCESSED_DATA_DIR}/{merged_data_file}')
    GROUP BY parent_asin;
"""
).df()


# build document for a single oroduct
def build_document(product, max_reviews=20, min_len=30, max_chars=None):
    reviews = product["reviews"]
    review_titles = product["review_titles"]
    helpful_votes = product["helpful_votes"]

    # Combine and sort reviews by helpful votes in descending order
    combined = list(zip(helpful_votes, review_titles, reviews))
    combined = sorted(
        combined, key=lambda x: x[0] if x[0] is not None else 0, reverse=True
    )

    review_lines = []
    logged_review = []
    for vote, title, review in combined:
        # filter short reviews
        if not review or len(review) < min_len:
            continue

        review = review[:max_chars]  # truncate long reviews

        # remove duplicate reviews
        if review not in logged_review:
            review_lines.append(f"- ({vote} votes) {title}: {review}")
            logged_review.append(review)

        # limit number of reviews
        if len(review_lines) >= max_reviews:
            break

    review_block = "\n".join(review_lines)

    doc = f"""
Title: {product.get('product_title', '')} {product.get('product_title', '')}
Category: {product.get('main_category', '')}
Store: {product.get('store', '')}
Price: {product.get('price', '')}
Average Rating: {product.get('avg_rating', '')}

Reviews:
{review_block}
""".strip()

    return doc


# Download product documents as pickle file
document_id_file = f"{CATEGORY}_doc_ids.pkl"
documents_file = f"{CATEGORY}_product_documents.pkl"

if document_id_file not in os.listdir(PROCESSED_DATA_DIR):
    print("Downloading document ids\nCategory: {}".format(CATEGORY))

    doc_ids = products["parent_asin"].tolist()

    with open(f"{PROCESSED_DATA_DIR}/{document_id_file}", "wb") as f:
        pickle.dump(doc_ids, f)

    print("Done")
else:
    print("Document id for {} is ready".format(CATEGORY))

if documents_file not in os.listdir(PROCESSED_DATA_DIR):
    print("Downloading documents\nCategory: {}".format(CATEGORY))

    documents = list(map(build_document, products.to_dict("records")))

    with open(f"{PROCESSED_DATA_DIR}/{documents_file}", "wb") as f:
        pickle.dump(documents, f)

    print("Done")
else:
    print("Document id for {} is ready".format(CATEGORY))
