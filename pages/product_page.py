from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_link.click()

    def should_be_correct_product_added_in_basket(self):
        book_name = self.browser.find_element(*ProductPageLocators.CORRECT_BOOK_NAME).text
        assert book_name == self.browser.find_element(*ProductPageLocators.BOOK_ADDED_IN_BASKET_MESSAGE).text, \
            f"Should be '{book_name}' added in basket"

    def should_be_correct_price_in_basket(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == self.browser.find_element(*ProductPageLocators.CORRECT_BOOK_PRICE).text, \
            f"Should be correct price in basket. Should be price: '{book_price}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but " \
                                                                                  "should not be "

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"
