from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_ACTIVE_INPUT = (By.XPATH, "//label[contains(@class, 'input__placeholder-focused') and text()='Пароль']")