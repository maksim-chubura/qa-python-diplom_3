import allure
from selenium.common.exceptions import TimeoutException
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
import logging
from urls import *

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = logging.getLogger(__name__)

    @allure.step("Дождаться полной загрузки страницы")
    def wait_load_page(self):
        self.driver.get(Urls.MAIN_PAGE)
        self.wait_for_page_load()

    @allure.step("Нажать на кнопку 'Конструктор'")
    def click_constructor_button(self):
        button = self.wait_for_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        button.click()

    @allure.step("Переход в раздел 'Конструктор'")
    def go_to_constructor(self):
        self.click_constructor_button()
        self.get_collect_burger_text()

    @allure.step("Получить текст 'Соберите бургер'")
    def get_collect_burger_text(self):
        return self.get_element_text(MainPageLocators.COLLECT_BURGER_TITLE)

    @allure.step("Нажать на кнопку 'Личный кабинет'")
    def click_profile_button(self):
        button = self.wait_for_visibility(MainPageLocators.PROFILE_BUTTON)
        button.click()

    @allure.step("Нажать на кнопку 'Войти в аккаунт'")
    def click_login_button(self):
        button = self.wait_for_clickable(MainPageLocators.LOGIN_BUTTON)
        button.click()

    @allure.step("Клик на ингредиент в конструкторе бургеров")
    def click_to_ingredient(self):
        element = self.wait_for_clickable(MainPageLocators.INGREDIENT)
        element.click()

    @allure.step("Получить текст 'Детали ингредиента'")
    def get_ingresient_details_text(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_DETAILS_TEXT)

    @allure.step("Проверка отображения модального окна ингредиента")
    def check_modal_window_ingredient_visibility(self):
        return self.wait_for_element(MainPageLocators.INGREDIENT_MODAL_WINDOW)
    
    @allure.step("Закрытие модального окна ингредиента с помощью крестика")
    def close_modal_window_ingredient(self):
        element = self.wait_for_clickable(MainPageLocators.CLOSE_MODAL_BUTTON)
        element.click()
    
    @allure.step("Проверяем, что мы на главной странице")
    def is_main_page(self):
        return self.wait_for_clickable(MainPageLocators.STELLAR_BURGERS_LOGO)
    
    @allure.step("Добавление краторной булки в заказ")
    def add_crater_bun_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.CRATER_BUN)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.CRATER_BUN_IN_ORDER)

    @allure.step("Добавление флюоресцентной булки в заказ")
    def add_fluorescent_bun_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.FLUORESCENT_BUN)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.FLUORESCENT_BUN_IN_ORDER)

    @allure.step("Добавление фирменного соуса Space Sauce в заказ")
    def add_space_sauce_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.SPACE_SAUCE)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.SPACE_SAUCE_IN_ORDER)

    @allure.step("Добавление соуса с шипами в заказ")
    def add_antarian_flatwalker_spiked_sauce_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.ANTARIAN_FLATWALKER_SPIKED_SAUCE)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.ANTARIAN_FLATWALKER_SPIKED_SAUCE_IN_ORDER)

    @allure.step("Добавление говяжего метеорита в заказ")
    def add_beef_meteorite_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.BEEF_METEORITE)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.BEEF_METEORITE_IN_ORDER)

    @allure.step("Добавление биокотлеты из марсианской Магнолии в заказ")
    def add_mars_magnolia_boicotelet_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.MARS_MAGNOLIA_BIOCOTELET)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.MARS_MAGNOLIA_BIOCOTELET_IN_ORDER)

    @allure.step("Добавление хрустящих минеральных колец в заказ")
    def add_crispy_mineral_rings_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.CRISPY_MINERAL_RINGS)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.CRISPY_MINERAL_RINGS_IN_ORDER)

    @allure.step("Добавление сыра с астероидной плесенью в заказ")
    def add_cheese_with_asteroid_mold_to_order(self):
        drag = self.wait_for_clickable(MainPageLocators.CHEESE_WITH_ASTEROID_MOLD)
        drop = self.wait_for_visibility(MainPageLocators.RESULT_ORDER)
        self.drag_and_drop(drag, drop)
        self.wait_for_visibility(MainPageLocators.CHEESE_WITH_ASTEROID_MOLD_IN_ORDER)

    @allure.step("Оформить заказ")
    def make_order(self):
        button = self.wait_for_clickable(MainPageLocators.ORDER_BUTTON)
        button.click()

    @allure.step("Получить номер заказа")
    def get_odrer_id(self):
        try:
            order_number_element = self.wait_for_element(MainPageLocators.ORDER_ID)
            order_number = order_number_element.text
            return order_number
        except Exception as e:
            print(f"Не удалось получить номер заказа: {e}")
            return ""

    @allure.step("Оформление заказа")
    def create_order(self):
        self.add_crater_bun_to_order()
        self.add_space_sauce_to_order()
        self.add_beef_meteorite_to_order()

    @allure.step("Оформление альтернативного заказа")
    def create_other_order(self):
        self.add_fluorescent_bun_to_order()
        self.add_antarian_flatwalker_spiked_sauce_to_order()
        self.add_space_sauce_to_order()
        self.add_mars_magnolia_boicotelet_to_order()
        self.add_beef_meteorite_to_order()
        self.add_crispy_mineral_rings_to_order()
        self.add_cheese_with_asteroid_mold_to_order()
        self.make_order()
        self.is_order_accepted()

    @allure.step("Проверяем, что заказ оформлен")
    def is_order_accepted(self):
        self.wait_for_visibility(MainPageLocators.ORDER_READY)
        return True

    @allure.step("Проверяет, что номер элемента не равен 9999")
    def order_id_in_modal_is_not_9999(self):
        try:
            element = self.wait_for_element(MainPageLocators.ORDER_ID)
            return element.text != '9999'
        except NoSuchElementException:
            self.logger.warning("Элемент с номером заказа не найден в модальном окне.")
            return False
        except Exception as e:
            self.logger.exception(f"Ошибка при проверке номера заказа в модальном окне: {e}")
            return False
        
    @allure.step("Ожидает, пока модальное окно загрузится и номер заказа будет отличен от 9999")
    def wait_for_valid_order_id_in_modal(self):
        try:
            self.wait.until(lambda driver: self.order_id_in_modal_is_not_9999())  # Используем метод класса
            return True
        except TimeoutException:
            self.logger.warning("Номер заказа в модальном окне не изменился за отведенное время.")
            return False
        except Exception as e:
            self.logger.exception(f"Непредвиденная ошибка при ожидании номера заказа в модальном окне: {e}")
            return False

    @allure.step("Закрываем окно с оформленным заказом")
    def click_button_close_order_window(self):
        button = self.wait_for_clickable(MainPageLocators.CLOSE_ORDER_WINDOW_BUTTON)
        self.driver.execute_script("arguments[0].click();", button)
    
    @allure.step("Получить каунтер ингридиента")
    def get_ingredient_counter(self):
        try:
            return int(self.find_element(MainPageLocators.INGREDIENT_COUNTER).text)
        except Exception:
            return 0