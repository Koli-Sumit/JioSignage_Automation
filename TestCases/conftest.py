import json
import subprocess
import threading
import time
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
import configparser
from selenium.webdriver.common.by import By
from Utilities import configReader
import ctypes
driver = None

# ------------------ Prevent sleep ------------------
# Windows key event constants
KEYEVENTF_KEYUP = 0x0002
VK_SHIFT = 0x10  # Virtual key code for SHIFT

def press_shift():
    ctypes.windll.user32.keybd_event(VK_SHIFT, 0, 0, 0)       # key down
    ctypes.windll.user32.keybd_event(VK_SHIFT, 0, KEYEVENTF_KEYUP, 0)  # key up

def keep_awake():
    while True:
        press_shift()
        time.sleep(30)  # press every 30 sec

@pytest.fixture(scope="session", autouse=True)
def prevent_sleep():
    t = threading.Thread(target=keep_awake, daemon=True)
    t.start()
    yield



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

def capture_app_version():
    config = configparser.ConfigParser()
    config.read('../ConfigurationData/testData.ini')
    if not config.has_section('TestData'):
        config.add_section('TestData')
    config.set('TestData', 'app_version', f'Not Available, Since validated only web portal.')
    with open('../ConfigurationData/testData.ini', 'w') as configfile:
        config.write(configfile)

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--force-device-scale-factor=1.0")
        driver = webdriver.Chrome(options=options)
    # elif browser_name == "firefox":
    #     driver = webdriver.Firefox()
    # elif browser_name == "IE":
    #     driver = webdriver.Ie()
    # elif browser_name == "edge":
    #     driver = webdriver.Edge()
    #service = Service(r'..\\utils\\chromedriver.exe')
    #options = webdriver.ChromeOptions()
    #options.add_argument("--disable-popup-blocking")
    #options.add_argument("--disable-web-security")
    #options.add_argument('--ignore-ssl-errors=yes')
    #options.add_argument('--ignore-certificate-errors')
    #driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(10)
    env = configReader.getTestData("TestData", "Environment")

    if env == "prod":
        driver.get("https://digitalsignage.jio.com/v2/dashboard")
        driver.maximize_window()
        with open("JioSignage_cookies_prod.json", 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        version = driver.find_element(By.XPATH, "//a[contains(.,'Version: ')]").text
        version = version.split(":")[-1].strip()
        config = configparser.ConfigParser()
        config.read('../ConfigurationData/testData.ini')

        if not config.has_section('TestData'):
            config.add_section('TestData')

        config.set('TestData', 'version', f'{version}')

        with open('../ConfigurationData/testData.ini', 'w') as configfile:
            config.write(configfile)
        capture_app_version()
        request.cls.driver = driver
        yield driver
        driver.close()

    elif env == "pre-prod":
        driver.get("https://preprod-jiosignage.jio.com/v2/dashboard")
        driver.maximize_window()
        with open("JioSignage_cookies_preprod.json", 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        version = driver.find_element(By.XPATH, "//a[contains(.,'Version: ')]").text
        version = version.split(":")[-1].strip()
        config = configparser.ConfigParser()
        config.read('../ConfigurationData/testData.ini')

        if not config.has_section('TestData'):
            config.add_section('TestData')

        config.set('TestData', 'version', f'{version}')

        with open('../ConfigurationData/testData.ini', 'w') as configfile:
            config.write(configfile)
        capture_app_version()
        request.cls.driver = driver
        yield driver
        driver.close()

    # Nihal : Added for SIT1 environment
    elif env == "sit1":
        driver.get("https://sit1.jiosignage.jio.com/v2/dashboard")
        driver.maximize_window()
        with open("JioSignage_cookies_sit1.json", 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        version = driver.find_element(By.XPATH, "//a[contains(.,'Version: ')]").text
        version = version.split(":")[-1].strip()
        config = configparser.ConfigParser()
        config.read('../ConfigurationData/testData.ini')

        if not config.has_section('TestData'):
            config.add_section('TestData')

        config.set('TestData', 'version', f'{version}')

        with open('../ConfigurationData/testData.ini', 'w') as configfile:
            config.write(configfile)
        capture_app_version()
        request.cls.driver = driver
        yield driver
        driver.close()

    # Nihal : Added for SIT1 environment
    elif env == "sit2":
        driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
        driver.maximize_window()
        with open("JioSignage_cookies_sit2.json", 'r') as file:
            cookies = json.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.refresh()
        version = driver.find_element(By.XPATH, "//a[contains(.,'Version: ')]").text
        version = version.split(":")[-1].strip()
        config = configparser.ConfigParser()
        config.read('../ConfigurationData/testData.ini')

        if not config.has_section('TestData'):
            config.add_section('TestData')

        config.set('TestData', 'version', f'{version}')

        with open('../ConfigurationData/testData.ini', 'w') as configfile:
            config.write(configfile)
        capture_app_version()
        request.cls.driver = driver
        yield driver
        driver.close()


@pytest.fixture()
def log_on_failure(request, setup):
    yield
    item = request.node
    driver = setup
    if item.rep_call.failed:
        # log.logger.info("Test {} Failed.".format(item.name))
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
    elif item.rep_call.passed:
        pass
        # log.logger.info("Test {} Passed.".format(item.name))
    elif item.rep_call.broken:
        pass
        # log.logger.info("Test {} Broken.".format(item.name))
