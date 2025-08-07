import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from urls import *

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить поле 'Eamil'")
    def fill_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Заполнить поле 'Пароль'")
    def fill_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажать на иконку глаза 'Показать/скрыт пароль'")
    def click_show_hide_password(self):
        logo = self.wait_for_clickable(LoginPageLocators.SHOW_PASSWORD)
        logo.click()

    @allure.step("Нажать кнопку 'Войти'")
    def click_enter_button(self):
        button = self.wait_for_clickable(LoginPageLocators.ENTER_BUTTON)
        button.click()

    @allure.step("Нажать на ссылку 'Восстановить пароль'")
    def click_recover_password_link(self):
        link = self.wait_for_clickable(LoginPageLocators.RECOVER_PASSWORD_BUTTON)
        link.click()
    
    @allure.step("Проверяем, что мы на странице авторизации")
    def is_login_page(self):
        return self.driver.current_url == Urls.LOGIN_URL