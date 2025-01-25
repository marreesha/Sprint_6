import pytest
import allure
from pages import MainPage, OrderPage
from helpers import generate_order_data
from conftest import driver, get_main_page, complete_order
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import URLs


@allure.feature("Тестирование оформления заказа")
class TestOrder:
    """Тесты для проверки функционала оформления заказа"""

    @allure.story("Тест для кнопки «Заказать»")
    @allure.title("Тест для кнопки «Заказать» вверху страницы")
    @allure.description("На странице ищем кнопку «Заказать» вверху страницы и проверяем переход на страницу заказа")
    def test_click_on_top_order_button(self, driver, get_main_page):
        """Тест для кнопки «Заказать» вверху страницы"""

        with allure.step("Открытие главной страницы"):
            main_page = get_main_page

        main_page.click_order_button_top()  # Кликаем по кнопке
        # Ожидание перехода на страницу заказа
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.ORDER_PAGE))

        with allure.step("Проверка URL страницы заказа"):
            assert driver.current_url == URLs.ORDER_PAGE, "Переход не удался"

    @allure.story("Тест для кнопки «Заказать»")
    @allure.description("На странице ищем кнопку «Заказать» внизу страницы и проверяем переход на страницу заказа")
    @allure.title("Тест для кнопки «Заказать» внизу страницы")
    def test_click_on_bottom_order_button(self, driver, get_main_page):
        """Тест для кнопки «Заказать» внизу страницы"""

        with allure.step("Открытие главной страницы"):
            main_page = get_main_page

        main_page.click_order_button_bottom()  # Кликаем по кнопке
        # Ожидание перехода на страницу заказа
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.ORDER_PAGE))

        with allure.step("Проверка URL страницы заказа"):
            assert driver.current_url == URLs.ORDER_PAGE, "Переход не удался"

    @allure.story("Тест оформления заказа самоката")
    @allure.title("Тест успешного оформления заказа самоката")
    @allure.description("Оформляем заказ со сгенерированными данными")
    @pytest.mark.repeat(2)
    def test_order_scooter_success(self, driver, get_order_page):
        """Тест оформления заказа самоката"""

        with allure.step("Генерация данных для заказа"):
            # Генерируем данные заказа
            order_data = generate_order_data()

        with allure.step("Открытие страницы заказа"):
            order_page = get_order_page

        order_page.set_order_information(order_data)
        order_page.submit_order()

        with allure.step("Проверка успешного оформления заказа"):
            success_message, order_number = order_page.get_success_message()
            allure.attach(order_number, name="order_number")
            assert "Заказ оформлен" in success_message, f"Не удалось оформить заказ. Сообщение: {success_message}"

    @allure.story("Тест для лого «Самокат»")
    @allure.title("Тест для лого «Самокат» вверху страницы")
    @allure.description("На странице ищем кнопку «Самокат» вверху страницы и проверяем переход на стартовую страницу")
    def test_click_on_scooter_logo(self, driver, complete_order):
        """Тест для лого «Самокат» вверху страницы"""

        with allure.step("Совершение заказа"):
            order_page = complete_order

        order_page.click_view_status()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderPage.look_button_locator))

        order_page.click_logo_scooter()  # Клик по кнопке «Самоката»
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.BASE_URL))

        with allure.step("Проверка URL страницы заказа"):
            assert driver.current_url == URLs.BASE_URL, "Переход не удался"

    @allure.story("Тест для лого «Яндекс»")
    @allure.title("Тест для лого «Яндекс» вверху страницы")
    @allure.description("На странице ищем кнопку «Яндекс» вверху страницы и проверяем переход на новую вкладку")
    def test_click_on_yandex_logo(self, driver, complete_order):
        """Тест для лого «Яндекс» вверху страницы"""

        with allure.step("Совершение заказа"):
            order_page = complete_order

        order_page.click_view_status()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(OrderPage.look_button_locator))

        order_page.click_logo_yandex()  # Клик по кнопке «Яндекс»
        driver.switch_to.window(driver.window_handles[1])  # Переход на новую вкладку
        WebDriverWait(driver, 3).until(EC.url_to_be(URLs.YANDEX_PAGE))

        with allure.step("Проверка URL страницы заказа"):
            assert driver.current_url == URLs.YANDEX_PAGE, "Переход не удался"