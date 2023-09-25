import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

    parser.addoption("--URL", action="store", default="stage")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        # chrome_options.add_argument("headless") this doesn't work for pytest!!
        service_obj = Service("D:/selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(4)

    elif browser_name == "firefox":
        service_obj = Service("D:/selenium/geckodriver-v0.33.0-win64/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(4)

    elif browser_name == "edge":
        service_obj = Service("D:/selenium/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(4)

    URL = request.config.getoption("URL")
    if URL == "dev":
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif URL == "stage":
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    elif URL == "preprod":
        driver.get("https://rahulshettyacademy.com/angularpractice/")

    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
