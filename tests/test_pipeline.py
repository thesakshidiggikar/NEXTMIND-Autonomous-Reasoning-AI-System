from core.pipeline import NextMindPipeline


def test_full_pipeline():
    pipeline = NextMindPipeline()

    result = pipeline.run({
        "uncertainty": 0.7,
        "novelty": 0.6
    })

    assert "curiosity_score" in result
    assert "meta_decision" in result
