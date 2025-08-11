import allure
from pages.base_page import BasePage
from locators.forgot_password_page_locators import ForgotPasswordPageLocators

class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Заполнить поле 'Email'")
    def fill_email(self, email):
        self.send_keys(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step("Нажать кнопку 'Восстановить'")
    def click_recover_button(self):
        button = self.wait_for_clickable(ForgotPasswordPageLocators.RECOVER_BUTTON)
        button.click()
    
    @allure.step("Проверка подсветки поля нового пароля при нажатии 'Показать пароль'")
    def get_show_password(self):
        return self.wait_for_visibility(ForgotPasswordPageLocators.PASSWORD_ACTIVE_INPUT)
    
    @allure.step("Проверяем, что мы на странице восстановления пароля")
    def is_forgot_password_page(self):
        return "reset-password" in self.driver.current_url or "forgot-password" in self.driver.current_url