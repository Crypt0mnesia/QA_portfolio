from selenium.webdriver.common.by import By

class OrderFeedLocators:
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(), 'Лента заказов')]")
    TOTAL_COUNTER = (By.XPATH,
                     "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    TODAY_COUNTER = (By.XPATH,
                     "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    ORDERS_IN_PROGRESS = (By.XPATH, "//li[contains(@class, 'text_type_digits-default mb-2')]")
