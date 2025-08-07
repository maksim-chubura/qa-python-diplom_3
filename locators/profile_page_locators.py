from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_TEXT = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[@href='/account/order-history']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    LAST_ORDER_NUMBER = (By.CSS_SELECTOR, "p.text.text_type_digits-default")
    LAST_ORDER_ITEM = (By.XPATH, "//ul[@class='OrderHistory_profileList__374GU OrderHistory_list__KcLDB']/li[last()]")