from typing import Dict


def select_best_model(confidence_scores: Dict[str, float]) -> str:
    if not confidence_scores:
        raise ValueError("No confidence scores provided.")
    return max(confidence_scores, key=confidence_scores.get)
