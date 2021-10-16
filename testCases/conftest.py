from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        print("lunching chrome")
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# pytest HTML Report
# command pytest -s -v -n=2 --html=Reports/reports.html testCase/test_login.py --browser chrome
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'eCommerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abir'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)