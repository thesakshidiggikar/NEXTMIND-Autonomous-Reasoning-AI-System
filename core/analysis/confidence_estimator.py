def estimate_confidence(metric_value: float) -> float:
    return min(max(metric_value, 0.0), 1.0)
