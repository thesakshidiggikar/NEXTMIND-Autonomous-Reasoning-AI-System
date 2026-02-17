from core.knowledge.knowledge_store import InMemoryKnowledgeStore
from core.knowledge.knowledge_types import KnowledgeItem, KnowledgeStatus


def test_knowledge_store():
    store = InMemoryKnowledgeStore()

    item = KnowledgeItem(
        hypothesis_id="H1",
        decision=KnowledgeStatus.SUCCESS,
        confidence=0.9
    )

    store.add(item)

    all_items = store.get_all()

    assert len(all_items) == 1
    assert all_items[0].hypothesis_id == "H1"
