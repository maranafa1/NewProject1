from selene import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
import time

def test_auth():
    browser.open('https://www.google.com.ua/')
    browser.driver.maximize_window()
    s(by.name('q')).type('dressa').press_enter()
    time.sleep(2)
    ss("//span[@data-dtld='dressa.com.ua']")[0].click()
    time.sleep(2)
    ss("//div[@id='profile__button']")[0].click()
    time.sleep(2)
    ss(by.text('Увійти / Зареєструватися'))[0].click()
    time.sleep(2)
    s("#regularUserLogin").type("irina071165@gmail.com").press_tab()
    time.sleep(2)
    s("#regularUserPassword").type().press_enter()

