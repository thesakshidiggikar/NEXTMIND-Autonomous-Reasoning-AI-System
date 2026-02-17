from core.experiment.experiment_designer import SimpleExperimentDesigner
from core.experiment.experiment_runner import SimpleExperimentRunner


def test_experiment_flow():
    designer = SimpleExperimentDesigner()
    runner = SimpleExperimentRunner()

    plan = designer.design(hypothesis_id="H1")
    result = runner.run(plan)

    assert result.status.value == "completed"
