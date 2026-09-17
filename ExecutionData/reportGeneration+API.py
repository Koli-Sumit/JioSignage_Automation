import os
import shutil
import time
import uuid
import base64
import requests
import configparser
from datetime import datetime
from flask import flash, redirect, url_for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import subprocess
from configparser import ConfigParser
# ---- Config ----
ALLURE_REPORT_BAT = os.path.join(os.getcwd(), 'BatchFiles', 'reportGeneration_signage.bat')

DOWNLOAD_REPORT_BAT = os.path.join(os.getcwd(), 'BatchFiles', 'reportDownload_signage.bat')

GENERATE_TOKEN_URL = "http://10.135.141.141:5000/generateToken"
UPLOAD_URL = "http://10.135.141.141:5000/common_upload"
EMAIL_ID = "shivaji.ghadage@ril.com"
PASSWORD = "codeS1@3"

def getConfigData(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\testData.ini")
    return config.get(section, key)

latest_report_path = os.path.join("..", "AutomationResult", "latest_report")
# Globals (will get values from config.ini)
exe_environment = getConfigData("TestData", "environment")
userName = getConfigData("TestData", "username")
test_type = getConfigData("TestData", "test_type")
module_from_config = getConfigData("TestData", "module")
html_file = os.path.abspath(os.path.join(latest_report_path, "index.html"))
screenshot_file = os.path.abspath(os.path.join(latest_report_path, "index_ss.png"))
appVersion = getConfigData("TestData", "app_version")
webPortalVersion = getConfigData("TestData", "version")
recipientEmails = getConfigData("TestData", "recipients")
releaseCycle = getConfigData("TestData", "release_cycle")


# ========== STEP 1: Generate Allure Report ==========
def generate_allure_report():
    try:
        subprocess.run([DOWNLOAD_REPORT_BAT], check=True)
        subprocess.run([ALLURE_REPORT_BAT], check=True)
        print("Report generated successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Batch execution failed: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# ========== STEP 2: Find latest report & take screenshot ==========
def latestReports():
    global exe_environment, test_type, module_from_config, html_file, screenshot_file

    # Read config.ini
    config = configparser.ConfigParser()
    config.read(os.path.abspath(os.path.join("..", "ConfigurationData", "testData.ini")))

    exe_environment = config.get("TestData", "environment")
    test_type = config.get("TestData", "test_type")
    module_from_config = config.get("TestData", "module")

    # Decide folder type
    folder_type = module_from_config if test_type.lower() == "modulewise" else test_type

    base_path = os.path.abspath(os.path.join("..", "AutomationResult", exe_environment, folder_type))
    report_folders = [os.path.join(base_path, d) for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    if not report_folders:
        raise FileNotFoundError(f"No reports found in {base_path}")

    # Get latest
    result_path_1 = max(report_folders, key=os.path.getmtime)

    # Prepare latest_report folder
    latest_report_path = os.path.abspath(os.path.join("..", "AutomationResult", "latest_report"))
    if os.path.exists(latest_report_path):
        shutil.rmtree(latest_report_path)
    shutil.copytree(result_path_1, latest_report_path)

    # Save paths for upload
    html_file = os.path.abspath(os.path.join(latest_report_path, "index.html"))
    screenshot_file = os.path.join(latest_report_path, "index_ss.png")

    # Take screenshot
    file_url = f"file:///{html_file.replace(os.sep, '/')}"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get(file_url)
        time.sleep(2)
        driver.save_screenshot(screenshot_file)
        print(f"Screenshot saved: {screenshot_file}")
    finally:
        driver.quit()


# ========== STEP 3: Encrypt + Get Token ==========
def encrypt_param(value):
    random_key_str = uuid.uuid4().hex
    key = random_key_str.encode("utf-8")
    iv = b"0000000000000000"
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(value.encode(), AES.block_size))
    encrypted_base64 = base64.b64encode(encrypted).decode()
    return random_key_str + encrypted_base64


def get_token():
    encrypted_email = encrypt_param(EMAIL_ID)
    encrypted_password = encrypt_param(PASSWORD)
    payload = {"emailId": encrypted_email, "password": encrypted_password}

    try:
        response = requests.post(GENERATE_TOKEN_URL, json=payload)
        response.raise_for_status()
        token = response.json().get("token")
        return token
    except Exception as e:
        print("Token generation failed:", e)
        return None


# ========== STEP 4: Upload Report ==========
def upload_allure_report():
    token = get_token()
    if not token:
        print("Skipping upload, token missing.")
        return

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "projectId": "projectJioSignageAutomation_Portal_Client",
        "TestEnvironment": exe_environment,
        "ReleaseCycle": releaseCycle,
        "JioSignageAppVersion": appVersion,
        "SoftwareReleaseVersion_Web": webPortalVersion,
        "TestType": test_type,
        "ModuleName": module_from_config,
        "TimeStamp": datetime.now().strftime("%d-%m-%Y %H:%M.%f")[:-3],
        "EmailRecipients": userName + ";" + recipientEmails,
    }

    files = {"file": (os.path.basename(html_file), open(html_file, "rb"), "text/html")}
    if screenshot_file and os.path.exists(screenshot_file):
        files["Screenshot"] = (os.path.basename(screenshot_file), open(screenshot_file, "rb"), "image/png")

    try:
        response = requests.post(UPLOAD_URL, headers=headers, data=payload, files=files)
        response.raise_for_status()
        print("Report uploaded successfully.")
    except Exception as e:
        print("Upload failed:", e)


# ========== MASTER FUNCTION ==========
def run_full_pipeline():
    import os, shutil
    latest_report_path = os.path.join("..", "AutomationResult", "latest_report")
    if os.path.exists(latest_report_path):
        for f in os.listdir(latest_report_path):
            p = os.path.join(latest_report_path, f)
            if os.path.isfile(p) or os.path.islink(p):
                os.remove(p)
            elif os.path.isdir(p):
                shutil.rmtree(p)
    allureData_path = os.path.abspath(os.path.join("..", "AllureReport"))
    if os.path.exists(allureData_path) and not os.listdir(allureData_path):
        pass
    else:
        generate_allure_report()  # Step 1
        latestReports()  # Step 2
        upload_allure_report()  # Step 3

if __name__ == "__main__":
    try:
        run_full_pipeline()
    except Exception as e:
        print(f"Pipeline failed with error: {e}")