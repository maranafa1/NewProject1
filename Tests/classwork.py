

import time
from itertools import count

from selene import by
from selene.support.conditions import have
from selene.support.shared import browser, config
from selene.support.shared.jquery_style import s

config.window_width = 1920
config.window_height = 1080

# Відкрити головну сторінку STEP IT Academy
browser.open('https://itstep.org/ru')

time.sleep(5)

# На мапі відкрити сторінку філії міста Кременчук
browser.all(('.marker-city cremenchug-small .marker-point')).first.click()

# Порахувати слово IT STEP на сторінці
page_text = browser.driver.page_source.swapcase()
count = page_text.count('it step')
print('Слово step повторяется на цій сторінці:', count, 'раз')





