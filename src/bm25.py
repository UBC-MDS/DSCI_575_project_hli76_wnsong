import os
import pickle
from rank_bm25 import BM25Okapi
from pathlib import Path
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)
from src.utils import simple_tokenize

RAW_DATA_DIR = Path("../data/raw")
PROCESSED_DATA_DIR = Path("../data/processed")


class BM25Search:
    def __init__(
        self,
        documents,
        model_path=f"{PROCESSED_DATA_DIR}/bm25.pkl",
        tokens_path=f"{PROCESSED_DATA_DIR}/tokenized_corpus.pkl",
    ):
        self.model_path = model_path
        self.tokens_path = tokens_path

        self.documents = documents
        self.bm25 = None
        self.tokenized_docs = None

        if os.path.exists(model_path) and os.path.exists(tokens_path):
            self.load()
        else:
            print("tokenizing products")
            self.build(documents)
            print("done")

    # load tokenized documents and bm25 index if exist
    def load(self):
        with open(self.model_path, "rb") as f:
            print("load bm25 index")
            self.bm25 = pickle.load(f)
            print("done")

        with open(self.tokens_path, "rb") as f:
            print("load tokenized products")
            self.tokenized_docs = pickle.load(f)
            print("done")

    # tokenize document and build bm25 index if don't
    def build(self, documents):
        self.documents = documents
        self.tokenized_docs = [simple_tokenize(doc) for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_docs)

        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

        with open(self.model_path, "wb") as f:
            pickle.dump(self.bm25, f)

        with open(self.tokens_path, "wb") as f:
            pickle.dump(self.tokenized_docs, f)

    # search with query
    def search(self, query, top_k=5):
        top_k = min(top_k, len(self.documents))

        query_tokens = simple_tokenize(query)
        scores = self.bm25.get_scores(query_tokens)

        ranked_idx = np.argsort(scores)[::-1][:top_k]

        return [(index, scores[index]) for index in ranked_idx]
