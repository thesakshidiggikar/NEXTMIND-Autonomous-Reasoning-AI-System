from core.meta.meta_controller import SimpleMetaController
from core.meta.meta_types import MetaDecision


def test_meta_explore():
    controller = SimpleMetaController()
    action = controller.decide(curiosity_score=0.8, success_rate=0.9)
    assert action.decision == MetaDecision.EXPLORE


def test_meta_exploit():
    controller = SimpleMetaController()
    action = controller.decide(curiosity_score=0.2, success_rate=0.8)
    assert action.decision == MetaDecision.EXPLOIT
