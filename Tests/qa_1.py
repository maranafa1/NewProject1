import pytest
from selene import Browser, by, have, config
import time

from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

def test_open_registration_page():
    browser.open('http://opencart.qatestlab.net/')

    browser.element(by.text('My Account')).click()
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/register"]').click()

    browser.element('[name="firstname"]').type('Edgar')
    browser.element('[name="lastname"]').type('1234')
    browser.element('[name="email"]').type('50125@friends.com')
    browser.element('[name="telephone"]').type('1515')
    browser.element('[name="password"]').type('12345pass')
    browser.element('[name="confirm"]').type('12345pass')

    browser.element('[href="http://opencart.qatestlab.net/index.php?route=information/information/agree&information_id=3"]').click()

    browser.element('[value="Continue"]').click()


def test_open_registration_page():
    browser.open('http://opencart.qatestlab.net/')

    browser.element(by.text('My Account')).click()
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/register"]').click()


def test_login():
    browser.element(by.text('My Account')).click()
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=account/login"]').click()

    browser.element('[name="email"]').type('50125@friends.com')
    browser.element('[name="password"]').type('12345pass')
    browser.element('[#top-links > ul > li > ul > li:nth-child(2) > a]').type('12345pass')

    time.sleep(5)
    browser.element('[value="Login"]').click()

def test_search_product():
    browser.open('http://opencart.qatestlab.net/')

    search_input = browser.element('[name="search"]').type('easipet')
    browser.element('#search > button').click()
    time.sleep(5)
    search_results = browser.all('.product-layout')
    assert len(search_results) > 0, "No search results found"

def test_add_product():
    browser.open('http://opencart.qatestlab.net/')
    s('[href="http://opencart.qatestlab.net/index.php?route=product/category&path=31"]').click()
    s('#content > div:nth-child(2) > div:nth-child(3) > div > div.content > div > h4 > a').click()
    ss('.sbHolder .sbToggle')[0].click()
    time.sleep(2)
    s('[href="#19"]').click()
    time.sleep(2)
    ss('.sbHolder .sbToggle')[1].click()
    time.sleep(2)
    s('[href="#22"]').click()
    time.sleep(2)
    s('#button-cart.btn-primary').click()
    time.sleep(2)
    s('#cart-total2').should(have.text('1'))

def test_shopping_cart():
    browser.open('http://opencart.qatestlab.net/')
    time.sleep(5)
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=product/category&path=31"]').click()
    time.sleep(5)
    browser.element('[href="http://opencart.qatestlab.net/index.php?route=product/product&path=31&product_id=34"]').click()
    time.sleep(5)
    browser.element('[href="#tab-specification"]').click()
    time.sleep(5)
    browser.element('.counter.counter-plus.material-design-add186').click()
    time.sleep(5)
    browser.element('#button-cart.btn-primary').click()
    time.sleep(5)
