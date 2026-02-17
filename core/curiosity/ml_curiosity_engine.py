import numpy as np
from sklearn.metrics import pairwise_distances
from core.curiosity.base import BaseCuriosityEngine
from core.curiosity.curiosity_types import (
    CuriosityScore,
    CuriositySignal,
    SignalType
)


class MLCuriosityEngine(BaseCuriosityEngine):
    """
    ML-based curiosity using distance from historical embeddings.
    """

    def __init__(self):
        self.history = []

    def compute_curiosity(self, context: dict) -> CuriosityScore:
        embedding = np.array(context.get("embedding", [0.0, 0.0]))

        novelty = 1.0
        if self.history:
            distances = pairwise_distances(
                [embedding],
                self.history,
                metric="euclidean"
            )
            novelty = float(distances.mean())

        self.history.append(embedding)

        uncertainty = float(context.get("uncertainty", 0.0))

        score = min((novelty + uncertainty) / 2, 1.0)

        signals = [
            CuriositySignal(SignalType.NOVELTY, novelty),
            CuriositySignal(SignalType.UNCERTAINTY, uncertainty)
        ]

        return CuriosityScore(score=score, signals=signals)
