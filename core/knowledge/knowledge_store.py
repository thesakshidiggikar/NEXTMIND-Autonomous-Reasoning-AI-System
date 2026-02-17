from typing import List
from core.knowledge.base import BaseKnowledgeStore
from core.knowledge.knowledge_types import KnowledgeItem


class InMemoryKnowledgeStore(BaseKnowledgeStore):

    def __init__(self):
        self._items: List[KnowledgeItem] = []

    def add(self, item: KnowledgeItem) -> None:
        self._items.append(item)

    def get_all(self) -> List[KnowledgeItem]:
        return self._items
