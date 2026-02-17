from core.meta.base import BaseMetaController
from core.meta.meta_types import MetaAction, MetaDecision


class SimpleMetaController(BaseMetaController):

    def decide(self, curiosity_score: float, success_rate: float) -> MetaAction:
        """
        Simple strategy:
        - High curiosity OR low success → explore
        - Otherwise → exploit
        """

        if curiosity_score >= 0.6 or success_rate < 0.5:
            return MetaAction(
                decision=MetaDecision.EXPLORE,
                reason="High curiosity or low success rate"
            )

        return MetaAction(
            decision=MetaDecision.EXPLOIT,
            reason="Stable success, refine existing knowledge"
        )
