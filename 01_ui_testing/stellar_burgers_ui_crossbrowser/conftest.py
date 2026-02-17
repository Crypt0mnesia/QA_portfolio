import pytest
from selenium import webdriver

from helpers.urls import MAIN, BASE_URL
from helpers.data import Credentials
from pages.main_page import MainPage
from pages.login_page import LoginPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def authenticated_user(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.open()
    main_page.click_login_account_button()
    login_page.login(Credentials.EMAIL, Credentials.PASSWORD)
    main_page.main_page_loading_wait()

    return driver