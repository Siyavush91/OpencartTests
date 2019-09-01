import time
import pytest
# import selenium.webdriver.common.alert.Alert

from selenium.webdriver import ActionChains

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
def login(browser):
    """
        Логин в админке
    """
    ins_user_name = browser.find_element(*Login.user_name).send_keys("admin")
    ins_password = browser.find_element(*Login.password_field).send_keys("25191")
    login_button = browser.find_element(*Login.login_button).click()


@pytest.mark.usefixtures("open_login_page")
class TestCreateProducts:

    @pytest.mark.usefixtures("login")
    def test_open_catalog(self, browser):
        """
            Атворизация в вдминке  Opencart
        """

        catalog_menu = browser.find_element_by_css_selector(Catalog.main_menu)
        catalog_menu.click()
        product_menu = catalog_menu.find_element_by_link_text(Catalog.products).click()
        time.sleep(2)


    def test_add_new(self, browser):
        """
        Тест добавления нового продукта
        """
        product_list = browser.find_element_by_xpath(Catalog.add_new_product).click()
        input_product_name = browser.find_element_by_name(Catalog.product_name_field).send_keys("IphoneXR")
        input_product_descript = browser.find_element_by_xpath(Catalog.product_description).send_keys("Some text")
        input_product_meta = browser.find_element_by_name(Catalog.meta_tag_title).send_keys("Iphone XR")
        open_data = browser.find_element_by_xpath(Catalog.data_tab).click()
        input_model = browser.find_element_by_name(Catalog.model_field).send_keys("10R")
        save_product = browser.find_element_by_xpath(Catalog.save_button).click()
        assert browser.find_elements_by_xpath(Alerts.add_to_wish_alert)
        time.sleep(5)


@pytest.mark.usefixtures("open_login_page")
class TestEditProducts:

    @pytest.mark.usefixtures("login")
    def test_open_catalog(self, browser):
        """
            Атворизация в вдминке  Opencart
        """

        catalog_menu = browser.find_element_by_css_selector(Catalog.main_menu)
        catalog_menu.click()
        product_menu = catalog_menu.find_element_by_link_text(Catalog.products).click()
        time.sleep(2)


    def test_edit(self, browser):
        """
            Тестирование редактирования первого продукта из списка
        """
        open_edit = browser.find_element_by_xpath(Catalog.edit_product).click()
        nav_tab = browser.find_elements_by_css_selector(Catalog.product_nav_tabs)
        for item in nav_tab:
            ActionChains(browser).move_to_element(item).pause(1).perform()
        save_product = browser.find_element_by_xpath(Catalog.save_button).click()
        assert browser.find_elements_by_xpath(Alerts.add_to_wish_alert)
        time.sleep(5)


# @pytest.mark.usefixtures("open_login_page")
# class TestDeleteProducts:
#
#     @pytest.mark.usefixtures("login")
#     def test_open_catalog(self, browser):
#         """
#             Атворизация в вдминке  Opencart
#         """
#         catalog_menu = browser.find_element_by_css_selector(Catalog.main_menu)
#         catalog_menu.click()
#         product_menu = catalog_menu.find_element_by_link_text(Catalog.products).click()
#         time.sleep(2)
#
#
#     # def test_delete(self,browser):


