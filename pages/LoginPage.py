from pages.BasePage import BasePage
from pages.DashboardPage import DashboardPage
import allure

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_field_css = "[name = 'username']"
    password_field_css = "[name = 'password']"
    login_button_css = "[type='submit']"
    alert_error_css = "[role='alert'] p"


    def enter_username(self, username):
        with allure.step(f"Enter username: {username}"):
            self.type_into_element("username_field_css", self.username_field_css, username)

    def enter_password(self, password):
        with allure.step(f"Enter password: {password}"):
            self.type_into_element("password_field_css", self.password_field_css, password)

    def click_login_button(self):
        with allure.step("Click on login button"):
            self.element_click("login_button_css", self.login_button_css)
            return DashboardPage(self.driver)

    def get_text_alert_error(self):
        return self.get_text_element("alert_error_css", self.alert_error_css)

    def alert_error_is_displayed(self):
        return self.element_is_displayed("alert_error_css", self.alert_error_css)

    def fill_login_form(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        return self.click_login_button()
