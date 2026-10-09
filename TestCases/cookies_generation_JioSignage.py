import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from Utilities import configReader
# from webdriver_manager.chrome import ChromeDriverManager

env = configReader.getTestData("TestData", "Environment")
userName = configReader.getTestData("TestData", "UserName")
password = configReader.getTestData("TestData", "Password")

# service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

if env == "prod":
    driver.implicitly_wait(10)
    driver.get("https://digitalsignage.jio.com/users/sign_in")
    driver.find_element(By.ID, "user_email").send_keys(userName)
    driver.find_element(By.ID, "userPassword").send_keys(password)
    driver.find_element(By.ID, "user_remember_me").click()
    time.sleep(2)
    driver.find_element(By.ID, "send_otp").click()
    time.sleep(60)
    driver.find_element(By.ID, "verify_otp").click()
    time.sleep(5)
    cookies = driver.get_cookies()
    # Save cookies to a JSON file
    with open('JioSignage_cookies_prod.json', 'w') as file:
        json.dump(cookies, file)

elif env == "pre-prod":
    driver.implicitly_wait(10)
    driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
    driver.find_element(By.ID, "user_email").send_keys(userName)
    driver.find_element(By.ID, "userPassword").send_keys(password)
    driver.find_element(By.ID, "user_remember_me").click()
    time.sleep(2)
    driver.find_element(By.ID, "send_otp").click()
    time.sleep(60)
    driver.find_element(By.ID, "verify_otp").click()
    time.sleep(5)
    cookies = driver.get_cookies()
    # Save cookies to a JSON file
    with open('JioSignage_cookies_preprod.json', 'w') as file:
        json.dump(cookies, file)

elif env == "sit1":
    driver.implicitly_wait(10)
    driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
    driver.find_element(By.ID, "user_email").send_keys(userName)
    driver.find_element(By.ID, "userPassword").send_keys(password)
    time.sleep(2)
    driver.find_element(By.ID, "user_remember_me").click()
    time.sleep(2)
    driver.find_element(By.ID, "send_otp").click()
    time.sleep(60)
    driver.find_element(By.ID, "verify_otp").click()
    time.sleep(5)
    cookies = driver.get_cookies()
    # Save cookies to a JSON file
    with open('JioSignage_cookies_sit1.json', 'w') as file:
        json.dump(cookies, file)

elif env == "sit2":
    driver.implicitly_wait(10)
    driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
    driver.find_element(By.ID, "user_email").send_keys(userName)
    driver.find_element(By.ID, "userPassword").send_keys(password)
    time.sleep(2)
    driver.find_element(By.ID, "user_remember_me").click()
    time.sleep(2)
    driver.find_element(By.ID, "send_otp").click()
    time.sleep(60)
    driver.find_element(By.ID, "verify_otp").click()
    time.sleep(5)
    cookies = driver.get_cookies()
    # Save cookies to a JSON file
    with open('JioSignage_cookies_sit2.json', 'w') as file:
        json.dump(cookies, file)
