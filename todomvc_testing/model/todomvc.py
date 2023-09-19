
from selene import have, command
from selene.support.shared import browser

completed = have.css_class('completed')

class TodoMVC:
    def __init__(self):
        self.todo_list = browser.all('#todo-list>li')

    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com')
        # app_loaded = "return $._data($('#clear-completed')[0], 'events')".hasOwnProperty('click')"
        # browser.should(have.js_returned(True, app_loaded))
        #
    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

