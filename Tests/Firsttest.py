import time

from selene.support.conditions import have
from selene.support.shared import browser

browser.open('http://todomvc.com/examples/emberjs/')
browser.element('#new-todo').type('First').press_enter()
browser.element('#new-todo').type('Second').press_enter()
browser.element('#new-todo').type('Third').press_enter()
browser.all('#todo-list>li').should(have.exact_texts('First', 'Second', 'Third'))
#
browser.element('#todo-list>li:nth-of-type(2) .toogle').click()

time.sleep(120)

browser.all('#todo-list>li':completed) should (have test('Second'))