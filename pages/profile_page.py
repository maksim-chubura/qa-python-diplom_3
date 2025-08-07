import allure
from pages.base_page import BasePage
from locators.profile_page_locators import ProfilePageLocators
from urls import *
from selenium.common.exceptions import TimeoutException

class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step("Перейти в раздел 'История заказов'")
    def click_order_history(self):
        link = self.wait_for_clickable(ProfilePageLocators.ORDER_HISTORY_LINK)
        link.click()

    @allure.step("Нажать кнопку 'Выход'")
    def click_logout_button(self):
        button = self.wait_for_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        button.click()

    @allure.step("Проверяем, что мы на странице личного кабинета")
    def is_profile_page(self):
        return self.get_element_text(ProfilePageLocators.PROFILE_TEXT)
    
    @allure.step("Проверяем, что мы на странице истории заказов")
    def is_order_history_page(self):
        return "order-history" in self.driver.current_url
    
    @allure.step("Дожидаемся загрузки страницы")
    def wait_load_page(self):
        self.wait_for_visibility(ProfilePageLocators.LOGIN_BUTTON)
        
    @allure.step("Находим последний элемент списка заказов и копирует номер заказа")
    def scroll_to_last_order_and_get_number(self):
        try:
            last_order_item = self.wait_for_element(ProfilePageLocators.LAST_ORDER_ITEM)
            order_number_element = last_order_item.find_element(*ProfilePageLocators.LAST_ORDER_NUMBER)
            order_number = order_number_element.text
            print(f"Найден номер заказа: {order_number}")
            return order_number
        except TimeoutException:
            print("Не удалось найти последний элемент заказа или номер заказа после ожидания.")
            return None
        except Exception as e:
            print(f"Ошибка при копировании номера заказа: {e}")
            return None