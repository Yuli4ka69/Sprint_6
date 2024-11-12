from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage

class FAQPage(BasePage):
    QUESTIONS_TEXT = [
        "Сколько это стоит? И как оплатить?",
        "Хочу сразу несколько самокатов! Так можно?",
        "Как рассчитывается время аренды?",
        "Можно ли заказать самокат прямо на сегодня?",
        "Можно ли продлить заказ или вернуть самокат раньше?",
        "Вы привозите зарядку вместе с самокатом?",
        "Можно ли отменить заказ?",
        "Я жизу за МКАДом, привезёте?"
    ]

    ANSWER_TEXTS = [
        "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        "Да, обязательно. Всем самокатов! И Москве, и Московской области."
    ]

    def click_question(self, index):
        """Находит вопрос по тексту и кликает на него, используя наведение и JavaScript."""
        question_text = self.QUESTIONS_TEXT[index]
        question_xpath = f'//div[contains(@class, "accordion__button") and text()="{question_text}"]'

        # Ожидание видимости элемента
        question_element = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, question_xpath))
        )

        # Скроллим к элементу и наводим на него курсор
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", question_element)
        ActionChains(self.driver).move_to_element(question_element).perform()

        # Клик через JavaScript
        self.driver.execute_script("arguments[0].click();", question_element)

        # Ожидание, чтобы `aria-expanded` установился в "true" после клика
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(By.XPATH, question_xpath).get_attribute("aria-expanded") == "true"
        )

    def get_answer_text(self, index):
        """Возвращает текст ответа для указанного вопроса, используя `aria-controls`."""
        question_text = self.QUESTIONS_TEXT[index]
        question_xpath = f'//div[contains(@class, "accordion__button") and text()="{question_text}"]'

        question_element = self.driver.find_element(By.XPATH, question_xpath)
        answer_id = question_element.get_attribute("aria-controls")

        answer_xpath = f'//*[@id="{answer_id}"]'
        answer_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, answer_xpath))
        )
        return answer_element.text
