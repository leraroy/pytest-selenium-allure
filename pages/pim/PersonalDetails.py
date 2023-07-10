from pages.BasePage import BasePage


class PersonalDetails(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    employee_name_css ="[class*='employee-name']"

    def employee_name_is_displayed(self):
        return self.element_is_displayed("employee_name_css", self.employee_name_css)