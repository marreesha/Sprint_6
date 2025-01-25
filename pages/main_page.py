from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import URLs
import allure
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    order_button_top = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    order_button_bottom = (By.XPATH, "//div[contains(@class, 'Home_RoadMap')]//button[text()='Заказать']")

    def get_main_page(self):
        self.driver.get(URLs.BASE_URL)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(URLs.BASE_URL))

    @allure.step("Клик по верхней кнопке и ожидание перехода")
    def click_order_button_top(self):
        self.driver.find_element(*self.order_button_top).click()

    @allure.step("Клик по нижней кнопке и ожидание перехода")
    def click_order_button_bottom(self):
        order_button = self.driver.find_element(*self.order_button_bottom)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
        order_button.click()
