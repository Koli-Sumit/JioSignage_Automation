import secrets
import time
import autoit
import os
import logging
from Utilities.LogUtil import Logger
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage, retry_action, generate_random_string
log = Logger(__name__, logging.INFO)
# from Pages.BasePage import BasePage
###added######
global schedule_name
schedule_name = generate_random_string(7)


# from Pages.BasePage import BasePage

def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def is_descending(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True


class Displays(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("O_CURRENT_ACCOUNT_TYPE_XPATH")

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

    def verifyDisplayURL(self):
        return self.get_current_url()

    def clickOnDisplayNAME_Clm(self):
        self.click("D_DisplayNAME_Col_XPATH")
        return Displays(self.driver)

    def clickOnAddNewDisplay(self):
        self.click("O_ADD_NEW_DISPLAY_BTN_XPATH")
        time.sleep(2)
        return Displays(self.driver)

    def isVisible_DisplayName(self):
        return self.is_visible("O_DISPLAY_NAME_XPATH")

    def isVisible_Password(self):
        return self.is_visible("O_DISPLAY_PASSWORD_XPATH")

    def isVisible_ConfPassword(self):
        return self.is_visible("O_DISPLAY_CONF_PASSWORD_XPATH")

    def isVisible_State(self):
        return self.is_visible("O_DISPLAY_STATE_XPATH")

    def isVisible_City(self):
        return self.is_visible("O_DISPLAY_CITY_XPATH")

    def isVisible_District(self):
        return self.is_visible("O_DISPLAY_DISTRICT_XPATH")

    def isVisible_Pincode(self):
        return self.is_visible("O_DISPLAY_PINCODE_XPATH")

    def isVisible_StoreAddress(self):
        return self.is_visible("O_DISPLAY_STORE_ADDRESS_XPATH")

    def isVisible_SyncRole(self):
        return self.is_visible("O_DISPLAY_SYNC_ROLE_XPATH")

    def isVisible_MobileNumber(self):
        return self.is_visible("O_DISPLAY_MOBILE_NUM_XPATH")

    def clickOnPopupAddBtn(self):
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Displays(self.driver)

    def clickOnPopupCancelBtn_AddNewDisplay(self):
        self.click("O_DISPLAY_POPUP_CLOSE_BTN_XPATH")
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Displays(self.driver)

    def isVisibleAddDisplayPopup(self):
        time.sleep(2)
        ele = self.find_elements("O_ADD_NEW_DISPLAY_HEADING_XPATH")
        c = len(ele)
        return c

    def enterDisplayName_RT(self):
        global r_displayName
        r_displayName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys("O_RT_DisplayName_XPATH", r_displayName)
        return Displays(self.driver)

    def enterDisplayName(self):
        global r_Displayname
        r_Displayname = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DISPLAY_NAME_XPATH", r_Displayname)
        return Displays(self.driver)

    def enterDisplayPassword(self):
        global r_pass
        r_pass = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        self.send_keys("O_DISPLAY_PASSWORD_XPATH", r_pass)
        return Displays(self.driver)

    def enterDisplayPassword_Conf(self):
        self.send_keys("O_DISPLAY_CONF_PASSWORD_XPATH", r_pass)
        return Displays(self.driver)

    def enterDisplayPassword_mismatch(self):
        self.send_keys("O_DISPLAY_CONF_PASSWORD_XPATH", "AutomationTesting")
        return Displays(self.driver)

    def enterDisplayPassword_4char(self):
        global r_pass_4char
        r_pass_4char = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(4))
        self.send_keys("O_DISPLAY_PASSWORD_XPATH", r_pass_4char)
        return Displays(self.driver)

    def enterDisplayPassword_Conf_4char(self):
        self.send_keys("O_DISPLAY_CONF_PASSWORD_XPATH", r_pass_4char)
        return Displays(self.driver)

    def enterDisplayDistrict_numbers(self):
        self.send_keys("O_DISPLAY_DISTRICT_XPATH", "12345")
        return Displays(self.driver)

    def clickOnShowPasswordBtn(self):
        self.selenium_click("O_SHOW_PASS_BTN_XPATH")
        return Displays(self.driver)

    def isVisiblePassword(self):
        time.sleep(2)
        ele = self.find_element("O_DISPLAY_PASSWORD_XPATH").get_attribute('type')
        return ele

    def selectStateAs_Karnataka(self):
        self.select_option_by_text_from_dropdown("O_DISPLAY_STATE_XPATH", "Karnataka")
        return Displays(self.driver)

    def getTextFromStateDropdown(self):
        return self.get_selected_text_from_dropdown("O_DISPLAY_STATE_XPATH")

    def selectCityAs_Bengaluru(self):
        self.select_option_by_text_from_dropdown("O_DISPLAY_CITY_XPATH", "Bengaluru")
        return Displays(self.driver)

    def getTextFromSCityDropdown(self):
        return self.get_selected_text_from_dropdown("O_DISPLAY_CITY_XPATH")

    def getTextFromWarningMsg(self):
        time.sleep(2)
        # return self.getText("O_WARNING_MSG_XPATH")
        ###changes made XPATH changed####
        return self.getText("O_WARNING_MSG_SIT_XPATH")

    def createNewDisplay(self):
        self.clickOnAddNewDisplay()
        self.enterDisplayName()
        self.enterDisplayPassword()
        self.enterDisplayPassword_Conf()
        self.clickOnPopupAddBtn()
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def goToAddNewTagPage_ForCreatedDisplay(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_TAG_XPATH")
        self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        time.sleep(1)
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Displays(self.driver)

    def goToRemoveTagPage_ForCreatedDisplay(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_TAG_XPATH")
        self.click("O_Remove_TAG_XPATH")

        self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        time.sleep(1)
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Displays(self.driver)

    def goToDeleteCompletelyPage_ForCreatedDisplay(self):
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        time.sleep(1)
        self.click("O_DELETE_COMPLETELY_CANCEL_BTN_XPATH")
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Displays(self.driver)

    def deleteCreatedDisplay(self):
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(3)
        return Displays(self.driver)

    def deleteCreatedDisplay_Cancel(self):
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_MOVE_TO_TRASH_CANCEL_BTN_XPATH")
        time.sleep(3)
        return Displays(self.driver)

    def enterTagName(self):
        global r_TagName
        r_TagName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_NEW_TAG_TEXTBOX_XPATH", r_TagName)
        return Displays(self.driver)

    def enterRemoveTagName(self):
        self.send_keys("O_searchTag_XPATH", r_TagName)
        return Displays(self.driver)

    def isVisibleAddTagPopup(self):
        time.sleep(2)
        ele = self.find_elements("O_ADD_TAG_HEADING_XPATH")
        c = len(ele)
        return c

    def isVisibleCreateFolderPopup(self):
        time.sleep(2)
        ele = self.find_elements("O_CreateFolder_HEADING_XPATH")
        ele2 = self.find_elements("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH")
        c = len(ele) + len(ele2)
        return c

    def goToCreateFolderPage(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.click("O_DISPLAY_POPUP_CLOSE_BTN_XPATH")
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Displays(self.driver)

    def goToCreateFolderPage_X_BTN(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.click("O_PHONE_NUM_X_BTN_XPATH")
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        # self.click("O_DISPLAY_POPUP_X_BTN_XPATH")
        return Displays(self.driver)

    def goToCreateFolderPage__(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        return Displays(self.driver)

    def createNewFolder(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.enterFolderName()
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Displays(self.driver)

    def createNewFolder_SplChar(self):
        self.click("O_DISPLAY_CREATE_FOLDER_BTN_XPATH")
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", "!@#$%^")
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Displays(self.driver)

    def enterFolderName(self):
        global r_FolderName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(4))
        r_FolderName = f"TestFolder00__{r_text}"
        self.send_keys("O_DISPLAY_CREATE_FOLDER_NAME_TEXTBOX_XPATH", r_FolderName)
        return Displays(self.driver)

    def verifyFolderIsCreated(self):
        #ele_XPATH = f"//button[.=' {r_FolderName} ']"
        ele_XPATH = f"//span//span[@title='{r_FolderName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def deleteCreatedFolder(self):
        time.sleep(1)
        self.click("O_DELETE_COMPLETELY_FOLDER_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(1)
        return Displays(self.driver)

    def selectFirstFolderFromDropdown(self):
        time.sleep(2)
        self.click("O_FolderDropdown_XPATH")
        time.sleep(2)
        self.click("O_FolderDropdown_FirstOption_XPATH")
        time.sleep(1)
        return Displays(self.driver)

    def selectFirstFolderFromDropdown_SearchBar(self):
        time.sleep(2)
        self.click("O_FolderDropdown_XPATH")
        time.sleep(2)
        self.send_keys("O_FolderDropdown_SearchBar_XPATH", f"{r_FolderName}")
        time.sleep(2)
        ele_XPATH = f"//a[normalize-space()='{r_FolderName}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        return Displays(self.driver)

    def clickOnHeadFolderBtn(self):
        time.sleep(2)
        self.click("O_HEAD_FOLDER_BTN_XPATH")
        return Displays(self.driver)

    def verifyFolderIsSelected(self):
        ele = self.find_elements("O_DELETE_COMPLETELY_FOLDER_XPATH")
        c = len(ele)
        return c

    def clickOnDeliverInstantlyBtn(self):
        self.refresh()
        time.sleep(1)
        self.click("O_DELIVER_INSTANTLY_BTN_XPATH")
        return Displays(self.driver)

    def isVisibleDeliverInstantlyRadioBTNs(self):
        time.sleep(2)
        ele = self.find_elements("O_DELIVER_INSTANTLY_Display_Radio_XPATH")
        ele2 = self.find_elements("O_DELIVER_INSTANTLY_Folder_Radio_XPATH")
        ele3 = self.find_elements("O_DELIVER_INSTANTLY_Base_Radio_XPATH")
        ele4 = self.find_elements("O_DELIVER_INSTANTLY_Tag_Radio_XPATH")
        c = len(ele) + len(ele2) + len(ele3) + len(ele4)
        return c

    def searchCreatedDisplayNameOnDeliverInstantlyPage(self):
        # DELIVER_INSTANTLY_SearchBar_XPATH = "//input[@placeholder='Search Display']"
        # self.send_keys("O_DELIVER_INSTANTLY_SearchBar_XPATH", f"{r_Displayname}")
        # self.driver.find_element(By.XPATH, DELIVER_INSTANTLY_SearchBar_XPATH).send_keys(Keys.ENTER)
        time.sleep(2)
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_SIT1_XPATH", f"{r_Displayname}")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Search Display Name']").send_keys(Keys.ENTER)
        time.sleep(2)
        ele_XPATH = f"//li[@title='{r_Displayname}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectCheckboxOfCreatedDisplayNameOnDeliverInstantlyPage(self):
        # self.send_keys("O_DELIVER_INSTANTLY_SearchBar_XPATH", f"{r_Displayname}")
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_SIT1_XPATH", f"{r_Displayname}")
        time.sleep(2)
        ele1_XPATH = f"//li[@role='option'][.='{r_Displayname}']"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        time.sleep(2)
        ele_XPATH = f"//li[@title='{r_Displayname}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectMultipleCheckboxesOfCreatedDisplayNameOnDeliverInstantlyPage(self):
        # self.click("O_DELIVER_INSTANTLY_SearchBar_XPATH")
        self.click("O_DELIVER_INSTANTLY_SearchBar_SIT1_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SelectFirstDisplay_XPATH")
        self.selenium_click("O_DELIVER_INSTANTLY_SelectSecondDisplay_XPATH")
        ele = self.find_elements("O_DELIVER_INSTANTLY_SelectedDisplayCount_XPATH")
        c = len(ele)
        return c

    def clickOnRadioBtn_Folder(self):
        self.click("O_DELIVER_INSTANTLY_Folder_Radio_XPATH")
        return Displays(self.driver)

    def clickOnRadioBtn_Base(self):
        self.click("O_DELIVER_INSTANTLY_Base_Radio_XPATH")
        return Displays(self.driver)

    def clickOnRadioBtn_Tag(self):
        self.click("O_DELIVER_INSTANTLY_Tag_Radio_XPATH")
        return Displays(self.driver)

    def searchCreatedFolderNameOnDeliverInstantlyPage(self):
        self.click("O_DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH")
        folder_name1 = self.getText("O_DELIVER_INSTANTLY_FOLDER_FIRST_OPTION_XPATH")
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH", f"{folder_name1}")
        DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH = "//input[@placeholder='Search Folder Name']"
        self.driver.find_element(By.XPATH, DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH).send_keys(Keys.ENTER)
        time.sleep(2)
        ele_XPATH = f"//li[@title='{folder_name1}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectCheckboxOfCreatedFolderNameOnDeliverInstantlyPage(self):
        self.click("O_DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH")
        folder_name1 = self.getText("O_DELIVER_INSTANTLY_FOLDER_FIRST_OPTION_XPATH")
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH", f"{folder_name1}")
        time.sleep(2)
        ele1_XPATH = f"//li[@role='option'][.='{folder_name1}']"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        time.sleep(2)
        ele_XPATH = f"//li[@title='{folder_name1}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectMultipleCheckboxesOfCreatedFolderNameOnDeliverInstantlyPage(self):
        self.click("O_DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SelectFirstDisplay_XPATH")
        self.selenium_click("O_DELIVER_INSTANTLY_SelectSecondDisplay_XPATH")
        ele = self.find_elements("O_DELIVER_INSTANTLY_SelectedDisplayCount_XPATH")
        c = len(ele)
        return c

    def searchCreatedBaseNameOnDeliverInstantlyPage(self):
        self.click("O_DELIVER_INSTANTLY_SearchBar_BASE_XPATH")
        base_name1 = self.getText("O_DELIVER_INSTANTLY_FOLDER_FIRST_OPTION_XPATH")
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_BASE_XPATH", f"{base_name1}")
        time.sleep(2)
        DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH = "//input[@placeholder='Search Base Name']"
        self.driver.find_element(By.XPATH, DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH).send_keys(Keys.ENTER)
        time.sleep(2)
        ele_XPATH = f"//li[@title='{base_name1}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectCheckboxOfCreatedBaseNameOnDeliverInstantlyPage(self):
        self.click("O_DELIVER_INSTANTLY_SearchBar_BASE_XPATH")
        base_name1 = self.getText("O_DELIVER_INSTANTLY_FOLDER_FIRST_OPTION_XPATH")
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_BASE_XPATH", f"{base_name1}")
        time.sleep(2)
        ele1_XPATH = f"//li[@role='option'][.='{base_name1}']"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        time.sleep(2)
        ele_XPATH = f"//li[@title='{base_name1}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectMultipleCheckboxesOfCreatedBaseNameOnDeliverInstantlyPage(self):
        self.click("O_DELIVER_INSTANTLY_SearchBar_BASE_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SelectFirstDisplay_XPATH")
        self.selenium_click("O_DELIVER_INSTANTLY_SelectSecondDisplay_XPATH")
        ele = self.find_elements("O_DELIVER_INSTANTLY_SelectedDisplayCount_XPATH")
        c = len(ele)
        return c

    def searchCreatedTagNameOnDeliverInstantlyPage(self):
        # self.click("O_DELIVER_INSTANTLY_SearchBar_TAG_XPATH")
        self.click("O_DELIVER_INSTANTLY_SearchBar_TAG_SIT1_XPATH")
        tag_name1 = self.getText("O_DELIVER_INSTANTLY_FOLDER_FIRST_OPTION_XPATH")
        # self.send_keys("O_DELIVER_INSTANTLY_SearchBar_TAG_XPATH", f"{tag_name1}")
        self.send_keys("O_DELIVER_INSTANTLY_SearchBar_TAG_SIT1_XPATH", f"{tag_name1}")
        time.sleep(2)
        # DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH = "//input[@placeholder='Search Tag']"
        DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH = "//input[@placeholder='Search Tag Name']"
        self.driver.find_element(By.XPATH,DELIVER_INSTANTLY_SearchBar_FOLDER_XPATH).send_keys(Keys.ENTER)
        time.sleep(2)
        ele_XPATH = f"//li[@title='{tag_name1}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(ele)
        return c

    def selectCheckboxOfCreatedTagNameOnDeliverInstantlyPage(self):
        # self.click("O_DELIVER_INSTANTLY_SearchBar_TAG_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SearchBar_TAG_SIT1_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SelectFirstDisplay_XPATH")
        ele = self.find_elements("O_DELIVER_INSTANTLY_SelectedDisplayCount_XPATH")
        c = len(ele)
        return c

    def selectMultipleCheckboxesOfCreatedTagNameOnDeliverInstantlyPage(self):
        # self.click("O_DELIVER_INSTANTLY_SearchBar_TAG_XPATH")
        self.click("O_DELIVER_INSTANTLY_SearchBar_TAG_SIT1_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SelectFirstDisplay_XPATH")
        self.selenium_click("O_DELIVER_INSTANTLY_SelectSecondDisplay_XPATH")
        ele = self.find_elements("O_DELIVER_INSTANTLY_SelectedDisplayCount_XPATH")
        c = len(ele)
        return c

    def clickOn_X_ICON_SELECTED_DISPLAY(self):
        # self.click("O_DELIVER_INSTANTLY_SearchBar_XPATH")
        self.click("O_DELIVER_INSTANTLY_SearchBar_SIT1_XPATH")
        time.sleep(2)
        self.selenium_click("O_DELIVER_INSTANTLY_SelectFirstDisplay_XPATH")
        time.sleep(1)
        self.click("O_DELIVER_INSTANTLY_X_ICON_FIRST_SELECTED_ITEM_XPATH")
        time.sleep(1)
        ele = self.find_elements("O_DELIVER_INSTANTLY_SelectedDisplayCount_XPATH")
        c = len(ele)
        return c

    def clickOn_X_ICON_DELIVER_INSTANTLY_PAGE(self):
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        time.sleep(2)
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        return Displays(self.driver)

    def isVisibleDeliverInstantlyPage(self):
        ele = self.find_elements("O_ADD_TAG_DELIVER_HEADING_XPATH")
        c = len(ele)
        return c

    def verifyDisplayDetailsPage_closeBtn(self):
        ele_XPATH = f"//a//span[.=' {r_Displayname}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        time.sleep(2)
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        heading_XPATH = f"//h5[.='Display Details of {r_Displayname}']"
        ele = self.driver.find_elements(By.XPATH, heading_XPATH)
        c = len(ele)
        return c

    def verifyDisplayDetailsPage(self):
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(5)
        ele_XPATH = f"//a//span[.=' {r_Displayname}']"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        heading_XPATH = f"//td[normalize-space()='{r_Displayname}']"
        ele = self.driver.find_elements(By.XPATH, heading_XPATH)
        c = len(ele)
        return c

    def clickOnSchedule(self):
        time.sleep(2)
        elements = self.find_elements("O_DELIVER_INSTANTLY_SCHEDULES_XPATH")
        ele = elements[0]
        ele.click()
        self.click("O_DELIVER_INSTANTLY_SCHEDULES_EDIT_TEXTBOX_XPATH")
        self.clear("O_DELIVER_INSTANTLY_SCHEDULES_EDIT_TEXTBOX_XPATH")
        global r_ScheduleName
        r_ScheduleName = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DELIVER_INSTANTLY_SCHEDULES_EDIT_TEXTBOX_XPATH", r_ScheduleName)
        time.sleep(1)
        self.click("O_DELIVER_INSTANTLY_SCHEDULES_UPDATE_BTN_XPATH")
        time.sleep(1)
        return Displays(self.driver)

    def getTextFromSuccessPopup(self):
        # txt = self.getText("O_SUCCESS_POPUP_XPATH")
        txt = self.getText("O_SUCCESS_POPUP_editsch_SIT1_XPATH")
        time.sleep(2)
        return txt

    def verifyMoveToDisplayPage_closeBtn(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_MOVE_TO_DISPLAY_XPATH")
        self.click("O_DELIVER_INSTANTLY_X_ICON_XPATH")
        time.sleep(2)
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_MOVE_TO_DISPLAY_HEADING_XPATH")
        c = len(ele)
        return c

    def verifyEditDisplayPage_closeBtn(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        self.click("O_EDIT_DISPLAY_X_BTN_XPATH")
        time.sleep(2)
        self.click("O_ASSIGN_SCHEDULE_BTN_XPATH")
        time.sleep(2)
        ele = self.find_elements("O_ADD_EDIT_DISPLAY_HEADING_XPATH")
        c = len(ele)
        return c

    def EditDisplayName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        self.clear("O_EDIT_DISPLAY_DISPLAY_NAME_TEXTBOX_XPATH")
        global r_Displayname_edited
        r_Displayname_edited = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_EDIT_DISPLAY_DISPLAY_NAME_TEXTBOX_XPATH", r_Displayname_edited)
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def deleteCreatedDisplay_edited(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname_edited)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname_edited}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        return Displays(self.driver)

    def verifyEditedDisplayName(self):
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname_edited}')]"
        elements = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(elements)
        return c

    def EditStateName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.selectStateAs_Karnataka()
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getStateName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        stateName = self.get_selected_text_from_dropdown("O_DISPLAY_STATE_XPATH")
        return stateName

    def EditCityName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.selectStateAs_Karnataka()
        self.selectCityAs_Bengaluru()
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getCityName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(3)
        cityName = self.get_selected_text_from_dropdown("O_DISPLAY_CITY_XPATH")
        return cityName

    def EditDistrictName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.clear("O_DISPLAY_DISTRICT_XPATH")
        self.send_keys("O_DISPLAY_DISTRICT_XPATH", "Thane")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getDistrictName(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        districtName = self.find_element("O_DISPLAY_DISTRICT_XPATH").get_attribute('value')
        return districtName

    def EditPincode(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.clear("O_DISPLAY_PINCODE_XPATH")
        self.send_keys("O_DISPLAY_PINCODE_XPATH", "400001")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getPincode(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        pincode = self.find_element("O_DISPLAY_PINCODE_XPATH").get_attribute('value')
        return pincode

    def EditStoreAddress(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.clear("O_DISPLAY_STORE_ADDRESS_XPATH")
        self.send_keys("O_DISPLAY_STORE_ADDRESS_XPATH", "Sample Store Address")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getStoreAddress(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        sAddress = self.find_element("O_DISPLAY_STORE_ADDRESS_XPATH").get_attribute('value')
        return sAddress

    def EditSyncRole(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.select_option_by_text_from_dropdown("O_DISPLAY_SYNC_ROLE_XPATH", "Slave")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getSyncRole(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(3)
        syncRole = self.get_selected_text_from_dropdown("O_DISPLAY_SYNC_ROLE_XPATH")
        return syncRole

    def EditMobileNumber(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(2)
        self.clear("O_DISPLAY_MOBILE_NUM_XPATH")
        self.send_keys("O_DISPLAY_MOBILE_NUM_XPATH", "1234567890")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def getMobileNumber(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        sAddress = self.find_element("O_DISPLAY_MOBILE_NUM_XPATH").get_attribute('value')
        return sAddress

    def verifyTagListPage(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[8]//a"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        time.sleep(1)
        ele = self.find_elements("O_TAG_LIST_HEADING_XPATH")
        c = len(ele)
        return c

    def bulkUpload_Display(self):
        self.wait_for_visible_all_elements("O_BULK_CREATE_BTN_XPATH")
        self.click("O_BULK_CREATE_BTN_XPATH")
        self.driver.find_element(By.XPATH, "//div[@class='mb-3']").click()
        time.sleep(2)
        cwd = os.getcwd()
        file_path = cwd + r'\TestData\JioSignageDisplays5.csv'
        autoit.control_focus("Open", "Edit1")
        time.sleep(2)
        autoit.control_set_text("Open", "Edit1", file_path)
        time.sleep(2)
        autoit.control_send("Open", "Button1", "{ENTER}")
        time.sleep(5)
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def verifyDisplayAddedFromBulkUpload(self):
        display1 = self.find_elements("O_BULK_UPLOADED_DISPLAY1_XPATH")
        display2 = self.find_elements("O_BULK_UPLOADED_DISPLAY2_XPATH")
        display3 = self.find_elements("O_BULK_UPLOADED_DISPLAY3_XPATH")
        display4 = self.find_elements("O_BULK_UPLOADED_DISPLAY4_XPATH")
        display5 = self.find_elements("O_BULK_UPLOADED_DISPLAY5_XPATH")
        display1 = len(display1)
        display2 = len(display2)
        display3 = len(display3)
        display4 = len(display4)
        display5 = len(display5)
        if display1 == 1 and display2 == 1 and display3 == 1 and display4 == 1 and display5 == 1:
            return True
        else:
            return False

    def deleteCreatedDisplay_byBulkUpload(self):
        self.refresh()
        time.sleep(3)
        checkbox1_XPATH = f"//td//a//span[contains(text(),'TestAutoDisplay')]/preceding::input[@type='checkbox'][1]"
        elements = self.driver.find_elements(By.XPATH, checkbox1_XPATH)
        for element in elements:
            element.click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        return Displays(self.driver)

    def searchDisplayName(self):
        time.sleep(2)
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", f"{r_Displayname}")
        time.sleep(4)
        elements = self.find_elements("O_ROLE_MGT_Role_entries_Count_XPATH")
        elements = len(elements)
        return elements

    def getCreatedDisplayId(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::td[1]"
        global display_id
        display_id = self.driver.find_element(By.XPATH, ele_XPATH).text
        self.driver.refresh()
        return Displays(self.driver)

    def searchDisplayId(self):
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", f"{display_id}")
        time.sleep(2)
        elements = self.find_elements("O_ROLE_MGT_Role_entries_Count_XPATH")
        elements = len(elements)
        return elements

    def select_20_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "20")
        time.sleep(2)
        return Displays(self.driver)

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "50")
        time.sleep(2)
        return Displays(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "100")
        time.sleep(2)
        return Displays(self.driver)

    def select_200_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "200")
        time.sleep(2)
        return Displays(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return Displays(self.driver)

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def gotouseraccess(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return Displays(self.driver)

    def createbaseuser(self):
        time.sleep(2)
        self.wait_for_visible("D_AddBase_Icon_XPATH")
        self.click("D_AddBase_Icon_XPATH")
        self.wait_for_visible("D_EnterBaseuserName_XPATH")
        self.click("D_EnterBaseuserName_XPATH")
        global D_baseusername
        D_baseusername = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("D_EnterBaseuserName_XPATH", D_baseusername)
        self.click("D_AddSchedulebutton_XPATH")
        return Displays(self.driver)

    def switchtobaseuser(self):
        ele_XPATH = "//input[@role='searchbox']"
        self.wait_for_visible("D_DropdownselectBaseUser_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        # self.click("D_DropdownselectBaseUser_XPATH")
        self.wait_for_visible("D_selectBase_XPATH")
        time.sleep(1)
        self.click("D_selectBase_XPATH")
        self.wait_for_visible("D_clickdropdown_selectbase_XPATH")
        time.sleep(2.5)
        self.selenium_click("D_clickdropdown_selectbase_XPATH")
        self.wait_for_visible("D_SearchSchedule_XPATH")
        self.click("D_SearchSchedule_XPATH")
        self.send_keys("D_SearchSchedule_XPATH", D_baseusername)
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        self.wait_for_visible("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return Displays(self.driver)

    def gotodisplaysBase(self):
        time.sleep(2)
        self.wait_for_visible("MENU_CONTENT_XPATH")
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return Displays(self.driver)

    def verifycreatedisplayBase(self):
        for i in range(1, 6):
            time.sleep(1)
            self.refresh()
            time.sleep(2)
            self.wait_for_visible("AddButton_Display_D_XPATH")
            self.selenium_click("AddButton_Display_D_XPATH")
            time.sleep(6)
            self.wait_for_visible("Display_name_D_XPATH")
            self.selenium_click("Display_name_D_XPATH")
            global d_displaynameb
            d_displaynameb = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
            self.send_keys("Display_name_D_XPATH", d_displaynameb)
            self.wait_for_visible("EnterPassword_Display_D_XPATH")
            self.click("EnterPassword_Display_D_XPATH")
            global p_pssdb
            p_pssdb = ''.join(secrets.choice('0123456789') for _ in range(9))
            self.send_keys("EnterPassword_Display_D_XPATH", p_pssdb)
            self.wait_for_visible("Confirm_Password_Display_D_XPATH")
            self.click("Confirm_Password_Display_D_XPATH")
            self.send_keys("Confirm_Password_Display_D_XPATH", p_pssdb)
            self.wait_for_visible_all_elements("Add_Display_D_XPATH")
            self.click("Add_Display_D_XPATH")
            time.sleep(6)
        return Displays(self.driver)

    def DeleteCreatedDisplay(self):
        self.wait_for_visible("D_All_Display_base_XPATH")
        self.click("D_All_Display_base_XPATH")
        self.selenium_click("D_Three_Dots_base_XPATH")
        self.wait_for_visible("D_delete_completely_XPATH")
        self.click("D_delete_completely_XPATH")
        self.click("D_OkButton_XPATH")
        return Displays(self.driver)

    def SwitchtoHeaduser(self):
        self.wait_for_visible("D_DropdownselectBaseUser_XPATH")
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        self.wait_for_visible("D_HeadAcoount_XPATH")
        self.click("D_HeadAcoount_XPATH")
        return Displays(self.driver)

    def deletecreatedbaseuser(self):
        self.wait_for_visible("D_Searchbaseuser_XPATH")
        self.click("D_Searchbaseuser_XPATH")
        self.send_keys("D_Searchbaseuser_XPATH", D_baseusername)
        time.sleep(2)
        self.wait_for_visible("D_Baseuser_threedot_XPATH")
        time.sleep(1)
        self.click("D_Baseuser_threedot_XPATH")
        time.sleep(1)
        self.click("D_Baseuser_Delete_XPATH")
        time.sleep(1)
        self.click("D_OkButton_XPATH")
        return Displays(self.driver)

    def verifyInDescendingOrder_Displayname(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_Displayname(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_id(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_id(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickOnDisplayID_Clm(self):
        self.click("D_DisplayID_Col_XPATH")
        return Displays(self.driver)

    ################################added#######################

    def searchDisplayNamecraeted(self):
        time.sleep(1)
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", f"{r_Displayname}")
        time.sleep(2)
        return Displays(self.driver)

    def clickonfirstcheckbox(self):
        self.wait_for_visible("D_Firstdisplay_Checkbox_XPATH")
        time.sleep(2)
        self.refresh()
        time.sleep(1)
        self.click("D_Firstdisplay_Checkbox_XPATH")
        return Displays(self.driver)

    def clickmore(self):
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return Displays(self.driver)

    def clickonMove(self):
        time.sleep(2)
        Move_options = self.find_element("D_Movedisplay_XPATH")
        self.driver.execute_script("arguments[0].click();", Move_options)
        return Displays(self.driver)

    def selectcreatedfolder(self):
        ele_XPATH = "//input[@role='searchbox']"
        self.wait_for_visible("D_clickdropdown_selectbase_XPATH")
        self.selenium_click("D_clickdropdown_selectbase_XPATH")
        self.wait_for_visible("D_SearchSchedule_XPATH")
        self.click("D_SearchSchedule_XPATH")
        self.send_keys("D_SearchSchedule_XPATH", r_FolderName)
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        self.wait_for_visible("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return Displays(self.driver)

    def verifydisplaynameinfolder(self):
        time.sleep(3)
        a = self.getText("D_Thirdrow_DisplayName_XPATH")
        time.sleep(2)
        if a == r_Displayname:
            assert True
            # print("pass")
        else:
            assert False
        return Displays(self.driver)

    def EditDisplayNameedit(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele_XPATH = f"//td//a//span[contains(.,'{r_Displayname}')]/ancestor::tr//td[9]//div//a[1]"
        self.driver.find_element(By.XPATH, ele_XPATH).click()
        self.clear("O_EDIT_DISPLAY_DISPLAY_NAME_TEXTBOX_XPATH")
        global r_Displayname_edited
        r_Displayname_edited = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_EDIT_DISPLAY_DISPLAY_NAME_TEXTBOX_XPATH", r_Displayname_edited)
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # time.sleep(2)
        # self.refresh()
        return Displays(self.driver)

    def gettextofeditdisplay(self):
        global gttxteddsp
        gttxteddsp = self.getText("D_Popup_XPATH")
        return Displays(self.driver)

    def printtext(self):
        ele = gttxteddsp
        return ele

    def clickonmigrate(self):
        time.sleep(1)
        self.wait_for_visible("D_Migrate_XPATH")
        self.click("D_Migrate_XPATH")
        return Displays(self.driver)

    def selectbasetomigratedisplay(self):
        self.wait_for_visible("D_Selectbasetomigrate_XPATH")
        self.click("D_Selectbasetomigrate_XPATH")
        # self.wait_for_visible("D_clickdropdown_selectbase_XPATH")
        # self.click("D_clickdropdown_selectbase_XPATH")
        self.select_option_by_text_from_dropdown("D_Selectbasetomigrate_XPATH", D_baseusername)
        # self.wait_for_visible("D_SearchSchedule_XPATH")
        # self.click("D_SearchSchedule_XPATH")
        # self.send_keys("D_SearchSchedule_XPATH", D_baseusername)
        # time.sleep(3)
        # self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        # self.wait_for_visible("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return Displays(self.driver)

    def getlengthofcurrentpass(self):
        time.sleep(1)
        global existp
        existpp = self.find_elements("O_DISPLAY_PASSWORD_XPATH")
        existp = len(existpp)
        return Displays(self.driver)

    def enterDisplayPasswordnew(self):
        self.wait_for_visible("O_NEW_PASS1_XPATH")
        self.click("O_NEW_PASS1_XPATH")
        global r_pass_new
        r_pass_new = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(9))
        self.send_keys("O_DISPLAY_PASSWORD_XPATH", r_pass_new)
        return Displays(self.driver)

    def enterDisplayPassword_Confnew(self):
        time.sleep(1)
        self.send_keys("O_NEW_PASS_Conf_XPATH", r_pass_new)
        return Displays(self.driver)

    def clickonsavepassword(self):
        self.wait_for_visible("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return Displays(self.driver)

    def clickonediticon(self):
        time.sleep(1)
        self.wait_for_visible("D_EditDisplay_XPATH")
        self.click("D_EditDisplay_XPATH")
        return Displays(self.driver)

    def clickoneditpassword(self):
        time.sleep(1)
        self.wait_for_visible("D_Changepass_XPATH")
        self.click("D_Changepass_XPATH")
        return Displays(self.driver)

    def gotoContentSchedules(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        return Displays(self.driver)

    def addSchedule(self):
        time.sleep(2)
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", schedule_name)
        self.click("S_ADD_BUTTON_NAME")
        # self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        # if configReader.getTestData("TestData", "Environment") == "prod":
        #     self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        # elif configReader.getTestData("TestData", "Environment") == "pre-prod":
        #     self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        # time.sleep(1)
        # schedule_xpath = f"//span[@title='{schedule_name}']"
        # log.logger.info("schedule_xpath : " + schedule_xpath)
        # schedule_count = self.driver.find_elements(By.XPATH, schedule_xpath)
        # log.logger.info("schedule_count : " + str(len(schedule_count)))
        return Displays(self.driver)

    def clickonscheduleicon(self):
        time.sleep(1)
        self.wait_for_visible("D_Schedule_icon_XPATH")
        self.click("D_Schedule_icon_XPATH")
        return Displays(self.driver)

    def Assignschedule(self):
        time.sleep(2)
        self.wait_for_visible("S_BASE_DROPDOWN_XPATH")
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        time.sleep(2)
        self.selenium_click("D_Searchboxfield_schedule_Display_XPATH")
        time.sleep(1)
        self.send_keys("D_Searchboxfield_schedule_Display_XPATH", schedule_name)
        self.driver.find_element(By.XPATH,
                                 "//span[@class='select2-search select2-search--dropdown']//input[@role='searchbox']").send_keys(
            Keys.ENTER)
        time.sleep(2)
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        time.sleep(15)
        return Displays(self.driver)

    def searchcreatedschedule(self):
        time.sleep(1)
        self.wait_for_visible("D_SEARCH_BAR_XPATH")
        self.click("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", schedule_name)
        time.sleep(1)
        return Displays(self.driver)

    def deletecreatedschedule(self):
        time.sleep(2)
        self.click("D_Firstdisplay_Checkbox_XPATH")
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(1)
        self.click("D_Movetotrash_Schedule_XPATH")
        time.sleep(2)
        self.click("D_OkButton_XPATH")
        return Displays(self.driver)

    def readScheuleofdisplay(self):
        time.sleep(4)
        self.getText("D_Schedulesectionofdisplay_XPATH")
        return Displays(self.driver)

    # def addScheduleWith5Char(self):
    #     return self.addSchedule(generate_random_string(7))

    def gotoContentDisplays_Page(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return Displays(self.driver)

    def verifyAddedDisplay(self):
        self.refresh()
        time.sleep(2)
        addedDisplay_XPATH = f"//td[3]//a//span[.=' {r_Displayname}']"
        ele = self.driver.find_elements(By.XPATH, addedDisplay_XPATH)
        ele = len(ele)
        return ele

    def createNewDisplay_Second(self):
        self.clickOnAddNewDisplay()
        self.enterDisplayName_second()
        self.enterDisplayPassword()
        self.enterDisplayPassword_Conf()
        self.clickOnPopupAddBtn()
        time.sleep(2)
        self.refresh()
        return Displays(self.driver)

    def enterDisplayName_second(self):
        global r_Displayname_second
        r_Displayname_second = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DISPLAY_NAME_XPATH", r_Displayname_second)
        return Displays(self.driver)

    def deleteCreatedDisplay_twoDisplays(self):
        time.sleep(1)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        checkbox2_XPATH = f"//td//a//span[contains(text(),'{r_Displayname_second}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox2_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        return Displays(self.driver)

    def verifyAddedDisplay_twoDisplays(self):
        addedDisplay_XPATH = f"//td[3]//a//span[.=' {r_Displayname}']"
        ele1 = self.driver.find_elements(By.XPATH, addedDisplay_XPATH)
        ele1 = len(ele1)
        addedDisplay2_XPATH = f"//td[3]//a//span[.=' {r_Displayname_second}']"
        ele2 = self.driver.find_elements(By.XPATH, addedDisplay2_XPATH)
        ele2 = len(ele2)
        ele = ele1 + ele2
        return ele

###############additional Funtion###########08-0402025
    def returnpasswordmissmatchtext(self):
        time.sleep(2)
        return self.getText("O_Warniong_MSG_Passdnotmatch_SIT_XPATH")

    def returnmin6charwarningmsg(self):
        time.sleep(2)
        return self.getText("O_Min8characterreq_SIT1_XPATH")

    def returninvalidfolderstring(self):
        time.sleep(2)
        return self.getText("O_Invalidfoldername_SIT_XPATH")

    def verifyDisplayNotDeleted(self):
        if len(self.driver.find_elements(By.XPATH, f"//span[@title='{r_Displayname}']")) == 1:
            return True
        else:
            return False

    def verifyDisplayDeleted(self):
        if len(self.driver.find_elements(By.XPATH, f"//span[@title='{r_Displayname}']")) == 0:
            return True
        else:
            return False

    def verifyScheduleHistory(self):
        time.sleep(2)
        ele1 =f"//span[@title='{r_Displayname}']//ancestor::td//following-sibling::td//div//a[@title='Schedule Deliver History']"
        ele2 = f"//td[contains(text(),'{schedule_name}')]//following-sibling::td[contains(text(),'Success')]"
        self.driver.find_element(By.XPATH, ele1).click()
        if len(self.driver.find_elements(By.XPATH, ele2))== 1:
            return True
        else:
            return False

    def verifyDisplayLogs(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        ele1 =f"//span[@title='{r_Displayname}']//ancestor::td//following-sibling::td//div//a[@title='Display Logs']"
        ele2 = f"//td[normalize-space()='Display created']"
        ele3 = "//table[@class='table table-bordered table-striped no-footer dataTable']//tbody//tr"
        self.driver.find_element(By.XPATH, ele1).click()
        if len(self.driver.find_elements(By.XPATH, ele2))== 1:
            if len(self.driver.find_elements(By.XPATH, ele3))== 1:
                return True
            else:
                return False
        else:
            return False


    def verifyDisplayInfolder(self):
        time.sleep(3)
        a = self.getText("D_Thirdrow_DisplayName_XPATH")
        if a == r_Displayname:
            return True
        else:
            return False

    def addTagToCreateDisplay(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_TAG_XPATH")
        self.enterTagName()
        self.click("N_CreateDisplayCommit_XPATH")
        return Displays(self.driver)

    def verifyAddedTag(self):
        time.sleep(2)
        self.refresh()
        time.sleep(1)
        ele = f"//a[contains(.,'{r_Displayname}')]//parent::td//following-sibling::td//a[@title='Tags']"
        self.driver.find_element(By.XPATH, ele).click()
        time.sleep(1)
        if len(self.driver.find_elements(By.XPATH, f"//td[normalize-space()='{r_TagName}']")) == 1:
            self.refresh()
            return True
        else:
            self.refresh()
            return False

    def removeTagToCreateDisplay(self):
        self.send_keys("O_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_ADD_TAG_XPATH")
        self.click("O_Remove_TAG_XPATH")
        self.click("O_searchTag_XPATH")
        self.enterRemoveTagName()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Select Tags']").send_keys(Keys.ENTER)
        time.sleep(1)
        self.click("O_PREVIEW_TITLE_XPATH")
        self.click("O_removeBtn_XPATH")
        return Displays(self.driver)

    def verifyRemovedTag(self):
        time.sleep(2)
        self.refresh()
        time.sleep(1)
        ele = f"//a[contains(.,'{r_Displayname}')]//parent::td//following-sibling::td//a[@title='Tags']"
        self.driver.find_element(By.XPATH, ele).click()
        time.sleep(1)
        if len(self.driver.find_elements(By.XPATH, f"//td[normalize-space()='{r_TagName}']")) == 0:
            self.refresh()
            return True
        else:
            self.refresh()
            return False

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

    # def goToRaiseTicket(self):
    #     time.sleep(1)
    #     self.hoverAndSelect("O_PROFILE_ICON_XPATH", "O_RAISE_TICKET_XPATH")
    #     return Displays(self.driver)

    # def fillRaiseTicketInfoAndSubmit(self):
    #     global window_handles
    #     window_handles = self.driver.window_handles
    #     self.driver.switch_to.window(window_handles[-1])
    #     self.enterDisplayName_RT()
    #     self.enterDisplayID()
    #     self.selenium_click("O_RT_ContactUsAbout_XPATH")
    #     self.click("O_BillingOption_XPATH")
    #     self.enterTitle()
    #     self.enterDescription()
    #     self.click("O_RT_SubmitBtn_XPATH")
    #     self.click("O_LOGOUT_OK_BTN_XPATH")
    #     return Displays(self.driver)

    def enterDisplayID(self):
        global r_displayID
        r_displayID = ''.join(
            secrets.choice('1234567890') for _ in range(6))
        self.send_keys("O_RT_DisplayID_XPATH", r_displayID)
        return Displays(self.driver)

    def enterTitle(self):
        global r_title
        r_title = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.send_keys("O_RT_Title_XPATH", r_title)
        return Displays(self.driver)

    def enterDescription(self):
        global r_description
        r_description = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(5))
        self.click("O_RT_Description_XPATH")
        self.send_keys("O_RT_Description_XPATH", r_description)
        # self.find_element("O_RT_Description_XPATH").send_keys(Keys.NUMPAD1)
        return Displays(self.driver)

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
