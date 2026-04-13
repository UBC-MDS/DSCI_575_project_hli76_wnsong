import numpy as np

class HybridSearch:
    """
    Combine BM25 and SemanticSearch results.

    Parameters
    ----------
    bm25 : BM25Search instance
        Already-initialized BM25 search object.
    semantic : SemanticSearch instance
        Already-initialized semantic search object.
    alpha : float, optional
        Weight for semantic score in [0,1]. Default 0.5.
    top_k_candidates : int, optional
        How many candidates to fetch from each backend before merging.
    """
    def __init__(self, bm25, semantic, alpha=0.5, top_k_candidates=100):
        """
        Initialize hybrid search system.

        Parameters
        ----------
        bm25 : BM25Search
            BM25 retrieval system instance.
        semantic : SemanticSearch
            Semantic retrieval system instance.
        alpha : float, optional
            Weight for semantic score in hybrid ranking.
        top_k_candidates : int, optional
            Number of candidates retrieved from each system.

        Returns
        -------
        None
        """
        self.bm25 = bm25
        self.semantic = semantic
        self.alpha = float(alpha)
        self.top_k_candidates = int(top_k_candidates)

    def _normalize_bm25(self, scores):
        """
        Normalize BM25 scores to the range [0, 1].

        Parameters
        ----------
        scores : array-like
            Raw BM25 scores.

        Returns
        -------
        np.ndarray
            Normalized scores in [0, 1].

        Notes
        -----
        Uses max-normalization. If max score is 0, returns zeros.
        """
        if len(scores) == 0:
            return np.array([])
        s = np.array(scores, dtype=float)
        maxv = s.max()
        if maxv <= 0:
            return np.zeros_like(s)
        return s / maxv

    def _normalize_semantic(self, scores):
        """
        Normalize semantic similarity scores to [0, 1].

        Parameters
        ----------
        scores : array-like
            Raw cosine similarity scores from FAISS.

        Returns
        -------
        np.ndarray
            Normalized scores in [0, 1].

        Notes
        -----
        Assumes FAISS IndexFlatIP with normalized embeddings,
        where scores are in approximately [-1, 1].
        """
        s = np.array(scores, dtype=float)
        s = (s + 1.0) / 2.0
        s = np.clip(s, 0.0, 1.0)
        return s

    def search(self, query, top_k=5):
        """
        Normalize semantic similarity scores to [0, 1].

        Parameters
        ----------
        scores : array-like
            Raw cosine similarity scores from FAISS.

        Returns
        -------
        np.ndarray
            Normalized scores in [0, 1].

        Notes
        -----
        Assumes FAISS IndexFlatIP with normalized embeddings,
        where scores are in approximately [-1, 1].
        """
        k = max(top_k, self.top_k_candidates)
        bm25_results = self.bm25.search(query, top_k=k)
        sem_results = self.semantic.search(query, top_k=k)

        bm25_idx = [r[0] for r in bm25_results]
        bm25_scores = [r[1] for r in bm25_results]
        sem_idx = [r[0] for r in sem_results]
        sem_scores = [r[1] for r in sem_results]

        candidate_indices = list(dict.fromkeys(bm25_idx + sem_idx))

        bm25_map = {idx: score for idx, score in zip(bm25_idx, bm25_scores)}
        sem_map = {idx: score for idx, score in zip(sem_idx, sem_scores)}

        bm25_arr = np.array([bm25_map.get(i, 0.0) for i in candidate_indices], dtype=float)
        sem_arr = np.array([sem_map.get(i, 0.0) for i in candidate_indices], dtype=float)

        norm_bm25 = self._normalize_bm25(bm25_arr)
        norm_sem = self._normalize_semantic(sem_arr)

        alpha = self.alpha
        hybrid_scores = alpha * norm_sem + (1.0 - alpha) * norm_bm25

        results = []
        for idx, hscore, bscore, sscore in zip(candidate_indices, hybrid_scores, bm25_arr, sem_arr):
            results.append((int(idx), float(hscore), {"bm25_score": float(bscore), "semantic_score": float(sscore)}))

        results = sorted(results, key=lambda x: x[1], reverse=True)
        return results[:top_k]