import math

from pages.locators import ProductPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_item_to_card(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CARD).click()

    def check_price_in_card(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRICE_IN_CARD).text

    def check_name_of_item(self):
        message = "product name in the alert doesn't match product name in description"
        assert self.browser.find_element(*ProductPageLocators.NAME_OF_ITEM).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_IN_SUCCESS_MESSAGE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
