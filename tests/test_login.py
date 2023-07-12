import allure
import pytest
from pages.LoginPage import LoginPage
from unilities.User import User


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
@allure.feature('Log in')
class TestLogin:

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.login_page = LoginPage(self.driver)

    @allure.story('Log in with valid credentials')
    def test_login_successful(self):
        """
        Check log in with valid credentials.
        """
        dashboard_page = self.login_page.fill_login_form(User.username_valid, User.password_valid)
        with allure.step('Check the url contains "dashboard"'):
            assert 'dashboard/' in self.driver.current_url
        with allure.step("Check profile is displayed on the page"):
            assert dashboard_page.profile_is_displayed()

    # @allure.story('Log in with invalid credentials')
    # def test_login_with_incorrect_creds(self):
    #     """
    #     Check log in with invalid credentials.
    #     """
    #     self.login_page.fill_login_form(User.username_invalid, User.password_invalid)
    #     with allure.step('Check the alert contains "Invalid credentials"'):
    #         assert 'Invalid credentials' in self.login_page.get_text_alert_error()
    #
    # @allure.story('Log in with empty fields')
    # def test_login_with_empty_fields(self):
    #     """
    #     Check log in with empty fields.
    #     """
    #     self.login_page.fill_login_form("", "")
    #     assert len(self.login_page.get_text_message_error()) == 2
    #     with allure.step('Check if error messages appear on the page'):
    #         for text in self.login_page.get_text_message_error():
    #             assert "Required" in text
    #
    # @allure.story('Log in with empty username')
    # def test_login_with_empty_username(self):
    #     """
    #     Check log in with empty username.
    #     """
    #     self.login_page.fill_login_form("", User.password_valid)
    #     with allure.step('Check if an error message is displayed on the page'):
    #         assert "Required" in self.login_page.get_text_message_error()
    #
    # @allure.story('Log in with empty password')
    # def test_login_with_empty_password(self):
    #     """
    #     Check log in with empty password.
    #     """
    #     self.login_page.fill_login_form(User.username_valid, "")
    #     with allure.step('Check if an error message is displayed on the page'):
    #         assert "Required" in self.login_page.get_text_message_error()
