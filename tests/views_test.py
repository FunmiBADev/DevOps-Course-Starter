import pytest
from todo_app.data.itemStatus import ItemStatus
from todo_app.data.todo_item import TodoItem
from todo_app.views.view_model import ViewModel

@pytest.fixture
def item_view_model():
    items = [
        TodoItem('1', 'task 1', ItemStatus.TODO.value,
                 'description of task 1'),
        TodoItem('2', 'task 2', ItemStatus.PROGRESS.value, ''),
        TodoItem('3', 'task 3', ItemStatus.PROGRESS.value, ''),
        TodoItem('4', 'task 4', ItemStatus.DONE.value, 'optional property')
    ]
    return ViewModel(items)

def test_return_done_items_only(item_view_model):

    # Get the expected list of items with 'Done' status
    expected_done_items = item_view_model.done_items

    assert item_view_model.done_items == expected_done_items
    assert len(expected_done_items) == 1
    assert expected_done_items[0].id == '4'
    for item in expected_done_items:
        assert item.status == ItemStatus.DONE.value

def test_return_in_progress_items_only(item_view_model):
    
    # Get the expected list of items with 'In Progress' status
    expected_progress_items = item_view_model.progress_items

    assert item_view_model.progress_items == expected_progress_items
    assert len(expected_progress_items) == 2
    assert expected_progress_items[0].id == '2'
    for item in expected_progress_items:
        assert item.status == ItemStatus.PROGRESS.value


def test_return_todo_items_only(item_view_model):

    # Get the expected list of items with 'To do' status
    expected_todo_items = item_view_model.todo_items

    assert item_view_model.todo_items == expected_todo_items
    assert len(expected_todo_items) == 1
    assert expected_todo_items[0].id == '1'
    for item in expected_todo_items:
        assert item.status == ItemStatus.TODO.value
