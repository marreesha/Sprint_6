import pytest
from selenium import webdriver
from pages import MainPage, OrderPage
from helpers import generate_order_data


@pytest.fixture
def driver():
    """Фикстура для запуска и завершения работы браузера"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def get_main_page(driver):
    """Фикстура для стартовой страницы"""
    main_page = MainPage(driver)
    main_page.get_main_page()

    return main_page


@pytest.fixture
def get_order_page(driver):
    """Фикстура для страницы заказа"""
    order_page = OrderPage(driver)
    order_page.get_order_page()

    return order_page


@pytest.fixture
def complete_order(get_order_page):
    """Фикстура для совершения заказа"""
    order_page = get_order_page
    order_data = generate_order_data()
    order_page.set_order_information(order_data)
    order_page.submit_order()

    return order_page
