from selene import by
from selene.support.conditions import have
from selene.support.shared import browser

from todomvc_testing.model import todos

todos.open()

# Відкриваємо браузер
browser.open('https://todomvc4tasj.herokuapp.com')

# Створюємо першу задачу
browser.element('#new-todo').type('First').press_enter()

# Створюємо другу задачу
browser.element('#new-todo').type('Second').press_enter()

# Створюємо третю задачу
browser.element('#new-todo').type('Third').press_enter()

# Перевіряємо наявність задач в списку
browser.all('#todo-list>li').should(have.exact_texts('First', 'Second', 'Third'))

# Видалити 2(другу) задачу зі списку
browser.element('#todo-list>li:nth-of-type(2) .toggle').click()

# Завершуємо всі задачі
browser.element(by.text('Completed')).click()

# Перевірка завершеної другої задачі
browser.all('#todo-list>li.completed').should(have.texts('Second'))

# Перевірка незавершених задач
browser.element(by.text('Active')).click()

# Закреслюємо всі задачі
browser.element('#toggle-all').click()

# Очистка листа задач
browser.element(by.text('Clear completed')).click()

input('Press Enter')
browser.close()


