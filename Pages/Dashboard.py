import glob
import glob
import logging
import secrets
import time
import re
from datetime import date

import autoit
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage, retry_action, generate_random_string, getTextAfterRetry, generate_random_number, \
    image_to_pdf
from Utilities import configReader
from Utilities.LogUtil import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


log = Logger(__name__, logging.INFO)


def rename_file():
    os.chdir(os.getcwd() + r"/TestData/masterPDF")
    new_file_name = generate_random_string(5) + '.pdf'
    for file in glob.glob("*.pdf"):
        file_name = file
        os.rename(file_name, new_file_name)
    return new_file_name


original_number = ""
display_1 = generate_random_string(5)
display_2 = generate_random_string(5)
base_acc1 = generate_random_string(5)
base_acc2 = generate_random_string(5)
content_1 = generate_random_string(5)
content_2 = generate_random_string(5)
content_3 = generate_random_string(5)
tagName = generate_random_string(3)


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def switch_to_default_win(self):
        default_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != default_window:
                self.driver.switch_to.window(window_handle)
                self.driver.close()

        # Switch back to default window
        self.driver.switch_to.window(default_window)

    def open_dashboard_url(self):
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/dashboard")
        elif env == "pre-prod":
            self.driver.get("ttps://preprod-jiosignage.jio.com/v2/dashboard")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/dashboard")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/dashboard")
        return Dashboard(self.driver)

    def checkForAccount(self):
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(1)
            retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
        else:
            pass
        self.refresh()
        time.sleep(1)
        return self.getCurrentAccount()

    def clearTrashImages(self):
        time.sleep(3)
        self.selenium_click("MENU_CONTENT_XPATH")
        time.sleep(1)
        self.selenium_click("SUBMENU_MATERIALS_XPATH")
        time.sleep(4)
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        self.click("S_TRASHED_XPATH")
        time.sleep(3)
        self.click("S_TYPE_DROPDOWN_XPATH")
        self.click("S_DROPDOWN_IMAGES_XPATH")
        total_images = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', total_images)[-1]
        log.logger.info("total Images count in trash : " + str(count))
        if int(count) != 0:
            self.click("S_ALL_DATA_ID")
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
        else:
            log.logger.info("No image present in trash..")
        return Dashboard(self.driver)

    def clearTrashVideos(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        time.sleep(1)
        self.click("S_TRASHED_XPATH")
        time.sleep(1.5)
        self.click("S_TYPE_DROPDOWN_XPATH")
        time.sleep(1)
        self.click("S_DROPDOWN_VIDEOS_XPATH")
        total_images = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', total_images)[-1]
        log.logger.info("total Images count in trash : " + str(count))
        if int(count) != 0:
            self.click("S_ALL_DATA_ID")
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            time.sleep(1)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
        else:
            log.logger.info("No video present in trash..")
        return Dashboard(self.driver)

    def clearTrashAudios(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        time.sleep(1)
        self.click("S_TRASHED_XPATH")
        time.sleep(1)
        self.click("S_TYPE_DROPDOWN_XPATH")
        time.sleep(2)
        self.click("S_DROPDOWN_AUDIOS_XPATH")
        total_images = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', total_images)[-1]
        log.logger.info("total Images count in trash : " + str(count))
        if int(count) != 0:
            self.click("S_ALL_DATA_ID")
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
        else:
            log.logger.info("No Audio present in trash..")
        return Dashboard(self.driver)

    def clearTrashDocuments(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        time.sleep(1)
        self.click("S_TRASHED_XPATH")
        time.sleep(1.5)
        self.click("S_TYPE_DROPDOWN_XPATH")
        time.sleep(1)
        self.click("S_DROPDOWN_DOC_XPATH")
        total_images = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', total_images)[-1]
        log.logger.info("total Images count in trash : " + str(count))
        if int(count) != 0:
            self.click("S_ALL_DATA_ID")
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
        else:
            log.logger.info("No video present in trash..")
        return Dashboard(self.driver)

    def createBase(self, BaseAcc):
        self.checkForAccount()
        self.selenium_click("S_UA_XPATH")
        self.selenium_click("S_BM_XPATH")
        self.click("S_NB_ACC_XPATH")
        self.send_keys("S_BASE_ACC_NAME_XPATH", BaseAcc)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)
        return Dashboard(self.driver)

    def createBaseAcc1(self):
        self.createBase(base_acc1)
        return Dashboard(self.driver)

    def createBaseAcc2(self):
        self.createBase(base_acc2)
        return Dashboard(self.driver)

    def delBase(self, baseName):
        self.checkForAccount()
        self.selenium_click("S_UA_XPATH")
        self.selenium_click("S_BM_XPATH")

    def contentPopupRemoval(self):
        # time.sleep(2)
        # self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return Dashboard(self.driver)

    def createContent(self, contentName):
        self.refresh()
        content_count = self.getText("S_ALL_CONTENT_COUNT_XPATH")
        if content_count == "0":
            self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
            self.click("S_CREATE_CONTENT_XPATH")
            self.send_keys("S_CONTENT_NAME_XPATH", contentName)
            self.click("S_BLANK_TMP_XPATH")
            self.click("S_SUBMIT_BUTTON_ID")
            self.contentPopupRemoval()
            self.click("O_CONTENT_OK_BTN_XPATH")
            self.contentPopupRemoval()
        else:
            pass
        return Dashboard(self.driver)

    def createContent1(self):
        self.createContent(content_1)
        return Dashboard(self.driver)

    def createContent2(self):
        self.createContent(content_2)
        return Dashboard(self.driver)

    def createContent3(self):
        self.createContent(content_3)
        return Dashboard(self.driver)

    def deleteContent(self):
        try:
            self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.selenium_click("O_ALL_CLM_XPATH")
            time.sleep(2)
            self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
            more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
            self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
            time.sleep(1)
            self.refresh()
            self.click("O_TRASHED_FOLDER_BTN_XPATH")
            time.sleep(2)
            self.click("O_ALL_CLM_XPATH")
            self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
            more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.click("D_delete_completely_XPATH")
            self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
            time.sleep(1)
            self.refresh()
            self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
            time.sleep(2)
            return Dashboard(self.driver)
        except:
            return Dashboard(self.driver)

    def switchToHead(self):
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Base User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(1)
            switch_to_head = self.driver.find_element(By.XPATH, "//input[@value='Switch to Head Account']")
            self.driver.execute_script("arguments[0].click();", switch_to_head)
            # retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
            time.sleep(1)
            # self.click("S_HEAD_ID")
            # self.click("S_SWITCH_TO_HEAD_XPATH")
        else:
            pass
        self.refresh()
        # return Dashboard(self.driver)

    def verifyDashboardURL(self):
        return self.get_current_url()

    def verifyWelcomeMsg(self):
        heading = self.getText("S_HEADING_XPATH")
        subheading = self.getText("S_SUBHEADING_XPATH")
        return heading + subheading

    def verifyDisplayCount(self):
        displayCount = self.getText("S_DISPLAY_COUNT_XPATH")
        return displayCount

    def get_used_display_count(self):
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "deliver_mgmt_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "deliver_mgmt_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "deliver_mgmt_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "deliver_mgmt_sit2_url"))
        self.refresh()
        total_display = self.getText("S_TOTAL_DISPLAY_XPATH")
        count = re.findall(r'\d+', total_display)[-1]
        log.logger.info("get_used_display_count is : " + str(count))
        return count

    def createDisplay(self, displayName):
        time.sleep(2)
        self.selenium_click("MENU_CONTENT_XPATH")
        self.wait_for_visible("SUBMENU_DISPLAY_XPATH")
        self.selenium_click("SUBMENU_DISPLAY_XPATH")
        self.click("S_ADD_NEW_DISPLAY_XPATH")
        self.send_keys("S_DISPLAY_NAME_XPATH", displayName)
        self.send_keys("S_DISPLAY_PASSWORD_XPATH", "February579")
        self.send_keys("S_DISPLAY_CONF_PASSWORD_XPATH", "February579")
        time.sleep(1)
        self.click("S_DISPLAY_POPUP_ADD_BTN_XPATH")
        time.sleep(2)
        return Dashboard(self.driver)

    def createDisplay_2(self):
        self.createDisplay(display_2)
        return Dashboard(self.driver)

    def addTagToDisplay(self):
        time.sleep(2)
        display_checkbox = f"//td//a//span[contains(text(),'{display_2}')]/preceding::input[@type='checkbox'][1]"
        time.sleep(3)
        self.driver.find_element(By.XPATH, display_checkbox).click()
        self.wait_for_visible_all_elements("O_DISPLAY_THREE_DOT_XPATH")
        self.click("O_DISPLAY_THREE_DOT_XPATH")
        self.click("S_ADD_TAG_XPATH")
        self.wait_for_visible("O_EDITNAME_POPUP_HEADING_XPATH")
        self.send_keys("O_NEW_TAG_TEXTBOX_XPATH", tagName)
        self.click("S_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Dashboard(self.driver)

    # code changes by shivaji
    def getDisplayOnDash(self):
        self.click("DASHBOARD_XPATH")
        time.sleep(2)
        used_disp = self.getText("S_USED_DISPLAY_XPATH")
        if int(used_disp) == 0:
            time.sleep(1)
            self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
            self.click("S_ADD_NEW_DISPLAY_XPATH")
            self.send_keys("S_DISPLAY_NAME_XPATH", display_1)
            self.send_keys("S_DISPLAY_PASSWORD_XPATH", "112233")
            self.send_keys("S_DISPLAY_CONF_PASSWORD_XPATH", "112233")
            self.click("S_DISPLAY_POPUP_ADD_BTN_XPATH")
            time.sleep(2)
        else:
            pass
        return Dashboard(self.driver)

    def verifyUsedDisplayCount(self):
        time.sleep(2)
        self.click("DASHBOARD_XPATH")
        self.refresh()
        time.sleep(2)
        use_display = self.getText("S_USED_DISPLAY_XPATH")
        return use_display

    def getUsedServerStorage(self):
        acc = self.find_element("S_USER_ID")
        # WebDriverWait(self.driver, 20).until(EC.staleness_of(acc))
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(3)
        self.click("S_SERVICE_PLAN_XPATH")
        total_storage = self.getText("S_STORAGE_XPATH")
        storage_num = re.search(r'\d+', total_storage).group()
        return storage_num

    def getUsedStoragePerValue(self):
        self.refresh()
        # acc = self.find_element("S_USER_ID")
        # WebDriverWait(self.driver, 20).until(EC.staleness_of(acc))
        self.click("S_USER_ID")
        self.click("S_SERVICE_PLAN_XPATH")
        total_Used_storage_per = self.getText("S_USED_STORAGE_ID")
        return total_Used_storage_per

    def getTotalServerStorage(self):
        acc = self.find_element("S_USER_ID")
        self.driver.execute_script("arguments[0].click();", acc)
        SERVICE_PLAN = self.find_element("S_SERVICE_PLAN_XPATH")
        self.driver.execute_script("arguments[0].click();", SERVICE_PLAN)
        total_storage = self.getText("S_STORAGE_XPATH")
        totalStorage = re.findall(r'\d+', total_storage)[-1]
        return totalStorage

    def verifyUsedStorage(self):
        storage = self.getText("S_SERVICE_PLAN_XPATH")
        return storage

    def redirectToStorage(self):
        acc = self.find_element("S_SP_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(2)
        return self.getText("S_SERVICE_PLAN_HOME_XPATH")

    def getServerDetails(self):
        acc = self.find_element("S_USER_ID")
        self.driver.execute_script("arguments[0].click();", acc)
        self.click("S_SERVICE_PLAN_XPATH")
        total_storage = self.getText("S_STORAGE_XPATH")
        return total_storage

    def verifyMediaUploadLoc(self):
        return self.is_visible("S_MEDIA_UPLOADED_XPATH")

    def checkForImage(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        photo_count = self.find_elements("S_PHOTO_XPATH")
        log.logger.info(len(photo_count))
        if len(photo_count) == 0:
            log.logger.info("THERE IS NO DATA")
        else:
            self.wait_for_visible_all_elements("S_CHECKBOX_XPATH")
            checkbox = self.find_element("S_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", checkbox)
            self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
            more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
            moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
            self.driver.execute_script("arguments[0].click();", moveTrash)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(3)
            self.click("S_TRASHED_XPATH")
            check = self.find_element("S_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", check)
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            time.sleep(1)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")

    # code by shivaji

    def uploadImageForTesting(self):
        img_count = self.getText("S_IMAGES_COUNT_XPATH")
        if img_count == "0":
            time.sleep(3)
            if configReader.getTestData("TestData", "Environment") == "prod":
                self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
            time.sleep(3)
            # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(3)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\thomas_cook.jpg'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        else:
            time.sleep(2)
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        return Dashboard(self.driver)

    def getTotalImagesCountOnDash(self):
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(3)
        img_count = self.getText("S_IMAGES_COUNT_XPATH")
        return img_count
        # acc = self.find_element("S_IMAGES_COUNT_XPATH")
        # self.driver.execute_script("arguments[0].click();", acc)
        # time.sleep(2)
        # totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        # count = re.findall(r'\d+', totalImages)[-1]
        # log.logger.info("totalImages count : " + count)
        # return count

    def getTotalImagesCount(self):
        acc = self.find_element("S_IMAGES_COUNT_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(2)
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("totalImages count : " + count)
        return count

    def getImgCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
        time.sleep(1)
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("Image count : " + str(count))
        return count

    def getTotalRowCount(self):
        acc = self.find_element("S_IMAGES_COUNT_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(2)
        # self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        # time.sleep(2)
        row_Count = len(self.find_elements("S_TOTAL_ROWS_XPATH"))
        log.logger.info("row_Count : " + str(row_Count))
        return row_Count - 1

    def getJpegPngImagesCount(self):
        acc = self.find_element("S_IMAGES_COUNT_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        jpegPng = len(self.find_elements("S_TOTAL_JPG_PNG_IMAGES_XPATH"))
        return jpegPng

    # shivaji code new
    def uploadVideoForTesting(self):
        img_count = self.getText("S_VIDEOS_COUNT_XPATH")
        if img_count == "0":
            time.sleep(3)
            if configReader.getTestData("TestData", "Environment") == "prod":
                self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
            time.sleep(3)
            # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(3)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\videoSample.mp4'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        else:
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        return Dashboard(self.driver)

    def getTotalVideosCount(self):
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(3)
        video_count = self.getText("S_VIDEOS_COUNT_XPATH")
        return video_count

        # self.click("DASHBOARD_XPATH")
        # retry_action(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=video']")
        # acc = self.find_element("S_VIDEOS_COUNT_XPATH")
        # WebDriverWait(self.driver, 20).until(EC.staleness_of(acc))
        # self.click("S_VIDEOS_COUNT_XPATH")
        # time.sleep(2)
        # totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        # count = re.findall(r'\d+', totalImages)[-1]
        # log.logger.info("count : " + count)
        # return count

    def getVideoRow(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        row_Count = len(self.find_elements("S_TOTAL_ROWS_XPATH"))
        return row_Count - 1

    def getVideos(self):
        retry_action(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=video']")
        # acc = self.find_element("S_VIDEOS_COUNT_XPATH")
        # WebDriverWait(self.driver, 20).until(EC.staleness_of(acc))
        # self.click("S_VIDEOS_COUNT_XPATH")
        # time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        videos = len(self.find_elements("S_TOTAL_VIDEOS_XPATH"))
        return videos

    def uploadDocForTesting(self):
        img_count = self.getText("S_DOC_COUNT_XPATH")
        if img_count == "0":
            time.sleep(3)
            if configReader.getTestData("TestData", "Environment") == "prod":
                self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
            time.sleep(3)
            # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(3)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\doc_Sample.pdf'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        else:
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        return Dashboard(self.driver)

    def uploadAudioForTesting(self):
        img_count = self.getText("S_AUDIO_COUNT_XPATH")
        if img_count == "0":
            time.sleep(3)
            if configReader.getTestData("TestData", "Environment") == "prod":
                self.driver.get(configReader.getTestData("TestData", "audio_content_prod_url"))
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                self.driver.get(configReader.getTestData("TestData", "audio_content_preprod_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                self.driver.get(configReader.getTestData("TestData", "audio_content_sit1_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                self.driver.get(configReader.getTestData("TestData", "audio_content_sit2_url"))
            time.sleep(3)
            # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(3)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\audio_sample.mp3'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        else:
            self.click("DASHBOARD_XPATH")
            time.sleep(2)
        return Dashboard(self.driver)

    def getTotalDocCount(self):
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(3)
        doc_count = self.getText("S_DOC_COUNT_XPATH")
        return doc_count

        # acc = self.find_element("S_DOC_COUNT_XPATH")
        # self.driver.execute_script("arguments[0].click();", acc)
        # time.sleep(2)
        # totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        # count = re.findall(r'\d+', totalImages)[-1]
        # log.logger.info("count : " + count)
        # return count

    def getDocumentCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
        time.sleep(2)
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("Document count : " + str(count))
        return count

    def getDocRow(self):
        time.sleep(1)
        acc = self.find_element("S_DOC_COUNT_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        row_Count = len(self.find_elements("S_TOTAL_ROWS_XPATH"))
        log.logger.info(row_Count)
        return row_Count - 1

    def getDoc(self):
        time.sleep(1)
        self.click("S_DOC_COUNT_XPATH")
        # acc = self.find_element("S_DOC_COUNT_XPATH")
        # self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        doc = len(self.find_elements("S_TOTAL_DOC_XPATH"))
        return doc

    def getTotalAudioCount(self):
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(3)
        doc_count = self.getText("S_AUDIO_COUNT_XPATH")
        return doc_count

    def getAudioCounts(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit2_url"))
        time.sleep(2)
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("Audio count : " + str(count))
        return count

    def getAudioRow(self):
        time.sleep(1)
        acc = self.find_element("S_AUDIO_COUNT_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(2)
        # self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        row_Count = len(self.find_elements("S_TOTAL_AUDIO_XPATH"))
        return row_Count - 1

    def getAudio(self):
        time.sleep(1)
        acc = self.find_element("S_AUDIO_COUNT_XPATH")
        self.driver.execute_script("arguments[0].click();", acc)
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        Audios = len(self.find_elements("S_TOTAL_AUDIO_XPATH"))
        return Audios

    def verifyImageUpload(self):
        self.refresh()
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        self.click("S_ADD_MATERIAL_XPATH")
        self.selenium_click("S_DRAG_DROP_XPATH")
        time.sleep(3)
        cwd = os.getcwd()
        log.logger.info(cwd)
        file_path = cwd + r'\TestData\IMG_20220809_103726_404.jpg'
        log.logger.info(file_path)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
        log.logger.info(self.getText("S_FILE_NAME_XPATH"))
        self.click("S_UPLOAD_BUTTON_ID")
        time.sleep(5)
        self.refresh()
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("count : " + count)
        return count

    def check_if_image_present(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        photo_count = self.find_elements("S_PHOTO_XPATH")
        log.logger.info(len(photo_count))
        if len(photo_count) == 0:
            log.logger.info("Image is not present hence uploading...")
            self.refresh()
            self.click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(3)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\IMG_20220809_103726_404.jpg'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
        else:
            log.logger.info("Image is present...")
            pass
        return Dashboard(self.driver)

    def deleteUploadedImage(self, imageName):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
        time.sleep(7)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{imageName}')]/preceding::input[@type='checkbox'][1]"
        #checkbox_XPATH = f"//td//a//span[contains(@title,'{imageName}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(4)
        self.click("S_TRASHED_XPATH")
        trashCheckbox_XPATH = f"//span[contains(text(),'{imageName}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, trashCheckbox_XPATH).click()
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(4)

    def deleteUploadedVideo(self, videoName):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        time.sleep(1)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{videoName}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        self.click("S_TRASHED_XPATH")
        trashCheckbox_XPATH = f"//span[contains(text(),'{videoName}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, trashCheckbox_XPATH).click()
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)

    def deleteUploadedAudio(self, audioName):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit2_url"))
        time.sleep(1)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{audioName}')]/preceding::input[@type='checkbox'][1]"
        #self.driver.find_element(By.XPATH, checkbox_XPATH).click()#Old one
        #Changed by Akash
        checkbox = self.driver.find_element(By.XPATH, checkbox_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", checkbox)
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", checkbox)
        #970 to 973

        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        self.click("S_TRASHED_XPATH")
        trashCheckbox_XPATH = f"//span[contains(text(),'{audioName}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, trashCheckbox_XPATH).click()
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)

    def deleteUploadedDocs(self, docName):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
        time.sleep(1)
        self.refresh()
        self.refresh()
        checkbox_XPATH = f"//td[normalize-space()='{docName}']/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        self.click("S_TRASHED_XPATH")
        trashCheckbox_XPATH = f"//td[normalize-space()='{docName}']/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, trashCheckbox_XPATH).click()
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)

    def delImage(self):
        #self.deleteUploadedImage("IMG_20220809_103726_404.jpg")
        self.deleteUploadedImage("IMG_20220809_103726_...")


    def delVideo(self):
        #self.deleteUploadedVideo("VID20220313071328.mp4")
        self.deleteUploadedVideo("VID20220313071328.mp...")

    def delAudio(self):
        #self.deleteUploadedAudio("file_example_MP3_1MG.mp3")
        self.deleteUploadedAudio("file_example_MP3_1MG...")

    def delDoc(self):
        self.deleteUploadedDocs("samplepdf.pdf")

    def delDoc1(self):
        self.deleteUploadedDocs("test_doc.pdf")
        return Dashboard(self.driver)

    def deleteImage(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
        time.sleep(2)
        self.wait_for_visible_all_elements("S_CHECKBOX_XPATH")
        checkbox = self.find_element("S_CHECKBOX_XPATH")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        self.click("S_TRASHED_XPATH")
        check = self.find_element("S_CHECKBOX_XPATH")
        self.driver.execute_script("arguments[0].click();", check)
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "image_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "image_content_sit2_url"))
        self.refresh()
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("image count after delete : " + count)
        return count

    def checkForVideo(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        self.refresh()
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        video_count = self.find_elements("S_VIDEO_XPATH")
        log.logger.info(len(video_count))
        if len(video_count) == 0:
            log.logger.info("THERE IS NO DATA")
        else:
            self.wait_for_visible_all_elements("S_VIDEO_CHECKBOX_XPATH")
            checkbox = self.find_element("S_VIDEO_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", checkbox)
            self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
            more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
            moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
            self.driver.execute_script("arguments[0].click();", moveTrash)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(3)
            self.click("S_TRASHED_XPATH")
            check = self.find_element("S_VIDEO_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", check)
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            time.sleep(1)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(10)

    def checkForVideo_ifPresent(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        self.refresh()
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        video_count = self.find_elements("S_VIDEO_XPATH")
        log.logger.info(len(video_count))
        if len(video_count) == 0:
            log.logger.info("THERE IS NO DATA HENCE UPLOADING")
            self.refresh()
            time.sleep(1)
            self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.selenium_click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(5)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\VID20220313071328.mp4'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.refresh()
        else:
            log.logger.info("Video is already present")

    def checkForAudio_ifPresent(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit2_url"))
        self.refresh()
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        audio_count = self.find_elements("S_AUDIO_XPATH")
        log.logger.info(len(audio_count))
        if len(audio_count) == 0:
            log.logger.info("THERE IS NO DATA HENCE UPLOADING")
            self.refresh()
            time.sleep(1)
            self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.selenium_click("S_ADD_MATERIAL_XPATH")
            self.selenium_click("S_DRAG_DROP_XPATH")
            time.sleep(5)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\file_example_MP3_1MG.mp3'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.refresh()
        else:
            log.logger.info("Audio file is already present")

    def getVideoCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        time.sleep(2)
        totalImages = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        count = re.findall(r'\d+', totalImages)[-1]
        log.logger.info("Image count : " + str(count))
        return count
        # getCount = self.getText("S_VIDEOS_COUNT_XPATH")
        # getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=video']")
        # return self.getText("S_VIDEOS_COUNT_XPATH")

    def getAudioCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(2)
        getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=sound']")
        return self.getText("S_AUDIO_COUNT_XPATH")

    def verifyAudioUpload(self):
        self.refresh()
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        self.click("S_ADD_MATERIAL_XPATH")
        self.selenium_click("S_DRAG_DROP_XPATH")
        time.sleep(3)
        cwd = os.getcwd()
        log.logger.info(cwd)
        file_path = cwd + r'\TestData\file_example_MP3_1MG.mp3'
        log.logger.info(file_path)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
        log.logger.info(self.getText("S_FILE_NAME_XPATH"))
        self.click("S_UPLOAD_BUTTON_ID")
        time.sleep(5)
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(2)
        getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=sound']")
        return self.getText("S_AUDIO_COUNT_XPATH")

    def deleteAudio(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit2_url"))
        self.wait_for_visible_all_elements("S_AUDIO_CHECKBOX_XPATH")
        checkbox = self.find_element("S_AUDIO_CHECKBOX_XPATH")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        self.click("S_TRASHED_XPATH")
        check = self.find_element("S_AUDIO_CHECKBOX_XPATH")
        self.driver.execute_script("arguments[0].click();", check)
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(1)
        getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=sound']")
        return self.getText("S_AUDIO_COUNT_XPATH")

    def checkForAudioFile(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "audio_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "audio_content_sit2_url"))
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        photo_count = self.find_elements("S_AUDIO_XPATH")
        log.logger.info(len(photo_count))
        if len(photo_count) == 0:
            log.logger.info("THERE IS NO DATA")
        else:
            self.wait_for_visible_all_elements("S_AUDIO_CHECKBOX_XPATH")
            checkbox = self.find_element("S_AUDIO_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", checkbox)
            self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
            more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
            moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
            self.driver.execute_script("arguments[0].click();", moveTrash)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(3)
            self.click("S_TRASHED_XPATH")
            check = self.find_element("S_AUDIO_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", check)
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            time.sleep(1)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(2)

    def checkForDoc_ifPresent(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        doc_count = self.find_elements("S_SAMPLE_PDF_XPATH")
        log.logger.info("document count is : " + str(len(doc_count)))
        if len(doc_count) == 0:
            log.logger.info("THERE IS NO DATA")
        else:
            self.wait_for_visible_all_elements("S_SAMPLE_DOC_CHECKBOX_XPATH")
            checkbox = self.find_element("S_SAMPLE_DOC_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", checkbox)
            self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
            more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
            moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
            self.driver.execute_script("arguments[0].click();", moveTrash)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(3)
            self.click("S_TRASHED_XPATH")
            check = self.find_element("S_SAMPLE_DOC_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", check)
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            time.sleep(1)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(2)

    def checkForDoc_isPresent(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        doc_count = self.find_elements("S_TEST_PDF_SAMPLE_XPATH")
        log.logger.info("document count is : " + str(len(doc_count)))
        if len(doc_count) == 0:
            log.logger.info("THERE IS NO DATA")
        else:
            self.wait_for_visible_all_elements("S_SAMPLE_DOC_CHECKBOX_XPATH")
            checkbox = self.find_element("S_SAMPLE_DOC_CHECKBOX_XPATH")
            self.driver.execute_script("arguments[0].click();", checkbox)
            self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
            more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
            moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
            self.driver.execute_script("arguments[0].click();", moveTrash)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(3)
            self.click("S_TRASHED_XPATH")
            check = self.find_element("S_TEST_PDF_SAMPLE_XPATH")
            self.driver.execute_script("arguments[0].click();", check)
            more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
            self.driver.execute_script("arguments[0].click();", more)
            time.sleep(1)
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(2)
        return Dashboard(self.driver)

    def DocUpload(self):
        self.refresh()
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        self.click("S_ADD_MATERIAL_XPATH")
        self.selenium_click("S_DRAG_DROP_XPATH")
        time.sleep(3)
        cwd = os.getcwd()
        log.logger.info(cwd)
        file_path = cwd + r'\TestData\test_doc.pdf'
        log.logger.info(file_path)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
        log.logger.info("File name  : " + self.getText("S_FILE_NAME_XPATH"))
        self.click("S_UPLOAD_BUTTON_ID")
        time.sleep(5)
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(1)
        self.refresh()
        self.refresh()
        time.sleep(2)
        # getTextAfterRetry(self.driver, By.XPATH, "S_TOTAL_DOC_COUNT_XPATH")
        return self.getText("S_TOTAL_DOC_COUNT_XPATH")

    def checkForDocFile(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
        self.refresh()
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        doc_count = self.find_elements("S_DOC_XPATH")
        log.logger.info(len(doc_count))
        if len(doc_count) == 0:
            log.logger.info("THERE IS NO DATA HENCE UPLOADING")
            self.refresh()
            time.sleep(1)
            self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
            self.click("S_ADD_MATERIAL_XPATH")
            self.click("S_DRAG_DROP_XPATH")
            time.sleep(5)
            cwd = os.getcwd()
            log.logger.info(cwd)
            file_path = cwd + r'\TestData\BP_26Jan.pdf'
            log.logger.info(file_path)
            autoit.control_focus("Open", "Edit1")
            time.sleep(2)
            autoit.control_set_text("Open", "Edit1", file_path)
            time.sleep(2)
            autoit.control_send("Open", "Button1", "{ENTER}")
            self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
            log.logger.info(self.getText("S_FILE_NAME_XPATH"))
            self.click("S_UPLOAD_BUTTON_ID")
            time.sleep(5)
            self.refresh()
        else:
            log.logger.info("Document is already present")

    def uploadDocument(self):
        name = rename_file()
        log.logger.info("File name os  : " + name)
        os.chdir("..")
        os.chdir("..")
        self.refresh()
        time.sleep(1)
        log.logger.info(name)
        self.click("MENU_CONTENT_XPATH")
        self.click("SUBMENU_MATERIALS_XPATH")
        self.click("S_ADD_MATERIAL_XPATH")
        self.selenium_click("S_DRAG_DROP_XPATH")
        time.sleep(3)
        file_path = os.getcwd() + "\\TestData\\masterPDF\\" + name
        log.logger.info(file_path)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
        log.logger.info(self.getText("S_FILE_NAME_XPATH"))
        self.click("S_UPLOAD_BUTTON_ID")
        self.wait_for_invisible("S_UPLOAD_XPATH")
        time.sleep(10)
        self.refresh()
        return name

    def getDocCount(self):
        time.sleep(2)
        self.selenium_click("DASHBOARD_XPATH")
        # if configReader.getTestData("TestData", "Environment") == "prod":
        #     self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        # elif configReader.getTestData("TestData", "Environment") == "pre-prod":
        #     self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        time.sleep(1)
        # getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=document']")
        return self.getText("S_DOC_COUNT_XPATH")

    def verifyDocumentUpload(self):
        self.refresh()
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        self.click("S_ADD_MATERIAL_XPATH")
        self.selenium_click("S_DRAG_DROP_XPATH")
        time.sleep(3)
        cwd = os.getcwd()
        log.logger.info(cwd)
        file_path = cwd + r'\TestData\samplepdf.pdf'
        log.logger.info(file_path)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
        log.logger.info("File name  : " + self.getText("S_FILE_NAME_XPATH"))
        self.click("S_UPLOAD_BUTTON_ID")
        time.sleep(5)
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(1)
        self.refresh()
        self.refresh()
        time.sleep(2)
        # getTextAfterRetry(self.driver, By.XPATH, "S_TOTAL_DOC_COUNT_XPATH")
        return self.getText("S_TOTAL_DOC_COUNT_XPATH")

    def deleteDocument(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "doc_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "doc_content_sit2_url"))
        time.sleep(2)
        ele = f"//td[normalize-space()='test_doc.pdf']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        self.click("S_TRASHED_XPATH")
        ele = f"//td[normalize-space()='test_doc.pdf']/preceding::input[@type='checkbox'][1]"
        check = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", check)
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(2)
        self.refresh()
        # getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=document']")
        return self.getText("S_DOC_COUNT_XPATH")

    def deleteVideo(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        time.sleep(2)
        self.wait_for_visible_all_elements("S_VIDEO_CHECKBOX_XPATH")
        checkbox = self.find_element("S_VIDEO_CHECKBOX_XPATH")
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_MATERIAL_XPATH")
        more_options = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        self.click("S_TRASHED_XPATH")
        check = self.find_element("S_VIDEO_CHECKBOX_XPATH")
        self.driver.execute_script("arguments[0].click();", check)
        more = self.find_element("S_MORE_OPTION_MATERIAL_XPATH")
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        time.sleep(2)
        getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=video']")
        return self.getText("S_VIDEOS_COUNT_XPATH")

    def uploadVideo(self):
        self.refresh()
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        self.click("S_ADD_MATERIAL_XPATH")
        self.selenium_click("S_DRAG_DROP_XPATH")
        time.sleep(5)
        cwd = os.getcwd()
        log.logger.info(cwd)
        file_path = cwd + r'\TestData\VID20220313071328.mp4'
        log.logger.info(file_path)
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.wait_for_visible_all_elements("S_FILE_NAME_XPATH")
        log.logger.info(self.getText("S_FILE_NAME_XPATH"))
        self.click("S_UPLOAD_BUTTON_ID")
        time.sleep(5)
        self.refresh()
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "video_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "video_content_sit2_url"))
        self.refresh()
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        row_Count = len(self.find_elements("S_TOTAL_ROWS_XPATH"))
        return row_Count - 1

    def verifyContentLoc(self):
        return self.is_visible("S_CONTENT_LOC_XPATH")

    def getAllContentCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        self.refresh()
        total_count = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        content_count = re.findall(r'\d+', total_count)[-1]
        return content_count

    def getContentCountOnDash(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        return self.getText("S_ALL_CONTENT_COUNT_XPATH")

    def get_7Days_content(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "content_expire_7_days_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "content_expire_7_days_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "content_expire_7_days_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "content_expire_7_days_sit2_url"))
        total_count = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        content_count = re.findall(r'\d+', total_count)[-1]
        return content_count

    def verify_7Days_content(self):
        self.refresh()
        self.wait_for_visible("S_CONTENT_EXPIRE_SEVEN_DAYS_XPATH")
        EXPIRE_SEVEN_DAYS = self.getText("S_CONTENT_EXPIRE_SEVEN_DAYS_XPATH")
        return int(EXPIRE_SEVEN_DAYS)

    def get_expired_content(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "content_expired_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "content_expired_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "content_expired_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "content_expired_sit2_url"))
        total_count = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        content_count = re.findall(r'\d+', total_count)[-1]
        return content_count

    def verify_expired_content(self):
        self.wait_for_visible("S_CONTENT_EXPIRED_XPATH")
        return self.getText("S_CONTENT_EXPIRED_XPATH")

    def verify_7_days_content_expire_url(self):
        retry_action(self.driver, By.XPATH, "//a[contains(@href,'/v2/contents?type=expire_within_7_days')]")
        return self.get_current_url()

    def verify_content_expired_url(self):
        time.sleep(1)
        self.click("S_CONTENT_EXPIRED_XPATH")
        time.sleep(1)
        # retry_action(self.driver, By.XPATH, "//a[contains(@href,'/v2/contents?type=expired')]")
        return self.get_current_url()

    def verifyContentAfterAdd(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        content_name = generate_random_string(5)
        self.send_keys("S_CONTENT_NAME_XPATH", content_name)
        self.click("S_BLANK_TMP_XPATH")
        self.click("S_SUBMIT_BUTTON_ID")
        self.wait_for_visible_all_elements("S_POPUP_XPATH")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "dashboard_sit2_url"))
        log.logger.info(self.getText("S_ALL_CONTENT_COUNT_XPATH"))
        return self.getText("S_ALL_CONTENT_COUNT_XPATH")

    def verifyPlaylistLoc(self):
        return self.is_visible("S_PLAYLIST_LOCATION_XPATH")

    def getPlaylistCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "playlist_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "playlist_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "playlist_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "playlist_sit2_url"))
        self.wait_for_visible_all_elements("S_TOTAL_IMAGES_COUNT_XPATH")
        total_count = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        content_count = re.findall(r'\d+', total_count)[-1]
        return content_count

    def getPlaylistDetail(self):
        self.wait_for_visible_all_elements("S_TOTAL_PLAYLIST_COUNT_XPATH")
        playlist = self.getText("S_TOTAL_PLAYLIST_COUNT_XPATH")
        return playlist

    def getTotalUploadedCount(self):
        time.sleep(3)
        return getTextAfterRetry(self.driver, By.XPATH, "//h5//a[@href='/v2/materials']")

    def get_allMaterialCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_material_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_material_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_material_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_material_sit2_url"))
        time.sleep(2)
        self.click("S_TYPE_DROPDOWN_XPATH")
        self.click("S_DROPDOWN_IMAGES_XPATH")
        ImageCount = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        img_count = re.findall(r'\d+', ImageCount)[-1]
        log.logger.info("images : " + img_count)
        self.refresh()
        self.click("S_TYPE_DROPDOWN_XPATH")
        self.click("S_DROPDOWN_VIDEOS_XPATH")
        time.sleep(1)
        videoCount = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        vid_count = re.findall(r'\d+', videoCount)[-1]
        log.logger.info("Videos : " + vid_count)
        self.refresh()
        self.click("S_TYPE_DROPDOWN_XPATH")
        self.click("S_DROPDOWN_AUDIOS_XPATH")
        time.sleep(1)
        audioCount = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        aud_count = re.findall(r'\d+', audioCount)[-1]
        log.logger.info("Audios : " + aud_count)
        self.refresh()
        self.click("S_TYPE_DROPDOWN_XPATH")
        self.click("S_DROPDOWN_DOC_XPATH")
        time.sleep(1)
        docCount = self.getText("S_TOTAL_IMAGES_COUNT_XPATH")
        doc_count = re.findall(r'\d+', docCount)[-1]
        log.logger.info("Document : " + doc_count)
        total_materials = int(img_count) + int(vid_count) + int(aud_count) + int(doc_count)
        log.logger.info("TOTAL : " + str(total_materials))
        return str(total_materials)

    def allContentMaterialCount(self):
        images_count = getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=image']")
        video_count = getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=video']")
        audio_count = getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=sound']")
        doc_count = getTextAfterRetry(self.driver, By.XPATH, "//h4//a[@href='/v2/materials?type=document']")
        total_materials = int(images_count) + int(video_count) + int(audio_count) + int(doc_count)
        return str(total_materials)

    def verifyStateWiseDisplayLoc(self):
        return self.is_visible("S_STATE_WISE_DISPLAY_LOCATION_XPATH")

    def verifyTagWiseDisplayLoc(self):
        self.scroll_to_element("N_TAG_WISE_DISPLAY_LOCATION_XPATH")
        time.sleep(2)
        return self.is_visible("N_TAG_WISE_DISPLAY_LOCATION_XPATH")

    def verifyUsedRemainingLicense(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "service_plan_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "service_plan_sit2_url"))
        time.sleep(1)
        display_text = self.getText("S_DISPLAYS_DETAIL_XPATH")
        log.logger.info(display_text)
        total_used = re.search(r'\d+', display_text).group()
        log.logger.info(total_used)
        total = re.findall(r'\d+', display_text)[-1]
        log.logger.info(total)
        log.logger.info(total_used + "/" + total + " license used")
        return total_used + "/" + total + " license used"

    def getDisplayCountOnDash(self):
        display_count = self.getText("S_DISPLAY_DETAIL_DASH_XPATH")
        log.logger.info(display_count)
        return display_count

    # added some commends for sit1 and sit2
    def verifyStorageDetails(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/profile/plan")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/profile/plan")
        time.sleep(1)
        storage_text = self.getText("S_STORAGE_DETAIL_XPATH")
        log.logger.info(storage_text)
        total_used = re.search(r'\d+', storage_text).group()
        log.logger.info(total_used)
        total = re.findall(r'\d+', storage_text)[-1]
        log.logger.info(total)
        log.logger.info(total_used + "/" + total + " MB")
        return total_used + "/" + total + " MB"

    def getStorageOnDash(self):
        storage_count = self.getText("S_STORAGE_DETAIL_DASH_XPATH")
        log.logger.info(storage_count)
        return storage_count

    def verifyDisplayStatusLocation(self):
        return self.is_visible("S_DISPLAY_SATUS_LOCATION_XPATH")

    def getTotalLicense(self):
        getTextAfterRetry(self.driver, By.XPATH, "//p//a[@href='/v2/displays/status']")
        used_license = self.getText("S_USED_DISPLAY_XPATH")
        log.logger.info(used_license)
        return int(used_license)

    def verifyDisplayStatusCount(self):
        getTextAfterRetry(self.driver, By.XPATH, "//p//a[@href='/v2/displays/status?online=true']")
        online_display = self.getText("S_ONLINE_DISPLAY_XPATH")
        getTextAfterRetry(self.driver, By.XPATH, "//p//a[@href='/v2/displays/status?online=all_offline']")
        offline_display = self.getText("S_OFFLINE_DISPLAY_XPATH")
        getTextAfterRetry(self.driver, By.XPATH, "//p//a[@href='/v2/displays/status?online=not_configured']")
        not_configured_display = self.getText("S_NOT_CONFIGURED_DISPLAY_XPATH")
        return int(online_display) + int(offline_display) + int(not_configured_display)

    def getOnlineDisplayAtDM(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "online_display_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "online_display_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "online_display_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "online_display_sit2_url"))
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        total_entries = self.getText("S_ENTRIES_COUNT_XPATH")
        count = re.findall(r'\d+', total_entries)[-1]
        log.logger.info("count : " + count)
        return count

    def getOfflineDisplayAtDM(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "offline_display_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "offline_display_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "offline_display_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "offline_display_sit2_url"))
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        total_entries = self.getText("S_ENTRIES_COUNT_XPATH")
        count = re.findall(r'\d+', total_entries)[-1]
        log.logger.info("total count is : " + count)
        return count

    def getOnlineDisplayCount(self):
        getTextAfterRetry(self.driver, By.XPATH, "//p//a[@href='/v2/displays/status?online=true']")
        online_display = self.getText("S_ONLINE_DISPLAY_XPATH")
        return online_display

    def getOfflineDisplayCount(self):
        getTextAfterRetry(self.driver, By.XPATH, "//p//a[@href='/v2/displays/status?online=all_offline']")
        offline_display = self.getText("S_OFFLINE_DISPLAY_XPATH")
        return offline_display

    def verifySchedulesLocation(self):
        return self.is_visible("S_SCHEDULES_LOCATION_XPATH")

    def getTotalSchedules(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        total_entries = self.getText("S_ENTRIES_COUNT_XPATH")
        count = re.findall(r'\d+', total_entries)[-1]
        log.logger.info("total count is : " + count)
        return count

    def getScheduleCountOnDashboard(self):
        getTextAfterRetry(self.driver, By.XPATH, "//h5//a[@href='/v2/schedules']")
        return self.getText("S_SCHEDULE_COUNT_XPATH")

    def getTagWiseData(self):
        tag = []
        total_sum = 0
        ele = self.find_element("S_TAG_WISE_CANVAS_XPATH")
        tagCount = ele.get_attribute("data-data")
        values = tagCount.split(', ')
        for value in values:
            tag.append(value)
        for num_str in tag:
            for digit_char in num_str:
                if digit_char.isdigit():
                    total_sum += int(digit_char)
        log.logger.info(str(total_sum))

    def verifyStateWiseDisplayLocation(self):
        return self.is_visible("S_SCHEDULES_LOCATION_XPATH")

    def verifyJioHelp(self):
        getTextAfterRetry(self.driver, By.XPATH, "(//a[@href='https://www.jiothings.com/jiosignage.html'])[2]")
        element = self.driver.find_element(By.XPATH, "(//a[@href='https://www.jiothings.com/jiosignage.html'])[2]")
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.get_current_url()
        self.switch_to_default_win()
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        return current_url

    def verifyJioHelpOnProfile(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//a[normalize-space()='Help']")
        time.sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(1)
        current_url = self.get_current_url()
        # self.driver.close()
        # time.sleep(2)
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # time.sleep(2)
        self.switch_to_default_win()
        return current_url

    def verifyFAQ(self):
        getTextAfterRetry(self.driver, By.XPATH, "//a[@href='/show_faq']")
        element = self.driver.find_element(By.XPATH, "//a[@href='/show_faq']")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(5)
        current_url = self.get_current_url()
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(window_handles[0])
        # self.switch_to_default_win()
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        return current_url

    def verifyFAQOptions(self):
        getTextAfterRetry(self.driver, By.XPATH, "//a[@href='/show_faq']")
        element = self.driver.find_element(By.XPATH, "//a[@href='/show_faq']")
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        time.sleep(5)
        try:
            JS_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[.=' JioSignage ']")
            display_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[.=' Display ']")
            trouble_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[.=' Trouble Shooting ']")
            #content_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[.=' Layout ']")
            try:
                content_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[contains(text(),'Layout')]")
            except:
                content_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[contains(text(),'Content')]")

            pop_txt = getTextAfterRetry(self.driver, By.XPATH, "//a[.=' Proof of Play ']")
            log.logger.info(JS_txt + display_txt + trouble_txt + content_txt + pop_txt)
        except:
            log.logger.info("No text found")    
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(window_handles[0])
        return JS_txt , display_txt , trouble_txt , content_txt , pop_txt

    def verifyLogout(self):
        self.driver.delete_all_cookies()
        retry_action(self.driver, By.ID, "myDropdown")
        self.click("S_LOGOUT_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        self.refresh()
        time.sleep(2)
        url = self.get_current_url()
        return url

    def verifyServicePlan(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//p[@align='center']//a[@href='/v2/profile/plan']")
        time.sleep(2)
        plan_name = self.getText("S_PLAN_NAME_XPATH")
        return plan_name

    def verifyServerUsagePlan(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//p[@align='center']//a[@href='/v2/profile/plan']")
        time.sleep(2)
        server_usage = self.getText("S_PLAN_SERVER_USAGE_XPATH")
        return server_usage

    def verifyDisplayStatusPlan(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//p[@align='center']//a[@href='/v2/profile/plan']")
        time.sleep(2)
        display_status = self.getText("S_PLAN_DISPLAY_STATUS_XPATH")
        return display_status

    def verifyUpdateMismatchPass(self):
        password = configReader.getTestData("TestData", "Password")
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_PASS_XPATH")
        self.clear("S_CURRENT_PASS_XPATH")
        self.clear("S_NEW_PASS1_XPATH")
        self.clear("S_NEW_PASS2_XPATH")
        self.send_keys("S_CURRENT_PASS_XPATH", password)
        self.send_keys("S_NEW_PASS1_XPATH", "Sun@08641")
        self.send_keys("S_NEW_PASS2_XPATH", "Sun@086410")
        self.click("S_SAVE_XPATH")
        self.wait_for_visible_all_elements("S_INVALID_MSG_XPATH")
        new_msg = self.getText("S_INVALID_MSG_XPATH")
        self.refresh()
        return new_msg

    def verifyCrossOnEditPassword(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_PASS_XPATH")
        self.wait_for_visible_all_elements("S_CLOSE_BUTTON_XPATH")
        self.getText("S_INFO_XPATH")
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(1)
        return self.getText("S_INFO_XPATH")

    def verifyCrossOnEditPhoneNum(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.selenium_click("S_EDIT_PHONE_NO_XPATH")
        self.wait_for_visible_all_elements("S_CLOSE_BUTTON_XPATH")
        self.getText("S_NEW_PHONE_ID")
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(1)
        return self.getText("S_NEW_PHONE_ID")

    def getUserName(self):
        time.sleep(2)
        retry_action(self.driver, By.ID, "myDropdown")
        time.sleep(1)
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        time.sleep(1)
        return self.find_element("S_USER_NAME_ID").get_attribute('value')

    def getOriginalNumber(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        return self.find_element("S_MOBILE_XPATH").get_attribute('value')

    def getMobileNumber(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        return self.find_element("S_MOBILE_XPATH").get_attribute('value')

    def verifySaveOptionOnChangeName(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_USER_NAME_XPATH")
        self.clear("S_EDIT_UN_XPATH")
        self.click("S_EDIT_UN_XPATH")
        time.sleep(1)
        name = generate_random_string(5)
        self.send_keys("S_EDIT_UN_XPATH", name)
        time.sleep(1)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)
        return self.find_element("S_USER_NAME_ID").get_attribute('value')

    def verifySaveOptionOnNumberChange(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.selenium_click("S_EDIT_MOBILE_XPATH")
        self.clear("S_UPDATE_MOBILE_XPATH")
        self.click("S_UPDATE_MOBILE_XPATH")
        time.sleep(1)
        mobile_no = generate_random_number(10)
        self.send_keys("S_UPDATE_MOBILE_XPATH", str(mobile_no))
        time.sleep(1)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)
        #return self.find_element("S_MOBILE_XPATH").get_attribute('value')
        #Changed by Akash
        self.wait_for_visible_all_elements("S_MOBILE_XPATH")
        return self.find_element("S_MOBILE_XPATH").get_attribute('value')

    def verifyCancelOptionOnUpdateMobile(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.selenium_click("S_EDIT_MOBILE_XPATH")
        self.clear("S_UPDATE_MOBILE_XPATH")
        self.click("S_UPDATE_MOBILE_XPATH")
        time.sleep(1)
        mobile_no = generate_random_number(10)
        self.send_keys("S_UPDATE_MOBILE_XPATH", str(mobile_no))
        time.sleep(1)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(2)
        return self.find_element("S_MOBILE_XPATH").get_attribute('value')

    def verifyCancelOptionOnMobNum(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_MOBILE_XPATH")
        self.clear("S_UPDATE_MOBILE_XPATH")
        self.click("S_UPDATE_MOBILE_XPATH")
        time.sleep(1)
        mobile_no = generate_random_number(10)
        self.send_keys("S_UPDATE_MOBILE_XPATH", str(mobile_no))
        time.sleep(1)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(2)
        return len(self.find_elements("S_CANCEL_BUTTON_XPATH"))

    def updateOriginalNum(self, num):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.selenium_click("S_EDIT_MOBILE_XPATH")
        self.clear("S_UPDATE_MOBILE_XPATH")
        self.click("S_UPDATE_MOBILE_XPATH")
        time.sleep(1)
        self.send_keys("S_UPDATE_MOBILE_XPATH", num)
        time.sleep(1)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)

    def verifyCancelOptionOnChangeName(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_USER_NAME_XPATH")
        self.clear("S_EDIT_UN_XPATH")
        self.click("S_EDIT_UN_XPATH")
        time.sleep(1)
        name = generate_random_string(5)
        self.send_keys("S_EDIT_UN_XPATH", name)
        time.sleep(1)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(2)
        return self.find_element("S_USER_NAME_ID").get_attribute('value')

    def verifyCancelOption(self):
        time.sleep(3)
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_USER_NAME_XPATH")
        self.clear("S_EDIT_UN_XPATH")
        self.click("S_EDIT_UN_XPATH")
        time.sleep(1)
        name = generate_random_string(5)
        self.send_keys("S_EDIT_UN_XPATH", name)
        time.sleep(1)
        self.click("S_CANCEL_BUTTON_XPATH")
        self.refresh()
        return len(self.find_elements("S_CANCEL_BUTTON_XPATH"))

    def verifyCancelOnEditName(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.CSS_SELECTOR, ".dropdown-item.sub-text.m-0")
        self.click("S_EDIT_USER_NAME_XPATH")
        self.clear("S_EDIT_UN_XPATH")
        self.click("S_EDIT_UN_XPATH")
        self.send_keys("S_EDIT_UN_XPATH", configReader.getTestData("TestData", "new_user_name"))
        self.click("S_SAVE_XPATH")
        time.sleep(2)
        return self.getText("S_USER_NAME_ID")

    def verifyApprovedContentCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        time.sleep(1)
        approved = self.find_elements("S_APPROVED_CONTENT_XPATH")
        return str(len(approved))

    def ApprovedContentCount(self):
        return self.getText("S_APPROVED_CONTENT_COUNT_XPATH")

    def verifyPendingApprovedContentCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            return self.getText("S_PENDING_APPROVAL_CONTENT_XPATH")
        if configReader.getTestData("TestData", "Environment") == "pre-prod":
            return self.getText("S_PENDING_APPROVAL_CONTENT_XPATH")
        if configReader.getTestData("TestData", "Environment") == "sit2":
            return self.getText("S_PENDING_APPROVAL_CONTENT_XPATH")
        if configReader.getTestData("TestData", "Environment") == "sit1":
            return self.getText("(//p[.=' Pending'])[1]/preceding::h4[1]")

    def verifyPendingContentCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(2)
        pending_approved = self.find_elements("S_PENDING_CONTENT_XPATH")
        return str(len(pending_approved))

    def get_totalContentCount(self):
        totalContentCount = getTextAfterRetry(self.driver, By.XPATH, "(//a[@href='/v2/contents'])[2]")
        log.logger.info(totalContentCount)

    def verifyProfileOptions(self):
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//a[@href='/v2/profile/user_details']")
        name = self.find_element("S_USER_NAME_ID").get_attribute('value')
        email_id = self.find_element("S_EMAIL_XPATH").get_attribute('value')
        phone_no = self.find_element("S_MOBILE_XPATH").get_attribute('value')
        password = self.find_element("S_PASSWORD_XPATH").get_attribute('value')
        log.logger.info(name + " " + email_id + " " + phone_no + " " + password)
        return name + " " + email_id + " " + phone_no + " " + password

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def checkForCurrentAccountTypePreProd(self):
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            log.logger.info("Current user is base user hence changing to head user")
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            log.logger.info("dropdownMenuButton1 selected")
            time.sleep(1)
            retry_action(self.driver, By.CSS_SELECTOR, "#switchHead")
            time.sleep(1)
            self.click("S_BASE_DROPDOWN_XPATH")
            time.sleep(1)
            self.click("S_SWITCH_TO_HEAD_XPATH")
            time.sleep(1)
            # self.click("S_ADD_BUTTON_NAME")
            log.logger.info("Changed user to HEAD")
        else:
            log.logger.info("Current user is HEAD user hence not changing")
            pass
        self.refresh()
        self.refresh()
        time.sleep(1)
        log.logger.info("Current account is HEAD : " + self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH"))
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def verifyOkOptionOnSwitchToBaseAccount(self):
        log.logger.info("starting verify Ok Option On Switch To Base Account PreProd ")
        time.sleep(1)
        retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
        time.sleep(1)
        self.selenium_click("S_SWITCH_BASE_ID")
        time.sleep(1)
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        time.sleep(1)
        log.logger.info(base_acc1)
        self.send_keys("S_INPUT_BASE_XPATH", base_acc1)
        time.sleep(1)
        base = f"//li[.='{base_acc1}']"
        self.driver.find_element(By.XPATH, base).click()
        time.sleep(1)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(3)
        self.wait_for_visible_all_elements("S_BU_XPATH")
        log.logger.info("changed account to base ")
        log.logger.info("Current account is BASE  : " + self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH"))
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def verifySwitchToBaseAccount(self):
        log.logger.info("starting verify Ok Option On Switch To Base Account PreProd ")
        time.sleep(1)
        retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
        time.sleep(1)
        self.selenium_click("S_SWITCH_BASE_ID")
        time.sleep(1)
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        time.sleep(1)
        log.logger.info(base_acc2)
        self.send_keys("S_INPUT_BASE_XPATH", base_acc2)
        time.sleep(1)
        base = f"//li[.='{base_acc2}']"
        self.driver.find_element(By.XPATH, base).click()
        time.sleep(1)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(3)
        self.wait_for_visible_all_elements("S_BU_XPATH")
        log.logger.info("changed account to base ")
        log.logger.info("Current account is BASE  : " + self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH"))
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def verifyCancelOptionOnSwitchToBaseAccount(self):
        time.sleep(1)
        retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
        time.sleep(1)
        self.click("S_SWITCH_BASE_ID")
        time.sleep(1)
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        time.sleep(1)
        log.logger.info(base_acc1)
        self.send_keys("S_INPUT_BASE_XPATH", base_acc1)
        time.sleep(1)
        base = f"//li[.='{base_acc1}']"
        self.driver.find_element(By.XPATH, base).click()
        time.sleep(2)
        self.selenium_click("S_CANCEL_BUTTON_XPATH")
        time.sleep(2)
        self.refresh()
        log.logger.info("Current account should be BASE  : " + self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH"))
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def checkForCurrentAccountTypeProd(self):
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(1)
            retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
        else:
            pass
        self.refresh()
        time.sleep(1)
        return self.getCurrentAccount()

    def verifyOkOptionOnSwitchToBaseAccountProd(self):
        log.logger.info("starting verify Ok Option On Switch To Base Account PreProd ")
        time.sleep(1)
        retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
        time.sleep(1)
        self.click("S_SWITCH_BASE_ID")
        time.sleep(1)
        self.click("S_BASE_DROPDOWN_XPATH")
        time.sleep(1)
        log.logger.info(base_acc1)
        self.send_keys("S_INPUT_BASE_XPATH", base_acc1)
        time.sleep(1)
        base = f"//li[.='{base_acc1}']"
        self.driver.find_element(By.XPATH, base).click()
        time.sleep(1)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        self.refresh()
        log.logger.info("changed account to base ")
        log.logger.info("Current account is BASE  : " + self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH"))
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def verifyCancelOptionOnSwitchToBaseAccountProd(self):
        time.sleep(1)
        retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
        time.sleep(1)
        self.click("S_SWITCH_BASE_ID")
        time.sleep(1)
        self.click("S_BASE_DROPDOWN_XPATH")
        time.sleep(1)
        log.logger.info(base_acc1)
        self.send_keys("S_INPUT_BASE_XPATH", base_acc1)
        time.sleep(1)
        base = f"//li[.='{base_acc1}']"
        self.driver.find_element(By.XPATH, base).click()
        time.sleep(1)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(1)
        self.refresh()
        log.logger.info("Current account should be BASE  : " + self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH"))
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def GetTotalUsedStorage(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "service_plan_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "service_plan_sit2_url"))
        time.sleep(1)
        storage_text = self.getText("S_STORAGE_DETAIL_XPATH")
        log.logger.info(storage_text)
        total_used = re.search(r'\d+', storage_text).group()
        log.logger.info(total_used)
        return total_used

    def GetTotalStorage(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "service_plan_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "service_plan_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "service_plan_sit2_url"))
        time.sleep(1)
        storage_text = self.getText("S_STORAGE_DETAIL_XPATH")
        log.logger.info(storage_text)
        total_storage = re.findall(r'\d+', storage_text)[-1]
        log.logger.info(total_storage)
        return total_storage

    def getStorageDataFromCanvas(self):
        data = self.find_element("S_STORAGE_CANVAS_XPATH").get_attribute('data-data')
        bal_storage = re.findall(r'\d+', data)[-1]
        return bal_storage

    def AddContent(self):
        today = date.today()
        d1 = today.strftime("%d%m%Y")
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        content_name = generate_random_string(5)
        self.send_keys("S_CONTENT_NAME_XPATH", content_name)
        time.sleep(1)
        self.click("S_BLANK_TMP_XPATH")
        time.sleep(2)
        self.click("S_SUBMIT_BUTTON_ID")
        time.sleep(10)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        time.sleep(1)
        EL_XPATH = f"//span[@title='{content_name}']"
        retry_action(self.driver, By.XPATH, EL_XPATH)
        time.sleep(3)
        self.wait_for_visible_all_elements("S_CA_NR_XPATH")
        self.wait_for_visible_all_elements("S_CROSS_ICON_XPATH")
        time.sleep(1)
        self.click("S_CROSS_ICON_XPATH")
        self.wait_for_visible_all_elements("S_OK_BUTTON_XPATH")
        self.click("S_OK_BUTTON_XPATH")
        time.sleep(2)
        self.send_keys("S_START_DATE_ID", d1)
        time.sleep(2)
        self.send_keys("S_END_DATE_ID", d1)
        time.sleep(2)
        self.click("S_REQ_APPROVAL_XPATH")
        time.sleep(10)

    def verifyPrivacyPolicy(self):
        self.wait_for_visible_all_elements("S_PRIVACY_XPATH")
        ele = self.find_element("S_PRIVACY_XPATH")
        getTextAfterRetry(self.driver, By.XPATH, "//a[@href='/v2/privacy_policy']")
        self.driver.execute_script("arguments[0].click();", ele)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.get_current_url()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return current_url

    def verifyTermsAndConditions(self):
        self.wait_for_visible_all_elements("S_TC_XPATH")
        ele = self.find_element("S_TC_XPATH")
        getTextAfterRetry(self.driver, By.XPATH, "//a[@href='/v2/terms_condition']")
        self.driver.execute_script("arguments[0].click();", ele)
        self.driver.switch_to.window(self.driver.window_handles[1])
        current_url = self.get_current_url()
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return current_url

        ##########additional######

    def gotoDeliveryMgmt(self):
        time.sleep(2)
        self.wait_for_visible("MENU_DELIVERY_MGMT_XPATH")
        more_options = self.find_element("MENU_DELIVERY_MGMT_XPATH")
        time.sleep(4)
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(1)
        return Dashboard(self.driver)

    def clickOnTagWiseOpt(self):
        time.sleep(2)
        self.wait_for_visible("D_TagWise_Option_XPATH")
        more_options = self.find_element("D_TagWise_Option_XPATH")
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(2)
        count = self.find_elements("D_DelivermngTagg_Count_XPATH")
        count = len(count)
        return count

    def getcounttagwise(self):
        time.sleep(2)
        self.scroll_to_element("D_DashboardTagwise_Count_XPATH")
        self.wait_for_visible("D_DashboardTagwise_Count_XPATH")
        count = self.find_element("D_DashboardTagwise_Count_XPATH").get_attribute("data-data")
        list_from_string = eval(count)
        count = len(list_from_string)
        return count

    def deleteCreatedDisplay(self, displayName):
        time.sleep(1)
        self.selenium_click("MENU_CONTENT_XPATH")
        self.wait_for_visible("SUBMENU_DISPLAY_XPATH")
        self.selenium_click("SUBMENU_DISPLAY_XPATH")
        time.sleep(1)
        display_title = f"//span[@title='{displayName}']"
        is_present = self.driver.find_elements(By.XPATH, display_title)
        if len(is_present) == 1:
            checkbox_XPATH = f"//td//a//span[contains(text(),'{displayName}')]/preceding::input[@type='checkbox'][1]"
            self.driver.find_element(By.XPATH, checkbox_XPATH).click()
            more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.click("O_DELETE_COMPLETELY_XPATH")
            self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
            time.sleep(3)
        else:
            pass
        return Dashboard(self.driver)

    def delete_display_2(self):
        self.deleteCreatedDisplay(display_2)
        return Dashboard(self.driver)

    def delete_display_1(self):
        self.deleteCreatedDisplay(display_1)
        return Dashboard(self.driver)

    def clickOnHDMIOpt(self):
        time.sleep(2)
        # self.click("D_CableDMStatus_XPATH")
        self.wait_for_visible("D_CableDMStatus_XPATH")
        more_options = self.find_element("D_CableDMStatus_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return Dashboard(self.driver)

    def clickondisconnected(self):
        time.sleep(3)
        self.wait_for_visible("D_Disconnectedopt_XPATH")
        more_options = self.find_element("D_Disconnectedopt_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return Dashboard(self.driver)

    def getcountdisconnected(self):
        time.sleep(2)
        self.wait_for_visible("D_Disconnected_Count_XPATH")
        time.sleep(1)
        count = len(self.find_elements("D_Disconnected_Count_XPATH"))
        return count

    def getcountdisconnecteddashboard(self):
        time.sleep(5)
        self.wait_for_visible("D_Disconnected_dashboard_Count_XPATH")
        dashdis = self.getText("D_Disconnected_dashboard_Count_XPATH")
        dashdis1 = int(dashdis)
        return dashdis1

    ######################
    def clickOnAddMaterialBtn(self):
        self.selenium_click("O_ADD_MATERIAL_BTN_XPATH")
        time.sleep(2)
        return Dashboard(self.driver)

    def uploadMaterial_Documents(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\"car1107" "mp3_sample1107" "earth1011107" "ppt_sample1107" '
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Dashboard(self.driver)

    def uploadMaterial_MP3(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\mp3_sample1107.mp3'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Dashboard(self.driver)

    def uploadMaterial_MP4101(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\earth1011107.mp4'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Dashboard(self.driver)

    def uploadMaterial_PPT(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\"ppt_sample1107.ppt,"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Dashboard(self.driver)

    def clickOnUpload_forMP4(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        time.sleep(30)
        self.refresh()
        return Dashboard(self.driver)

    def gotoContentMaterials_DB(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        return Dashboard(self.driver)

    #### smoke nihal TC ###########

    def ReturnDisplayCount(self):
        time.sleep(3)
        return self.getText("N_DisplayCountDashboard_CSS")

    def CreateDisplay(self):
        time.sleep(1.5)
        display_name = generate_random_string(5)
        self.selenium_click("N_ContentManager_XPATH")
        time.sleep(3)
        self.selenium_click("N_ContentManagerDisplay_XPATH")
        time.sleep(3)
        self.selenium_click("N_createNewDisplayIcon_XPATH")
        self.send_keys("N_CreateNewDisplayNameField_NAME", display_name)
        self.send_keys("N_CreateNewDisplayPasswordField_CSS", "Jkrt@531")
        self.send_keys("N_CreateNewDisplayConfirmPasswordField_CSS", "Jkrt@531")
        self.scroll_to_element("N_CreateDisplayCommit_XPATH")
        self.selenium_click("N_CreateDisplayCommit_XPATH")
        time.sleep(3)
        return Dashboard(self.driver)

    def ReturnOfflineDisplayCount(self):
        return self.getText("N_OfflineDisplayCountDashboard_XPATH")

    def ReturnOnlineDisplayCount(self):
        return self.getText("N_OnlineDisplayCountDashboard_XPATH")

    def goToRaiseTicket(self):
        time.sleep(1)
        self.hoverAndSelect("O_PROFILE_ICON_XPATH","O_RAISE_TICKET_XPATH")
        return Dashboard(self.driver)

    def enterDisplayName(self):
        global r_displayName
        r_displayName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys("O_RT_DisplayName_XPATH", r_displayName)
        return Dashboard(self.driver)

    def enterDisplayID(self):
        global r_displayID
        r_displayID = ''.join(
            secrets.choice('1234567890') for _ in range(6))
        self.send_keys("O_RT_DisplayID_XPATH", r_displayID)
        return Dashboard(self.driver)

    def enterTitle(self):
        global r_title
        r_title = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys("O_RT_Title_XPATH", r_title)
        return Dashboard(self.driver)

    def enterDescription(self):
        global r_description
        r_description = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.click("O_RT_Description_XPATH")
        self.send_keys("O_RT_Description_XPATH", r_description)
        # self.find_element("O_RT_Description_XPATH").send_keys(Keys.NUMPAD1)
        return Dashboard(self.driver)

    def fillRaiseTicketInfoAndSubmit(self):
        global window_handles
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[-1])
        self.enterDisplayName()
        self.enterDisplayID()
        self.selenium_click("O_RT_ContactUsAbout_XPATH")
        self.click("O_BillingOption_XPATH")
        self.enterTitle()
        self.enterDescription()
        self.click("O_RT_SubmitBtn_XPATH")
        self.click("O_LOGOUT_OK_BTN_XPATH")
        return Dashboard(self.driver)

    def verifyTicketIsRaised(self):
        ticket_XPATH = f"//a[normalize-space()='{r_title}']"
        c = self.driver.find_elements(By.XPATH, ticket_XPATH)
        c = len(c)
        self.driver.close()
        self.driver.switch_to.window(window_handles[0])
        if c == 1:
            return True
        else:
            return False

    def verifyCard_DisplayLicence(self):
        r = len(self.find_elements("O_Card_DisplayLicence_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_Storage(self):
        r = len(self.find_elements("O_Card_Storage_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_DisplayStatus(self):
        r = len(self.find_elements("O_Card_DisplayStatus_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_CableStatus(self):
        r = len(self.find_elements("O_Card_CableStatus_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_MediaUploaded(self):
        r = len(self.find_elements("O_Card_MediaUploaded_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_Layout(self):
        r = len(self.find_elements("O_Card_Layout_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_Playlists(self):
        r = len(self.find_elements("O_Card_Playlists_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_Schedules(self):
        r = len(self.find_elements("O_Card_Schedules_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_DisplayOfflineSince(self):
        r = len(self.find_elements("O_Card_DisplayOfflineSince_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_TagWiseDisplay(self):
        r = len(self.find_elements("O_Card_TagWiseDisplay_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_StateWiseDisplay(self):
        r = len(self.find_elements("O_Card_StateWiseDisplay_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_CityWiseDisplay(self):
        r = len(self.find_elements("O_Card_CityWiseDisplay_XPATH"))
        if r == 1:
            return True
        else:
            return False

    def verifyCard_LocationWiseDisplay(self):
        r = len(self.find_elements("O_Card_LocationWiseDisplay_XPATH"))
        if r == 1:
            return True
        else:
            return False
