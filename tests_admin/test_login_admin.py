import pytest
import time

from locators import Login


@pytest.fixture(scope="session")
def open_login_page(browser , request):
    url = '/admin/'
    return browser.get("".join([request.config.getoption("--url"), url]))


@pytest.fixture(scope="function")
def login(browser):
    ins_user_name = browser.find_element(*Login.user_name).send_keys("admin")
    ins_password = browser.find_element(*Login.password_field).send_keys("25191")
    login_button = browser.find_element(*Login.login_button).click()


@pytest.mark.usefixtures("open_login_page")
class TestLogin:

    @pytest.mark.usefixtures("login")
    def test_login(self, browser):
        print(browser.current_url)
        assert "dashboard" in browser.current_url
