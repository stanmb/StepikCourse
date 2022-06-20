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
