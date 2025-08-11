import allure
from conftest import BaseTest

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