from .base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.common.by import By
import time

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "current url doesn't contain login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
    
    def register_new_user(self, email, password):
        em = self.browser.find_element(By.ID, "id_registration-email")
        em.click()
        em.send_keys(email)
        ps = self.browser.find_element(By.ID, "id_registration-password1")
        ps.click()
        ps.send_keys(password)
        pss = self.browser.find_element(By.ID, "id_registration-password2")
        pss.click()
        pss.send_keys(password)
        regbut = self.browser.find_element(By.NAME, "registration_submit")
        regbut.click()