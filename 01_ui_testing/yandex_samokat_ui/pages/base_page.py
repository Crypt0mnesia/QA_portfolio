import allure
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, wait, url):
        self.driver = driver
        self.wait = wait
        self.url = url

    @allure.step('Ожидаем кликабельность элемента')
    def wait_until_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидаем видимость элемента')
    def wait_until_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Открываем страницу и ожидаем ее загрузки')
    def open(self):
        self.driver.get(self.url)
        self.wait.until(EC.url_to_be(self.url))

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Находим элемент и кликаем')
    def click(self, locator):
        element = self.wait_until_clickable(locator)
        element.click()

    @allure.step('Скролл к элементу')
    def scroll_to_element(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element

    @allure.step('Скролл к элементу и клик')
    def scroll_and_click(self, locator):
        element = self.scroll_to_element(locator)
        element.click()

    @allure.step('Вводим текст в поле')
    def set_value(self, locator, value):
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        element = self.wait_until_visible(locator)
        return element.text

    @allure.step('Проверяем видимость элемента')
    def is_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    @allure.step('Получаем количество открытых вкладок')
    def get_tabs_count(self):
        return len(self.driver.window_handles)

    @allure.step('Ожидаем количество вкладок: {number}')
    def wait_for_number_of_windows(self, number):
        return self.wait.until(EC.number_of_windows_to_be(number))

    @allure.step('Ожидаем что URL содержит: {text}')
    def wait_until_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    @allure.step('Проверить что URL содержит {expected_url}')
    def url_should_contain(self, expected_url):
        assert expected_url in self.driver.current_url

    @allure.step('Переключаемся на последнюю вкладку')
    def switch_to_last_tab(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[-1])

    @allure.step('Клик по элементу через JavaScript')
    def click_via_js(self, locator):
        element = self.wait_until_visible(locator)
        self.driver.execute_script("arguments[0].click();", element)