from core.experiment.experiment_types import ExperimentPlan


class SimpleExperimentDesigner:

    def design(self, hypothesis_id: str) -> ExperimentPlan:
        return ExperimentPlan(
            id="EXP-1",
            hypothesis_id=hypothesis_id,
            description="Test hypothesis with a simple controlled experiment",
            metric_name="performance_score"
        )
