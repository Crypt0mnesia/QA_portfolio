from selenium.webdriver.support import expected_conditions as EC
from locators import LoginFormLocators

def login_user(driver, wait, email, password):
    """Метод для входа пользователя"""
    email_input = wait.until(EC.presence_of_element_located(LoginFormLocators.EMAIL_INPUT))
    email_input.send_keys(email)

    password_input = driver.find_element(*LoginFormLocators.PASSWORD_INPUT)
    password_input.send_keys(password)

    login_button = wait.until(EC.element_to_be_clickable(LoginFormLocators.LOGIN_BUTTON))
    driver.execute_script("arguments[0].click();", login_button)