from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest


import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="choose your browser")
    parser.addoption("--url", "-U", action="store", default="http://localhost:8888/Opencart/opencart-3.0.3.2/upload/", help="choose your browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    browser_param = request.config.getoption("--browser")
    if browser_param == "chrome":
        capabilities = DesiredCapabilities.CHROME
        options = webdriver.ChromeOptions()
        options.add_argument("--kiosk")
        dr = webdriver.Chrome(options=options)
    elif browser_param == "firefox":
        capabilities = DesiredCapabilities.FIREFOX
        options = webdriver.FirefoxOptions()
        dr = webdriver.Firefox(options=options)
        dr.maximize_window()
    elif browser_param == "safari":
        dr = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")

    dr.implicitly_wait(10)
    request.addfinalizer(dr.close)
    dr.get(request.config.getoption("--url"))

    return dr
