from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import allure
from datetime import date
from helpers import URLs
from locators import OrderPageLocators
from .base_page import BasePage


class OrderPage(OrderPageLocators, BasePage):

    # Методы
    def get_order_page(self):
        self.driver.get(URLs.ORDER_PAGE)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(URLs.ORDER_PAGE))

    @allure.step("Заполнение первой страницы формы заказа")
    def fill_first_order_form(self, name, surname, address, phone):
        """Функция для заполнения первой страницы"""
        self.driver.find_element(*self.name_input_locator).send_keys(name)
        self.driver.find_element(*self.surname_input_locator).send_keys(surname)
        self.driver.find_element(*self.address_input_locator).send_keys(address)
        self.select_random_metro_station()
        self.driver.find_element(*self.phone_input_locator).send_keys(phone)

    def select_random_metro_station(self):
        """Функция для случайного выбора станции метро"""
        self.driver.find_element(*self.metro_field_locator).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.metro_field_locator))
        metro_options = self.driver.find_elements(*self.metro_options_locator)
        random_station = random.choice(metro_options)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", random_station)
        random_station.click()
        station_name = self.driver.find_element(*self.metro_field_locator).get_attribute("value")
        allure.attach(station_name, name="station")

    @allure.step("Переход на следующую страницу формы заказа")
    def click_next_page(self):
        self.driver.find_element(*self.next_button_locator).click()

    @allure.step("Заполнение второй страницы формы заказа")
    def fill_second_order_form(self, delivery_date, comment):
        self.set_delivery_date(delivery_date)
        self.select_rental_period()
        self.select_scooter_color()
        self.driver.find_element(*self.comment_input_locator).send_keys(comment)

    def set_delivery_date(self, delivery_date):
        """Функция для выбора даты заказа"""
        # Клик по полю даты, чтобы открыть календарь
        self.driver.find_element(*self.delivery_date_locator).click()
        self.driver.find_element(*self.delivery_date_locator).send_keys(delivery_date)
        # Динамический локатор для выбора нужной даты
        date_to_select = (
            By.XPATH,
            f"//div[contains(@class, 'react-datepicker__day') and text()='{int(delivery_date.split('.')[0])}']")
        self.driver.find_element(*date_to_select).click()

    def select_rental_period(self):
        """Функция для случайного выбора периода аренды"""
        self.driver.find_element(*self.rental_period_locator).click()
        rental_options = self.driver.find_elements(*self.rental_options_locator)
        random_rental_period = random.choice(rental_options)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", random_rental_period)
        random_rental_period.click()
        rental_period = self.driver.find_element(*self.rental_period_locator).text
        allure.attach(rental_period, name="rental_period")

    def select_scooter_color(self):
        """Функция для случайного выбора цвета самоката"""
        color_options = self.driver.find_elements(*self.color_locator)
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
        self.driver.find_element(*self.order_button_locator).click()
        self.driver.find_element(*self.confirm_button_locator).click()

    @staticmethod
    def get_order_number(text):
        parts = text.split(":")
        if len(parts) > 1:
            return parts[1].strip().split(".")[0]
        else:
            return None

    def get_success_message(self):
        order_info = self.driver.find_element(*self.success_message_locator).text
        return order_info, self.get_order_number(order_info)

    @allure.step("Клик на «Посмотреть статус»")
    def click_view_status(self):
        self.driver.find_element(*self.view_status_button_locator).click()
