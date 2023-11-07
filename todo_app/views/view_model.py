from enum import Enum
from typing import List
from todo_app.data.itemStatus import ItemStatus
from todo_app.data.todo_item import TodoItem


class ViewModel:
    def __init__(self, items: List[TodoItem]):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def done_items(self):
        return self._filter_items_by_status(ItemStatus.DONE)

    @property
    def progress_items(self):
        return self._filter_items_by_status(ItemStatus.PROGRESS)

    @property
    def todo_items(self):
        return self._filter_items_by_status(ItemStatus.TODO)

    def _filter_items_by_status(self, status: Enum) -> List[TodoItem]:
        return [item for item in self.items if item.status == status.value]
