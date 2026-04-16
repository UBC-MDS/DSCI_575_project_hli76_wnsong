from typing import List, Set, Dict

def precision_at_k(retrieved: List[int], relevant: Set[int], k: int) -> float:
    """
    retrieved: list of document indices returned by the system
    relevant: set of relevant document indices
    k: cutoff
    """
    if k == 0:
        return 0.0

    retrieved_k = retrieved[:k]
    hits = sum(1 for doc in retrieved_k if doc in relevant)
    return hits / k


def average_precision_at_k(retrieved: List[int], relevant: Set[int], k: int) -> float:
    """
    Calculate Average Precision (AP) at K.
    AP rewards systems that put the relevant documents at the very top of the list.
    """
    if not relevant:
        return 0.0
        
    retrieved_k = retrieved[:k]
    
    score = 0.0
    hits = 0
    
    for i, doc in enumerate(retrieved_k):
        if doc in relevant:
            hits += 1
            # Calculate precision at this specific rank
            score += hits / (i + 1.0)
            
    return score / min(len(relevant), k)


def recall_at_k(retrieved: List[int], relevant: Set[int], k: int) -> float:
    """
    recall@k = (# of relevant docs retrieved in top-k) / (total relevant docs)
    """
    if len(relevant) == 0:
        return 0.0

    retrieved_k = retrieved[:k]
    hits = sum(1 for doc in retrieved_k if doc in relevant)
    return hits / len(relevant)


def mrr(retrieved: List[int], relevant: Set[int]) -> float:
    """
    Mean Reciprocal Rank for a single query.
    MRR = 1 / rank_of_first_relevant
    """
    for rank, doc in enumerate(retrieved, start=1):
        if doc in relevant:
            return 1.0 / rank
    return 0.0


def evaluate_query(
    retrieved: List[int],
    relevant: Set[int],
    ks: List[int] = [1, 3, 5]
) -> Dict[str, float]:
    """
    Compute metrics for a single query.
    """
    metrics = {}

    for k in ks:
        metrics[f"precision@{k}"] = precision_at_k(retrieved, relevant, k)
        metrics[f"avg precision@{k}"] = average_precision_at_k(retrieved, relevant, k)
        metrics[f"recall@{k}"] = recall_at_k(retrieved, relevant, k)

    metrics["mrr"] = mrr(retrieved, relevant)
    return metrics
