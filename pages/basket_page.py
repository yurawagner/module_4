from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import BasePageLocators

class BasketPage(BasePage):
    def basket_should_be_empty (self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#content_inner p").text == "Your basket is empty. Continue shopping"