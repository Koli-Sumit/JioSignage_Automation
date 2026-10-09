import shutil
from configparser import ConfigParser
import requests
import base64
import uuid
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
def getConfigData(section, key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\testData.ini")
    return config.get(section, key)

test_type = getConfigData("TestData", "test_type")
module_from_config = getConfigData("TestData", "module")
exe_environment = getConfigData("TestData", "environment")
REPORT_PATH = r"C:\pychram\JioSignage_Master_v.3.0\AutomationResult\sit2\smoke\smoke_sit2_Ver-8.4__2025-08-18_09-59-10\index.html"

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
allure_report_folder = "\\AllureReport\\history"
destination_folder = os.path.join(parent_directory + allure_report_folder)

# Function to get the latest directory created in a specified path
def get_latest_directory_created(parent_dir):
    directories = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d))]

    if not directories:
        return None

    dir_with_times = []
    for directory in directories:
        dir_path = os.path.join(parent_dir, directory)
        creation_time = os.path.getctime(dir_path)
        dir_with_times.append((dir_path, creation_time))

    dir_with_times.sort(key=lambda x: x[1], reverse=True)

    latest_dir = dir_with_times[0][0]
    return latest_dir

# Function to copy a folder
def copy_folder(src, dest):
    try:
        shutil.copytree(src, dest, dirs_exist_ok=True)
        print(f"History Folder copied from {src} to {dest}")
    except Exception as e:
        print(f"Error copying folder: {e}")

def run():
    environment = getConfigData("TestData", "environment")
    if test_type == "detailed":
        module_directory = f"\\Result_Detail\\{environment}\\detailed"
        history_folder = "\\history"
        path = os.path.join(parent_directory + module_directory)
        latest_folder = get_latest_directory_created(path)
        history_path = os.path.join(latest_folder + history_folder)
        copy_folder(history_path, destination_folder)
    elif test_type == "sanity":
        module_directory = f"\\Result_Detail\\{environment}\\sanity"
        history_folder = "\\history"
        path = os.path.join(parent_directory + module_directory)
        latest_folder = get_latest_directory_created(path)
        history_path = os.path.join(latest_folder + history_folder)
        copy_folder(history_path, destination_folder)
    if test_type == "smoke":
        module_directory = f"\\Result_Detail\\{environment}\\smoke"
        history_folder = "\\history"
        path = os.path.join(parent_directory + module_directory)
        latest_folder = get_latest_directory_created(path)
        history_path = os.path.join(latest_folder + history_folder)
        copy_folder(history_path, destination_folder)
    elif test_type == "modulewise":
        modules_list = [
            "Dashboard",
            "Displays",
            "DisplayStatus",
            "EmergencyAlerts",
            "Layout",
            "LayoutApproval",
            "LoginAndProfile",
            "Media",
            "Playlists",
            "Schedules",
            "UserAccess"
        ]
        for module_name in modules_list:
            if module_name == module_from_config:
                try:
                    module_directory = f"\\Result_Detail\\{environment}\\{module_from_config}"
                    history_folder = "\\history"
                    path = os.path.join(parent_directory + module_directory)
                    latest_folder = get_latest_directory_created(path)
                    history_path = os.path.join(latest_folder + history_folder)
                    copy_folder(history_path, destination_folder)
                except Exception:
                    print(f"Previous execution data is not available for {module_from_config} module.!")


if __name__ == '__main__':
    run()
