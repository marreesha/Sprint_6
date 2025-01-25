from selenium.webdriver.common.by import By
import allure


class BasePage:
    # Локаторы
    logo_scooter = (By.XPATH, "//img[@alt='Scooter']")  # Локатор логотипа «Самоката»
    logo_yandex = (By.XPATH, "//img[@alt='Yandex']")  # Локатор логотипа «Яндекса»

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Клик на логотип «Самоката»")
    def click_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()

    @allure.step("Клик на логотип «Яндекса»")
    def click_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()
