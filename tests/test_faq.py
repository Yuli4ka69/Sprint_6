import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.faq_page import FAQPage
from locators import FAQPageLocators
from urls import BASE_URL

class TestFAQ:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    @allure.title("Тест проверки вопросов FAQ")
    @allure.description("Проверка каждого вопроса и ответа на странице FAQ")
    def test_all_faq_questions(self):
        faq_page = FAQPage(self.driver)
        with allure.step("Открытие страницы FAQ"):
            self.driver.get(BASE_URL)

        with allure.step("Ожидание загрузки и прокрутка к разделу FAQ"):
            faq_section = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(FAQPageLocators.FAQ_SECTION)
            )
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", faq_section)

        with allure.step("Проверка всех вопросов и их ответов"):
            for index in range(len(FAQPage.QUESTIONS_TEXT)):
                question_text = FAQPage.QUESTIONS_TEXT[index]
                expected_answer = FAQPage.ANSWER_TEXTS[index]

                with allure.step(f"Проверка вопроса {index + 1}: {question_text}"):
                    faq_page.click_question(index)

                    answer_text = faq_page.get_answer_text(index)
                    allure.attach(answer_text, name=f"Текст ответа для вопроса {index + 1}",
                                  attachment_type=allure.attachment_type.TEXT)
                    assert answer_text == expected_answer, f"Ответ для вопроса {index + 1} не совпадает с ожиданием."

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if hasattr(self, 'driver'):
            self.driver.quit()
