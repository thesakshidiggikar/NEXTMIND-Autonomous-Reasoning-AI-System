import random
from core.experiment.base import BaseExperimentRunner
from core.experiment.experiment_types import (
    ExperimentResult,
    ExperimentStatus,
    ExperimentPlan
)


class SimpleExperimentRunner(BaseExperimentRunner):

    def run(self, plan: ExperimentPlan) -> ExperimentResult:
        metric_value = random.uniform(0.0, 1.0)

        return ExperimentResult(
            experiment_id=plan.id,
            metric_value=metric_value,
            status=ExperimentStatus.COMPLETED
        )
