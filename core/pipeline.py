from core.curiosity.curiosity_engine import SimpleCuriosityEngine
from core.analysis.result_analyzer import SimpleResultAnalyzer
from core.meta.meta_controller import SimpleMetaController
from core.llm.hypothesis_llm import HypothesisLLM


class NextMindPipeline:
    def __init__(self):
        self.curiosity_engine = SimpleCuriosityEngine()
        self.analyzer = SimpleResultAnalyzer()
        self.meta_controller = SimpleMetaController()
        self.hypothesis_llm = HypothesisLLM()   # ✅ VERY IMPORTANT

    def run(self, context: dict) -> dict:
        # 1. Curiosity
        curiosity_result = self.curiosity_engine.compute_curiosity(context)
        curiosity_score = curiosity_result.score

        # 2. Hypothesis (Local LLM)
        hypothesis = self.hypothesis_llm.generate(curiosity_score)

        # 3. Analysis
        analysis_decision = self.analyzer.analyze(curiosity_score)

        # 4. Meta decision
        meta_decision = self.meta_controller.decide(
            curiosity_score=curiosity_score,
            success_rate=0.5
        )

        return {
            "curiosity_score": curiosity_score,
            "hypothesis": hypothesis,
            "analysis_decision": analysis_decision.decision.value,
            "meta_decision": meta_decision.decision.value
        }
