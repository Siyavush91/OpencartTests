from locators import MainPage
from locators import ProductPage
from locators import Alerts
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_elements_by_css_selector1(browser):
    navbar_items = browser.find_elements_by_css_selector(MainPage.nav_top_right)
    for item in navbar_items:
        ActionChains(browser).move_to_element(item).pause(1).perform()


def test_elements_by_class(browser):
    credit_type_1 = browser.find_element_by_class_name(MainPage.nav_top_left).click()


def test_element_by_class_name_selector(browser):
    browser.find_element_by_class_name(MainPage.promoblock).click()
    browser.find_element_by_class_name("breadcrumb")


def test_element_search(browser):
    search = browser.find_element_by_name(MainPage.search)
    search.click()
    search.clear()
    search.send_keys('1')
    search.send_keys(Keys.ENTER)


def test_elements_by_css_selector2(browser):
    navbar_items = browser.find_elements_by_css_selector(MainPage.footer_elements)
    for item in navbar_items:
        ActionChains(browser).move_to_element(item).pause(1).perform()


def test_add_to_wish_list(browser):
    browser.find_element_by_class_name(MainPage.promoblock).click()
    browser.find_element_by_xpath(ProductPage.add_to_wish_list).click()
    browser.find_element_by_xpath(Alerts.add_to_wish_alert)
