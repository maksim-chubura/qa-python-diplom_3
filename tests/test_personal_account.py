import pytest
import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_feed_page import OrderFeed
from helpers import *

class BaseTest: 

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)
        self.login_page = LoginPage(driver)
        self.profile_page = ProfilePage(driver)
        self.order_feed = OrderFeed(driver)

        self.main_page.click_login_button()
        self.login_page.fill_email(EMAIL)
        self.login_page.fill_password(PASSWORD)
        self.login_page.click_enter_button()
        assert self.main_page.is_main_page(), "Не удалось войти в аккаунт"

@allure.feature("Личный кабинет")
class TestProfile(BaseTest):
    
    @allure.title("Переход личный кабинет")
    def test_go_to_profile_page(self):
        self.main_page.click_profile_button()
        assert self.profile_page.is_profile_page(), "Не удалось войти в личный кабинет"

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_orders_history(self):
        self.main_page.click_profile_button()
        self.profile_page.click_order_history()
        assert self.profile_page.is_order_history_page(), "Не удалось открыть историю заказов"

    @allure.title("Выход из аккаунта")
    def test_logout(self):
        self.main_page.click_profile_button()
        self.profile_page.click_logout_button()
        self.profile_page.wait_load_page()
        assert self.login_page.is_login_page(), "Не удалось выйти из личного кабинета"