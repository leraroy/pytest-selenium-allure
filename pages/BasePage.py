from selenium.webdriver.common.by import By
from unilities import ReadConfigurations
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    error_message_css = "[class*='error-message']"

    def open(self, url):
        self.driver.get(ReadConfigurations.read_configurations("basic_info", "base_url")+url)

    def get_text_message_error(self):
        text = []
        for element in self.finds("error_message_css", self.error_message_css):
            text.append(element.text)
        return text

    def wait(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))

    def waits(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((locator)))

    def find(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("xpath"):
            element = self.wait((By.XPATH, locator_value))
        elif locator_name.endswith("css"):
            element = self.wait((By.CSS_SELECTOR, locator_value))
        elif locator_name.endswith("name"):
            element = self.wait((By.NAME, locator_value))
        elif locator_name.endswith("class_name"):
            element = self.wait((By.CLASS_NAME, locator_value))
        elif locator_name.endswith("id"):
            element = self.wait((By.ID, locator_value))
        elif locator_name.endswith("link_text"):
            element = self.wait((By.NAME, locator_value))
        return element

    def type_into_element(self, locator_name, locator_value, text):
        element = self.find(locator_name, locator_value)
        element.clear()
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        self.find(locator_name, locator_value).click()

    def get_text_element(self, locator_name, locator_value):
        return self.find(locator_name, locator_value).text

    def element_is_displayed(self, locator_name, locator_value):
        element = self.find(locator_name, locator_value)
        return element.is_displayed()

    def finds(self, locator_name, locator_value):
        elements = None
        if locator_name.__contains__("xpath"):
            elements = self.waits((By.XPATH, locator_value))
        elif locator_name.__contains__("css"):
            elements = self.waits((By.CSS_SELECTOR, locator_value))
        elif locator_name.__contains__("name"):
            elements = self.waits((By.NAME, locator_value))
        elif locator_name.__contains__("class_name"):
            elements = self.waits((By.CLASS_NAME, locator_value))
        elif locator_name.__contains__("id"):
            elements = self.waits((By.ID, locator_value))
        elif locator_name.__contains__("link_text"):
            elements = self.waits((By.NAME, locator_value))
        return elements

    def click_on_element_menu(self, name):
        self.driver.find_element(By.CSS_SELECTOR, f"a[href*='{name}']")