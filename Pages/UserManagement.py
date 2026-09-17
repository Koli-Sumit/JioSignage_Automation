import secrets
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage, retry_action


def is_ascending(lst):
    return all(lst[i].lower() <= lst[i + 1].lower() for i in range(len(lst) - 1))


def is_descending(lst):
    return all(lst[i].lower() >= lst[i + 1].lower() for i in range(len(lst) - 1))


class UserManagement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyUserMgmtURL(self):
        time.sleep(2)
        return self.get_current_url()

    def getSubTitleOfUserMgtPage(self):
        return self.getText("O_USER_MGT_AddDeleteModify_TEXT_XPATH")

    def isVisibleAddUserOpt(self):
        return self.is_visible("O_USER_MGT_ADD_USER_BTN_XPATH")

    def isVisibleSearchBar(self):
        return self.is_visible("O_USER_MGT_SEARCHBAR_XPATH")

    def isVisibleNameCLM(self):
        return self.is_visible("O_USER_MGT_NAME_COLUMN_XPATH")

    def isVisibleEmailCLM(self):
        return self.is_visible("O_USER_MGT_EMAIL_COLUMN_XPATH")

    def isVisibleRoleCLM(self):
        return self.is_visible("O_USER_MGT_ROLE_COLUMN_XPATH")

    def isVisiblePermissionCLM(self):
        return self.is_visible("O_USER_MGT_PERMISSION_COLUMN_XPATH")

    def isVisibleActStatusCLM(self):
        return self.is_visible("O_USER_MGT_ACTIVATION_STATUS_COLUMN_XPATH")

    def isVisibleActionCLM(self):
        return self.is_visible("O_USER_MGT_ACTION_COLUMN_XPATH")

    def clickOnAddUser(self):
        self.click("O_USER_MGT_ADD_USER_BTN_XPATH")
        return UserManagement(self.driver)

    def enterUserName(self):
        global r_UserName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        r_UserName = f"Test Account {r_text}"
        self.send_keys("O_USER_MGT_USER_NAME_TEXTBOX_XPATH", r_UserName)
        return UserManagement(self.driver)

    def enterEmailAddress(self):
        global r_gmail
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))
        r_gmail = f"{r_text}@auto.com"
        self.send_keys("O_USER_MGT_EMAIL_TEXTBOX_XPATH", r_gmail)
        return UserManagement(self.driver)

    def enterConfEmailAddress(self):
        self.send_keys("O_USER_MGT_EMAIL_Conf_TEXTBOX_XPATH", r_gmail)
        return UserManagement(self.driver)

    def enterPhoneNumber(self):
        time.sleep(1)
        global r_phoneNum
        r_phoneNum = ''.join(
            secrets.choice('1234567890') for _ in range(10))
        self.send_keys("O_PHONE_NUM_TEXTBOX_XPATH", r_phoneNum)
        return UserManagement(self.driver)

    def selectContractorUser(self):
        self.click("O_USER_MGT_Contractor_USER_XPATH")
        return UserManagement(self.driver)

    def selectEditorUser(self):
        self.click("O_USER_MGT_Editor_USER_XPATH")
        return UserManagement(self.driver)

    def selectAdvertiserUser(self):
        self.click("O_USER_MGT_Advertiser_USER_XPATH")
        return UserManagement(self.driver)

    def selectCustomUser(self):
        self.click("O_USER_MGT_Custom_USER_XPATH")
        return UserManagement(self.driver)

    def clickOnAddOpt(self):
        self.click("O_USER_MGT_POP_UP_ADD_BTN_XPATH")
        return UserManagement(self.driver)

    def clickOnCancelOpt(self):
        self.click("O_USER_MGT_POP_UP_CANCEL_BTN_XPATH")
        return UserManagement(self.driver)

    def deleteCreatedUser(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(1)
        self.searchUserName()
        delete_BTN_XPATH = f"//tr//td[normalize-space()='{r_gmail}']//following-sibling::td[4]//a[2]"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        self.click("O_USER_MGT_DELETE_POP_UP_OK_BTN_XPATH")
        return UserManagement(self.driver)

    def deleteCreatedUser_additional(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(1)
        ele_XPATH = "//input[@placeholder='Search...']"
        self.send_keys("O_USER_MGT_SearchBox_XPATH", f"{r_gmail_additional}")
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        time.sleep(3)
        delete_BTN_XPATH = f"//tr//td[normalize-space()='{r_gmail_additional}']//following-sibling::td[4]//a[2]"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        self.click("O_USER_MGT_DELETE_POP_UP_OK_BTN_XPATH")
        return UserManagement(self.driver)

    def addNewUser(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectContractorUser()
        self.clickOnAddOpt()
        self.refresh()
        return UserManagement(self.driver)

    def addNewUser_cancelBtn(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectContractorUser()
        self.clickOnCancelOpt()
        self.refresh()
        return UserManagement(self.driver)

    def enterUserName_additional(self):
        global r_UserName_additional
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        r_UserName_additional = f"Test Account {r_text}"
        self.send_keys("O_USER_MGT_USER_NAME_TEXTBOX_XPATH", r_UserName_additional)
        return UserManagement(self.driver)

    def enterEmailAddress_additional(self):
        global r_gmail_additional
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))
        r_gmail_additional = f"{r_text}@auto.com"
        self.send_keys("O_USER_MGT_EMAIL_TEXTBOX_XPATH", r_gmail_additional)
        return UserManagement(self.driver)

    def enterConfEmailAddress_additional(self):
        self.send_keys("O_USER_MGT_EMAIL_Conf_TEXTBOX_XPATH", r_gmail_additional)
        return UserManagement(self.driver)

    def enterPhoneNumber_additional(self):
        global r_phoneNum_additional
        r_phoneNum_additional = ''.join(
            secrets.choice('1234567890') for _ in range(10))
        self.send_keys("O_PHONE_NUM_TEXTBOX_XPATH", r_phoneNum_additional)
        return UserManagement(self.driver)

    def enterPhoneNumber_same(self):
        time.sleep(1)
        self.send_keys("O_PHONE_NUM_TEXTBOX_XPATH", r_phoneNum)
        return UserManagement(self.driver)

    def verifyAlertDuplicateMobileNum(self):
        if len(self.find_elements("O_USER_MGT_MOBILE_NUM_DUPLICATE_ALERT_XPATH")) == 1:
            return self.getText("O_USER_MGT_MOBILE_NUM_DUPLICATE_ALERT_XPATH")
        else:
            return "false"

    def verifyAlertDuplicateEmail(self):
        return self.getText("O_USER_MGT_EMAIL_DUPLICATE_ALERT_XPATH")

    def enterEmailAddress_same(self):
        self.send_keys("O_USER_MGT_EMAIL_TEXTBOX_XPATH", r_gmail)
        return UserManagement(self.driver)

    def enterConfEmailAddress_same(self):
        self.send_keys("O_USER_MGT_EMAIL_Conf_TEXTBOX_XPATH", r_gmail)
        return UserManagement(self.driver)

    def enterUserName_same(self):
        self.send_keys("O_USER_MGT_USER_NAME_TEXTBOX_XPATH", r_UserName)
        return UserManagement(self.driver)

    def verifyUserWithExistingName(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = f"//td[text()='{r_UserName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        u_count = len(ele)
        if u_count == 2:
            return True
        else:
            return False

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def searchUserName(self):
        self.refresh()
        self.refresh()
        ele_XPATH = "//input[@placeholder='Search...']"
        self.send_keys("O_USER_MGT_SearchBox_XPATH", f"{r_UserName}")
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        time.sleep(3)
        return UserManagement(self.driver)

    def searchEmailAddress(self):
        self.refresh()
        self.refresh()
        ele_XPATH = "//input[@placeholder='Search...']"
        self.send_keys("O_USER_MGT_SearchBox_XPATH", f"{r_gmail}")
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        return UserManagement(self.driver)

    def searchRole_admin(self):
        self.refresh()
        self.refresh()
        ele_XPATH = "//input[@placeholder='Search...']"
        self.send_keys("O_USER_MGT_SearchBox_XPATH", "admin")
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        return UserManagement(self.driver)

    def search_permission(self):
        self.refresh()
        self.refresh()
        ele_XPATH = "//input[@placeholder='Search...']"
        self.send_keys("O_USER_MGT_SearchBox_XPATH", "Delete items, Complete delete, Base delete, Delivery")
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        return UserManagement(self.driver)

    def search_active(self):
        self.refresh()
        self.refresh()
        ele_XPATH = "//input[@placeholder='Search...']"
        self.send_keys("O_USER_MGT_SearchBox_XPATH", "Active")
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        return UserManagement(self.driver)

    def countOfAdminUsers(self):
        self.select_100_entries()
        time.sleep(3)
        ele_XPATH = "//tr//td[.='admin']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        admin_count = len(ele)
        return admin_count

    def countOfPermission_Selected(self):
        self.select_100_entries()
        time.sleep(3)
        # count for following permissions (Delete items, Complete delete, Base delete, Delivery)
        ele_XPATH = "//td[contains(text(),'Delete items, Complete delete, Base delete, Delivery')]"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        p_count = len(ele)
        return p_count

    def countOfActive_status(self):
        self.select_100_entries()
        time.sleep(3)
        ele_XPATH = "//td[contains(text(),'Active')]"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        active_count = len(ele)
        return active_count

    def UserCount_forSearch(self):
        self.select_100_entries()
        time.sleep(3)
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def verifyInDescendingOrder_name(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_name(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickOnNameClm(self):
        self.click("O_USER_MGT_NAME_COLUMN_XPATH")
        return UserManagement(self.driver)

    def verifyInDescendingOrder_email(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_email(self):
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

    def clickOnEmailClm(self):
        self.click("O_USER_MGT_EMAIL_COLUMN_XPATH")
        return UserManagement(self.driver)

    def clickOnRoleClm(self):
        self.click("O_USER_MGT_ROLE_COLUMN_XPATH")
        return UserManagement(self.driver)

    def clickOnPermissionClm(self):
        self.click("O_USER_MGT_PERMISSION_COLUMN_XPATH")
        return UserManagement(self.driver)

    def clickOnActivationStatusClm(self):
        self.click("O_USER_MGT_ACTIVATION_STATUS_COLUMN_XPATH")
        return UserManagement(self.driver)

    def verifyInDescendingOrder_role(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_role(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_permission(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_permission(self):
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

    def verifyInDescendingOrder_ActivationStatus(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[5]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_ActivationStatus(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[5]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def addNewUser_contractorUser(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectContractorUser()
        return UserManagement(self.driver)

    def addNewUser_editorUser(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectEditorUser()
        return UserManagement(self.driver)

    def addNewUser_advertiserUser(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectAdvertiserUser()
        return UserManagement(self.driver)

    def addNewUser_customUser(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectCustomUser()
        return UserManagement(self.driver)

    def clickOnCheckbox1(self):
        self.click("O_ADD_USER_CHECKBOX1_XPATH")
        return UserManagement(self.driver)

    def clickOnCheckbox2(self):
        self.click("O_ADD_USER_CHECKBOX2_XPATH")
        self.click("O_ADD_USER_CHECKBOX4_XPATH")
        return UserManagement(self.driver)

    def clickOnCheckbox3(self):
        self.click("O_ADD_USER_CHECKBOX3_XPATH")
        return UserManagement(self.driver)

    def clickOnCheckbox4(self):
        self.click("O_ADD_USER_CHECKBOX4_XPATH")
        return UserManagement(self.driver)

    def isDisableCheckbox1(self):
        return self.is_disable("O_ADD_USER_CHECKBOX1_XPATH")

    def isDisableCheckbox2(self):
        return self.is_disable("O_ADD_USER_CHECKBOX2_XPATH")

    def isDisableCheckbox3(self):
        return self.is_disable("O_ADD_USER_CHECKBOX3_XPATH")

    def isDisableCheckbox4(self):
        return self.is_disable("O_ADD_USER_CHECKBOX4_XPATH")

    def getPermissions_CreatedUsers(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(0.5)
        self.send_keys("O_USER_MGT_SearchBox_XPATH", f"{r_gmail}")
        time.sleep(0.7)
        delete_BTN_XPATH = f"//tr//td[normalize-space()='{r_gmail}']//following-sibling::td[2]"
        permissions = self.driver.find_element(By.XPATH, delete_BTN_XPATH).text
        return permissions

    def isOptionsAvailableInDropdown_advertiserTag(self):
        options = self.find_elements("O_ADD_USER_Advertiser_tag_options_XPATH")
        options_count = len(options)
        if options_count > 0:
            return True
        else:
            return False

    def isOptionsAvailableInDropdown_customerRole(self):
        options = self.find_elements("O_ADD_USER_Customer_role_options_XPATH")
        options_count = len(options)
        if options_count > 0:
            return True
        else:
            return False

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "50")
        time.sleep(2)
        return UserManagement(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "100")
        time.sleep(2)
        return UserManagement(self.driver)

    def select_200_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "200")
        time.sleep(2)
        return UserManagement(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return UserManagement(self.driver)

    ####Sanity

    def verify_UM_BM_RM_options(self):
        ele = self.find_elements("O_UM_RM_BM_length_XPATH")
        ele = len(ele)
        return ele

    def verify_UM_option(self):
        ele = self.find_elements("O_UM_XPATH")
        ele = len(ele)
        return ele

    def verify_BM_option(self):
        ele = self.find_elements("O_BM_XPATH")
        ele = len(ele)
        return ele

    def verify_RM_option(self):
        ele = self.find_elements("O_RM_XPATH")
        ele = len(ele)
        return ele

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
        self.gotoUABaseMgmt_UMPage().createBaseUser().switchToBaseUser()
        return UserManagement(self.driver)

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("O_CURRENT_ACCOUNT_TYPE_XPATH")

    def gotoUABaseMgmt_UMPage(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return UserManagement(self.driver)

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
        return UserManagement(self.driver)

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
        return UserManagement(self.driver)

    def getCurrentBaseName(self):
        global BASENAME
        self.wait_for_visible_all_elements("O_CURRENT_BASE_NAME_XPATH")
        BASENAME = self.getText("O_CURRENT_BASE_NAME_XPATH")
        return BASENAME

    def switchToBaseUser(self):
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
        time.sleep(4)
        return UserManagement(self.driver)

    def CheckAndSwitchToBase(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        self.createBaseUser()
        useraccounttext = self.getText("N_UserAccountNameHeadOrBase_XPATH")
        if useraccounttext == "Head User":
            time.sleep(2)
            self.selenium_click("N_UserAccountNameHeadOrBase_XPATH")
            self.selenium_click("N_SwitchToBaseDashboard_XPATH")
            self.selenium_click("N_SearchBoxOfBaseUserBox_XPATH")
            self.send_keys("D_SearchSchedule_XPATH", BaseUserName)
            CreatededBase = self.driver.find_element(By.XPATH, f"//li[text()='{BaseUserName}']")
            CreatededBase.click()
            self.selenium_click("N_CommitOfSwitchToBase_XPATH")
            time.sleep(5)
        basename = self.getText("N_UserAccountName_CSS")
        if basename == BaseUserName:
            return True
        else:
            return False

    def CheckAndSwitchToHead(self):
        useraccounttext = self.getText("N_UserAccountNameHeadOrBase_XPATH")
        if useraccounttext == "Base User":
            self.selenium_click("N_UserAccountNameHeadOrBase_XPATH")
            self.selenium_click("N_SwitchToHeadAccount_XPATH")
            time.sleep(5)
        headname = self.getText("N_UserAccountName_CSS")
        return headname

    def ReturnHeadName(self):
        return self.getText("N_HeadAccountName_XPATH")

    def SearchBase(self):
        BaseUserName1 = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        self.wait_for_visible("O_AddBase_Icon_XPATH")
        self.click("O_AddBase_Icon_XPATH")
        self.wait_for_visible("O_EnterBaseUserName_XPATH")
        self.click("O_EnterBaseUserName_XPATH")
        self.send_keys("O_EnterBaseUserName_XPATH", BaseUserName1)
        self.click("O_AddScheduleButton_XPATH")
        time.sleep(3)
        self.refresh()
        self.selenium_click("N_SearchBase_XPATH")
        self.send_keys("N_SearchBase_XPATH", BaseUserName1)
        time.sleep(3)
        basecount = len(self.find_elements("N_NoOfBaseAccount_XPATH"))
        if basecount == 1:
            return True
        else:
            return False

    def SearchBaseWithRandomName(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        self.send_keys("N_SearchBase_XPATH", "98UYTREUIWEYRIUEWRWERREWR")
        if self.getText("N_NoMatchRecordFound_XPATH") == "No matching records found.":
            return True
        else:
            return False

    def verifyUserDeleted(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = f"//td[text()='{r_UserName}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        u_count = len(ele)
        if u_count == 0:
            return True
        else:
            return False



