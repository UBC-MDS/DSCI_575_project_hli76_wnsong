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
    """
    BM25-based search system for ranking documents using term frequency
    and inverse document frequency.

    Parameters
    ----------
    documents : list of str
        The corpus of documents to index and search.
    model_path : str, optional
        File path to save/load the serialized BM25 model.
        Default is "../data/processed/bm25.pkl".
    tokens_path : str, optional
        File path to save/load tokenized documents.
        Default is "../data/processed/tokenized_corpus.pkl".

    Attributes
    ----------
    documents : list of str
        The original input documents.
    bm25 : BM25Okapi or None
        The BM25 model instance used for scoring documents.
    tokenized_docs : list of list of str or None
        Tokenized representation of the documents.
    model_path : str
        Path to the saved BM25 model.
    tokens_path : str
        Path to the saved tokenized documents.
    """

    def __init__(
        self,
        documents,
        model_path=f"{PROCESSED_DATA_DIR}/bm25.pkl",
        tokens_path=f"{PROCESSED_DATA_DIR}/tokenized_corpus.pkl",
    ):
        """
        Initialize the BM25Search object. Loads existing model if available,
        otherwise builds a new one.

        Parameters
        ----------
        documents : list of str
            The corpus of documents to index.
        model_path : str, optional
            Path to the serialized BM25 model.
        tokens_path : str, optional
            Path to the serialized tokenized documents.

        Returns
        -------
        None
        """
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

    def load(self):
        """
        Load a precomputed BM25 model and tokenized documents from disk.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        This method assumes that both the model file and tokenized corpus
        file exist at the specified paths.
        """
        with open(self.model_path, "rb") as f:
            print("load bm25 index")
            self.bm25 = pickle.load(f)
            print("done")

        with open(self.tokens_path, "rb") as f:
            print("load tokenized products")
            self.tokenized_docs = pickle.load(f)
            print("done")

    def build(self, documents):
        """
        Tokenize documents and build a BM25 index, then persist them to disk.

        Parameters
        ----------
        documents : list of str
            The corpus of documents to tokenize and index.

        Returns
        -------
        None

        Notes
        -----
        - Uses `simple_tokenize` for preprocessing text.
        - Saves both the BM25 model and tokenized documents to disk.
        """
        self.documents = documents
        self.tokenized_docs = [simple_tokenize(doc) for doc in documents]
        self.bm25 = BM25Okapi(self.tokenized_docs)

        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)

        with open(self.model_path, "wb") as f:
            pickle.dump(self.bm25, f)

        with open(self.tokens_path, "wb") as f:
            pickle.dump(self.tokenized_docs, f)

    def search(self, query, top_k=5):
        """
        Search the document corpus using a BM25 scoring function.

        Parameters
        ----------
        query : str
            The search query string.
        top_k : int, optional
            The number of top results to return. Default is 5.

        Returns
        -------
        list of tuple
            A list of (index, score) tuples where:
            - index : int
                Index of the document in the original corpus.
            - score : float
                BM25 relevance score for the document.

        Notes
        -----
        - The query is tokenized using `simple_tokenize`.
        - Results are sorted in descending order of relevance score.
        - If `top_k` exceeds the number of documents, it is clipped.
        """
        top_k = min(top_k, len(self.documents))

        query_tokens = simple_tokenize(query)
        scores = self.bm25.get_scores(query_tokens)

        ranked_idx = np.argsort(scores)[::-1][:top_k]

        return [(index, scores[index]) for index in ranked_idx]
