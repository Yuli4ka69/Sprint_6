from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.common.exceptions import ElementClickInterceptedException
from locators import OrderFormPageLocators
from urls import BASE_URL

class OrderFormPage(BasePage):
    def open_order_page(self):
        """Открывает страницу заказа"""
        self.driver.get(BASE_URL)
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(OrderFormPageLocators.START_ORDER_HEADER_BUTTON)
        )

    def click_start_button(self, button_locator):
        """Кликает на переданную кнопку начала заказа"""
        self._click_element(button_locator)

    def fill_name(self, name):
        self._fill_field(OrderFormPageLocators.NAME_FIELD, name)

    def fill_surname(self, surname):
        self._fill_field(OrderFormPageLocators.SURNAME_FIELD, surname)

    def fill_address(self, address):
        self._fill_field(OrderFormPageLocators.ADDRESS_FIELD, address)

    def fill_metro_station(self, station_index=0):
        """Открывает поле станции метро и выбирает станцию по заданному индексу."""
        metro_field = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderFormPageLocators.METRO_FIELD))
        metro_field.click()

        metro_options = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(OrderFormPageLocators.METRO_OPTION_LIST)
        )

        if station_index < len(metro_options):
            metro_options[station_index].click()
        else:
            print(f"Ошибка: Индекс {station_index} вне диапазона, выбирается первая станция.")
            metro_options[0].click()

    def fill_phone(self, phone):
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderFormPageLocators.PHONE_FIELD))
        field.clear()
        field.send_keys(phone)
        print(f"Введен номер телефона: {phone}")

    def click_next(self):
        self._click_element(OrderFormPageLocators.NEXT_BUTTON)

    def fill_date(self, order_date):
        """Заполняет поле даты заказа и выбирает дату в календаре."""
        self._click_element(OrderFormPageLocators.DATE_FIELD)

        # Извлекаем день из order_date и подставляем в шаблон DATE_PICKER_DAY_TEMPLATE
        day = order_date.split(".")[0]
        date_locator = (By.XPATH, OrderFormPageLocators.DATE_PICKER_DAY_TEMPLATE.format(day))

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(date_locator)).click()

    def select_rental_term(self):
        self._click_element(OrderFormPageLocators.RENTAL_TERM_DROPDOWN)

        rental_option_sutki = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderFormPageLocators.RENTAL_OPTION)
        )
        rental_option_sutki.click()

    def select_color(self, color="black"):
        if color == "black":
            self._click_element(OrderFormPageLocators.BLACK_COLOR_CHECKBOX)
        elif color == "grey":
            self._click_element(OrderFormPageLocators.GREY_COLOR_CHECKBOX)

    def fill_comment(self, comment):
        self._fill_field(OrderFormPageLocators.COMMENT_FIELD, comment)

    def click_order(self):
        self._click_element(OrderFormPageLocators.ORDER_BUTTON)

    def confirm_order(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderFormPageLocators.CONFIRM_MODAL))
        print("Модальное окно с запросом на подтверждение заказа появилось.")

        self._click_element(OrderFormPageLocators.CONFIRM_YES_BUTTON)

        modal = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderFormPageLocators.CONFIRM_MODAL))
        print("Модальное окно с подтверждением заказа появилось.")

        confirmation_text = modal.find_element(*OrderFormPageLocators.ORDER_CONFIRMATION_TEXT)
        print(f"Найденный текст подтверждения: '{confirmation_text.text}'")
        assert "Заказ оформлен" in confirmation_text.text, "Текст 'Заказ оформлен' не найден."

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderFormPageLocators.VIEW_STATUS_BUTTON))
        print("Кнопка 'Посмотреть статус' доступна для клика.")

    def _fill_field(self, locator, value):
        field = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        field.clear()
        field.send_keys(value)

    def _click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

        attempts = 0
        while attempts < 3:
            try:
                element.click()
                return
            except ElementClickInterceptedException:
                attempts += 1
                print(f"Попытка {attempts}: элемент был перекрыт. Пробую снова...")
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)

        raise Exception("Элемент остается перекрытым после 3 попыток клика.")
