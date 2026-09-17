import datetime
import os
import random
import secrets
import shutil
import string
import time

import autoit

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage
from selenium.common.exceptions import StaleElementReferenceException
from Pages.BasePage import BasePage, retry_action
from Utilities import configReader
import logging
from Utilities.LogUtil import Logger
def generate_unique_string(length):
    if length > 26:
        raise ValueError("Length exceeds the number of available characters (26)")
    unique_chars = random.sample('abcdefghijklmnopqrstuvwxyz', length)
    unique_string = ''.join(unique_chars)
    return unique_string

log = Logger(__name__, logging.INFO)
base_account = "base_" + generate_unique_string(3)
playlist1 = generate_unique_string(5)

class Content(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifyContentURL(self):
        return self.get_current_url()

    def gotoContentContents_Page(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Content(self.driver)
    #Click on playlist
    def gotoContentsContent_Ppage(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
        return Content(self.driver)


    def getCurrentAccount(self):
        time.sleep(2)
        return self.getText("O_CURRENT_ACCOUNT_TYPE_XPATH")

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
        return Content(self.driver)

    def gotoUABaseMgmt_MaterialPage(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return Content(self.driver)

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
        return Content(self.driver)

    def switchToBaseUser(self):
        time.sleep(6)
        ele_XPATH = "//input[@role='searchbox']"
        self.wait_for_visible("O_DropdownSelectBaseUser_XPATH")
        time.sleep(3)
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        # self.click("D_DropdownselectBaseUser_XPATH")
        self.wait_for_visible("O_selectBase_XPATH")
        time.sleep(2)
        self.selenium_click("O_selectBase_XPATH")
        self.wait_for_visible("O_clickDropdownSelectBase_XPATH")
        time.sleep(2)
        self.selenium_click("O_clickDropdownSelectBase_XPATH")
        self.wait_for_visible("O_SearchSchedule_XPATH")
        time.sleep(2)
        self.selenium_click("O_SearchSchedule_XPATH")
        time.sleep(2)
        self.send_keys("O_SearchSchedule_XPATH", BaseUserName)
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        self.wait_for_visible("O_AddScheduleButton_XPATH")
        self.selenium_click("O_AddScheduleButton_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def stayOnBaseAccount(self):
        current_user = self.getCurrentAccount()
        if current_user != "Base User":
            # retry_action(self.driver, By.ID, "dropdownMenuButton1")
            # time.sleep(2)
            # retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
            self.refresh()
            time.sleep(5)
            self.gotoUABaseMgmt_MaterialPage().createBaseUser().switchToBaseUser()
        else:
            pass
        return Content(self.driver)

    def verifyTooltipOfAddNewMaterialBtn(self):
        title = self.find_element("O_CONTENT_AddNewContent_BTN_XPATH").get_attribute('title')
        if title == "Add New Layout":
            return True
        else:
            return False


    def verify_AddNewMaterial_OSD(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        ele = self.find_elements("O_CONTENT_AddNewContent_HEADING_XPATH")
        ele = len(ele)
        return ele

    def enterContentName(self):
        global r_ContentName
        r_ContentName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_CONTENT_ContentNameTextbox_XPATH", r_ContentName)
        return Content(self.driver)

    def enterContentName_SpecialChar(self):
        self.send_keys("O_CONTENT_ContentNameTextbox_XPATH", "@#gddd")
        return Content(self.driver)

    def addNewContent(self):
        time.sleep(1)
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        time.sleep(1)
        self.enterContentName()
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.contentPopupRemoval()
        return Content(self.driver)

    def addNewContent_TemplateForDocument(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForDocument_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        self.click("O_CONTENT_OK_BTN_TemplateForDocument_XPATH")
        self.contentPopupRemoval()
        return Content(self.driver)

    def addNewContent_TemplateForPlayingVideo(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForVideo_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        self.contentPopupRemoval()
        return Content(self.driver)

    def addNewContent_TemplateForSplitScreen(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT1_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def addNewContent_VerifySlides(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_BLANK_XPATH")
        self.is_visible("O_CONTENT_Op1_XPATH")
        # self.is_visible("O_CONTENT_Op2_XPATH")
        self.is_visible("O_CONTENT_Op3_XPATH")
        self.is_visible("O_CONTENT_Op4_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verifyAddedContent(self):
        time.sleep(2)
        #ele_XPATH =  f"//span[@class='main_panel_menu_name' and @title='{r_ContentName}']"
        ele_XPATH = f"//span[@title='{r_ContentName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        ele = len(ele)
        return ele

    def verifyEditContentPageTitle(self):
        # ele = self.find_elements("O_CONTENT_EditContent_HEADING_XPATH")
        ele = self.find_elements("O_CONTENT_EditContent_HEADING_SIT_XPATH")
        ele = len(ele)
        # print(ele)
        return ele

    def AllContentMoveToTrash(self):
        self.refresh()
        time.sleep(1)
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_CSS")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        return Content(self.driver)

    def createdContentMoveToTrash(self):
        time.sleep(3)
        self.gotoContentContents_Page()
        self.selenium_click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_CSS")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.selenium_click("O_ALL_CLM_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("D_delete_completely_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(3)
        return Content(self.driver)

    def addNewContent_SpecialChar(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName_SpecialChar()
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        return Content(self.driver)

    def getTextFromWarnMsg(self):
        # ele = self.getText("O_WARNING_MSG_XPATH")
        ele = self.getText("O_WARNING_L_MSG_XPATH")
        return ele

    def verifyHorizontalOption(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.click("O_CONTENT_HORIZONTAL_XPATH")
        ele = self.get_selected_text_from_dropdown("O_CONTENT_DROPDOWN_HORIZONTAL_XPATH")
        return ele

    def verifyVerticalOption(self):
        self.click("O_CONTENT_VERTICAL_XPATH")
        time.sleep(1)
        ele = self.get_selected_text_from_dropdown("O_CONTENT_DROPDOWN_VERTICAL_XPATH")
        return ele

    def verifyDDOption_Horizontal(self):
        options = []
        reference = ['hdtv1080', '3840x2160', '7680x4320', '1366x768', '1280x752', 'hdtv720', '1024x768',
                     'Other resolution']
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        elements = self.find_elements("O_CONTENT_DROPDOWN_HORIZONTAL_OPTIONS_XPATH")
        for element in elements:
            option = element.get_attribute('value')
            options.append(option)
        if reference == options:
            return True
        else:
            return False

    def verifyDDOption_Vertical(self):
        options = []
        reference = ['1080x1920', '4320x7680', '2160x3840', 'hdtv720v', 'Other resolution']
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.click("O_CONTENT_VERTICAL_XPATH")
        elements = self.find_elements("O_CONTENT_DROPDOWN_VERTICAL_OPTIONS_XPATH")
        for element in elements:
            option = element.get_attribute('value')
            options.append(option)
        if reference == options:
            return True
        else:
            return False

    def verify_OtherResolution(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        time.sleep(2)
        self.select_option_by_text_from_dropdown("O_CONTENT_DROPDOWN_HORIZONTAL_XPATH", "Other resolution")
        self.click("O_CONTENT_BLANK_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_ENTER_DIS_RESOLUTION_HEADING_XPATH")
        ele = len(ele)
        self.enterContentName()
        time.sleep(1)
        self.send_keys("O_CONTENT_WidthTextbox_XPATH", "105")
        self.send_keys("O_CONTENT_HeightTextbox_XPATH", "105")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return ele

    def verifyBlankSlide(self):
        ele = self.find_elements("O_Slide1_text_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_1(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT1_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_1(self):
        ele = self.find_elements("O_Validate_Split_OPT1_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_2(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT2_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_2(self):
        ele = self.find_elements("O_Validate_Split_OPT2_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_3(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT3_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_3(self):
        ele = self.find_elements("O_Validate_Split_OPT3_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_4(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT4_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_4(self):
        ele = self.find_elements("O_Validate_Split_OPT4_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_5(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT5_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_5(self):
        ele = self.find_elements("O_Validate_Split_OPT5_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_6(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT6_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_6(self):
        ele = self.find_elements("O_Validate_Split_OPT6_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_7(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT7_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_7(self):
        ele = self.find_elements("O_Validate_Split_OPT7_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_8(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT8_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_8(self):
        ele = self.find_elements("O_Validate_Split_OPT8_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_9(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT9_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_9(self):
        ele = self.find_elements("O_Validate_Split_OPT9_XPATH")
        ele = len(ele)
        return ele

    def addNewContent_TemplateForSplitScreen_Opt_10(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_TemplateForSplitScreen_XPATH")
        self.click("O_CONTENT_SPLIT_OPT10_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def verify_Split_Opt_10(self):
        ele = self.find_elements("O_Validate_Split_OPT10_XPATH")
        ele = len(ele)
        return ele

    def verifyEditButton_SplitScreen(self):
        # self.click("O_EDIT_BUTTON_XPATH")
        self.click("O_EDIT_BUTTON_SIT_XPATH")
        ele = self.find_elements("O_EDIT_SLIDE_TEXT_XPATH")
        ele = len(ele)
        return ele

    def verifyDeleteButton_SplitScreen(self):
        self.click("O_DELETE_BUTTON_XPATH")
        self.click("O_DELETE_OK_BUTTON_XPATH")
        ele = self.find_elements("O_Validate_Split_OPT1_XPATH")
        ele = len(ele)
        return ele

    def verifyAddSlide_afterDelete(self):
        time.sleep(1)
        self.click("O_ADD_SLIDE_BUTTON_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_Validate_Split_OPT1_XPATH")
        ele = len(ele)
        return ele

    def verify_2_Slides(self):
        ele1 = self.find_elements("O_SLIDE1_XPATH")
        ele1 = len(ele1)
        ele2 = self.find_elements("O_SLIDE2_XPATH")
        ele2 = len(ele2)
        ele = ele1 + ele2
        return ele

    def verifyRedlineOnSlide1(self):
        time.sleep(1)
        ele = self.find_elements("O_RED_LINE_1_XPATH")
        ele = len(ele)
        return ele

    def verifyRedlineOnSlide2(self):
        time.sleep(1)
        ele = self.find_elements("O_RED_LINE_2_XPATH")
        ele = len(ele)
        return ele

    def clickOnSlide1(self):
        self.selenium_click("O_SLIDE1_XPATH")
        return Content(self.driver)

    def clickOnSlide2(self):
        self.selenium_click("O_SLIDE2_XPATH")
        return Content(self.driver)

    def clickOnEditButton(self):
        # self.click("O_EDIT_BUTTON_XPATH")
        self.click("O_EDIT_BUTTON_SIT_XPATH")
        return Content(self.driver)

    def verifyImageObject(self):
        self.click("O_IMAGE_OBJECT_XPATH")
        ele = self.find_elements("O_SLIDE_IMAGE_ICON_XPATH")
        ele = len(ele)
        return ele

    def verifyImageObject_X_Btn(self):
        self.click("O_IMAGE_OBJECT_XPATH")
        self.click("O_REMOVE_OBJECT_X_BTN_XPATH")
        ele = self.find_elements("O_SLIDE_IMAGE_ICON_XPATH")
        ele = len(ele)
        return ele

    def verifyTextObjectOn_AllSlides(self):
        self.clickOnSlide1()
        self.click("O_TEXT_OBJECT_XPATH")
        self.clickOnSlide2()
        self.click("O_TEXT_OBJECT_XPATH")
        ele = self.find_elements("O_SLIDE_TEXT_ICON_XPATH")
        ele = len(ele)
        return ele

    def verifyPreviewOfTextObject(self):
        self.click("O_PREVIEW_BUTTON_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_ENTER_TEXT_LABEL_XPATH")
        ele = len(ele)
        self.refresh()
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return ele

    def verifyXBtn(self):
        ele = self.find_elements("O_REMOVE_OBJECT_X_BTN_XPATH")
        ele = len(ele)
        return ele

    def verifyNumbersOfSlides(self):
        ele1 = self.find_elements("O_SLIDE_1_NUM_XPATH")
        ele1 = len(ele1)
        ele2 = self.find_elements("O_SLIDE_2_NUM_XPATH")
        ele2 = len(ele2)
        ele = ele1 + ele2
        return ele

    def verifyColumnCount(self):
        ele = self.find_elements("O_TABLE_COLUMNS_XPATH")
        ele = len(ele)
        return ele

    def verifySearchContentByName(self):
        time.sleep(1)
        self.send_keys("O_SEARCHBAR_XPATH", f"{r_ContentName}")
        time.sleep(2)
        ele = self.find_elements("O_TABLE_ROW_XPATH")
        ele = len(ele)
        return ele

    def getDataCountOfContentPage(self):
        return self.getText("O_MATERIAL_PAGE_DATA_COUNT_XPATH")

    def createdContentMoveToTrash_OG(self):
        self.gotoContentContents_Page()
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_CSS")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        return Content(self.driver)

    def createdContentMoveToTrash_CancelBtn(self):
        self.gotoContentContents_Page()
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_CSS")
        self.click("O_MOVE_TO_TRASH_CANCEL_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        return Content(self.driver)

    def deleteContentInTrash(self):
        time.sleep(2)
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
        return Content(self.driver)

    def clickOnContentName(self):
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def getValueOfCreatedContent(self):
        time.sleep(2)
        global val
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/preceding::td//input"
        val = self.driver.find_element(By.XPATH, ele_XPATH).get_attribute('value')
        return Content(self.driver)

    def clickOnPlaylistCount(self):
        time.sleep(1)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[4]//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        return Content(self.driver)

    def clickOnScheduleCount(self):
        time.sleep(1)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[4]//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        return Content(self.driver)

    def clickOnPreviewFromActions(self):
        time.sleep(2)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[3]//div//a[1]"
        # ele_XPATH = "//tbody/tr[1]/td[5]/div[1]/a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        return Content(self.driver)

    def getUrlOfScheduleWithValue(self):
        global schedule_val
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            schedule_val = f"https://digitalsignage.jio.com/v2/schedules?content_id={val}"
        elif env == "pre-prod":
            schedule_val = f"https://preprod-jiosignage.jio.com/v2/schedules?content_id={val}"
        elif env == "sit1":
            schedule_val = f"https://sit1.jiosignage.jio.com/v2/schedules?content_id={val}"
        elif env == "sit2":
            schedule_val = f"https://sit2.jiosignage.jio.com/v2/schedules?content_id={val}"
        return schedule_val

    def getUrlOfPlaylistWithValue(self):
        global playlist_val
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            playlist_val = f"https://digitalsignage.jio.com/v2/playlists?content_id={val}"
        elif env == "pre-prod":
            playlist_val = f"https://preprod-jiosignage.jio.com/v2/playlists?content_id={val}"
        elif env == "sit1":
            playlist_val = f"https://sit1.jiosignage.jio.com/v2/playlists?content_id={val}"
        elif env == "sit2":
            playlist_val = f"https://sit2.jiosignage.jio.com/v2/playlists?content_id={val}"
        return playlist_val

    def verifyPreviewTitle(self):
        time.sleep(3)
        actual_title = self.getText("O_PREVIEW_TITLE_XPATH")
        expected_title = f"Preview Layout [{r_ContentName}]"
        if actual_title == expected_title:
            return True
        else:
            return False

    def createCopiedContent(self):
        time.sleep(1)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[3]//div//a[2]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        self.clear("O_CONTENT_ContentNameTextbox_XPATH")
        global r_Copied_ContentName
        r_Copied_ContentName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_CONTENT_ContentNameTextbox_XPATH", r_Copied_ContentName)
        self.click("O_AddScheduleButton_XPATH")
        time.sleep(1)
        self.refresh()
        return Content(self.driver)

    def verifyDimensions(self):
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[5]"
        content_dimensions = self.driver.find_element(By.XPATH, ele_XPATH).text
        ele2_XPATH = f"//tr//td[2]//span[.=' {r_Copied_ContentName}']/following::td[5]"
        copied_content_dimensions = self.driver.find_element(By.XPATH, ele2_XPATH).text
        if content_dimensions == copied_content_dimensions:
            return True
        else:
            return False

    def verify_More_MoveContent(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("O_MOVE_CONTENT_XPATH")
        self.click("O_MOVE_CONTENT_SIT_XPATH")
        time.sleep(3)
        title = self.getText("O_PREVIEW_TITLE_XPATH")
        self.refresh()
        time.sleep(1)
        return title

    def verify_More_MoveToTrash(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_CSS")
        time.sleep(3)
        title = self.getText("O_MOVE_TO_TRASH_HEADING_XPATH")
        self.refresh()
        time.sleep(1)
        return title

    def verify_More_RemoveTag(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_REMOVE_THE_TAG_XPATH")
        time.sleep(4)
        title = self.getText("O_PREVIEW_TITLE_XPATH")
        self.refresh()
        time.sleep(1)
        return title

    def verify_More_AddTag(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_THE_Tag_XPATH")
        time.sleep(4)
        title = self.getText("O_PREVIEW_TITLE_XPATH")
        self.refresh()
        time.sleep(1)
        return title

    def createNewFolder(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.enterFolderName()
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        time.sleep(3)
        return Content(self.driver)

    def enterFolderName(self):
        global r_FolderName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
        r_FolderName = f"TestFolder00__{r_text}"
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", r_FolderName)
        return Content(self.driver)

    def MoveContentToFolder(self):
        self.click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("O_MOVE_CONTENT_XPATH")
        self.click("O_MOVE_CONTENT_SIT_XPATH")
        self.selenium_click("O_CONTENT_FOLDER_DD_XPATH")
        self.selenium_click("O_SearchSchedule_XPATH")
        self.send_keys("O_SearchSchedule_XPATH", f"{r_FolderName}")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(Keys.ENTER)
        time.sleep(1)
        self.click("O_AddScheduleButton_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def getTextFromPopUp(self):
        self.wait_for_visible_all_elements("O_WARN1_POPUP_XPATH")
        ele = self.getText("O_WARN1_POPUP_XPATH")
        return ele

    def verifyPopupMsg_MoveContent(self):
        popup_msg = self.getTextFromPopUp()
        if popup_msg == f"Layout moved inside {r_FolderName} successfully. ×":
            return True
        else:
            return False

    def clickOnMovedFolderName(self):
        self.refresh()
        time.sleep(1)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[2]//a"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        return Content(self.driver)

    def verifyContentInFolder(self):
        ele = self.find_elements("O_FOLDER_DELETE_BTN_XPATH")
        ele = len(ele)
        return ele

    def deleteCreatedFolder(self):
        ele = self.driver.find_elements(By.XPATH,f"//tr//td[4]//a//span[.=' {r_FolderName}']")
        c = len(ele)
        if c ==1:
            self.driver.find_element(By.XPATH,f"//tr//td[4]//a//span[.=' {r_FolderName}']").click()
        self.click("O_FOLDER_DELETE_BTN_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(4)
        self.click("O_TYPE_OF_MATERIAL_DROPDOWN_XPATH")
        self.send_keys("O_FolderDropdown_SearchBar_XPATH", f"{r_FolderName}")
        time.sleep(4)
        ele_XPATH = f"//a[normalize-space()='{r_FolderName}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        self.click("O_DELETE_COMPLETELY_FOLDER_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        return Content(self.driver)

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
        return Content(self.driver)

    def switchToBaseUser_Previous(self):
        current_user = self.getCurrentAccount()
        if temp_val == 1:
            if current_user != "Base User":
                ele_XPATH = "//input[@role='searchbox']"
                self.wait_for_visible("O_DropdownSelectBaseUser_XPATH")
                time.sleep(7)
                retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                                    "@id='dropdownMenuButton1']")
                # self.click("D_DropdownselectBaseUser_XPATH")
                self.wait_for_visible("O_selectBase_XPATH")
                self.click("O_selectBase_XPATH")
                self.wait_for_visible("O_clickDropdownSelectBase_XPATH")
                self.selenium_click("O_clickDropdownSelectBase_XPATH")
                self.wait_for_visible("O_SearchSchedule_XPATH")
                self.selenium_click("O_SearchSchedule_XPATH")
                self.send_keys("O_SearchSchedule_XPATH", BASENAME)
                time.sleep(3)
                self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
                self.wait_for_visible("O_AddScheduleButton_XPATH")
                self.click("O_AddScheduleButton_XPATH")
                time.sleep(6)
            else:
                pass
        else:
            self.stayOnBaseAccount()
        return Content(self.driver)

    def getCurrentBaseName(self):
        global BASENAME
        self.wait_for_visible_all_elements("O_CURRENT_BASE_NAME_XPATH")
        BASENAME = self.getText("O_CURRENT_BASE_NAME_XPATH")
        return BASENAME

    def createdContentCopyToShared_OSD_isVisible_CancelBtn(self):
        self.click("O_MATERIAL_FIRST_CHECKBOX_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
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

    def createdContentCopyToShared(self):
        time.sleep(4)
        self.click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_CopyToShared_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(3)
        return Content(self.driver)

    def clickOnSharedFolder(self):
        time.sleep(6)
        self.click("O_SHARED_FOLDER_XPATH")
        time.sleep(5)
        return Content(self.driver)

    def clickOnHeadOrBaseFolder(self):
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        return Content(self.driver)

    def deleteFromSharedFolder(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_MORE_OPT_SHARED_PAGE_XPATH")
        more_options = self.find_element("O_MORE_OPT_SHARED_PAGE_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_SHARED_FOLDER_CONTENT_XPATH")
        self.click("O_OkBtn_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def deleteFromSharedFolder_single(self):
        #self.click("O_SHARED_FOLDER_XPATH")
        self.click("O_CHK_BOX_1_XPATH")
        time.sleep(4)
        self.wait_for_visible_all_elements("O_MORE_OPT_SHARED_PAGE_XPATH")
        more_options = self.find_element("O_MORE_OPT_SHARED_PAGE_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_SHARED_FOLDER_CONTENT_XPATH")
        self.click("O_OkBtn_XPATH")
        time.sleep(5)
        return Content(self.driver)

    def verify_more_AddTag_RadioBtn(self):
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_THE_Tag_XPATH")
        time.sleep(4)
        ele1 = self.find_elements("O_ADD_NEW_TAG_RADIO_BTN_XPATH")
        ele1 = len(ele1)
        # print("length is", ele1)
        ele2 = self.find_elements("O_SELECT_EXISTING_TAG_XPATH")
        ele2 = len(ele2)
        # print("length is", ele2)
        ele = ele1 + ele2
        # print("total is", ele)
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        return ele

    def verify_AddNewTag_popup(self):
        self.selenium_click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.selenium_click("O_ADD_THE_Tag_XPATH")
        time.sleep(2)
        self.selenium_click("O_ADD_NEW_TAG_RADIO_BTN_XPATH")
        global r_TagName
        r_text = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890') for _ in range(4))
        r_TagName = f"TestTag_{r_text}"
        self.send_keys("O_ADD_NEW_TAG_TEXTBOX_XPATH", f"{r_TagName}")
        self.click("O_AddScheduleButton_XPATH")
        ele = self.getTextFromPopUp()
        print("text is -------", ele)
        if ele == "Tag Added successfully ×":
            return True
        else:
            return False

    def verify_AddExistingTag_popup(self):
        self.click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_THE_Tag_XPATH")
        time.sleep(2)
        self.click("O_SELECT_EXISTING_TAG_XPATH")
        self.click("O_EXISTING_TAG_TEXTBOX_XPATH")
        time.sleep(2)
        self.selenium_click("O_SELECT_FIRST_TAG_XPATH")
        time.sleep(2)
        self.click("O_POPUP_BODY_XPATH")
        self.click("O_EXISTING_TAG_TEXTBOX_XPATH")
        self.click("O_AddScheduleButton_XPATH")
        ele = self.getTextFromPopUp()
        print("text is -------", ele)
        if ele == "Tag Added successfully ×":
            return True
        else:
            return False

    def verify_AddNewTag_WarnMsg(self):
        self.click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_THE_Tag_XPATH")
        time.sleep(2)
        self.send_keys("O_ADD_NEW_TAG_TEXTBOX_XPATH", "@@@@")
        self.click("O_AddScheduleButton_XPATH")
        time.sleep(2)
        # ele = self.find_elements("O_TAG_WARN_MSG_XPATH")
        ele = self.find_elements("O_TAG_WARN_MSG_SIT_XPATH")
        # print("Warn msg is:", ele)
        ele = len(ele)
        return ele

    def clickOnTagBtn(self):
        time.sleep(1)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[9]//a"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        return Content(self.driver)

    def verifyAddedTag(self):
        time.sleep(2)
        ele = self.getText("O_ADDED_TAG_NAME_XPATH")
        if ele == r_TagName:
            return True
        else:
            return False


    def getTextTagBtn(self):
        time.sleep(1)
        ele_XPATH = f"//tr//td[2]//span[.=' {r_ContentName}']/following::td[9]//a"
        ele = self.driver.find_element(By.XPATH, ele_XPATH).text
        return ele

    def verify_RemoveTag_popup(self):
        self.click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_REMOVE_THE_TAG_XPATH")
        time.sleep(3)
        self.selenium_click("O_EXISTING_TAG_TEXTBOX_XPATH")
        self.selenium_click("O_SELECT_FIRST_TAG_XPATH")
        self.selenium_click("O_EDITNAME_POPUP_HEADING_XPATH")
        time.sleep(1)
        self.click("O_AddScheduleButton_XPATH")
        ele = self.getTextFromPopUp()
        if ele == "Tag Removed successfully ×":
            return True
        else:
            return False

    def verify_RemoveTag_popup_2Tag(self):
        self.selenium_click("O_CHK_BOX_1_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.selenium_click("O_REMOVE_THE_TAG_XPATH")
        time.sleep(2)
        self.selenium_click("O_EXISTING_TAG_TEXTBOX_XPATH")
        self.selenium_click("O_SELECT_FIRST_TAG_XPATH")
        self.selenium_click("O_SELECT_SECOND_TAG_XPATH")
        time.sleep(1)
        self.selenium_click("O_EDITNAME_POPUP_HEADING_XPATH")
        self.selenium_click("O_AddScheduleButton_XPATH")
        ele = self.getTextFromPopUp()
        if ele == "Tag Removed successfully ×":
            return True
        else:
            return False

    def createNewFolder_SplChar(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", "!@#$%^")
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Content(self.driver)

    def getTextFromWarningMsg(self):
        return self.getText("O_WARNING_F_MSG_XPATH")

    def verifyFolderIsCreated(self):
        #ele_XPATH = f"//button[.=' {r_FolderName} ']"
        ele_XPATH = f"//span//span[@title='{r_FolderName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def addNewContent_folder(self):
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName()
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        # self.click("O_EDIT_CONTENT_CLOSE_BTN_XPATH")
        time.sleep(1)
        # self.contentOkBtn()
        return Content(self.driver)

    def verifyAddedContentInTable(self):
        time.sleep(1)
        ele_XPATH = f"//span[@title='{r_ContentName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        ele = len(ele)
        return ele

    def ClickOnTrashFolder(self):
        time.sleep(3)
        self.selenium_click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def restoreDeletedAllFiles(self):
        time.sleep(2)
        self.click("O_TRASHED_FOLDER_BTN_XPATH")
        time.sleep(2)
        self.click("O_ALL_CLM_XPATH")
        self.wait_for_visible_all_elements("O_CONTENT_MORE_OPTION_XPATH")
        more_options = self.find_element("O_CONTENT_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_RESTORE_OPTION_XPATH")
        self.click("O_MATERIAL_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def clickOnAddedContentNameInTable(self):
        time.sleep(1)
        ele_XPATH = f"//span[@title='{r_ContentName}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.contentPopupRemoval()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        # self.contentPopupRemoval()
        return Content(self.driver)

    def clickOnAddedContentNameInTable__(self):
        time.sleep(1)
        ele_XPATH = f"//span[@title='{r_ContentName}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        # time.sleep(3)
        # self.click("O_CONTENT_OK_BTN_XPATH")
        return Content(self.driver)

    def editContent(self):
        self.click("O_EDIT_CONTENT_SAVE_BTN_SIT_Create_XPATH")
        time.sleep(1)
        durationbox = self.find_element("O_SLIDE_DURATION_TB_XPATH")
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.find_element("O_SLIDE_DURATION_TB_XPATH").send_keys(Keys.BACKSPACE)
        self.send_keys("O_SLIDE_DURATION_TB_XPATH", "20.0")
        self.selenium_click("O_SLIDE_DURATION_TB_XPATH")
        time.sleep(1)
        self.selenium_click("O_EDIT_SAVE_Button_XPATH")
        self.click("O_EDIT_SAVE_Button_XPATH")
        time.sleep(3)
        ele = self.find_elements("O_TWO_SLIDES_DURATION_XPATH")
        ele = len(ele)
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        return ele

    def uploadMaterial_JPEG(self):
        self.clickOnAddMaterialBtn()
        self.wait_for_visible_all_elements("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        self.selenium_click("O_UPLOAD_MATERIALS_DragAndDrop_XPATH")
        time.sleep(3)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\car_folder_content.jpg'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(3)
        # self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(1)
        # self.refresh()
        return Content(self.driver)

    def clickOnAddMaterialBtn(self):
        self.click("O_ADD_MATERIAL_BTN_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def gotoContentMaterials_MaterialPage(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        return Content(self.driver)

    def clickOnUpload_forMP4(self):
        time.sleep(2)
        self.click("O_UPLOAD_MATERIALS_UPLOAD_BTN_XPATH")
        time.sleep(13)
        self.refresh()
        return Content(self.driver)

    def clickOnSharedFolderBtn(self):
        time.sleep(2)
        # self.click("O_SHARED_FOLDER_BTN_XPATH")
        self.click("O_SHARED_FOLDER_BTN_SIT_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def addMaterialToSharedFolder(self):
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
        return Content(self.driver)

    def verifySharedFolderOnEditContentPage(self):
        #//button[@class='shared_button checked']
        time.sleep(2)
        self.click("O_CONTENT_SHARED_FOLDER_BTN_XPATH")
        time.sleep(3)
        image = self.find_element("O_CONTENT_IMAGE_PLUS_SIGN_XPATH")
        self.driver.execute_script("arguments[0].click();", image)
        time.sleep(2)
        ele = self.find_elements("O_CAR_FOLDER_TEXT_XPATH")
        ele = len(ele)
        return ele

    def createdMaterialDeleteCompletely(self):
        self.gotoContentMaterials_MaterialPage()
        self.select_ImageFolderType()
        time.sleep(1)
        self.click("O_ALL_CLM_XPATH")
        time.sleep(2)
        # retry_action(self.driver, By.CLASS_NAME, "btn btn-action btn-action-button ")
        # self.click("O_MATERIAL_THREE_DOT_XPATH")
        self.wait_for_visible_all_elements("O_MORE_OPTION_XPATH")
        more_options = self.find_element("O_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MATERIAL_MOVE_TO_TRASH_CSS")
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
        self.click("O_HEAD_OR_BASE_FOLDER_BTN_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def verifyPreviewFromEditContentPage(self):
        self.click("O_PREVIEW_BUTTON_XPATH")
        time.sleep(1)
        actual_title = self.getText("O_EDIT_CONTENT_PAGE_PREVIEW_TITLE_XPATH")
        expected_title = f"Preview [{r_ContentName}]"
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")

        if actual_title == expected_title:
            return True
        else:
            return False

    def verifyDisabledSaveBtn(self):
        ele = self.find_elements("O_DISABLE_SAVE_BTN_XPATH")
        return len(ele)

    def verifyContentNameInTable(self):
        time.sleep(1)
        ele_XPATH = f"//span[@title='{r_ContentName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        ele = len(ele)
        return ele

    def editContent_verifyDisabledAddSlideBtn(self):
        for x in range(1, 21):
            self.scroll_to_element("O_ADD_SLIDE_BTN_XPATH")
            time.sleep(1)
            self.click("O_ADD_SLIDE_BTN_XPATH")
        ele = self.find_elements("O_DISABLE_ADD_SLIDE_BTN_XPATH")
        ele = len(ele)
        return ele


    def editContent_verifyDisabledCopyBtn(self):
        for x in range(1, 2):
            self.scroll_to_element("O_COPY_SLIDE_BTN_XPATH")
            time.sleep(2)
            self.click("O_COPY_SLIDE_BTN_XPATH")
        for x in range(1, 20):
            self.scroll_to_element("O_ADD_SLIDE_BTN_XPATH")
            time.sleep(1)
            self.click("O_ADD_SLIDE_BTN_XPATH")
        ele = self.find_elements("O_DISABLE_COPY_BTN_XPATH")
        ele = len(ele)
        return ele

    def verify20SlidesDuration(self):
        self.scroll_to_element("O_TWENTY_SLIDES_DURATION_XPATH")
        ele = self.find_elements("O_TWENTY_SLIDES_DURATION_XPATH")
        ele = len(ele)
        return ele

    def editContent_verifyPlaytime_20Slides(self):
        for x in range(1, 21):
            self.scroll_to_element("O_ADD_SLIDE_BTN_XPATH")
            time.sleep(1)
            self.click("O_ADD_SLIDE_BTN_XPATH")
        self.scroll_to_element("O_TWENTY_SLIDES_DURATION_XPATH")
        ele = self.find_elements("O_TWENTY_SLIDES_DURATION_XPATH")
        ele = len(ele)
        return ele

    def editContent_verifyPlaytime_1Slide(self):
        self.scroll_to_element("O_One_SLIDES_DURATION_XPATH")
        ele = self.find_elements("O_One_SLIDES_DURATION_XPATH")
        ele = len(ele)
        return ele
    ##Manually NOTPossible
    def verifyDeleteButton_BlankSheet(self):
        self.click("O_ADD_SLIDE_BTN_XPATH")
        self.click("O_DELETE_TWO_SLIDES_BUTTON_XPATH")
        self.click("O_DELETE_TWO_SLIDES_OK_BUTTON_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_DELETE_TWO_SLIDES_BUTTON_XPATH")
        self.click("O_EDIT_CONTENT_SAVE_BTN_XPATH")
        ele = len(ele)
        return ele

    def verifyEditBtnFromEditContentOSD(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_MAIN_PROPERTY_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyPreview_Save_Back_Close_Btn(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        ele1 = self.find_elements("O_PREVIEW_BUTTON_XPATH")
        ele1 = len(ele1)
        ele2 = self.find_elements("O_EDIT_CONTENT_SAVE_BTN_XPATH")
        ele2 = len(ele2)
        ele3 = self.find_elements("O_BACK_SLIDE_BTN_XPATH")
        ele3 = len(ele3)
        ele4 = self.find_elements("O_EDIT_CONTENT_CLOSE_BTN_XPATH")
        ele4 = len(ele4)
        ele = ele1+ele2+ele3+ele4
        return ele

    def verifyBackBtnFromEditContentOSD_WithoutChanges(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_BACK_SLIDE_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_OK_BTN_AFTER_BACK_BTN_XPATH")
        # self.contentPopupRemoval()
        ele = self.find_elements("O_MAIN_PROPERTY_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyBackBtnFromEditContentOSD_WithChanges(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_PLAY_TIME_INCREASE_BTN_XPATH")
        self.click("O_BACK_SLIDE_BTN_XPATH")
        self.contentPopupRemoval()
        # self.click("O_OK_BTN_AFTER_BACK_BTN_AfterChanges_XPATH")
        # self.contentPopupRemoval()
        ele = self.find_elements("O_One_SLIDES_DURATION_XPATH")
        ele = len(ele)
        return ele

    def verifySaveBtnFromEditContentOSD_WithChanges(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.selenium_click("O_PLAY_TIME_INCREASE_BTN_XPATH")
        self.selenium_click("O_EDIT_CONTENT_SAVE_BTN_XPATH")
        ele = self.find_elements("O_One_SLIDES_11Sec_DURATION_XPATH")
        ele = len(ele)
        return ele

    def select_ImageFolderType(self):
        self.click("O_folderType_XPATH")
        time.sleep(1)
        self.click("O_folderType_IMAGE_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def verifyPreviewFromEditSlidePage(self):
        self.click("O_PREVIEW_BUTTON_XPATH")
        time.sleep(2)
        action = ActionChains(self.driver)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(2)
        action.send_keys(Keys.ARROW_UP).perform()
        time.sleep(2)
        actual_title = self.getText("O_EDIT_CONTENT_PAGE_PREVIEW_TITLE_XPATH")
        # print(actual_title)
        expected_title = f"Preview [{r_ContentName}]"
        # print(expected_title)
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        if actual_title == expected_title:
            return True
        else:
            return False
        # self.gotocontentlink()
        # self.click("O_CancelPreviewIcon_SIT_XPATH")

    def verifyNumberOfObjects(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_OBJECTS_COUNT_XPATH")
        ele = len(ele)
        return ele

    def verifyTooltipOfObjects(self):
        global tooltip
        elements = self.find_elements("O_OBJECTS_COUNT_XPATH")
        for element in elements:
            title = element.get_attribute('title')
            isTitleAvailable = len(title)
            if isTitleAvailable == 0:
                tooltip = 0
                break
            else:
                tooltip = 1
        return tooltip

    def verifyObject_AddText(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_TEXT_OBJECT_XPATH")
        ele = self.find_elements("O_TEXT_OBJECT_ON_EDIT_CONTENT_OSD_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddImage(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_IMAGE_OBJECT_XPATH")
        ele = self.find_elements("O_IMAGE_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddVideo(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_VIDEO_OBJECT_XPATH")
        ele = self.find_elements("O_VIDEO_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddOnscreenText(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_OnscreenText_OBJECT_XPATH")
        ele = self.find_elements("O_OnscreenText_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddRssFeed(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_RssFeed_OBJECT_XPATH")
        ele = self.find_elements("O_RssFeed_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddShape(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_Shape_OBJECT_XPATH")
        ele = self.find_elements("O_Shape_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddJioSaavan(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_JioSaavan_OBJECT_XPATH")
        ele = self.find_elements("O_JioSaavan_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddInstagram(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_Instagram_OBJECT_XPATH")
        ele = self.find_elements("O_Instagram_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele


    def verifyObject_AddGoogle(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_Google_OBJECT_XPATH")
        ele = self.find_elements("O_Google_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddYoutube(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_Youtube_OBJECT_XPATH")
        ele = self.find_elements("O_Youtube_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedImage(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_TEXT_OBJECT_ON_EDIT_CONTENT_OSD_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedYoutube(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_Youtube_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedVideo(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_VIDEO_OBJECT_ON_EDIT_CONTENT_OSD_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedGoogle(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_Google_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedShape(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_Shape_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedJioSaavan(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_JioSaavan_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyDelete_AddedInstagram(self):
        self.click("O_DELETE_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_Instagram_TEXT_TITLE_XPATH")
        ele = len(ele)
        return ele

    def verifyCopy_AddedText(self):
        self.click("O_COPY_ADDED_OBJECT_BTN_XPATH")
        ele = self.find_elements("O_TEXT_OBJECT_ON_EDIT_CONTENT_OSD_XPATH")
        ele = len(ele)
        return ele

    def verifyCloseBtnFromEditContentOSD_WithoutChanges(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(2)
        self.selenium_click("O_EDIT_CONTENT_CLOSE_BTN_XPATH")
        time.sleep(1)
        self.contentOkBtn_AfterCloseBtnFromEditSlide()
        time.sleep(2)
        ele = self.find_elements("O_ADD_MATERIAL_BTN_XPATH")
        ele = len(ele)
        return ele

    def verifyCloseBtnFromEditContentOSD_WithChanges(self):
        self.clickOnContentName()
        # self.click("O_CONTENT_OK_BTN_XPATH")
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(2)
        self.selenium_click("O_PLAY_TIME_INCREASE_BTN_XPATH")
        self.click("O_EDIT_CONTENT_CLOSE_BTN_XPATH")
        time.sleep(2)
        self.contentOkBtn_AfterCloseBtnFromEditSlide()
        time.sleep(3)
        ele = self.find_elements("O_ADD_MATERIAL_BTN_XPATH")
        ele = len(ele)
        return ele

    def verifyObject_AddImage__(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_IMAGE_OBJECT_XPATH")
        ele = self.find_elements("O_TEXT_OBJECT_ON_EDIT_CONTENT_OSD_XPATH")
        ele = len(ele)
        return ele

    def verifyEditInfoWhile_AddVideo(self):
        self.click("O_CHECKBOX_FitToScreen_XPATH")
        ele = self.find_elements("O_Verify_Checked_CHECKBOX_FitToScreen_XPATH")
        ele = len(ele)
        return ele

    def verifyEditInfoWhile_AddOnscreenText(self):
        self.click("O_CHECKBOX_UseDisplayName_XPATH")
        ele = self.find_elements("O_Verify_Checked_CHECKBOX_UseDisplayName_XPATH")
        ele = len(ele)
        return ele

    def verifyEditInfoWhile_AddRssFeed(self):
        self.click("O_CHECKBOX_CustomFeed_XPATH")
        ele = self.find_elements("O_Verify_Checked_CHECKBOX_CustomFeed_XPATH")
        ele = len(ele)
        return ele

    def verifyEditInfoWhile_AddShape(self):
        self.scroll_to_element("O_aspectRatio_XPATH")
        self.send_keys("O_SHAPE_OBJECT_EDIT_XPATH", "10")
        ele = self.find_element("O_SHAPE_OBJECT_EDIT_XPATH").get_attribute('value')
        return ele

    def verify_IncreaseDuration(self):
        self.selenium_click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.selenium_click("O_PLAY_TIME_INCREASE_BTN_XPATH")
        sam = self.find_elements("O_SAVE_BUTTON_ENABLED_XPATH")
        sam = len(sam)
        if sam == 1:
            self.selenium_click("O_EDIT_CONTENT_SAVE_BTN_XPATH")
            ele = self.find_elements("O_One_SLIDES_11Sec_DURATION_XPATH")
            ele = len(ele)
            return ele
        else:
            return 0

    def verify_DecreaseDuration(self):
        time.sleep(2)
        self.selenium_click("O_PLAY_TIME_DECREASE_BTN_XPATH")
        sam = self.find_elements("O_SAVE_BUTTON_ENABLED_XPATH")
        sam = len(sam)
        if sam == 1:
            self.selenium_click("O_EDIT_CONTENT_SAVE_BTN_XPATH")
            ele = self.find_elements("O_One_SLIDES_DURATION_XPATH")
            ele = len(ele)
            return ele
        else:
            return 0

    def verify_TransitionEffectSlide1(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_TransitionEffect_textbox_disabled_XPATH")
        ele = len(ele)
        return ele

    def verify_TransitionEffectSlide2(self):
        self.click("O_SLIDE2_EDIT_BTN_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_TransitionEffect_textbox_disabled_XPATH")
        ele = len(ele)
        if ele == 0:
            element = self.find_elements("O_VALIDATE_None_XPATH")
            element = len(element)
            return element
        else:
            return 0

    def clickOnAddSlide(self):
        self.click("O_ADD_SLIDE_BTN_XPATH")
        return Content(self.driver)

    def goToEditContentPage(self):
        self.gotoContentContents_Page()
        self.clickOnContentName()
        self.clickOnAddSlide()
        # self.click("O_AFTER_SAVE_OK_BTN_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def verifyBgColour(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        self.click("O_BACKGROUND_OPTION_XPATH")
        self.click("O_CHECKBOX_BackgroundColor_XPATH")
        self.click("O_BG_COLOUR_BOX_XPATH")
        self.click("O_SELECT_RED_COLOUR_XPATH")
        self.click("O_OK_BTN_AFTER_COLOUR_SELECTION_XPATH")
        time.sleep(3)
        element = self.driver.find_element(By.XPATH, "//div[@id='page1page']")
        bg_color = element.value_of_css_property("background-color")
        if bg_color in ["rgb(255, 0, 0)", "rgba(255, 0, 0, 1)"]:
            return True 
        else:
            return False
        

    def verifyDeselectBgColour(self):
        self.click("O_BACKGROUND_OPTION_XPATH")
        self.click("O_CHECKBOX_BackgroundColor_XPATH")
        element = self.driver.find_element(By.XPATH, "//div[@id='page1page']")
        bg_color = element.value_of_css_property("background-color")
        if bg_color in ["rgb(255, 255, 255)", "rgba(255, 255, 255, 1)"]:
            return True 
        else:
            return False

    def verifyObject_AddText_Custom(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_TEXT_OBJECT_XPATH")
        self.clear("O_ENTER_TEXT_TEXTBOX_XPATH")
        self.send_keys("O_ENTER_TEXT_TEXTBOX_XPATH", "~!@#$%^&*()_+`1234567890-=qwertyuiop[]\{}|QWERTYUIOPASDFGHJKL:asdfghjkl;'zxcvbnm,./ZXCVBNM<>?")
        time.sleep(3)
        ele = self.getText("O_TEXT_OBJECT_ON_EDIT_CONTENT_OSD_XPATH")
        print(ele)
        return ele

    def verifyPreviewFromEditSlidePage_Custom(self):
        self.click("O_PREVIEW_BUTTON_XPATH")
        time.sleep(1)
        actual_title = self.getText("O_EDIT_CONTENT_PAGE_PREVIEW_TITLE_XPATH")
        expected_title = f"Preview [{r_ContentName}]"
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        if actual_title == expected_title:
            return True
        else:
            return False




    def gotoReportsPlaylogs_omkar(self):
        self.hoverAndSelect("MENU_REPORTS_XPATH", "SUBMENU_PLAYLOGS_XPATH")
        self.click("O_GENERATE_REPORT_XPATH")
        self.click("O_CONTENT_XPATH")
        time.sleep(10)
        return Content(self.driver)


    def contentPopupRemoval(self):
        time.sleep(6)
        self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        # element = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, "//span[.='Message']//following-sibling::span//span")))
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return Content(self.driver)

    def contentOkBtn(self):
        # time.sleep(2)
        # self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        contentApprovalMsgBox = self.find_elements("O_DELETE_OK_BUTTON_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_DELETE_OK_BUTTON_XPATH")
        else:
            pass
        return Content(self.driver)

    def contentOkBtn_AfterCloseBtnFromEditSlide(self):
        # time.sleep(2)
        # self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        # contentApprovalMsgBox = self.find_elements("O_Ok_BTN_AfterCloseBtn_XPATH")
        contentApprovalMsgBox = self.find_elements("O_Ok_BTN_AfterCloseBtn_SIT_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_Ok_BTN_AfterCloseBtn_SIT_XPATH")
        else:
            pass
        return Content(self.driver)
###Sanity


    def verifyCopyBtnFromEditContentOSD(self):
        self.click("O_COPY_SLIDE_BTN_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_SLIDES_COUNT_XPATH")
        ele = len(ele)
        return ele

    def readprofileusername(self):
        time.sleep(2)
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_VIEW_PROFILE_XPATH")
        time.sleep(2)
        edit = self.find_element("O_EDIT_UNAME_BTN_XPATH")
        self.driver.execute_script("arguments[0].click();", edit)
        self.wait_for_visible("O_USER_NAME_TEXTBOX_XPATH")
        global existusern
        existusern = self.find_element("O_USER_NAME_TEXTBOX_XPATH").get_attribute('value')
        return Content(self.driver)

    def clikonaddContent(self):
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.wait_for_visible("D_Plus_Add_Content_XPATH")
        self.click("D_Plus_Add_Content_XPATH")
        return Content(self.driver)

    def EnterContentname(self):
        self.wait_for_visible("D_Contentname_CSS")
        self.click("D_Contentname_CSS")
        global content_name
        content_name = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("D_Contentname_CSS", content_name)
        self.click("D_Blank_XPATH")
        time.sleep(2)
        self.scroll_to_element("D_Add_Content_Submit_XPATH")
        self.click("D_Add_Content_Submit_XPATH")
        return Content(self.driver)

    def cancelcontentmessage(self):
        self.wait_for_visible("D_Cancel_Content_Message_new_XPATH")
        self.click("D_Cancel_Content_Message_new_XPATH")
        self.wait_for_visible("D_Ok_Button_XPATH")
        self.click("D_Ok_Button_XPATH")
        return Content(self.driver)

    def setDateContent(self):
        self.wait_for_visible("D_StartDate_ID")
        self.scroll_to_element("D_StartDate_ID")
        self.send_keys("D_StartDate_ID", "07-04-2024")
        self.scroll_to_element("D_EndDate_ID")
        self.send_keys("D_EndDate_ID", "08-04-2028")
        return Content(self.driver)

    def clickonRequestApproval(self):
        time.sleep(2)
        self.scroll_to_element("D_requestApproval_CSS")
        self.click("D_requestApproval_CSS")
        return Content(self.driver)

    def clickonSend(self):
        time.sleep(2)
        self.scroll_to_element("D_Sendkey_XPATH")
        # self.click("D_Sendkey_XPATH")
        self.wait_for_visible("D_Sendkey_new_XPATH")
        self.click("D_Sendkey_new_XPATH")
        # ele = self.find_element("D_Sendkey_XPATH")
        # self.driver.execute_script("arguments[0].click();", ele)
        return Content(self.driver)

    def verifyApprovaltext(self):
        self.wait_for_visible("D_approvaltext_XPATH")
        a = self.getText("D_approvaltext_XPATH")
        print(a)
        # self.click("D_Cancelpopup_XPATH")
        time.sleep(2)
        self.wait_for_visible("D_Cancel_Content_Message_new_XPATH")
        ele = self.find_element("D_Cancel_Content_Message_new_XPATH")
        self.driver.execute_script("arguments[0].click();", ele)
        # retry_action(self.driver, By.XPATH, "//div[@id='dijit_Dialog_16']//span[2]//span[@title='Cancel']")
        return a

    def selectuserforapproval(self):
        time.sleep(3)
        self.wait_for_visible("D_Usernamebox_CA_XPATH")
        self.click("D_Usernamebox_CA_XPATH")
        self.send_keys("D_Usernamebox_CA_XPATH", existusern)
        # self.driver.find_element(By.XPATH,"//input[@id='user_list']").send_keys(Keys.ENTER)
        return Content(self.driver)

    def goToContentPage_byURL(self):
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")

        return Content(self.driver)

    def verifyWarnDatetext(self):
        self.wait_for_visible("O_SELECT_DATE_WARN_MSG_XPATH")
        a = self.getText("O_SELECT_DATE_WARN_MSG_XPATH")
        print(a)
        # self.click("D_Cancelpopup_XPATH")
        time.sleep(2)
        self.wait_for_visible("O_Cancel_Content_Message_new_XPATH")
        ele = self.find_element("O_Cancel_Content_Message_new_XPATH")
        self.driver.execute_script("arguments[0].click();", ele)
        # retry_action(self.driver, By.XPATH, "//div[@id='dijit_Dialog_16']//span[2]//span[@title='Cancel']")
        return a

    def clickclosepreviewicon(self):
        action = ActionChains(self.driver)
        # action.sendKeys(Keys.PAGE_DOWN).sendKeys(Keys.PAGE_DOWN).build().perform()
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        action.send_keys(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        action.send_keys(Keys.ARROW_UP).perform()
        self.click("O_X_ICON_PREVIEW_XPATH")
        return Content(self.driver)

    def editContentSIT(self):
        # self.click("O_ADD_SLIDE_BTN_XPATH")
        time.sleep(2)
        # self.click("O_EDIT_CONTENT_SAVE_BTN_XPATH")
        # self.driver.wait.until(EC.invisibility_of_element_located((By.XPATH, "(//input[@class='value']/ancestor::form/following-sibling::div//span//span//span//span)[3]")))
        # self.selenium_click("O_EDIT_CONTENT_SAVE_BTN_SIT_XPATH")
        self.click("O_EDIT_CONTENT_SAVE_BTN_SIT_Create_XPATH")
        time.sleep(2)
        self.gotoContentContents_Page()
        time.sleep(2)
        self.clickOnAddedContentNameInTable__()
        ele = self.find_elements("O_One_SLIDES_DURATION_XPATH")
        ele = len(ele)
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env =="pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        return ele

    def sendkeystofield(self):
        self.send_keys("O_TB_entertext_SIT_XPATH","XYZ")
        return Content(self.driver)

    def closetagoption(self):
        time.sleep(2)
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        return Content(self.driver)

    ######################## 09-04-25#####################

    def gotocontentlink(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        return Content(self.driver)

    def InitialUsageCount(self):
        self.send_keys("N_MediaSearchBar_XPATH", r_ContentName)
        time.sleep(3)
        count = self.getText("N_UsageCountInLayout_XPATH")
        return count

    def VerifyUsageCount(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.send_keys("N_MediaSearchBar_XPATH", r_ContentName)
        time.sleep(3)
        PlaylistCount = self.getText("N_UsageCountPlaylist_XPATH")
        ScheduleCount = self.getText("N_UsageCountSchedule_XPATH")
        return PlaylistCount, ScheduleCount

    def AssignLayoutToPlaylist(self):
        playlist_name = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
        self.selenium_click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist_name)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(3)
        self.selenium_click("N_LayoutOptionInsidePlaylistedit_XPATH")
        self.selenium_click("N_SearchBoxInsidePlaylistEdit_XPATH")
        self.send_keys("N_SearchBoxInsidePlaylistEdit_XPATH", r_ContentName)
        time.sleep(3)
        action = ActionChains(self.driver)
        source = self.driver.find_element(By.XPATH, f"//li[@title='{r_ContentName}']")
        target = self.driver.find_element(By.XPATH, "//section[@id='uploadPlaylist']")
        action.drag_and_drop(source, target).perform()
        time.sleep(2)
        self.selenium_click("N_SavePlaylist_XPATH")
        time.sleep(2)
        self.selenium_click("N_savePlaylistconfirmation_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def AssignLayoutToSchedule(self):
        Schedule_name = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        self.selenium_click("N_ScheduleCreateIcon_XPATH")
        self.send_keys("N_ScheduleNameField_XPATH", Schedule_name)
        self.selenium_click("N_ScheduleCreateCommit_XPATH")
        time.sleep(3)
        self.selenium_click("N_ScheduleEditPageLayoutOption_XPATH")
        self.selenium_click("N_ScheduleEditPageSearchIcon_XPATH")
        self.send_keys("N_ScheduleEditPageSearchIcon_XPATH", r_ContentName)
        source = self.driver.find_element(By.XPATH, f"//li[@title='{r_ContentName}']")
        target = self.driver.find_element(By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[2]")
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()
        time.sleep(2)
        self.selenium_click("N_ScheduleEditPageCloseIcon_XPATH")
        time.sleep(3)
        return Content(self.driver)

    def LayoutHeaderDetails(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        actual = [
            self.getText("N_LayoutPageNameOption_XPATH"),
            self.getText("N_LayoutPageFolderOption_XPATH"),
            self.getText("N_LayoutPageActionOption_XPATH"),
            self.getText("N_LayoutPageUsageCountOption_XPATH"),
            self.getText("N_LayoutPageDurationOption_XPATH"),
            self.getText("N_LayoutPageDetailOption_XPATH"),
            self.getText("N_LayoutPageModifiedByOption_XPATH"),
            self.getText("N_LayoutPageModifiedAtOption_XPATH"),
            self.getText("N_LayoutPageTagOption_XPATH") ]
        expected = [
            "Name", "Folder", "Action", "Usage Count", "Duration",
            "Details", "Modified By", "Modified At", "Tag" ]
        return actual == expected

    def CreatedLayoutDetails(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.send_keys("N_MediaSearchBar_XPATH", r_ContentName)
        time.sleep(3)
        text_actual = [
            self.getText("N_LayoutPageNameOptionLayout_XPATH"),
            self.getText("N_LayoutPageFolderOptionLayout_XPATH"),
            self.getText("N_LayoutPageUsageCountOptionLayout_XPATH"),
            self.getText("N_LayoutPageDurationOptionLayout_XPATH")]
        text_expected = [
            r_ContentName,"Root Folder","Playlist: 0\nSchedule: 0","00:00:10"]
        visibility_checks = [
            self.is_visible("N_LayoutPageActionOptionLayout_XPATH"),
            self.is_visible("N_LayoutPageModifiedByOptionLayout_XPATH"),
            self.is_visible("N_LayoutPageModifiedAtOptionLayout_XPATH"),
            self.is_visible("N_LayoutPageTagOptionLayout_XPATH"),
            self.is_visible("N_LayoutPageDetailOptionLayout_XPATH")]
        return text_actual == text_expected and all(visibility_checks)


    def verifyObject_videoObject(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("O_VIDEO_OBJECT_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_verify_videoObj_XPATH")
        ele = len(ele)
        if ele == 1:
            return True
        else:
            return False

    def verifyObject_multislideObject(self):
        self.click("O_EDIT_SLIDE_BTN_XPATH")
        time.sleep(1)
        self.click("O_ADD_OBJECT_BTN_XPATH")
        self.click("multiSlideObj_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_verify_videoObj_XPATH")
        ele = len(ele)
        return ele

    def CreateLayoutWithBlankTemplateForVideo_3min(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("LayoutVideoIcon_XPATH")
        time.sleep(3)
        print(Videoname)
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{Videoname}']")
        SourceElement = self.driver.find_element(By.XPATH, f"//span[@title='{Videoname}']")
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        self.click("videoObject_XPATH")
        # self.scroll_to_element("fullScreen_XPATH")
        self.click("fullScreen_XPATH")
        TargetElement = self.find_element("LayoutTargetElementForVideo_XPATH")
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
        time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.click("LayoutEditPageEntireTimeOption_XPATH")
        durationbox = self.find_element("LayoutEditPageEntireTimeDurationOption_XPATH")
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.driver.find_element(By.XPATH, "//input[@id='slide_duration']").send_keys(Keys.BACKSPACE)
        time.sleep(3)
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def Uploadmedia_video(self):
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\earth.mp4"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.mp4"
        shutil.copy(ImageOldName, imageNewName)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(11)
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Videoname
        Videoname = ImageRandomName+".mp4"
        return Content(self.driver)


    def Uploadmedia1(self):
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
        global Imagename1
        Imagename1= ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename1)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename1:
            return True
        else:
            return False

    def Uploadmedia2(self):
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
        global Imagename2
        Imagename2 = ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename2)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename2:
            return True
        else:
            return False

    def Uploadmedia3(self):
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\123.jpg"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.jpg"
        shutil.copy(ImageOldName, imageNewName)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(12)
        self.refresh()
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Imagename3
        Imagename3 = ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename3)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename3:
            return True
        else:
            return False

    def CreateLayoutWithBlankTemplateForImagesMultiSlide(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("LayoutImageIcon_XPATH")
        time.sleep(3)
        SourceElement1 = self.driver.find_element(By.XPATH, f"//span[@title='{Imagename1}']")
        SourceElement2 = self.driver.find_element(By.XPATH, f"//span[@title='{Imagename2}']")
        SourceElement3 = self.driver.find_element(By.XPATH, f"//span[@title='{Imagename3}']")
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        self.click("multiSlideObj_XPATH")
        self.click("fullScreen_XPATH")
        time.sleep(2)
        TargetElement1 = self.find_element("target_multislide_XPATH")
        # Assume driver and SourceElement, TargetElement are already defined
        source1_location = SourceElement1.location
        target1_location = TargetElement1.location
        # Calculate dynamic offset
        x_offset = target1_location['x'] - source1_location['x']
        y_offset = target1_location['y'] - source1_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement1).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
        time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(2)
        self.click("addSlideBtn_XPATH")
        time.sleep(1)
        TargetElement2 = self.find_element("target_2_multislide_XPATH")
        source2_location = SourceElement2.location
        target2_location = TargetElement2.location
        # Calculate dynamic offset
        x_offset = target2_location['x'] - source2_location['x']
        y_offset = target2_location['y'] - source2_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement2).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
        time.sleep(delay_per_step)
        actions.release().perform()
        self.click("addSlideBtn_XPATH")
        time.sleep(1)
        TargetElement3 = self.find_element("target_2_multislide_XPATH")
        source3_location = SourceElement3.location
        target3_location = TargetElement3.location
        # Calculate dynamic offset
        x_offset = target3_location['x'] - source3_location['x']
        y_offset = target3_location['y'] - source3_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement3).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
        time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.contentPopupRemoval()
        return Content(self.driver)

    def verifyMultiSlide(self):
        ele1 = len(self.driver.find_elements(By.XPATH, f"//div[@aria-pressed='false']//span[@class='dijitTitlePaneTextNode'][normalize-space()='{Imagename1}']"))
        print(ele1)
        if ele1 == 1:
            return True
        else:
            return False

    def CreateLayoutWithBlankTemplateFor_ExternalWebpageObj(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        self.click("O_EXTERNAL_WEBPAGE_XPATH")
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def CreateLayoutWithBlankTemplateFor_ButtonObj(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        self.click("O_ButtonObj_XPATH")
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def CreateLayoutWithBlankTemplateFor_ButtonBoxObj(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        self.click("O_ButtonBoxObj_XPATH")
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def verifyButtonBoxObj(self):
        r1 = len(self.find_elements("O_ButtonBox_title_XPATH"))
        r2= len(self.find_elements("O_ButtonBox_frame_XPATH"))
        if r1+r2 == 2:
            return True
        else:
            return False

    def CreateLayoutWithBlankTemplateFor_ClockObj(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        self.click("O_ClockObj_XPATH")
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def CreateLayoutWithBlankTemplateFor_FTPObj(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(2)
        self.contentPopupRemoval()
        self.click("editLayoutBtn_XPATH")
        self.click("objectBtn_XPATH")
        #self.click("O_FTPObj_XPATH")
        self.click("A_FTPObject_XPATH")
        self.click("LayoutSaveOption_XPATH")
        #self.click("LayoutSaveOption_XPATH")
        time.sleep(2)
        return Content(self.driver)

    def verifyClockObj(self):
        r1 = len(self.find_elements("O_Clock_title_XPATH"))
        r2= len(self.find_elements("O_Clock_frame_XPATH"))
        if r1+r2 == 2:
            return True
        else:
            return False

    def verifyFTPObj(self):
        r1 = len(self.find_elements("O_FTP_title_XPATH"))
        r2= len(self.find_elements("O_FTP_frame_XPATH"))
        if r1+r2 == 2:
            return True
        else:
            return False

    def verifyExternalWebpage(self):
        r1 = len(self.find_elements("O_EXTERNAL_WEBPAGE_title_XPATH"))
        r2= len(self.driver.find_elements(By.XPATH, "//iframe[@class='external_page_control_iframe']"))
        if r1+r2 == 2:
            return True
        else:
            return False

    def verifyButtonObj(self):
        r1 = len(self.find_elements("O_Button_title_XPATH"))
        r2= len(self.find_elements("O_Button_frame_XPATH"))
        if r1+r2 == 2:
            return True
        else:
            return False

# Akash
#     def verifyCreateLayoutWithBlankTemplate12(self):
#         time.sleep(2)
#         #ele_XPATH =  f"//span[@class='main_panel_menu_name' and @title='{r_ContentName}']"
#         #ele_XPATH = f"//span[@title='{r_ContentName}']"
#         ele_XPATH = F"//span[@title='{r_ContentName}']"
#         ele = self.driver.find_elements(By.XPATH, ele_XPATH)
#         ele = len(ele)
#         return ele
#     def gotoContentContents_PlayPage12(self):
#         time.sleep(2)
#         self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
#         return Content(self.driver)
#     def gotoContentPlaylists12(self):
#         self.wait_for_visible_all_elements("S_CONTENT_HEAD_XPATH")
#         time.sleep(3)
#         self.selenium_click("S_CONTENT_HEAD_XPATH")
#         self.wait_for_visible_all_elements("SUBMENU_PLAYLIST_XPATH")
#         self.selenium_click("SUBMENU_PLAYLIST_XPATH")
#         # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
#         return Content(self.driver)
#
#
#     def CreateLayoutWithBlankTemplate12(self):
#         global LayoutName1
#         LayoutName1 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
#         self.click("ContentManager_XPATH")
#         self.click("ContentManagerLayout_XPATH")
#         self.click("LayoutCreateNewIcon_XPATH")
#         self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName1)
#         self.click("LayoutBlankTemplate_XPATH")
#         self.click("LayoutCreateButton_XPATH")
#         time.sleep(2)
#         self.gotoContentPlaylists12()
#
#
#     def CreatePlaylistImage12(self):
#         self.refresh()
#         # self.hoverAndSelect("O_ContentManager_XPATH", "O_ContentManagerPlaylist_XPATH")
#         # self.click("O_DisplayCreateIcon_XPATH")
#         global PlaylistName
#         PlaylistName = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
#         self.send_keys("playlistTB_XPATH", PlaylistName)
#         self.click("O_ScheduleCreateCommit_XPATH")
#         self.click("ScheduleEditPageLayoutOption_XPATH")
#         self.click("ScheduleEditPageSearchIcon_XPATH")
#         #self.send_keys("ScheduleEditPageSearchIcon_XPATH", LayoutName1)
#         search = self.find_element("ScheduleEditPageSearchIcon_XPATH")
#         search.clear()
#         search.send_keys(LayoutName1)
#
#         time.sleep(3)
#         CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
#         Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
#         Target = self.find_element("targetElement_XPATH")
#         actions = ActionChains(self.driver)
#         actions.drag_and_drop(Source, Target).perform()
#         #time.sleep(2)
#         self.click("savePlaylist_XPATH")
#         self.click("savePlaylist_Yes_XPATH")
#         return Content(self.driver)

    def verifyCreatePlaylist(self):
        countBeforeAdd = self.getText("S_TOTAL_COUNT_XPATH")
        self.createPlaylist(playlist1)
        countAfterAdd = self.getText("S_TOTAL_COUNT_XPATH")
        assert countBeforeAdd != countAfterAdd

    def generatePlaylistName(self):
        global rPlaylistName
        rPlaylistName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        return rPlaylistName

    def createPlaylist(self):
        self.generatePlaylistName()
        self.navToPlaylistURL()
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", rPlaylistName)
        self.click("O_ScheduleCreateCommit_XPATH")
        time.sleep(3)
        self.click("ScheduleEditPageLayoutOption_XPATH")
        self.click("ScheduleEditPageSearchIcon_XPATH")
        self.send_keys("ScheduleEditPageSearchIcon_XPATH", r_ContentName)
        time.sleep(4)
        CreatedLayout_xpath = (By.XPATH, f"//li//span[contains(.,'{r_ContentName}')]")
        Source = self.find_element(CreatedLayout_xpath)
        Target = self.find_element("targetElement_XPATH")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click("savePlaylist_XPATH")
        self.click("savePlaylist_Yes_XPATH")
        time.sleep(2)
        log.logger.info("playlist_name is : " + rPlaylistName)
        return Content(self.driver)

    def navToPlaylistURL(self):
        time.sleep(2)
        log.logger.info("navToPlaylistURL")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "playlist_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "playlist_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "playlist_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "playlist_sit2_url"))
        self.refresh()
        time.sleep(2)
        return Content(self.driver)


