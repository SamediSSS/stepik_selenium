from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_to_basket(self):
        self.should_be_add_to_basket_button()
        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), \
            "Button for adding product in basket is not presented"
        
        
    def correct_product_added(self):
        product_name_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ON_PAGE)
        product_name_in_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE)
        assert  product_name_in_message.text == product_name_on_page.text, "Added incorrect product"
    
    def correct_basket_price(self):
        product_price_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE)
        basket_price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE)
        assert product_price_on_page.text == basket_price_in_message.text, "Incorrect basket price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"
        
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"

