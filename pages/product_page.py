from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_able_to_add_to_cart(self):
        self.should_be_cart_button()
        self.should_be_right_message()
        self.should_be_right_price()

    def should_be_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.CART_BUTTON)

    def should_be_right_message(self):
        cart_button = self.browser.find_element(*ProductPageLocators.CART_BUTTON)
        cart_button.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(By.CSS_SELECTOR, "div.alert-success strong").text == self.browser.find_element(By.CSS_SELECTOR, "div.product_main h1").text, "Something is wrong(cart)"
    
    def should_be_right_price(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "div.alert-info div p strong").text == self.browser.find_element(By.CSS_SELECTOR, "div.product_main p").text, "Something is wrong(price)"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"    
    
    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't disappear"