class SimpleKnowledgeGraph:
    """
    Very simple graph using dictionary.
    """

    def __init__(self):
        self.edges = {}

    def add_relation(self, source: str, target: str) -> None:
        self.edges.setdefault(source, []).append(target)
