class TodoItem:
    def __init__(self, id: str, name: str, status: str, description: str):
        self.id = id
        self.name = name
        self.status = status
        self.description = description

    @classmethod
    def trello_card(cls, card: dict, list: dict) -> 'TodoItem':
        return cls(
            id=card['id'],
            name=card['name'],
            status=list['name'],
            description=card.get('desc', '')  # Handle the possibility of 'description' not being present
        )