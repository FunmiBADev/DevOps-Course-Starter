from enum import Enum
from typing import List


class ItemStatus(Enum):
    DONE = 'Done'
    TODO = 'To do'
    PROGRESS = 'In Progress'

    @classmethod
    def get_item_by_status(cls, list_id: str, board_lists: List[dict]) -> Enum:
        status_mapping = {
            'Done': cls.DONE,
            'To do': cls.TODO,
            'In Progress': cls.PROGRESS
        }
        for board_list in board_lists:
            if board_list['id'] == list_id:
                status = board_list['name']
            if status in status_mapping:
                return status_mapping[status]
            raise ValueError('Status Unknown')
