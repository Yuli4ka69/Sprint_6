import pytest
import allure
from datetime import datetime, timedelta
from selenium import webdriver
from pages.order_page import OrderFormPage
from locators import OrderFormPageLocators


class TestOrderProcess:
    @pytest.fixture(autouse=True)
    def setup_method(self):
        """Настройка перед каждым тестом"""
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.page = OrderFormPage(self.driver)
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

    @allure.title("Тест на оформление заказа с различными параметрами")
    @allure.description("Тест проверяет оформление заказа через верхнюю или нижнюю кнопку, "
                        "с выбором станции метро, цвета самоката, даты и комментария.")
    @pytest.mark.parametrize("start_button", [OrderFormPageLocators.START_ORDER_HEADER_BUTTON,
                                              OrderFormPageLocators.START_ORDER_FOOTER_BUTTON])
    @pytest.mark.parametrize("station_index", [0, 1])
    @pytest.mark.parametrize("color", ["black", "grey"])
    @pytest.mark.parametrize("date", ["today", "tomorrow"])
    @pytest.mark.parametrize("comment", [None, "Пожалуйста, позвоните за час до прибытия."])
    def test_complete_order_with_params(self, start_button, generate_user_data, station_index, color, date, comment):
        """Тест для оформления заказа с параметризацией станции метро, цвета, даты и комментария."""
        user_data = generate_user_data

        with allure.step("Нажатие на кнопку начала заказа"):
            self.page._click_element(start_button)

        with allure.step("Заполнение имени и фамилии"):
            self.page.fill_name(user_data["name"])
            self.page.fill_surname(user_data["surname"])

        with allure.step("Заполнение адреса и выбора станции метро"):
            self.page.fill_address(user_data["address"])
            self.page.fill_metro_station(station_index)

        with allure.step("Заполнение номера телефона"):
            self.page.fill_phone(user_data["phone"])

        with allure.step("Переход к следующему шагу"):
            self.page.click_next()

        with allure.step("Выбор даты заказа"):
            order_date = datetime.now().strftime("%d.%m.%Y") if date == "today" else (
                        datetime.now() + timedelta(days=1)).strftime("%d.%m.%Y")
            self.page.fill_date(order_date)

        with allure.step("Выбор срока аренды"):
            self.page.select_rental_term()

        with allure.step("Выбор цвета самоката"):
            self.page.select_color(color)

        if comment:
            with allure.step("Добавление комментария"):
                self.page.fill_comment(comment)

        with allure.step("Подтверждение заказа"):
            self.page.click_order()
            self.page.confirm_order()

    def teardown_method(self):
        """Закрытие браузера после теста"""
        if hasattr(self, 'driver'):
            self.driver.quit()
