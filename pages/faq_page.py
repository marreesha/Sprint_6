from selenium.webdriver.common.by import By
import allure
from helpers import URLs
from .base_page import BasePage


class FAQPage(BasePage):
    """Класс Page Object для раздела FAQ"""

    # Локатор вопроса
    QUESTION_LOCATOR = lambda self, question_text: (By.XPATH, f"//div[text()='{question_text}']")
    # Локатор ответа
    ANSWER_LOCATOR = lambda self, question_text: (
        By.XPATH, f"//div[text()='{question_text}']/../following-sibling::div[@class='accordion__panel']/p")

    def get_faq_page(self):
        """Загружает страницу сайта"""
        self.get_page(URLs.BASE_URL)

    @allure.step("Клик по вопросу")
    def click_on_question(self, question_text):
        """Прокрутить страницу к вопросу и кликнуть по нему"""
        self.scroll_to(self.QUESTION_LOCATOR(question_text))
        self.wait_for_element_to_be_visible(self.QUESTION_LOCATOR(question_text))
        self.click_on(self.QUESTION_LOCATOR(question_text))

    @allure.step("Извлечение текста ответа на вопрос")
    def get_answer_text(self, question_text):
        """Получить текст ответа на вопрос"""
        # Дождаться видимости ответа и получить его текст
        answer_element = self.wait_for_element_to_be_visible(self.ANSWER_LOCATOR(question_text))

        return answer_element.text, answer_element.is_displayed()
