import os
import secrets
import time
import autoit
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage, generate_random_string, generate_unique_string, retry_action, getTextAfterRetry
from Pages.BasePage import BasePage, retry_action
from Utilities import configReader
import random
import string
import shutil


class Materials(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifyMaterialsURL(self):
        return self.get_current_url()

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("O_CURRENT_ACCOUNT_TYPE_XPATH")

    def gotoUABaseMgmt_MaterialPage(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return Materials(self.driver)

    def createBaseUser(self):
        time.sleep(2)
        self.wait_for_visible("O_AddBase_Icon_XPATH")
        self.click("O_AddBase_Icon_XPATH")
        self.wait_for_visible("O_EnterBaseUserName_XPATH")
        self.click("O_EnterBaseUserName_XPATH")
        global BaseUserName
        BaseUserName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("O_EnterBaseUserName_XPATH", BaseUserName)
        self.click("O_AddScheduleButton_XPATH")
        time.sleep(5)
        return Materials(self.driver)

    def switchToBaseUser(self):
        ele_XPATH = "//input[@role='searchbox']"
        self.wait_for_visible("O_DropdownSelectBaseUser_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        # self.click("D_DropdownselectBaseUser_XPATH")
        self.wait_for_visible("O_selectBase_XPATH")
        self.safest_click("O_selectBase_XPATH")
        # time.sleep(1)
        self.wait_for_visible("O_clickDropdownSelectBase_XPATH")
        self.safest_click("O_clickDropdownSelectBase_XPATH")
        # time.sleep(1)
        self.wait_for_visible("O_SearchSchedule_XPATH")
        self.safest_click("O_SearchSchedule_XPATH")
        # time.sleep(2)
        self.send_keys("O_SearchSchedule_XPATH", BaseUserName)
        time.sleep(1)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        self.wait_for_visible("O_AddScheduleButton_XPATH")
        self.safest_click("O_AddScheduleButton_XPATH")
        time.sleep(3)
        return Materials(self.driver)

    def switchToBaseUser_Previous(self):
        current_user = self.getCurrentAccount()
        if temp_val == 1:
            if current_user != "Base User":
                ele_XPATH = "//input[@role='searchbox']"
                self.wait_for_visible("O_DropdownSelectBaseUser_XPATH")
                time.sleep(2)
                retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                                    "@id='dropdownMenuButton1']")
                # self.click("D_DropdownselectBaseUser_XPATH")
                self.wait_for_visible("O_selectBase_XPATH")
                self.selenium_click("O_selectBase_XPATH")
                time.sleep(2)
                self.wait_for_visible("O_clickDropdownSelectBase_XPATH")
                self.selenium_click("O_clickDropdownSelectBase_XPATH")
                time.sleep(2)
                self.wait_for_visible("O_SearchSchedule_XPATH")
                self.selenium_click("O_SearchSchedule_XPATH")
                self.send_keys("O_SearchSchedule_XPATH", BASENAME)
                time.sleep(3)
                self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
                self.wait_for_visible("O_AddScheduleButton_XPATH")
                self.click("O_AddScheduleButton_XPATH")
                time.sleep(2)
            else:
                pass
        else:
            self.stayOnBaseAccount()
        return Materials(self.driver)

    def SwitchtoHeadUser(self):
        self.wait_for_visible("O_clickDropdownSelectBase_XPATH")
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        self.wait_for_visible("O_HeadAccount_XPATH")
        self.click("O_HeadAccount_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def deleteCreatedBaseUser(self):
        time.sleep(1)
        self.wait_for_visible("O_SearchBaseUser_XPATH")
        self.click("O_SearchBaseUser_XPATH")
        self.send_keys("O_SearchBaseUser_XPATH", BaseUserName)
        time.sleep(2)
        self.wait_for_visible("O_BaseUserThreeDot_XPATH")
        time.sleep(1)
        self.click("O_BaseUserThreeDot_XPATH")
        time.sleep(1)
        self.click("O_BaseUserDelete_XPATH")
        time.sleep(1)
        self.click("O_OkBtn_XPATH")
        return Materials(self.driver)

    def createBaseAccount_SwitchToBaseUser(self):
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(2)
            retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
        else:
            pass
        self.refresh()
        time.sleep(2)
        self.gotoUABaseMgmt_MaterialPage().createBaseUser().switchToBaseUser()
        return Materials(self.driver)

    def stayOnBaseAccount(self):
        current_user = self.getCurrentAccount()
        if current_user != "Base User":
            # retry_action(self.driver, By.ID, "dropdownMenuButton1")
            # time.sleep(2)
            # retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
            self.refresh()
            time.sleep(2)
            self.gotoUABaseMgmt_MaterialPage().createBaseUser().switchToBaseUser()
        else:
            pass
            time.sleep(2)
        return Materials(self.driver)

    def SwitchToHeadUser(self):
        global temp_val
        self.getCurrentBaseName()
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(2)
            retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
            temp_val = 1
        else:
            temp_val = 2
            pass
        self.refresh()
        time.sleep(2)
        return Materials(self.driver)

    def deleteCreatedBaseAccount_SwitchToHeadUser(self):
        self.SwitchtoHeadUser().gotoUABaseMgmt_MaterialPage().deleteCreatedBaseUser()
        return Materials(self.driver)

    def gotoContentMaterials_MaterialPage(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        return Materials(self.driver)

    def getDataCountOfMaterialPage(self):
        return self.getText("O_MATERIAL_PAGE_DATA_COUNT_XPATH")

    def getDataCountOfTrashPage(self):
        return self.getText("O_TRASH_PAGE_DATA_COUNT_XPATH")

    def getDataCountOfSharedPage(self):
        return self.getText("O_Shared_PAGE_DATA_COUNT_XPATH")
    def clickOnAddMaterialBtn(self):
        self.click("O_ADD_MATERIAL_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def isVisibleUploadMaterialsHeading(self):
        return self.is_visible("O_UPLOAD_MATERIALS_HEADING_XPATH")

    def isVisibleFileMaxSize(self):
        time.sleep(3)
        return self.is_visible("O_UPLOAD_MATERIALS_MaxFileSize_XPATH")

    def isVisibleMaxFiles(self):
        return self.is_visible("O_UPLOAD_MATERIALS_MaxFiles_XPATH")

    def isVisibleUploadMaterials_X_BTN(self):
        return self.is_visible("O_UPLOAD_MATERIALS_X_ICON_XPATH")

    def isVisibleUploadMaterialsSUPPORTED_FILES(self):
        return self.is_visible("O_UPLOAD_MATERIALS_SUPPORTED_FILES_XPATH")

    def uploadMaterial(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG_preview(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car_preview.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG_thumbnail(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car_thumbnail.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG_folder(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car_folder.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG_preview_X_Btn(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car_preview_X.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG_editName(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car_edit.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG51(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car51.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG52(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car52.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG53(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car53.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG54(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car54.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG55(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car55.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG56(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car56.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG57(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car57.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG58(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car58.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG59(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car59.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG60(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car60.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG61(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car61.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JPEG62(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car62.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)
    def uploadMaterial_JPEG101(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car101.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_MP4101(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\earth101.mp4'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_MP3101(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\mp3_sample101.mp3'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_PDF101(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\pdf_sample101.pdf'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_PNG(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\flag.png'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_GIF(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\flower.gif'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_JFIF(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\lake.jfif'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_MP4(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\earth.mp4'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_MOV(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\mov_sample.mov'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_WEBM(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\webm_sample.webm'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_MP3(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\mp3_sample.mp3'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_OGG(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\ogg_sample.ogg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_WAV(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\wav_sample.wav'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_PDF(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\pdf_sample.pdf'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_PPT(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\ppt_sample.ppt'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_PPTX(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\pptx_sample.pptx'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_DOCX(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\docx_sample.docx'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_99Files(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\99images\"1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" ' \
                          r'"21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40"' \
                          r'"41" "42" "43" "44" "45" "46" "47" "48" "49" "50" "51" "52" "53" "54" "55" "56" "57" "58" "59" "60"' \
                          r'"61" "62" "63" "64" "65" "66" "67" "68" "69" "70" "71" "72" "73" "74" "75" "76" "77" "78" "79" "80"' \
                          r'"81" "82" "83" "84" "85" "86" "87" "88" "89" "90" "91" "92" "93" "94" "95" "96" "97" "98" "99"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(4)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        return Materials(self.driver)

    def uploadMaterial_10Files(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\110images\"1" "2" "3" "4" "5" "6" "7" "8" "9" "10"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(4)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_100Files(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.scroll_to_element("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\110images\"1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" ' \
                          r'"21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40"' \
                          r'"41" "42" "43" "44" "45" "46" "47" "48" "49" "50" "51" "52" "53" "54" "55" "56" "57" "58" "59" "60"' \
                          r'"61" "62" "63" "64" "65" "66" "67" "68" "69" "70" "71" "72" "73" "74" "75" "76" "77" "78" "79" "80"' \
                          r'"81" "82" "83" "84" "85" "86" "87" "88" "89" "90" "91" "92" "93" "94" "95" "96" "97" "98" "99" "100"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(4)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_10Files_20(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\110images\"11" "12" "13" "14" "15" "16" "17" "18" "19" "20"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_10Files_30(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\110images\"21" "22" "23" "24" "25" "26" "27" "28" "29" "30"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_101Files(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\110images\"1" "2" "3" "4" "5" "6" "7" "8" "9" "10" "11" "12" "13" "14" "15" "16" "17" "18" "19" "20" ' \
                          r'"21" "22" "23" "24" "25" "26" "27" "28" "29" "30" "31" "32" "33" "34" "35" "36" "37" "38" "39" "40"' \
                          r'"41" "42" "43" "44" "45" "46" "47" "48" "49" "50" "51" "52" "53" "54" "55" "56" "57" "58" "59" "60"' \
                          r'"61" "62" "63" "64" "65" "66" "67" "68" "69" "70" "71" "72" "73" "74" "75" "76" "77" "78" "79" "80"' \
                          r'"81" "82" "83" "84" "85" "86" "87" "88" "89" "90" "91" "92" "93" "94" "95" "96" "97" "98" "99" "100" "101"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_1MoreFile(self):
        # actions = ActionChains(self.driver)
        # OO_UPLOAD_MATERIALS_DragAndDrop1_XPATH = self.driver.find_element(By.XPATH, "//div[@class='files-ui-dropzone-children-container']")
        # # self.clickOnAddMaterialBtn()
        # time.sleep(5)
        # self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop1_XPATH")
        # time.sleep(5)
        # self.scroll_to_element("O_UPLOAD_MATERIALS_DragAndDrop1_XPATH")
        # time.sleep(4)
        # # self.driver.find_element(By.XPATH, "//div[@class='files-ui-dropzone-children-container']").send_keys(Keys.ENTER)
        # # self.driver.find_element(By.XPATH, "//div[@class='files-ui-dropzone-children-container']").send_keys(Keys.ENTER)
        # # actions.double_click(OO_UPLOAD_MATERIALS_DragAndDrop1_XPATH).perform()
        # # # self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop1_XPATH")
        # self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop1_XPATH")
        # time.sleep(3)
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\110images\"101"'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_1_99GB_SIZE(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\1.99GB.docx'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_2GB_SIZE(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\2GB.docx'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def uploadMaterial_2_1GB_SIZE(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\2.1GB.docx'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.errorHandlerForAutoIt()
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Materials(self.driver)

    def numberOfUploadedFiles(self):
        time.sleep(2)
        ele = self.find_elements("O_UPLOAD_MATERIALS_NumberOfFiles_XPATH")
        count = len(ele)
        return count

    def clickOnUpload(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        time.sleep(15)
        return Materials(self.driver)

    def clickOnUpload_ForProgressBar(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        return Materials(self.driver)

    def clickOnUpload_forMP4(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        time.sleep(13)
        self.refresh()
        return Materials(self.driver)

    def clickOnUpload_for100files(self):
        time.sleep(2)
        self.scroll_to_element("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        time.sleep(240)
        self.refresh()
        return Materials(self.driver)

    def clickOnUpload_for10files(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        time.sleep(90)
        self.refresh()
        return Materials(self.driver)

    def clickOnUpload_for11Files(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        return Materials(self.driver)

    def getNumberOfEntries(self):
        ele = self.find_elements("O_NumberOfEntries_XPATH")
        c = len(ele)
        return c

    def select_ImageFolderType(self):
        self.click("O_folderType_XPATH")
        time.sleep(1)
        self.click("O_folderType_IMAGE_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def select_VideoFolderType(self):
        self.click("O_folderType_XPATH")
        time.sleep(1)
        self.click("O_folderType_VIDEO_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def select_AudioFolderType(self):
        self.click("O_folderType_XPATH")
        time.sleep(1)
        self.click("O_folderType_AUDIO_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def select_DOCFolderType(self):
        self.click("O_folderType_XPATH")
        time.sleep(1)
        self.click("O_folderType_DOC_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def createdContentMoveToTrash(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_ALL_CLM_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("D_delete_completely_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(5)
        self.refresh()
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def createdContentMoveToTrash_OG(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        # self.click("O_TRASHED_FOLDER_BTN_XPATH")
        # time.sleep(2)
        # self.click("O_ALL_CLM_XPATH")
        # self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        # more_options = self.find_element("O_MORE_OPTION_XPATH")
        # self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("D_delete_completely_XPATH")
        # self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        # self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        # time.sleep(2)
        return Materials(self.driver)

    def createdContentMoveToTrash_fromTrashFolder(self):
        # self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        # time.sleep(2)
        # # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # # self.click("O_MATERIAL_THREE_DOT_XPATH")
        # self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        # more_options = self.find_element("O_MORE_OPTION_XPATH")
        # self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        # self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_ALL_CLM_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("D_delete_completely_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def createdContentMoveToTrash_OSDisVisible(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        time.sleep(5)
        ele = self.find_elements("O_MOVE_TO_TRASH_HEADING_XPATH")
        ele = len(ele)
        return ele

    def MoveMaterial_OSD_isVisible(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_MATERIAL_XPATH")
        time.sleep(5)
        ele = self.find_elements("O_MOVE_MATERIAL_XPATH")
        ele = len(ele)
        return ele

    def CopyToShared_OSD_isVisible(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_CopyToShared_XPATH")
        time.sleep(5)
        ele = self.find_elements("O_SHARED_XPATH")
        ele = len(ele)
        return ele

    def createdContentMoveToTrash_OSDisVisible_CancelBtn(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MOVE_TO_TRASH_CANCEL_BTN_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        ele = self.find_elements("O_MOVE_TO_TRASH_HEADING_XPATH")
        ele = len(ele)
        return ele

    def createdContentMoveMaterial_OSD_isVisible_CancelBtn(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_MATERIAL_XPATH")
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        ele = self.find_elements("O_MOVE_TO_TRASH_HEADING_XPATH")
        ele = len(ele)
        return ele

    def createdContentCopyToShared_OSD_isVisible_CancelBtn(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_CopyToShared_XPATH")
        self.click("O_MOVE_TO_TRASH_CANCEL_BTN_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        ele = self.find_elements("O_SHARED_XPATH")
        ele = len(ele)
        return ele

    def createdContentCopyToShared_OSD_isVisible_X_Btn(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_CopyToShared_XPATH")
        self.click("D_X_Icon_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        ele = self.find_elements("O_SHARED_XPATH")
        ele = len(ele)
        return ele

    def createdContentMoveToTrash_OSDisVisible_X_Btn(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MOVE_TO_TRASH_X_BTN_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        ele = self.find_elements("O_MOVE_TO_TRASH_HEADING_XPATH")
        ele = len(ele)
        return ele

    def AllContentdeletecompletelyfromtrash(self):
        self.refresh()
        time.sleep(1)
        self.selenium_click("N_Material_trash_xpath")
        self.refresh()
        time.sleep(1)
        self.select_100_entries()
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.click("O_ALL_CLM_XPATH")
        time.sleep(5)
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        self.selenium_click("O_MORE_OPTION_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        # more_options = self.find_element("O_MORE_OPTION_XPATH")
        # self.driver.execute_script("arguments[0].click();", more_options)
        self.click("N_MATERIAL_Deletecompletely_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(30)
        self.refresh()
        return Materials(self.driver)

    def AllContentMoveToTrash(self):
        try:
            self.refresh()
            time.sleep(1)
            self.select_100_entries()
            time.sleep(4)
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.click("O_ALL_CLM_XPATH")
            time.sleep(5)
            self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
            self.selenium_click("O_MORE_OPTION_XPATH")
            self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
            # more_options = self.find_element("O_MORE_OPTION_XPATH")
            # self.driver.execute_script("arguments[0].click();", more_options)
            self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
            self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
            time.sleep(1)
            self.refresh()
            time.sleep(2)
            self.click("O_TRASHED_FOLDER_BTN_XPATH")
            time.sleep(2)
            self.click("O_ALL_CLM_XPATH")
            self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
            more_options = self.find_element("O_MORE_OPTION_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            self.click("D_delete_completely_XPATH")
            self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
            time.sleep(30)
            self.refresh()
            self.refresh()
            self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
            return Materials(self.driver)
        except:
            pass

    def changeTypeImageToVideo(self):
        self.selenium_click("O_TYPE_OF_MATERIAL_DROPDOWN_XPATH")
        time.sleep(1)
        self.selenium_click("O_TYPE_OF_MATERIAL_VIDEO_OPT_XPATH")
        time.sleep(4)
        return Materials(self.driver)

    def changeTypeImageToAudio(self):
        self.selenium_click("O_TYPE_OF_MATERIAL_DROPDOWN_XPATH")
        self.selenium_click("O_TYPE_OF_MATERIAL_AUDIO_OPT_XPATH")
        time.sleep(4)
        return Materials(self.driver)

    def changeTypeImageToDocument(self):
        self.selenium_click("O_TYPE_OF_MATERIAL_DROPDOWN_XPATH")
        self.selenium_click("O_TYPE_OF_MATERIAL_DOCUMENT_OPT_XPATH")
        time.sleep(4)
        return Materials(self.driver)

    # def verifyPopup_MaterialUploadedSuccessfully(self):
    #     self.refresh()
    #     if popup_msg_text == "Material uploaded successfully":
    #         return True
    #     else:
    #         return False

    def getTextFromSuccessPopup(self):
        print(self.driver.page_source)
        self.wait_for_visible_all_elements("O_SUCCESS_POPUP_XPATH")
        txt = self.getText("O_SUCCESS_POPUP_XPATH")
        return txt

    def verify_addNewMaterial_OSD_X_BTN(self):
        self.click("O_UPLOAD_MATERIALS_X_ICON_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_UPLOAD_MATERIALS_HEADING_XPATH")
        ele = len(ele)
        return ele

    def getTextFromWarnPopup(self):
        self.wait_for_visible_all_elements("O_WARN_POPUP_XPATHH")
        return self.getText("O_WARN_POPUP_XPATHH")

    def length_getTextFromWarnPopup(self):
        ele = self.find_elements("O_WARN_POPUP_XPATH")
        ele = len(ele)
        if ele == 1:
            ele_txt = self.getText("O_WARN_POPUP_XPATH")
        else:
            ele_txt = ""  
        return ele, ele_txt

    def clickOn_X_BTN_DESELECT_FILES(self):
        time.sleep(3)
        self.selenium_click("O_X_BTN_TO_DESELECT_FILE_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def clickOn_X_BTN_DESELECT_ALL_FILES(self):
        time.sleep(3)
        self.selenium_click("O_X_BTN_TO_DESELECT_FILE_ALL_FILES_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def clickOn_I_BTN_SELECTED_FILE(self):
        time.sleep(3)
        self.selenium_click("O_I_BTN_TO_SELECTED_FILE_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def getNameOfSelectedFile(self):
        return self.getText("O_IMAGE_NAME_DETAILS_XPATH")

    def getSizeOfSelectedFile(self):
        return self.getText("O_IMAGE_SIZE_DETAILS_XPATH")

    def getTypeOfSelectedFile(self):
        return self.getText("O_IMAGE_TYPE_DETAILS_XPATH")

    def isValid(self):
        return self.getText("O_VALID_FILE_XPATH")

    def isVisibleProgressBar(self):
        time.sleep(1)
        self.wait_for_visible_all_elements("O_PROGRESS_BAR_XPATH")
        ele = self.find_elements("O_PROGRESS_BAR_XPATH")
        ele = len(ele)
        return ele

    def verifyFileInTrashFolder(self):
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        elements = self.find_elements("O_FILE_NAMES_XPATH")
        for element in elements:
            name = element.text
            if name == "car53.jpg":
                return True
            else:
                return False

    def searchByName(self):
        time.sleep(3)
        self.refresh()
        self.wait_for_visible_all_elements("O_USER_MGT_SEARCHBAR_XPATH")
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", "car59.jpg")
        time.sleep(3)
        ele = self.find_elements("O_SEARCHED_IMAGE_NAME59_XPATH")
        ele = len(ele)
        return ele

    def searchByName_filter(self):
        self.wait_for_visible_all_elements("O_FILTER_ICON_XPATH")
        self.refresh()
        time.sleep(5)
        self.click("O_FILTER_ICON_XPATH")
        self.wait_for_visible_all_elements("O_FILTER_BY_NAME_XPATH")
        self.send_keys("O_FILTER_BY_NAME_XPATH", "car60.jpg")
        time.sleep(3)
        ele = self.find_elements("O_SEARCHED_IMAGE_NAME60_XPATH")
        ele = len(ele)
        return ele

    def clickOnCreateFolderIcon(self):
        time.sleep(3)
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        return Materials(self.driver)

    def isVisibleCreateFolder_OSD(self):
        ele = self.find_elements("O_CreateFolder_HEADING_XPATH")
        ele = len(ele)
        return ele

    def enterFolderName(self):
        global r_FolderName
        r_FolderName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", r_FolderName)
        return Materials(self.driver)

    def clickOnAddBtn(self):
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Materials(self.driver)

    def verifyFolderIsCreated(self):
        ele_XPATH = f"//span//span[@title='{r_FolderName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def deleteCreatedFolder(self):
        time.sleep(1)
        self.click("O_FOLDER_DELETE_BTN_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        return Materials(self.driver)

    def createNewFolder_SplChar(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", "!@#$%^")
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Materials(self.driver)

    def getTextFromWarningMsg(self):
        return self.getText("O_WARNING_F_MSG_XPATH")

    def verifyFolderNameInDropdown(self):
        ele_XPATH = f"//button[normalize-space()='{r_FolderName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        ele = len(ele)
        return ele

    def goToCreateFolderPage(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.click("O_DISPLAY_POPUP_CLOSE_BTN_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Materials(self.driver)

    def isVisibleCreateFolderPopup(self):
        time.sleep(2)
        ele = self.find_elements("O_CreateFolder_HEADING_XPATH")
        ele2 = self.find_elements("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH")
        c = len(ele) + len(ele2)
        return c

    def goToCreateFolderPage_X_BTN(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.click("O_PHONE_NUM_X_BTN_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Materials(self.driver)

    def goToHeadFolder(self):
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        return Materials(self.driver)

    def goToSharedFolder(self):
        self.click("O_SHARED_FOLDER_BTN_XPATH")
        return Materials(self.driver)

    def goToTrashedFolder(self):
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        return Materials(self.driver)

    def isVisibleTableHeadings(self):
        ele = self.find_elements("O_TABLE_HEADINGS_XPATH")
        ele = len(ele)
        return ele

    def verifyImage101(self):
        c = self.find_elements("O_car101_XPATH")
        c = len(c)
        return c

    def verifyVideo101(self):
        c = self.find_elements("O_earth101_XPATH")
        c = len(c)
        return c

    def verifyAudio101(self):
        c = self.find_elements("O_mp3101_XPATH")
        c = len(c)
        return c

    def verifyDoc101(self):
        c = self.find_elements("O_pdf101_XPATH")
        c = len(c)
        return c

    def selectFirstFolderFromDropdown(self):
        time.sleep(2)
        self.click("O_MATERIAL_FOLDER_DROPDOWN_XPATH")
        time.sleep(1)
        self.click("O_FolderDropdown_FirstOption_XPATH")
        return Materials(self.driver)

    def verifyFolderIsSelected(self):
        ele = self.find_elements("O_DELETE_FOLDER_BTN_XPATH")
        c = len(ele)
        return c

    def getCurrentBaseName(self):
        global BASENAME
        self.wait_for_visible_all_elements("O_CURRENT_BASE_NAME_XPATH")
        BASENAME = self.getText("O_CURRENT_BASE_NAME_XPATH")
        return BASENAME

    def verify_Preview(self):
        self.click("O_IMAGE_NAME_FOR_PREVIEW_XPATH")
        c = self.find_elements("O_IMAGE_FOR_PREVIEW_XPATH")
        c = len(c)
        return c

    def verify_thumbnail(self):
        self.click("O_IMAGE_NAME_FOR_Thumbnail_XPATH")
        c = self.find_elements("O_IMAGE_FOR_PREVIEW_XPATH")
        c = len(c)
        return c

    def verifyEditedMaterialName(self):
        self.click("O_IMAGE_NAME_FOR_EDIT_XPATH")
        existing_name = self.find_element("O_MATERIAL_EDIT_TEXTBOX_XPATH").get_attribute('value')
        self.clear("O_MATERIAL_EDIT_TEXTBOX_XPATH")
        editedName = f"edited_{existing_name}"
        self.send_keys("O_MATERIAL_EDIT_TEXTBOX_XPATH", f"{editedName}")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        c = self.driver.find_elements(By.XPATH, f"//span[@title='{editedName}']")
        c = len(c)
        return c

    def verifyNameAlreadyExistToastMsg(self):
        self.click("O_IMAGE_NAME_FOR_EDIT_XPATH")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        r = self.getText("O_WARNING_MSG_XPATH")
        if r == "Name already used":
            return True
        else:
            return False

    def verify_PreviewPage_X_Btn(self):
        self.click("O_IMAGE_NAME_FOR_PREVIEW_X_XPATH")
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        c = self.find_elements("O_MATERIAL_EDIT_TEXTBOX_XPATH")
        c = len(c)
        return c

    def verifyFolderMaterial(self):
        self.click("O_IMAGE_NAME_FOR_checkbox_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.selenium_click("O_MATERIAL_MOVE_MATERIAL_XPATH")
        time.sleep(2)
        self.selenium_click("O_MOVE_TO_MATERIAL_SEARCH_BOX_XPATH")
        self.selenium_click("D_SearchSchedule_XPATH")
        self.send_keys("D_SearchSchedule_XPATH", f"{r_FolderName}")
        self.find_element("D_SearchSchedule_XPATH").send_keys(Keys.ENTER)
        time.sleep(2)
        self.selenium_click("O_AddScheduleButton_XPATH")
        time.sleep(1)
        self.click("O_IMAGE_NAME_FOR_folder_XPATH")
        c = self.find_elements("O_IMAGE_NAME_FOR_folder__XPATH")
        c = len(c)
        return c

    def editFolderName(self):
        self.click("O_EDIT_FOLDER_NAME_XPATH")
        self.clear("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH")
        r_FolderName_og = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", r_FolderName_og)
        self.click("Add_Display_D_XPATH")
        time.sleep(2)
        ele = f"//button[normalize-space()='{r_FolderName_og}']"
        c = self.driver.find_elements(By.XPATH, ele)
        c = len(c)
        return c

    def editFolderName_CancelBtn(self):
        self.click("O_EDIT_FOLDER_NAME_XPATH")
        time.sleep(1)
        self.click("O_USER_MGT_POP_UP_CANCEL_BTN_XPATH")
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        c = self.find_elements("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH")
        c = len(c)
        return c

    def folderMoveToTrash_CloseBtn(self):
        self.click("O_FOLDER_DELETE_BTN_XPATH")
        time.sleep(1)
        self.click("O_DELETE_COMPLETELY_CANCEL_BTN_XPATH")
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        c = self.find_elements("O_MOVE_TO_TRASH_HEADING_XPATH")
        c = len(c)
        return c

    def createNewFolder(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.enterFolderName()
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def selectFirstFolderFromDropdown_SearchBar(self):
        time.sleep(2)
        sam_XPATH = "//input[@id='myInputimage']"
        self.click("O_MATERIAL_FOLDER_DROPDOWN_XPATH")
        time.sleep(3)
        ele_XPATH = f"//a[normalize-space()='{r_FolderName}']"
        self.send_keys("O_SEARCH_FOLDER_XPATH", f"{r_FolderName}")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        return Materials(self.driver)

    def verifyHeadings(self):
        c = self.find_elements("O_HEADINGS_MATERIAL_PAGE_XPATH")
        c = len(c)
        return c

    def verify_All_Option(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Materials(self.driver)

    def verify_1_Checkbox(self):
        time.sleep(2)
        self.click("O_CHECKBOX_1_XPATH")
        time.sleep(1)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(3)
        self.refresh()
        return Materials(self.driver)

    def verify_2_Checkboxes(self):
        time.sleep(2)
        self.click("O_CHECKBOX_1_XPATH")
        self.click("O_CHECKBOX_2_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(1)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Materials(self.driver)

    def restoreDeletedAllFiles(self):
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_ALL_CLM_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_RESTORE_OPTION_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def restoreDeletedFilesForSharedFolder(self):
        time.sleep(2)
        self.click("O_CHECKBOX_1_XPATH")
        self.click("O_CHECKBOX_2_XPATH")
        self.click("O_CHECKBOX_3_XPATH")
        time.sleep(1)
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_SHARED_FOLDER_CONTENT_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def clickOnTrashBtn(self):
        time.sleep(2)
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(10)
        return Materials(self.driver)

    def clickOnHEAD_OR_BASEBtn(self):
        time.sleep(2)
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def clickOnSharedFolderBtn(self):
        time.sleep(2)
        self.click("O_SHARED_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def verify_1_Checkbox_sharedFolder(self):
        time.sleep(2)
        self.click("O_CHECKBOX_1_XPATH")
        time.sleep(1)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_CopyToShared_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Materials(self.driver)

    def verify_2_Checkboxes_sharedFolder(self):
        time.sleep(2)
        self.click("O_CHECKBOX_2_XPATH")
        self.click("O_CHECKBOX_3_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(1)
        self.click("O_CopyToShared_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Materials(self.driver)

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "50")
        time.sleep(2)
        return Materials(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "100")
        time.sleep(2)
        return Materials(self.driver)

    def select_10_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "10")
        time.sleep(10)
        return Materials(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return Materials(self.driver)

    def getScheduleCount(self):
        return self.getText("O_ENTRIES_COUNT_XPATH")

    def verifyNextOption(self):
        self.driver.execute_script("arguments[0].click();", self.find_element("O_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("O_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("O_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("O_ENTRIES_COUNT_XPATH")

    def moreSchedules(self):
        self.driver.execute_script("arguments[0].click();", self.find_element("O_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("O_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("O_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("O_ENTRIES_COUNT_XPATH")

    def verifyPreviousOptionOnSchedule(self):
        time.sleep(1)
        previous_button_xpath = f"//a[@data-dt-idx='0']"
        getTextAfterRetry(self.driver, By.XPATH, previous_button_xpath)
        self.driver.execute_script("arguments[0].click();", self.find_element("O_PREVIOUS_BUTTON_XPATH"))
        time.sleep(1)
        getTextAfterRetry(self.driver, By.XPATH, previous_button_xpath)
        self.driver.execute_script("arguments[0].click();", self.find_element("O_PREVIOUS_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("O_ENTRIES_COUNT_XPATH")

    def scroll(self):
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True

    def errorHandlerForAutoIt(self):
        time.sleep(2)
        if autoit.win_active("Open"):
            try:
                autoit.control_click("Open", "Button1")
                time.sleep(1)
                autoit.win_close("Open")
            except Exception as e:
                pass
        else:
            pass

    def Uploadmedia(self):
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\123.jpg"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.jpg"
        shutil.copy(ImageOldName, imageNewName)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(11)
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Imagename
        Imagename = ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        print(Imagename)
        print(uplodedsamplename)
        if uplodedsamplename == Imagename:
            return True
        else:
            return False


    def DeleteMedia(self):
        time.sleep(5)
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        self.click("N_FirstMediaCheckBox_XPATH")
        self.click("N_MoreOption_XPATH")
        self.click("N_MoveToTrash_XPATH")
        self.click("N_OKOption_XPATH")
        time.sleep(3)
        return Materials(self.driver)

    def RestoreMedia(self):
        self.click("N_TrashedOption_XPATH")
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        self.click("N_FirstMediaCheckBox_XPATH")
        self.click("N_MoreOption_XPATH")
        self.click("N_RestoreFromTrash_XPATH")
        self.click("N_OKOption_XPATH")
        time.sleep(3)
        return Materials(self.driver)

    def DeletePermanentlyMedia(self):
        time.sleep(3)
        # self.click("N_HeadFolder_XPATH")
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        self.click("N_FirstMediaCheckBox_XPATH")
        self.click("N_MoreOption_XPATH")
        self.click("N_MoveToTrash_XPATH")
        self.click("N_OKOption_XPATH")
        time.sleep(3)
        self.click("N_TrashedOption_XPATH")
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        self.click("N_FirstMediaCheckBox_XPATH")
        self.click("N_MoreOption_XPATH")
        self.click("N_DeletePermanently_XPATH")
        self.click("N_OKOption_XPATH")
        time.sleep(3)
        return Materials(self.driver)

    def VerifyMedia(self):
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        ele = len(self.find_elements("N_EmptyTable_XPATH"))
        if ele == 1:
            return True
        else:
            return False

    def CreateFolder(self):
        global FolderRandomName
        FolderRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=6))
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/a").click()
        self.driver.find_element(By.XPATH, "//input[@name='v2_folder[name]']").send_keys(FolderRandomName)
        self.driver.find_element(By.XPATH, "//input[@name='commit']").click()
        time.sleep(3)
        full_text = self.driver.find_element(By.XPATH, "//span[@class='subfolder-name']").text
        folder_name = full_text.split('>')[-1].strip()
        if folder_name == FolderRandomName:
            return True
        else:
            return False

    def UploadMediaInsideFolder(self):
        self.selenium_click("N_FolderOptionMediaPage_XPATH")
        self.selenium_click("N_FolderOptionSearchBar_XPATH")
        self.send_keys("N_FolderOptionSearchBar_XPATH",FolderRandomName)
        self.driver.find_element(By.XPATH, f"//a[normalize-space()='{FolderRandomName}']").click()
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\123.jpg"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.jpg"
        shutil.copy(ImageOldName, imageNewName)
        time.sleep(3)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(8)
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Imagename
        Imagename = ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename:
            return True
        else:
            return False

    def MediaLogsOptions(self):
        self.send_keys("N_MediaSearchBar_XPATH", Imagename)
        time.sleep(3)
        #self.selenium_click("N_MediaPageLogsOption_XPATH")
        self.selenium_click("A_MediaPageLogsOption_XPATH")
        time.sleep(3)
        elements = [
            self.is_visible("N_MediaLogsTextInMediaLogsPage_XPATH"),
            self.is_visible("N_SearchBarInsideMediaLogsPage_XPATH"),
            self.is_visible("N_FilterIconInsideMediaLogsPage_XPATH"),
            self.is_visible("N_MediaIdandNameInsideMediaLogsPage_XPATH"),
            self.is_visible("N_TableHeaderUserInsideMediaLogsPage_XPATH"),
            self.is_visible("N_TableHeaderUserActivityInsideMediaLogsPage_XPATH"),
            self.is_visible("N_TableHeaderTimestampInsideMediaLogsPage_XPATH"),
            self.is_visible("N_UserNameInsideMedialOgsPage_XPATH"),
            self.is_visible("N_UserActivityMedialOgsPage_XPATH"),
            self.is_visible("N_timeMedialOgsPage_XPATH"),
            self.is_visible("N_EntriesInsideMediaLogsPage_XPATH"),
            self.is_visible("N_ShowingEntries_XPATH"),
            self.is_visible("N_LeftArrowInsideMediaLogsPage_XPATH"),
            self.is_visible("N_RightArrowInsideMediaLogsPage_XPATH"),
            self.is_visible("N_CloseOptionInsideMediaLogsPage_XPATH")
        ]

        return all(elements)

    def moveMedia(self):
        self.send_keys("N_MediaSearchBar_XPATH", f"{Imagename}")
        time.sleep(2)
        self.click("O_firstCHKBSK_XPATH")
        self.click("S_MORE_OPTION_MATERIAL_XPATH")
        self.click("O_MATERIAL_MOVE_MATERIAL_XPATH")
        self.selenium_click("O_searchFolderName_MoveMedia_XPATH")
        self.send_keys("D_SearchSchedule_XPATH",f"{r_FolderName}")
        folderXpath = f"//ul//li[.='{r_FolderName}']"
        self.driver.find_element(By.XPATH,folderXpath).click()
        self.click("O_USER_MGT_POP_UP_ADD_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def copyToShared(self):
        self.send_keys("N_MediaSearchBar_XPATH", f"{Imagename}")
        time.sleep(2)
        self.click("O_firstCHKBSK_XPATH")
        self.click("S_MORE_OPTION_MATERIAL_XPATH")
        self.click("O_CopyToShared_XPATH")
        self.click("D_Ok_Content_XPATH")
        time.sleep(3)
        return Materials(self.driver)

    def createPlaylistFromMedia(self):
        self.send_keys("N_MediaSearchBar_XPATH", f"{Imagename}")
        time.sleep(2)
        self.click("O_firstCHKBSK_XPATH")
        self.click("S_MORE_OPTION_MATERIAL_XPATH")
        self.click("O_createPlaylist_XPATH")
        global PlaylistNameFromMediaPage
        r = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        PlaylistNameFromMediaPage = "11Automation_" + r
        self.send_keys("O_PlaylistNameTB_XPATH", PlaylistNameFromMediaPage)
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        return Materials(self.driver)

    def verifyMoveMedia(self):
        self.refresh()
        self.send_keys("N_MediaSearchBar_XPATH", f"{Imagename}")
        time.sleep(2)
        r = len(self.driver.find_elements(By.XPATH, f"//td//a//span[@title='{r_FolderName}']"))
        if r ==1:
            return True
        else:
            return False

    def verifyCopiedMediaInSharedMedia(self):
        self.refresh()
        self.click("O_sharedFolder_XPATH")
        time.sleep(2)
        self.send_keys("N_MediaSearchBar_XPATH", f"{Imagename}")
        time.sleep(3)
        r = self.getNumberOfEntries()
        print(r)
        if r == 1:
            return True
        else:
            return False

    def createdContentMoveToTrashForCreatedMedia(self):
        self.refresh()
        self.send_keys("N_MediaSearchBar_XPATH", f"{Imagename}")
        time.sleep(2)
        self.click("O_ALL_CLM_XPATH")
        time.sleep(1)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_ALL_CLM_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("D_delete_completely_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Materials(self.driver)

    def verifyCreatePlaylist(self):
        time.sleep(2)
        r = len(self.driver.find_elements(By.XPATH, f"//input[@id='nameEdit'][@value='{PlaylistNameFromMediaPage}']"))
        if r ==1:
            return True
        else:
            return False
