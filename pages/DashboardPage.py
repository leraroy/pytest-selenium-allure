from pages.BasePage import BasePage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    profile_css = "span[class*='oxd-userdropdown']"

    def profile_is_displayed(self):
        return self.element_is_displayed("profile_css", self.profile_css)