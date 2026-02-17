from selenium.webdriver.common.by import By


class MainPageLocators:

    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    INGREDIENT = (By.XPATH, "//a[contains(@href, 'ingredient')][.//p[contains(text(), 'Флюоресцентная булка R2-D3')]]")
    COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter__ZNLkj')]")
    MODAL = (By.CSS_SELECTOR, "[class*='Modal_modal']")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    MODAL_INGREDIENT_NAME = (By.XPATH, "//p[contains(@class, 'text_type_main-medium')]")
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    MODAL_ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Modal_modal__')]//h2")
    CONSTRUCTOR_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__l9dp_')]")
