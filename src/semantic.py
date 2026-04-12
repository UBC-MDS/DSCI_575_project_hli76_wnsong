import os
import faiss
from sentence_transformers import SentenceTransformer
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

RAW_DATA_DIR = Path("../data/raw")
PROCESSED_DATA_DIR = Path("../data/processed")


class SemanticSearch:
    def __init__(
        self,
        documents,
        index_path=f"{PROCESSED_DATA_DIR}/faiss.index",
    ):
        self.documents = documents
        self.index_path = index_path

        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.embeddings = None

        if os.path.exists(index_path):
            print("load faiss index")
            self.load()
            print("done")
        else:
            print("build faiss index")
            self.build(documents)
            print("done")

    # Build and save index
    def build(self, documents):
        self.documents = documents
        self.embeddings = self.model.encode(documents)

        self.index = faiss.IndexFlatIP(self.embeddings.shape[1])
        self.index.add(self.embeddings)

        os.makedirs(os.path.dirname(self.index_path), exist_ok=True)
        faiss.write_index(self.index, self.index_path)

    # load index
    def load(self):
        self.index = faiss.read_index(self.index_path)

    # search query
    def search(self, query, top_k=5):
        top_k = min(top_k, len(self.documents))

        query_vec = self.model.encode([query])
        scores, indices = self.index.search(query_vec, top_k)

        return [
            (index, float(score))
            for index, score in zip(indices[0], scores[0])
        ]
