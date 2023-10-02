import time

from todomvc_testing.model import todos


def test_open():
    todos.maximize_window()
    todos.open_tasks('1', '2', '3')
    time.sleep(2)
    todos.should_be('1', '2', '3')
    time.sleep(2)
    todos.edit('3', '3++')
    time.sleep(2)
    todos.completed('3++')
    time.sleep(3)
    todos.clear_completed()
    time.sleep(2)
    todos.should_be('1', '2')
    time.sleep(2)
    todos.edit('1','one')
    time.sleep(6)
    todos.delete('2')
    time.sleep(2)
    todos.should_be('one')
    time.sleep(2)
    todos.completed('one')
    time.sleep(2)
    todos.delete('one')
    time.sleep(2)
    todos.add_tasks('Test_completed')
    time.sleep(2)
    todos.should_be('Test_completed')
    time.sleep(2)

