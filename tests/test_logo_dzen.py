import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage

class TestLogoNavigation:

    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    @allure.title("Проверка перенаправления по логотипу Яндекс")
    @allure.description("Тест проверяет, что клик на логотип Яндекс приводит к правильной ссылке")
    def test_logo_redirect(self):
        home_page = HomePage(self.driver)

        with allure.step("Открытие страницы заказа"):
            self.driver.get("https://qa-scooter.praktikum-services.ru/order")
            original_window = self.driver.current_window_handle

        with allure.step("Клик по логотипу Яндекс"):
            home_page.click_logo_yandex()

        with allure.step("Ожидание открытия нового окна"):
            WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([original_window]))
            new_window = [window for window in self.driver.window_handles if window != original_window][0]
            self.driver.switch_to.window(new_window)

        with allure.step("Проверка, что текущий URL равен ожидаемому"):
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.current_url == "https://dzen.ru/?yredirect=true"
            )
            assert self.driver.current_url == "https://dzen.ru/?yredirect=true"
            allure.attach(self.driver.current_url, name="Фактический URL", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Закрытие новой вкладки и возврат на исходную"):
            self.driver.close()
            self.driver.switch_to.window(original_window)

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if hasattr(self, 'driver'):
            self.driver.quit()
