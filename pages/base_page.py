from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import logging

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_page_load(self):
        self.wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")

    # Ждёт появления элемента в DOM
    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def wait_for_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    # Ждёт, пока элемент станет кликабельным
    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    # Кликает по элементу, ожидая его готовности
    def click(self, locator):  
        element = self.wait_for_clickable(locator)
        element.click()
    
    # Ждёт, пока элемент станет видимым
    def wait_for_visibility(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    # Ждёт, пока элемент станет невидимым
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    # Заполняет поле
    def send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    # Получает текст элемента, после его видимости
    def get_element_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text
    
    # Находит элемент на странице
    def find_element(self, locator):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            print(f"Элемент с локатором {locator} не найден. Ошибка: {e}")
            raise
    
    # Перемещает элемент
    def drag_and_drop(self, drag, drop):
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    # Прокручивает страницу до элемента
    def scroll_into_view(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)