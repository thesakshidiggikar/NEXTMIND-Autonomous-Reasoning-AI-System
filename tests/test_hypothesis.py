from core.hypothesis.hypothesis_generator import SimpleHypothesisGenerator


def test_hypothesis_generation():
    generator = SimpleHypothesisGenerator()

    context = {
        "curiosity_score": 0.8
    }

    hypotheses = generator.generate(context)

    assert len(hypotheses) > 0
    assert hypotheses[0].confidence == 0.8
