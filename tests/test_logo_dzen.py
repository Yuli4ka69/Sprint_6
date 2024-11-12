import pytest
import allure
from selenium import webdriver
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
            home_page.open_order_page()
            original_window = self.driver.current_window_handle

        with allure.step("Клик по логотипу Яндекс"):
            home_page.click_logo_yandex()

        with allure.step("Переход на новую вкладку и проверка URL"):
            home_page.switch_to_new_window()
            home_page.verify_redirect_to_yandex()
            allure.attach(self.driver.current_url, name="Фактический URL", attachment_type=allure.attachment_type.TEXT)

        with allure.step("Закрытие новой вкладки и возврат на исходную"):
            self.driver.close()
            self.driver.switch_to.window(original_window)

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if hasattr(self, 'driver'):
            self.driver.quit()
