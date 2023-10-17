from todo_app.data.itemStatus import ItemStatus
from todo_app.data.todo_item import TodoItem
from todo_app.views.view_model import ViewModel


def test_return_done_items_only():
    items = [
        TodoItem('1', 'task 1', ItemStatus.TODO.value,
                 'description of task 1'),
        TodoItem('2', 'task 2', ItemStatus.TODO.value, ''),
        TodoItem('3', 'task 3', ItemStatus.PROGRESS.value, ''),
        TodoItem('4', 'task 4', ItemStatus.DONE.value, 'optional property')
    ]
    item_view_model = ViewModel(items)

    # Get the expected list of items with 'Done' status
    expected_done_items = [
        item for item in items if item.status == ItemStatus.DONE.value]

    assert item_view_model.done_items == expected_done_items
    assert len(expected_done_items) == 1


def test_return_in_progress_items_only():
    items = [
        TodoItem('1', 'task 1', ItemStatus.TODO.value,
                 'description of task 1'),
        TodoItem('2', 'task 2', ItemStatus.PROGRESS.value, ''),
        TodoItem('3', 'task 3', ItemStatus.PROGRESS.value, ''),
        TodoItem('4', 'task 4', ItemStatus.DONE.value, 'optional property')
    ]
    item_view_model = ViewModel(items)

    # Get the expected list of items with 'In Progress' status
    expected_progress_items = [
        item for item in items if item.status == ItemStatus.PROGRESS.value]

    assert item_view_model.progress_items == expected_progress_items
    assert len(expected_progress_items) == 2


def test_return_todo_items_only():
    items = [
        TodoItem('1', 'task 1', ItemStatus.TODO.value,
                 'description of task 1'),
        TodoItem('2', 'task 2', ItemStatus.TODO.value, ''),
        TodoItem('3', 'task 3', ItemStatus.PROGRESS.value, ''),
        TodoItem('4', 'task 4', ItemStatus.DONE.value, 'optional property')
    ]
    item_view_model = ViewModel(items)

    # Get the expected list of items with 'To do' status
    expected_todo_items = [
        item for item in items if item.status == ItemStatus.TODO.value]

    assert item_view_model.todo_items == expected_todo_items
    assert len(expected_todo_items) == 2
