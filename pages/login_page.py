from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL doesn't contain login in it's path"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)
        # assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), f"Element LOGIN_FORM doesn't exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM)
        assert self.browser.find_element(*LoginPageLocators.REG_FORM), f"Element REG_FORM doesn't exist"
