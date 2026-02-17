from core.curiosity.base import BaseCuriosityEngine
from core.curiosity.curiosity_types import (
    CuriosityScore,
    CuriositySignal,
    SignalType
)


class SimpleCuriosityEngine(BaseCuriosityEngine):

    def compute_curiosity(self, context: dict) -> CuriosityScore:
        uncertainty = context.get("uncertainty", 0.0)
        novelty = context.get("novelty", 0.0)

        score = (uncertainty + novelty) / 2

        signals = [
            CuriositySignal(SignalType.UNCERTAINTY, uncertainty),
            CuriositySignal(SignalType.NOVELTY, novelty),
        ]

        return CuriosityScore(score=score, signals=signals)
