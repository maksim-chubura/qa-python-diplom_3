import allure
from conftest import BaseTest
from helpers import *


@allure.feature("Восстановление пароля")
class TestForgotPassword(BaseTest):
    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password_page(self):
        self.main_page.click_profile_button()
        self.profile_page.click_logout_button()
        self.profile_page.wait_load_page()
        self.login_page.click_recover_password_link()
        assert self.forgot_password.is_forgot_password_page(), "Не удалось перейти на страницу восстановления пароля"

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_recover_button(self):
        self.main_page.click_profile_button()
        self.profile_page.click_logout_button()
        self.profile_page.wait_load_page()
        self.login_page.click_recover_password_link()
        self.forgot_password.fill_email(EMAIL)
        self.forgot_password.click_recover_button()
        assert self.forgot_password.is_forgot_password_page(), "Не удалось перейти на страницу восстановления пароля"


    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_hide_password(self):
        self.main_page.click_profile_button()
        self.profile_page.click_logout_button()
        self.profile_page.wait_load_page()
        self.login_page.fill_email(EMAIL)
        self.login_page.fill_password(PASSWORD)
        self.login_page.click_show_hide_password()
        assert self.forgot_password.get_show_password(), 'Поле ввода нового пароля не подсвечивается'