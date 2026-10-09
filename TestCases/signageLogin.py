import json
import time
from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities import configReader

# Read environment and credentials
env = configReader.getTestData("TestData", "Environment").lower()
userName = configReader.getTestData("TestData", "UserName")
password = configReader.getTestData("TestData", "Password")

# Environment URL and cookie file mapping
env_config = {
    "prod": {
        "url": "https://digitalsignage.jio.com/users/sign_in",
        "cookie_file": "JioSignage_cookies_prod.json"
    },
    "pre-prod": {
        "url": "https://preprod-jiosignage.jio.com/users/sign_in",
        "cookie_file": "JioSignage_cookies_preprod.json"
    },
    "sit1": {
        "url": "https://sit1.jiosignage.jio.com/users/sign_in",
        "cookie_file": "JioSignage_cookies_sit1.json"
    },
    "sit2": {
        "url": "https://sit2.jiosignage.jio.com/users/sign_in",
        "cookie_file": "JioSignage_cookies_sit2.json"
    }
}

def wait_for_attribute_change(driver, by, locator, attribute, initial_value, timeout=120):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.find_element(by, locator).get_attribute(attribute) != initial_value
        )
        # print(f"Attribute '{attribute}' changed from '{initial_value}'")
        return True
    except TimeoutException:
        # print(f"Timeout: Attribute '{attribute}' did not change within {timeout}s.")
        return False

def is_wrong_otp_displayed(driver):
    try:
        msg = driver.find_element(By.CSS_SELECTOR, "label[id='wrong_otp_message'] span")
        return "Wrong OTP" in msg.text.lower()
    except NoSuchElementException:
        return False

def login_and_save_cookies(driver, wait, url, cookie_file):
    driver.get(url)

    # Fill in credentials
    wait.until(EC.presence_of_element_located((By.ID, "user_email"))).send_keys(userName)
    driver.find_element(By.ID, "userPassword").send_keys(password)

    # Try to click 'Remember me' checkbox if present
    try:
        wait.until(EC.element_to_be_clickable((By.ID, "user_remember_me"))).click()
    except:
        pass  # Continue if not found

    # Click Send OTP
    wait.until(EC.element_to_be_clickable((By.ID, "send_otp"))).click()
    
    time.sleep(3)

    element = WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located((By.ID, "user_login_otp1"))
    )
    element.clear()  # optional, but often helpful for OTP fields
    element.send_keys("0")
    verify_btn = driver.find_element(By.ID, "verify_otp")
    driver.find_element(By.ID, "user_login_otp1").clear()
    driver.find_element(By.ID, "user_login_otp1").click()
    initial_status = verify_btn.get_attribute("disabled")

    if wait_for_attribute_change(driver, By.ID, "verify_otp", "disabled", initial_status, timeout=120):
        sleep(0.5)
        verify_btn.click()
        sleep(1)
        try:
            wrong_otp = driver.find_element(By.CSS_SELECTOR,"label[id='wrong_otp_message'] span").text
            if  "Wrong OTP" in wrong_otp:
                for i in range(1, 7):  # 1 to 6
                    driver.find_element(By.ID, f"user_login_otp{i}").clear()
                driver.find_element(By.ID, "user_login_otp1").click()
                sleep(30)
                verify_btn.click()
        except NoSuchElementException:
            pass

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Save cookies to file
    with open(cookie_file, 'w') as file:
        json.dump(driver.get_cookies(), file)

# Start browser and wait setup
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 20)

# Perform login
if env in env_config:
    login_and_save_cookies(
        driver,
        wait,
        env_config[env]["url"],
        env_config[env]["cookie_file"]
    )
else:
    raise ValueError(f"Unknown environment: {env}")

driver.quit()
