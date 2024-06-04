class TodoItem:
    def __init__(self, id: str, name: str, status: str, description: str):
        self.id = id
        self.name = name
        self.status = status
        self.description = description

    @classmethod
    def from_mongodb_doc(cls, doc: dict) -> 'TodoItem':
        return cls(
            id=str(doc['_id']),
            name=doc['name'],
            status=doc['status'],
            description=doc.get('description', '')
        )
