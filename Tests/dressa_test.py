from selene import by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss
import time

def test_auth():
    browser.driver.maximize_window()
    browser.open('https://dressa.com.ua/uk/')
    # browser.driver.maximize_window()
    # s(by.name('q')).type('dressa').press_enter()
    # time.sleep(2)
    # ss("//span[@data-dtld='dressa.com.ua']")[0].click()
    # time.sleep(2)
    # ss('.categories__inner_item.ng-star-inserted')[0].click()
    ss("//div[@id='profile__button']")[0].click()
    time.sleep(2)
    ss(by.text('Увійти / Зареєструватися'))[0].click()
    time.sleep(2)
    s("#regularUserLogin").type("irina071165@gmail.com").press_tab()
    time.sleep(2)
    s("#regularUserPassword").type("n!vw47Y").press_enter()
    time.sleep(5)
    # ss(by.text('Шапки'))[1].click()
    ss('.header__nav .ng-tns-c32-0.ng-star-inserted')[12].click()
    ss('.categories__inner_item.ng-star-inserted')[0].click()
    # time.sleep(10)
    s('.ng-star-inserted [dressavendor="56133"]').click()
    time.sleep(2)
    s("//div[@class='button__inner button__inner--buy']").click()
    time.sleep(2)
    s("//div[@class='link__shopping_title']").click()
    time.sleep(2)
    s("//div[@class='button__inner button__inner--white']").click()
    time.sleep(2)
    ss(".counter__add")[0].click()
    time.sleep(2)
    s("//div[@class='icon__trash']").click()
    time.sleep(2)





