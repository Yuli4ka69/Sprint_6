from selenium.webdriver.common.by import By

class FAQPageLocators:
    FAQ_SECTION = (By.CLASS_NAME, "Home_FAQ__3uVm4")
    QUESTION = (By.CSS_SELECTOR, ".accordion__item .accordion__question")
    ANSWER = (By.CSS_SELECTOR, ".accordion__item .accordion__answer")

class HomePageLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, 'button_order_top')
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, 'button_order_bottom')
    LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")

class OrderFormPageLocators:
    START_ORDER_HEADER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Заказать"]')
    START_ORDER_FOOTER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g Button_Middle__1CSJM") and text()="Заказать"]')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Имя"]')
    SURNAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]')
    METRO_OPTION_LIST = (By.CLASS_NAME, "select-search__row")
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Далее"]')
    DATE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]')
    RENTAL_TERM_DROPDOWN = (By.XPATH, '//div[@class="Dropdown-control"]')
    RENTAL_OPTION = (By.XPATH, '//div[@class="Dropdown-option" and text()="сутки"]')
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//*[contains(concat(" ", @class, " "), " Button_Middle__1CSJM ") and text()="Заказать"]')
    CONFIRM_YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and contains(@class, "Button_Middle__1CSJM") and text()="Да"]')
    CONFIRM_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    ORDER_CONFIRMATION_TEXT = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Посмотреть статус"]')
