from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")
    ENTER_MAIL = (By.ID, "id_login-username")
    ENTER_PASS = (By.ID, "id_login-password")
    ENTER_BUTTON = (By.CSS_SELECTOR, "[name=""login_submit""]")

    REG_MAIL = (By.ID, "id_registration-email")
    REG_PASS = (By.ID, "id_registration-password1")
    REG_BUTTON = (By.CSS_SELECTOR, "[name=""registration_submit""]")


class ProductPageLocators:
    ADD_TO_CARD = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_OF_ITEM = (By.CSS_SELECTOR, "div.product_main > h1")
    PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-success")
    PRODUCT_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alertinner > strong")
    TOTAL_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert-info > .alertinner > p > strong")
    PRICE_IN_CARD = (By.CSS_SELECTOR, "div.alertinner > p > strong")


class BasePageLocators:
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators:
    CART_CONTENT = (By.CSS_SELECTOR, "#content_inner > p")
