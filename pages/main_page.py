from selenium.webdriver.common.by import By
from helpers import URLs
import allure
from .base_page import BasePage


class MainPage(BasePage):
    # Локаторы
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_RoadMap')]//button[text()='Заказать']")

    def get_main_page(self):
        self.get_page(URLs.BASE_URL)

    @allure.step("Клик по верхней кнопке и ожидание перехода")
    def click_order_button_top(self):
        self.click_on(self.ORDER_BUTTON_TOP)
        self.wait_for_page(URLs.ORDER_PAGE)

    @allure.step("Клик по нижней кнопке и ожидание перехода")
    def click_order_button_bottom(self):
        self.scroll_to(self.ORDER_BUTTON_BOTTOM)
        self.click_on(self.ORDER_BUTTON_BOTTOM)
        self.wait_for_page(URLs.ORDER_PAGE)
