from core.analysis.result_analyzer import SimpleResultAnalyzer
from core.analysis.analysis_types import AnalysisDecision


def test_analysis_accept():
    analyzer = SimpleResultAnalyzer()
    result = analyzer.analyze(hypothesis_id="H1", metric_value=0.8)
    assert result.decision == AnalysisDecision.ACCEPT


def test_analysis_reject():
    analyzer = SimpleResultAnalyzer()
    result = analyzer.analyze(hypothesis_id="H2", metric_value=0.3)
    assert result.decision == AnalysisDecision.REJECT
