import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from helpers.data import TIMEOUT, LONG_TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидать элемент')
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Дождаться скрытия элемента')
    def wait_for_element_hide(self, locator, timeout=TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step('Кликнуть')
    def click(self, locator, timeout=TIMEOUT):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Ввести текст')
    def input_text(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст')
    def get_text(self, locator):
        return self.wait_for_element(locator).text

    @allure.step('Проверить видимость')
    def is_visible(self, locator):
        elements = self.driver.find_elements(*locator)
        if not elements:
            return False
        return elements[0].is_displayed()

    @allure.step('Перетащить элемент')
    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.wait_for_presence(source_locator)
        target = self.wait_for_presence(target_locator)
        drag_and_drop(self.driver, source, target)

    @allure.step('Дождаться оверлея')
    def wait_for_overlay_to_disappear(self, overlay_locator, timeout=LONG_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(overlay_locator)
        )

    @allure.step('Безопасный клик')
    def safe_click(self, locator, overlay_locator=None, timeout=LONG_TIMEOUT):
        if overlay_locator:
            self.wait_for_overlay_to_disappear(overlay_locator, timeout)
        self.click(locator, timeout)

    @allure.step('Дождаться наличия элемента')
    def wait_for_presence(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step('Дождаться текста в элементе')
    def wait_for_text_in_element(self, locator, text, timeout=TIMEOUT):
        return bool(WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        ))

    @allure.step('Дождаться условия')
    def wait_for_custom_condition(self, condition, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(condition)

    @allure.step('Получить все элементы')
    def get_all_elements(self, locator):
        return self.driver.find_elements(*locator)