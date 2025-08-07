import pytest
from urls import Urls
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Choose browser: chrome or firefox"
    )

@pytest.fixture
def driver(request):
    browser = request.config.getoption("browser")   
    if browser == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError("Unsupported browser")

    driver.maximize_window()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()