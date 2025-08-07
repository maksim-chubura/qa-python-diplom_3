import pytest
import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeed
from pages.login_page import LoginPage
from helpers import *

class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.main_page = MainPage(driver)
        self.order_feed = OrderFeed(driver)
        self.login_page = LoginPage(driver)
        yield

@allure.feature("Проверка основного функционала")
class TestMainPage(BaseTest):

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_order_feed(self):
        self.order_feed.click_order_feed_button()
        assert "Лента заказов" == self.order_feed.get_order_feed_text(), "Не удалось перейти на страницу ленты заказов"

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self):
        self.order_feed.click_order_feed_button()
        self.order_feed.get_order_feed_text()
        self.main_page.click_constructor_button()
        assert "Соберите бургер" == self.main_page.get_collect_burger_text(), "Не удалось перейти в раздел Конструктор"
    
    @allure.title("Проверка отображения модального окна с информацией об ингредиенте")
    def test_click_to_ingredient_show_modal_ingredient_window(self):
        self.main_page.click_to_ingredient()
        self.main_page.check_modal_window_ingredient_visibility()
        assert self.main_page.get_ingresient_details_text(), 'Модальное окно детальной информации об ингредиенте не отображается'

    @allure.title("Закрытие модального окна с информацией об ингредиенте")
    def test_close_modal_ingredient_window(self):
        self.main_page.click_to_ingredient()
        self.main_page.check_modal_window_ingredient_visibility()
        self.main_page.close_modal_window_ingredient()
        assert "Соберите бургер" == self.main_page.get_collect_burger_text(), "Не удалось зыкрыть модальное окно"

    @allure.title("Увеличение каунтера ингредиента, при добавлении его в заказ")
    def test_increasing_counter(self):
        initial_counter = self.main_page.get_ingredient_counter()
        print(f"Начальное значение счетчика: {initial_counter}")
        self.main_page.add_fluorescent_bun_to_order()
        final_counter = self.main_page.get_ingredient_counter()
        print(f"Конечное значение счетчика: {final_counter}")
        assert final_counter > initial_counter

    @allure.title("Создание заказа")
    def test_create_order(self):
        self.main_page.click_login_button()
        self.login_page.fill_email(EMAIL)
        self.login_page.fill_password(PASSWORD)
        self.login_page.click_enter_button()
        self.main_page.is_main_page()
        self.main_page.create_order()
        self.main_page.make_order()
        assert self.main_page.is_order_accepted(), "Не удалось оформить заказ"