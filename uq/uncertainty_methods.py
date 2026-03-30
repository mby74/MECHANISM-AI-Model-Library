from typing import List


def simple_confidence_from_variance(values: List[float]) -> float:
    if not values:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    confidence = 1.0 / (1.0 + variance)
    return max(0.0, min(1.0, confidence))
