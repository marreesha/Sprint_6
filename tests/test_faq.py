import pytest
import allure
from pages import FAQPage
from conftest import driver

QUESTIONS_AND_ANSWERS = [
    {"question": "Сколько это стоит? И как оплатить?",
     "expected": "Сутки — 400 рублей. Оплата курьеру — наличными или картой."},
    {"question": "Хочу сразу несколько самокатов! Так можно?",
     "expected": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто \
сделать несколько заказов — один за другим."},
    {"question": "Как рассчитывается время аренды?",
     "expected": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени \
аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда \
закончится 9 мая в 20:30."},
    {"question": "Можно ли заказать самокат прямо на сегодня?",
     "expected": "Только начиная с завтрашнего дня. Но скоро станем расторопнее."},
    {"question": "Можно ли продлить заказ или вернуть самокат раньше?",
     "expected": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."},
    {"question": "Вы привозите зарядку вместе с самокатом?",
     "expected": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься \
без передышек и во сне. Зарядка не понадобится."},
    {"question": "Можно ли отменить заказ?",
     "expected": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."},
    {"question": "Я жизу за МКАДом, привезёте?",
     "expected": "Да, обязательно. Всем самокатов! И Москве, и Московской области."}
]


@allure.feature("Вопросы о важном")
class TestFAQPage:
    """Тесты для поля FAQ"""

    @pytest.mark.parametrize("question_data", QUESTIONS_AND_ANSWERS)
    @allure.story("Тест для раздела «Вопросы о важном»")
    @allure.title("Тест для вопроса: {question_data[question]}")
    @allure.description("На странице ищем вопрос и проверяем, что ответ ему соответствует")
    def test_faq_click_on_questions(self, driver, question_data):
        """Тест для проверки вопросов и ответов в разделе FAQ"""
        question_text = question_data["question"]
        expected_text = question_data["expected"]

        faq_page = FAQPage(driver)
        with allure.step(f"Открытие страницы FAQ и клик по вопросу: {question_text}"):
            faq_page.get_faq_page()
            faq_page.click_on_question(question_text)  # Клик по вопросу

        actual_answer, visibility = faq_page.get_answer_text(question_text)

        with allure.step(f"Проверяем текст ответа"):
            allure.attach(f"Ожидаемый ответ: {expected_text}", name="Expected Answer",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"Фактический ответ: {actual_answer}", name="Actual Answer",
                          attachment_type=allure.attachment_type.TEXT)

        # Проверяем, что текст ответа соответствует ожидаемому
        assert actual_answer == expected_text and visibility, f"Ожидание: {expected_text} - реальность: {actual_answer}"
