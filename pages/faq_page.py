from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import URLs


class FAQPage:
    """Класс Page Object для раздела FAQ"""

    # Локатор вопроса
    question_locator = lambda self, question_text: (By.XPATH, f"//div[text()='{question_text}']")
    # Локатор ответа
    answer_locator = lambda self, question_text: (
        By.XPATH, f"//div[text()='{question_text}']/../following-sibling::div[@class='accordion__panel']/p")

    def __init__(self, driver):
        self.driver = driver

    def get_faq_page(self):
        """Загружает страницу сайта"""
        self.driver.get(URLs.BASE_URL)
        WebDriverWait(self.driver, 3).until(EC.url_to_be(URLs.BASE_URL))

    def click_on_question(self, question_text):
        """Прокрутить страницу к вопросу и кликнуть по нему"""
        question_element = self.driver.find_element(*self.question_locator(question_text))
        # Прокрутка к вопросу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        # Дождаться, чтобы вопрос стал видимым
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.question_locator(question_text)))
        question_element.click()  # Клик по вопросу

    def get_answer_text(self, question_text):
        """Получить текст ответа на вопрос"""
        # Дождаться видимости ответа и получить его текст
        answer_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.answer_locator(question_text)))

        return answer_element.text, answer_element.is_displayed()
