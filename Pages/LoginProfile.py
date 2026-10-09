import secrets
import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage, retry_action
from Utilities import configReader

EMAIL = configReader.getTestData("TestData", "O_LOGIN_EMAIL")
PASSWORD = configReader.getTestData("TestData", "O_LOGIN_PASSWORD")


class LoginProfile(BasePage):

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

    def isVisible_SignAge_Logo(self):
        return self.is_visible("O_SIGNAGELOGO_SIGNINPAGE_XPATH")

    def textOfLogin(self):
        return self.getText("O_LOGIN_TEXT_XPATH")

    def textOfEmail(self):
        return self.getText("O_EMAIL_TEXT_XPATH")

    def textOfPassword(self):
        return self.getText("O_PASSWORD_TEXT_XPATH")

    def textOfGetOTPBTN(self):
        return self.getText("O_GetOTP_BTN_XPATH")

    def isVisible_EnterEmail_Textbox(self):
        return self.is_visible("O_ENTER_EMAIL_XPATH")

    def isVisible_EnterPassword_Textbox(self):
        return self.is_visible("O_ENTER_PASSWORD_XPATH")

    def Enter_EmailAddress(self):
        global r_gmail
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(6))
        r_gmail = f"{r_text}@gmail.com"
        self.send_keys("O_ENTER_EMAIL_XPATH", r_gmail)
        return LoginProfile(self.driver)

    def Enter_Password(self):
        global r_pass
        r_pass = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        self.send_keys("O_ENTER_PASSWORD_XPATH", r_pass)
        return LoginProfile(self.driver)

    def Enter_EmailAddress_testAccount(self):
        self.clear("O_ENTER_EMAIL_XPATH")
        self.send_keys("O_ENTER_EMAIL_XPATH", EMAIL)
        return LoginProfile(self.driver)

    def Enter_Password_testAccount(self):
        self.send_keys("O_ENTER_PASSWORD_XPATH", PASSWORD)
        return LoginProfile(self.driver)

    def verifyEmailAddressField(self):
        mail = self.find_element("O_ENTER_EMAIL_XPATH").get_attribute('value')
        if mail == r_gmail:
            return True
        else:
            return False

    def verifyPasswordField(self):
        password = self.find_element("O_ENTER_PASSWORD_XPATH").get_attribute('value')
        if password == r_pass:
            return True
        else:
            return False

    def verifyShowPasswordBtn(self):
        self.click("O_SHOW_PASSWORD_BTN_XPATH")
        return self.find_element("O_ENTER_PASSWORD_XPATH").get_attribute('type')

    def clickOnRememberMeBtn(self):
        self.click("O_REMEMBER_ME_BTN_XPATH")
        return LoginProfile(self.driver)

    def clickOnGetOTPBtn(self):
        self.click("O_GET_OTP_XPATH")
        return LoginProfile(self.driver)

    def getValueOfUserNameField(self):
        return self.find_element("O_PROFILE_USERNAME_XPATH").get_attribute('value')

    def getValueOfEmailField(self):
        return self.find_element("O_PROFILE_EMAIL_XPATH").get_attribute('value')

    def getValueOfPhoneNumberField(self):
        return self.find_element("O_PROFILE_PHONE_NUMBER_XPATH").get_attribute('value')

    def getValueOfPasswordField(self):
        return self.find_element("O_PROFILE_PASSWORD_XPATH").get_attribute('value')

    def clickOnEditUNameBtn(self):
        edit = self.find_element("O_EDIT_UNAME_BTN_XPATH")
        self.driver.execute_script("arguments[0].click();", edit)
        # self.click("O_EDIT_UNAME_BTN_XPATH")
        # time.sleep(20)
        return LoginProfile(self.driver)

    def editUserName(self):
        self.clear("O_USER_NAME_TEXTBOX_XPATH")
        global r_edited_UserName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
        r_edited_UserName = f"Test Account {r_text}"
        self.send_keys("O_USER_NAME_TEXTBOX_XPATH", r_edited_UserName)
        return LoginProfile(self.driver)

    def clickOnEditUNameSaveBtn(self):
        time.sleep(2)
        self.wait_for_visible("O_EDIT_UNAME_SAVE_BTN_XPATH")
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        # ele =self.is_visible("O_POPUP_XPATH")
        # print(ele)
        # self.wait_for_visible_all_elements("O_POPUP_XPATH")
        # print(len(self.find_elements("O_POPUP_XPATH")))
        # time.sleep(2)
        return LoginProfile(self.driver)

    # def getTextFromPopup(self):
    #     return self.getText("oooooo_XPATH")
    def clickOnEditUNameCancelBtn(self):
        self.click("O_EDIT_UNAME_CANCEL_BTN_XPATH")
        return LoginProfile(self.driver)

    def verifyEditedUserName(self):
        time.sleep(2)
        ele = self.find_element("O_PROFILE_USERNAME_XPATH").get_attribute('value')
        if ele == r_edited_UserName:
            return True
        else:
            return False

    # def getAlertValue(self):
    #     time.sleep(1)
    #     textq = self.getText("O_ALERT_CSS")
    #     print(textq)

    def isVisibleEDITNAME_POPUP_HEADING(self):
        time.sleep(2)
        return self.is_visible("O_EDITNAME_POPUP_HEADING_XPATH")

    def clickOnEditPhoneNumBtn(self):
        self.selenium_click("O_PHONE_NUM_BTN_XPATH")
        return LoginProfile(self.driver)

    def editPhoneNum(self):
        self.clear("O_PHONE_NUM_TEXTBOX_XPATH")
        global r_edited_phoneNum
        r_edited_phoneNum = ''.join(
            secrets.choice('1234567890') for _ in range(10))
        self.send_keys("O_PHONE_NUM_TEXTBOX_XPATH", r_edited_phoneNum)
        return LoginProfile(self.driver)

    def clickOnEditPhoneNumSaveBtn(self):
        self.click("O_EDIT_UNAME_SAVE_BTN_XPATH")
        return LoginProfile(self.driver)

    def clickOnEditPhoneNumCancelBtn(self):
        self.click("O_EDIT_UNAME_CANCEL_BTN_XPATH")
        return LoginProfile(self.driver)

    def verifyEditedPhoneNum(self):
        time.sleep(2)
        ele = self.find_element("O_PROFILE_PHONE_NUMBER_XPATH").get_attribute('value')
        if ele == r_edited_phoneNum:
            return True
        else:
            return False

    def clickOnEditPhoneNum_X_Btn(self):
        self.click("O_PHONE_NUM_X_BTN_XPATH")
        return LoginProfile(self.driver)

    def clickOnEditPasswordBtn(self):
        self.selenium_click("O_EDIT_PASSWORD_BTN_XPATH")
        time.sleep(2)
        return LoginProfile(self.driver)

    def getTitleOfServicePlanPage(self):
        return self.getText("O_SERVICE_PLAN_TEXT_XPATH")

    def EnterCurrentPassword(self):
        CurrentPassword = configReader.getTestData("TestData", "Password")
        self.send_keys("N_Current_Password_Field_XPATH", CurrentPassword)
        return LoginProfile(self.driver)

    def enterNewPassword(self):
        self.send_keys("O_NEW_PASS_XPATH","Tgehrn@8584")
        return LoginProfile(self.driver)

    def enterNewPassword_Conf(self):
        self.send_keys("O_NEW_PASS_Conf_XPATH","Teflkjfj@359")
        return LoginProfile(self.driver)

    def getTextFromAlertMsg(self):
        return self.getText("O_alert_XPATH")

#####additonal case######

    def gettextexisitingusername(self):
        self.wait_for_visible("O_USER_NAME_TEXTBOX_XPATH")
        global existusern
        existusern =self.find_element("O_USER_NAME_TEXTBOX_XPATH").get_attribute('value')
        return existusern

    def gettextexistingphonenumber(self):
        self.wait_for_visible("O_PHONE_NUM_TEXTBOX_XPATH")
        global existphoneno
        existphoneno = self.find_element("O_PHONE_NUM_TEXTBOX_XPATH").get_attribute('value')
        print(existphoneno)
        return existphoneno

    def verifyEdited_UserNameadded(self):
        time.sleep(2)
        self.wait_for_visible("O_PROFILE_USERNAME_XPATH")
        ele = self.find_element("O_PROFILE_USERNAME_XPATH").get_attribute('value')
        if ele == r_edited_UserName:
            assert True
        else:
            assert False


    def verifyEditedPhoneNumadded(self):
        time.sleep(2)
        ele = self.find_element("O_PROFILE_PHONE_NUMBER_XPATH").get_attribute('value')
        if ele == r_edited_phoneNum:
            assert True
        else:
            assert False

    def renterusername(self):
        self.wait_for_visible("O_USER_NAME_TEXTBOX_XPATH")
        self.clear("O_USER_NAME_TEXTBOX_XPATH")
        self.send_keys("O_USER_NAME_TEXTBOX_XPATH",existusern)
        return LoginProfile(self.driver)
    def renterphoneno(self):
        self.wait_for_visible("O_PHONE_NUM_TEXTBOX_XPATH")
        self.clear("O_PHONE_NUM_TEXTBOX_XPATH")
        self.send_keys("O_PHONE_NUM_TEXTBOX_XPATH",existphoneno)
        return LoginProfile(self.driver)

    def verifyrenteredusername(self):
        time.sleep(2)
        self.wait_for_visible("O_USER_NAME_TEXTBOX_XPATH")
        renteredu = self.find_element("O_USER_NAME_TEXTBOX_XPATH").get_attribute('value')
        if renteredu == existusern:
            assert True
        else:
            assert False

    def verifyrenteredPhonename(self):
        self.wait_for_visible("O_PROFILE_PHONE_NUMBER_XPATH")
        phonep = self.find_element("O_PROFILE_PHONE_NUMBER_XPATH").get_attribute('value')
        if phonep == existphoneno:
            assert True
        else:
            assert False