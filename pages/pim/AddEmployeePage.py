import allure

from pages.BasePage import BasePage
from pages.pim.PersonalDetails import PersonalDetails


class AddEmployeePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_name = "firstName"
    last_name_field_name = "lastName"
    middle_name_field_name = "middleName"
    save_button_css = "[type='submit']"
    success_message_css = "div[class*='success'] p[class*='message']"

    def open_page(self):
        with allure.step("Open page add employee"):
            self.open("/pim/addEmployee")

    def enter_first_name(self, first_name):
        with allure.step(f"Enter first name: {first_name}"):
            self.type_into_element("first_name_field_name", self.first_name_field_name, first_name)

    def enter_middle_name(self, middle_name):
        with allure.step(f"Enter middle name: {middle_name}"):
            self.type_into_element("middle_name_field_name", self.middle_name_field_name, middle_name)

    def enter_last_name(self, last_name):
        with allure.step(f"Enter last name: {last_name}"):
            self.type_into_element("last_name_field_name", self.last_name_field_name, last_name)

    def click_save_button(self):
        with allure.step("Click on save button"):
            self.element_click("save_button_css", self.save_button_css)
        return PersonalDetails(self.driver)

    def get_text_message(self):
        return self.get_text_element("success_message_css", self.success_message_css)

    def message_is_displayed(self):
        return self.element_is_displayed("success_message_css", self.success_message_css)

    def fill_add_employee_form(self, first_name, middle_name, last_name):
        self.enter_first_name(first_name)
        self.enter_middle_name(middle_name)
        self.enter_last_name(last_name)
        return self.click_save_button()

