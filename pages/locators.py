from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CORRECT_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")
    BOOK_ADDED_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages  div:nth-child(1) strong")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    CORRECT_BOOK_PRICE = (By.CSS_SELECTOR, "#messages  div:nth-child(3) strong")
