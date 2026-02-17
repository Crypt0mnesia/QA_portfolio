import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Settings
from locators.base_page_locators import BasePageLocators

@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, Settings.DEFAULT_TIMEOUT)

@pytest.fixture(autouse=True)
def close_cookies(driver, wait):
    """Автоматически закрывает куки-баннер"""
    try:
        cookie_banner = BasePageLocators.COOKIE_BUTTON
        wait.until(EC.element_to_be_clickable(cookie_banner)).click()
    except:
        pass