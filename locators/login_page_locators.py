from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")
    SHOW_PASSWORD = (By.XPATH, "//div[@class='input__icon input__icon-action']")
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")