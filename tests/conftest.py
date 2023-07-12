import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

from pages.LoginPage import LoginPage
from unilities import ReadConfigurations
from unilities.User import User

def pytest_addoption(parser):
    """Declaring the command-line options for test run"""
    parser.addoption('--headless',
                     default='true',
                     help='headless options: "true" or "false"')
    parser.addoption('--browser',
                     default=ReadConfigurations.read_configurations("basic_info", "browser"),
                     help='option to define type of browser')

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    global driver
    driver =None
    headless = request.config.getoption('--headless')
    browser = request.config.getoption('--browser')
    if browser.lower() == "chrome":
        options = webdriver.ChromeOptions()
        if headless == 'true':
            options.add_argument('--headless')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser.lower() == "firefox":
        options = webdriver.FirefoxOptions()
        if headless == 'true':
            options.add_argument('--headless')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    elif browser.lower() == "edge":
        options = webdriver.EdgeOptions()
        if headless == 'true':
            options.add_argument('--headless')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
    else:
        print("Provide a valid browser name from this list chrome/firefox/edge")
    driver.maximize_window()
    driver.implicitly_wait(10)
    url = ReadConfigurations.read_configurations("basic_info", "base_url")
    driver.get(url)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture()
def setup_with_login_and_teardown(setup_and_teardown):
    driver = setup_and_teardown
    login_page = LoginPage(driver)
    login_page.fill_login_form(User.username_valid, User.password_valid)
