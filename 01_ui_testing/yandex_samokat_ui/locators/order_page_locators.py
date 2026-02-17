from selenium.webdriver.common.by import By

class OrderPageLocators:

    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_OPTION = (By.XPATH, '//div[@class="select-search__select"]//button[contains(., "{}")]')
    METRO_DROPDOWN = (By.CLASS_NAME, 'select-search__select')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_SELECT =  (By.XPATH, '//div[text()="* Срок аренды"]')
    RENTAL_PERIOD_DROPDOWN = (By.CSS_SELECTOR, 'div.Dropdown-menu[aria-expanded="true"]')
    RENTAL_PERIOD_OPTION = (By.XPATH, '//div[@class="Dropdown-option" and text()="{}"]')

    ORDER_BUTTON = (By.XPATH, '//div[contains(@class, "Order_Buttons__1xGrp")]//button[text()="Заказать"]')
    CONFIRM_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_NUMBER = (By.CLASS_NAME, 'Order_Text__2broi')
    STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

