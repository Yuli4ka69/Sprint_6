from pages.base_page import BasePage
from locators import HomePageLocators
from urls import ORDER_URL, YANDEX_REDIRECT_URL, BASE_URL
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    def open_order_page(self):
        """Открывает страницу заказа"""
        self.driver.get(ORDER_URL)

    def click_order_button_top(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click_element(HomePageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(HomePageLocators.LOGO_YANDEX)

    def switch_to_new_window(self):
        """Переключается на новое окно, когда оно открыто"""
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(EC.new_window_is_opened([original_window]))
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

    def verify_redirect_to_main_page(self):
        """Ожидает и проверяет, что текущий URL соответствует главной странице с дополнительной проверкой"""
        WebDriverWait(self.driver, 20).until(lambda driver: driver.current_url.startswith(BASE_URL))
        assert self.driver.current_url.rstrip('/') == BASE_URL.rstrip(
            '/'), f"Expected URL: {BASE_URL}, but got: {self.driver.current_url}"

    def verify_redirect_to_yandex(self):
        """Ожидает и проверяет, что текущий URL соответствует URL редиректа на Яндекс"""
        WebDriverWait(self.driver, 10).until(EC.url_to_be(YANDEX_REDIRECT_URL))
        assert self.driver.current_url == YANDEX_REDIRECT_URL, f"Expected URL: {YANDEX_REDIRECT_URL}, but got: {self.driver.current_url}"