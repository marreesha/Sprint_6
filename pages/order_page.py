from selenium.webdriver.common.by import By
import random
import allure
from datetime import date
from helpers import URLs
from locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(BasePage):

    def get_order_page(self):
        self.get_page(URLs.ORDER_PAGE)

    @allure.step("Заполнение первой страницы формы заказа")
    def fill_first_order_form(self, name, surname, address, phone):
        """Функция для заполнения первой страницы"""
        self.send_keys(OrderPageLocators.NAME_INPUT_LOCATOR, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT_LOCATOR, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT_LOCATOR, address)
        self.select_random_metro_station()
        self.send_keys(OrderPageLocators.PHONE_INPUT_LOCATOR, phone)

    def select_random_metro_station(self):
        """Функция для случайного выбора станции метро"""
        self.click_on(OrderPageLocators.METRO_FIELD_LOCATOR)
        self.wait_for_element_to_be_visible(OrderPageLocators.METRO_FIELD_LOCATOR)
        metro_options = self.find_elements(OrderPageLocators.METRO_OPTIONS_LOCATOR)
        random_station = random.choice(metro_options)
        self.scroll_to_element(random_station)
        random_station.click()
        station_name = self.find_element(OrderPageLocators.METRO_FIELD_LOCATOR).get_attribute("value")
        allure.attach(station_name, name="station")

    @allure.step("Переход на следующую страницу формы заказа")
    def click_next_page(self):
        self.click_on(OrderPageLocators.NEXT_BUTTON_LOCATOR)

    @allure.step("Заполнение второй страницы формы заказа")
    def fill_second_order_form(self, delivery_date, comment):
        self.set_delivery_date(delivery_date)
        self.select_rental_period()
        self.select_scooter_color()
        self.send_keys(OrderPageLocators.COMMENT_INPUT_LOCATOR, comment)

    def set_delivery_date(self, delivery_date):
        """Функция для выбора даты заказа"""
        # Клик по полю даты, чтобы открыть календарь
        self.click_on(OrderPageLocators.DELIVERY_DATE_LOCATOR)
        self.send_keys(OrderPageLocators.DELIVERY_DATE_LOCATOR, delivery_date)
        # Динамический локатор для выбора нужной даты
        date_to_select = (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day') and text()='{int(delivery_date.split('.')[0])}']")
        self.click_on(date_to_select)

    def select_rental_period(self):
        """Функция для случайного выбора периода аренды"""
        self.click_on(OrderPageLocators.RENTAL_PERIOD_LOCATOR)
        rental_options = self.find_elements(OrderPageLocators.RENTAL_OPTIONS_LOCATOR)
        random_rental_period = random.choice(rental_options)
        self.scroll_to_element(random_rental_period)
        random_rental_period.click()
        rental_period = self.find_element(OrderPageLocators.RENTAL_PERIOD_LOCATOR).text
        allure.attach(rental_period, name="rental_period")

    def select_scooter_color(self):
        """Функция для случайного выбора цвета самоката"""
        color_options = self.find_elements(OrderPageLocators.COLOR_LOCATOR)
        random_color = random.choice(color_options)
        random_color.click()

    def set_order_information(self, order_data):
        name = order_data.get('name', 'Не указано')
        surname = order_data.get('surname', 'Не указано')
        address = order_data.get('address', 'Не указан')
        phone = order_data.get('phone', 'Не указан')
        delivery_date = order_data.get('delivery_date', date.today().strftime("%d.%m.%Y"))
        comment = order_data.get('comment', '')

        self.fill_first_order_form(name, surname, address, phone)
        self.click_next_page()
        self.fill_second_order_form(delivery_date, comment)

    @allure.step("Подтверждение заказа")
    def submit_order(self):
        self.click_on(OrderPageLocators.ORDER_BUTTON_LOCATOR)
        self.click_on(OrderPageLocators.CONFIRM_BUTTON_LOCATOR)

    @staticmethod
    def get_order_number(text):
        parts = text.split(":")
        if len(parts) > 1:
            return parts[1].strip().split(".")[0]
        else:
            return None

    def get_success_message(self):
        order_info = self.find_element(OrderPageLocators.SUCCESS_MESSAGE_LOCATOR).text
        return order_info, self.get_order_number(order_info)

    @allure.step("Клик на «Посмотреть статус»")
    def click_view_status(self):
        self.click_on(OrderPageLocators.VIEW_STATUS_BUTTON_LOCATOR)
        self.wait_for_element_to_be_visible(OrderPageLocators.LOOK_BUTTON_LOCATOR)

    @allure.step("Клик на логотип «Самоката»")
    def click_logo_scooter(self):
        self.click_on(OrderPageLocators.LOGO_SCOOTER)
        self.wait_for_page(URLs.BASE_URL)

    @allure.step("Клик на логотип «Яндекса»")
    def click_logo_yandex(self):
        self.click_on(OrderPageLocators.LOGO_YANDEX)
        self.driver.switch_to.window(self.driver.window_handles[1])  # Переход на новую вкладку
        self.wait_for_page(URLs.YANDEX_PAGE)
