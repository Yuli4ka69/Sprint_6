import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.home_page import HomePage
from urls import ORDER_URL
class TestLogoNavigation:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    @allure.title("Проверка перенаправления по логотипу Scooter")
    @allure.description("Тест проверяет, что клик на логотип Scooter перенаправляет на главную страницу.")
    def test_logo_scooter_redirect(self):
        home_page = HomePage(self.driver)

        with allure.step("Открытие страницы заказа"):
            self.driver.get(ORDER_URL)

        with allure.step("Клик по логотипу Scooter"):
            home_page.click_logo_scooter()

        with allure.step("Проверка, что текущий URL равен главной странице"):
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url == "https://qa-scooter.praktikum-services.ru/"
            )
            assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"
            allure.attach(self.driver.current_url, name="Фактический URL", attachment_type=allure.attachment_type.TEXT)

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if hasattr(self, 'driver'):
            self.driver.quit()
