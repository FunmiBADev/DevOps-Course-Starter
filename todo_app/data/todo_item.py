class TodoItem:
    def __init__(self, id: str, name: str, status: str, description: str):
        self.id = id
        self.name = name
        self.status = status
        self.description = description

    @classmethod
    def from_trello_card(cls, card: dict, list: dict) -> 'TodoItem':
        return cls(
            id=card['id'],
            name=card['name'],
            status=list['name'],
            # Handle the possibility of 'description' not being present
            description=card.get('desc', '')
        )
