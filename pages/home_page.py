from pages.base_page import BasePage
from locators import HomePageLocators

class HomePage(BasePage):
    def click_order_button_top(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        self.click_element(HomePageLocators.ORDER_BUTTON_BOTTOM)

    def click_logo_scooter(self):
        self.click_element(HomePageLocators.LOGO_SCOOTER)

    def click_logo_yandex(self):
        self.click_element(HomePageLocators.LOGO_YANDEX)
