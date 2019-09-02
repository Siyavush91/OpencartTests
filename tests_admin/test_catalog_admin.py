import pytest

from selenium.webdriver import ActionChains
from selenium.webdriver.common.alert import Alert

from locators import Login
from locators import Catalog
from locators import Alerts


@pytest.fixture(scope="session")
def open_login_page(browser, request):
    """
        Открытие страницы авторизации
    """
    url = '/admin/'
    return browser.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture(scope="function")
def login(browser, request):
    """
        Логин в админке
    """
    browser.find_element(*Login.user_name).send_keys("admin")
    browser.find_element(*Login.password_field).send_keys("25191")
    browser.find_element(*Login.login_button).click()



@pytest.mark.usefixtures("open_login_page")
class TestCreateProducts:

    @pytest.mark.usefixtures("login")
    def test_open_catalog(self, browser):
        """
        Тест открытия экрана авторизация
        """

        catalog_menu = browser.find_element_by_css_selector(Catalog.main_menu)
        catalog_menu.click()
        catalog_menu.find_element_by_link_text(Catalog.products).click()


    def test_add_new(self, browser):
        """
        Тест добавления нового продукта
        """
        browser.find_element_by_xpath(Catalog.add_new_product).click()
        browser.find_element_by_name(Catalog.product_name_field).send_keys("IphoneXR")
        browser.find_element_by_xpath(Catalog.product_description).send_keys("Some text")
        browser.find_element_by_name(Catalog.meta_tag_title).send_keys("Iphone XR")
        browser.find_element_by_xpath(Catalog.data_tab).click()
        browser.find_element_by_name(Catalog.model_field).send_keys("10R")
        browser.find_element_by_xpath(Catalog.save_button).click()
        assert browser.find_elements_by_xpath(Alerts.add_to_wish_alert)


    def test_edit(self, browser):
        """
            Тестирование редактирования первого продукта из списка
        """
        browser.find_element_by_xpath(Catalog.edit_product).click()
        nav_tab = browser.find_elements_by_css_selector(Catalog.product_nav_tabs)
        for item in nav_tab:
            ActionChains(browser).move_to_element(item).pause(1).perform()
        browser.find_element_by_xpath(Catalog.save_button).click()
        assert browser.find_elements_by_xpath(Alerts.add_to_wish_alert)


    def test_delete(self, browser):
         """
            Тест удаления добавленного продукта
         """
         browser.find_element_by_name(Catalog.product_name_filter).send_keys("IphoneXR")
         browser.find_element_by_xpath(Catalog.filter_button).click()
         browser.find_element_by_xpath(Catalog.product_check_box).click()
         browser.find_element_by_xpath(Catalog.delete_button).click()
         Alert(browser).accept()
