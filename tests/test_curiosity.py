from core.curiosity.curiosity_engine import SimpleCuriosityEngine


def test_curiosity_score():
    engine = SimpleCuriosityEngine()
    result = engine.compute_curiosity({
        "uncertainty": 0.7,
        "novelty": 0.5
    })
    assert result.score > 0
