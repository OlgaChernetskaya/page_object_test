from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Product is presented in basket"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "Message is  not presented in basket"
