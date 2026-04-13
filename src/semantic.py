import os
import faiss
from sentence_transformers import SentenceTransformer
from pathlib import Path


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(SCRIPT_DIR)

RAW_DATA_DIR = Path("../data/raw")
PROCESSED_DATA_DIR = Path("../data/processed")


class SemanticSearch:
    """
    Semantic search system using SentenceTransformer embeddings and FAISS
    for efficient nearest-neighbor retrieval.

    Parameters
    ----------
    documents : list of str
        Corpus of documents to embed and index.
    index_path : str, optional
        Path to save/load FAISS index. Default is
        "../data/processed/faiss.index".

    Attributes
    ----------
    documents : list of str
        Input document corpus.
    model : SentenceTransformer
        Pretrained transformer model used for encoding text.
    index : faiss.Index or None
        FAISS index for similarity search.
    embeddings : np.ndarray or None
        Dense vector representations of documents.
    """

    def __init__(
        self,
        documents,
        index_path=f"{PROCESSED_DATA_DIR}/faiss.index",
    ):
        """
        Semantic search system using SentenceTransformer embeddings and FAISS
        for efficient nearest-neighbor retrieval.

        Parameters
        ----------
        documents : list of str
            Corpus of documents to embed and index.
        index_path : str, optional
            Path to save/load FAISS index. Default is
            "../data/processed/faiss.index".

        Attributes
        ----------
        documents : list of str
            Input document corpus.
        model : SentenceTransformer
            Pretrained transformer model used for encoding text.
        index : faiss.Index or None
            FAISS index for similarity search.
        embeddings : np.ndarray or None
            Dense vector representations of documents.
        """
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

    def build(self, documents):
        """
        Build FAISS index from document embeddings and save it to disk.

        Parameters
        ----------
        documents : list of str
            Corpus of documents to encode and index.

        Returns
        -------
        None

        Notes
        -----
        - Uses SentenceTransformer to generate embeddings.
        - Embeddings are L2-normalized for cosine similarity.
        - FAISS IndexFlatIP is used (inner product similarity).
        - Index is persisted to disk.
        """
        self.documents = documents
        self.embeddings = self.model.encode(documents).astype("float32")
        faiss.normalize_L2(self.embeddings)

        self.index = faiss.IndexFlatIP(self.embeddings.shape[1])
        self.index.add(self.embeddings)

        faiss.write_index(self.index, self.index_path)

    def load(self):
        """
        Load a prebuilt FAISS index from disk.

        Parameters
        ----------
        None

        Returns
        -------
        None

        Notes
        -----
        Only the FAISS index is loaded; document embeddings are not restored.
        Ensure `self.documents` matches the indexed corpus.
        """
        self.index = faiss.read_index(self.index_path)

    def search(self, query, top_k=5):
        """
        Perform semantic search over the document corpus.

        Parameters
        ----------
        query : str
            Input query string.
        top_k : int, optional
            Number of top results to return. Default is 5.

        Returns
        -------
        list of tuple
            List of (document_index, similarity_score) pairs sorted by relevance.

        Notes
        -----
        - Query is embedded using SentenceTransformer.
        - Cosine similarity is computed via FAISS inner product on normalized vectors.
        - Returned indices correspond to positions in `self.documents`.
        """
        top_k = min(top_k, len(self.documents))

        query_vec = self.model.encode([query]).astype("float32")
        faiss.normalize_L2(query_vec)

        scores, indices = self.index.search(query_vec, top_k)

        return [(index, float(score)) for index, score in zip(indices[0], scores[0])]
