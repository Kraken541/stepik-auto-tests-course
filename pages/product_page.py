from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_correct_product_name_in_message(self, expected_name):
        message_product_name = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE_PRODUCT_NAME).text
        assert expected_name == message_product_name, \
            f"Expected product name '{expected_name}', but got '{message_product_name}'"

    def should_be_correct_basket_price(self, expected_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert expected_price == basket_price, \
            f"Expected basket price '{expected_price}', but got '{basket_price}'"