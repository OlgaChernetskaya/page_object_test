import time

from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "login is not found in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login_form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register_form is not presented"

    def register_new_user(self, email: str, password: str):
        user_email = str(time.time()) + email
        user_password = str(time.time()) + password
        input_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        input_email.send_keys(user_email)
        input_password1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1_INPUT)
        input_password1.send_keys(user_password)
        input_password2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2_INPUT)
        input_password2.send_keys(user_password)
        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        registration_submit.click()
