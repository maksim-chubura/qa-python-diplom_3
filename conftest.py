import pytest
from urls import Urls
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeed
from pages.forgot_password_page import ForgotPasswordPage
from helpers import *


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

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.order_feed = OrderFeed(driver)
        self.forgot_password = ForgotPasswordPage(driver)

        self.main_page.click_login_button()
        self.login_page.fill_email(EMAIL)
        self.login_page.fill_password(PASSWORD)
        self.login_page.click_enter_button()
        assert self.main_page.is_main_page(), "Не удалось войти в аккаунт"