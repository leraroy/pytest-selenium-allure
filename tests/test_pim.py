# import allure
# import pytest
# from faker import Faker
#
# from pages.pim.AddEmployeePage import AddEmployeePage
# from unilities.GeneratorData import GeneratorData
#
# fake = Faker()
# data = GeneratorData()
#
# @allure.feature('Add employee')
# @pytest.mark.usefixtures("setup_with_login_and_teardown", "log_on_failure")
# class TestAddEmployee:
#
#     @pytest.fixture(autouse=True)
#     def class_setup(self):
#         self.add_employee = AddEmployeePage(self.driver)
#         self.add_employee.open_page()
#
#     def test_add_employee_with_correct_creds(self):
#         """
#         Check add employee with valid credentials.
#         """
#         self.add_employee.fill_add_employee_form(data.first_name, data.middle_name, data.last_name)
#         with allure.step('Check if the message contains a "Successfully saved"'):
#             assert "Successfully Saved" in self.add_employee.get_text_message()
#

#     def test_add_employee_with_empty_fields(self):
#         """
#         Check add employee with empty fields.
#         """
#         self.add_employee.fill_add_employee_form("", "", "")
#         assert len(self.add_employee.get_text_message_error()) == 2
#         with allure.step('Check if error messages appear on the page'):
#             for text in self.add_employee.get_text_message_error():
#                 assert "Required" in text
#
