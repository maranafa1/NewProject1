import time

from selene import browser, by
from selene.support.shared import browser


def test_open_friends():
    browser.open('https://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('#stuck > div > div > div > div > div > div > div > div > ul > li:nth-child(10) > a').click()
    time.sleep(5)
    browser.element('content > div > div:nth-child(1) > a').click()
    time.sleep(5)
    browser.element('#input-firstname').type('12345').press_enter()
    time.sleep(5)
    browser.element('#input-lastname').type('12345').press_enter()
    time.sleep(5)
    browser.element('#input-email').type('irina@gmail.com').press_enter()
    time.sleep(3)
    browser.element('#input-telephone').type('123456789').press_enter()
    time.sleep(3)
    browser.element('#input-password').type('12345qwert').press_enter()
    time.sleep(3)
    browser.element('#input-confirm').type('12345qwert').press_enter()
    time.sleep(5)
    browser.element(by.css('[type="radio"][name="agree"]')).click()
    time.sleep(5)

    browser.element(by.css('[value="Продолжить"]')).click()
    time.sleep(5)


def test_authorization():
    browser.open('https://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('#stuck > div > div > div > div > div > div > div > div > ul > li:nth-child(10) > a').click()
    time.sleep(5)
    browser.element('content > div > div:nth-child(1) > a').click()
    time.sleep(5)
    browser.element('#input-firstname').type('12345').press_enter()
    time.sleep(5)
    browser.element('#input-lastname').type('12345').press_enter()
    time.sleep(5)
    browser.element('#input-email').type('irina@gmail.com').press_enter()
    time.sleep(3)
    browser.element('#input-telephone').type('123456789').press_enter()
    time.sleep(3)
    browser.element('#input-password').type('12345qwert').press_enter()
    time.sleep(3)
    # browser.element(by.css('[value="Войти"]')).click
    # time.sleep(5)


# def test_search():
#     browser.element('http://opencart.qatestlab.net/')
#     time.sleep(5)
