import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators

class OrderFeed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Нажать на кнопку 'Лента заказов'")
    def click_order_feed_button(self):
        button = self.wait_for_clickable(OrderFeedPageLocators.ORDER_FEED_BUTTON)
        button.click()

    @allure.step("Дождаться загрузки страницы 'Лента заказов'")
    def wait_load_order_feed_page(self):
        return self.wait_for_visibility(OrderFeedPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Переход в ленту заказов")
    def go_to_order_feed(self):
        self.click_order_feed_button()
        self.wait_load_order_feed_page()

    @allure.step("Нажать на первый в списке заказ")
    def click_first_order_in_order_feed(self):
        element = self.wait_for_clickable(OrderFeedPageLocators.FIRST_LINK_ORDER_FEED)
        element.click()

    @allure.step("Дождаться отображения модального окна с деталями заказа")
    def wait_load_modal_window_order_details(self):
        return self.wait_for_element(OrderFeedPageLocators.MODAL_WINDOW_ORDER_DETAILS)
    
    @allure.step("Проверить отображение модального окна по номеру заказа")
    def get_number_order(self):
        return self.get_element_text(OrderFeedPageLocators.NUMBER_ORDER)

    @allure.step("Проверить назание раздела 'Лента заказов'")
    def get_order_feed_text(self):
        return self.get_element_text(OrderFeedPageLocators.ORDER_FEED_TITLE)
    
    @allure.step("Получить количество заказов за все время")
    def get_orders_count_for_all_time(self):
        self.wait_for_visibility(OrderFeedPageLocators.ALL_ORDERS_COUNTER)
        counters = self.wait_for_elements(OrderFeedPageLocators.ALL_ORDERS_COUNTER)
        try:
            first_count_element = counters[0]
            second_count_element = counters[1]
            first_count = int(first_count_element.text)
            second_count = int(second_count_element.text)
            return first_count, second_count
        except IndexError:
            return 0, 0
        except ValueError:
            return 0, 0
        
    @allure.step("Получить количество заказов за сегодня")
    def get_orders_count_for_today(self):
        self.wait_for_visibility(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)
        counters = self.wait_for_elements(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)
        try:
            first_count_element = counters[0]
            second_count_element = counters[1]
            first_count = int(first_count_element.text)
            second_count = int(second_count_element.text)
            return first_count, second_count
        except IndexError:
            return 0, 0
        except ValueError:
            return 0, 0
    
    @allure.step("Получить номер заказа в работе")
    def get_order_number_in_progress(self):
        element = self.wait_for_visibility(OrderFeedPageLocators.ORDER_IN_PROGRESS)
        if element:
            return element.text
        else:
            return "0"
            
    @allure.step("Получает номер заказа из первого элемента в ленте заказов.")
    def get_order_number_from_feed(self):
        try:
            order_feed_element = self.wait_for_element(OrderFeedPageLocators.ORDER_FEED_ITEM_LOCATOR)
            order_number_feed = order_feed_element.text
            return order_number_feed
        except Exception as e:
            print(f"Не удалось получить номер заказа из ленты: {e}")
            return None
        
    @allure.step("Прокручивает страницу до количества заказов за сегодня")
    def scroll_to_count_for_today(self):
        self.scroll_into_view(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)
        self.wait_for_visibility(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)