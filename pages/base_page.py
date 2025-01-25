from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator):
        """Метод для поиска элемента на странице"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Метод для поиска множества элементов"""
        return self.driver.find_elements(*locator)

    def click_on(self, locator):
        """Метод для клика по элементу"""
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """Метод для ввода текста в поле"""
        element = self.find_element(locator)
        element.clear()  # Очищаем поле перед вводом
        element.send_keys(text)

    def wait_for_page(self, url):
        """Метод ожидания появления страницы"""
        return self.wait.until(EC.url_to_be(url))

    def wait_for_element(self, locator):
        """Метод ожидания появления элемента на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        """Метод ожидания, чтобы элемент стал кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        """Метод ожидания видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, element):
        """Метод прокрутки страницы до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to(self, locator):
        """Метод прокрутки страницы до элемента"""
        element = self.find_element(locator)
        self.scroll_to_element(element)

    def get_page(self, url):
        """Метод вызова и ожидания загрузки страницы"""
        self.driver.get(url)
        self.wait_for_page(url)
