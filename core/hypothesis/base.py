from abc import ABC, abstractmethod
from typing import List
from core.hypothesis.hypothesis_types import Hypothesis


class BaseHypothesisGenerator(ABC):

    @abstractmethod
    def generate(self, context: dict) -> List[Hypothesis]:
        """
        Generate hypotheses based on given context.
        """
        pass
