from selenium.webdriver.common.by import By

class BasePageLocators:

    YANDEX_LOGO = (By.CSS_SELECTOR, '.Header_Logo__23yGT > .Header_LogoYandex__3TSOI')
    SCOOTER_LOGO = (By.CSS_SELECTOR, '.Header_Logo__23yGT > .Header_LogoScooter__3lsAR')
    TOP_ORDER_BUTTON = (By.CSS_SELECTOR, '.Header_Nav__AGCXC > .Button_Button__ra12g')
    ORDER_STATUS_BUTTON = (By.CSS_SELECTOR, '.Header_Nav__AGCXC > .Header_Link__1TAG7')
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")