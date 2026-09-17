import json
import time
import logging

import pytest

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import configReader
from pytest_check import check
from Utilities.LogUtil import Logger
from utils.TC_LoginProfile import TC_LoginProfile

log = Logger(__name__, logging.INFO)

SIGNIN_PAGE_URL = configReader.getTestData("TestData", "O_SignInPage_URL")
SIGNIN_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_SignInPage_URL_PREPROD")
SIGNIN_PAGE_URL_SIT1 = configReader.getTestData("TestData", "sit1_sign_in_url")
SIGNIN_PAGE_URL_SIT2 = configReader.getTestData("TestData", "sit2_sign_in_url")
SIGNIN_PAGE_LOGIN_TEXT = configReader.getTestData("TestData", "O_Login_Text")
SIGNIN_PAGE_EMAIL_TEXT = configReader.getTestData("TestData", "O_Email_Text")
SIGNIN_PAGE_PASSWORD_TEXT = configReader.getTestData("TestData", "O_Password_Text")
SIGNIN_PAGE_GetOTP_TEXT = configReader.getTestData("TestData", "O_GetOTP_Text")
DASHBOARD_PAGE_URL = configReader.getTestData("TestData", "O_DashBoard_URL")
DASHBOARD_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_DashBoard_URL_PREPROD")
DASHBOARD_PAGE_URL_SIT1 = configReader.getTestData("TestData", "dashboard_sit1_url")
DASHBOARD_PAGE_URL_SIT2 = configReader.getTestData("TestData", "dashboard_sit2_url")
PROFILE_PAGE_URL = configReader.getTestData("TestData", "O_ProfilePage_URL")
PROFILE_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_ProfilePage_URL_PREPROD")
PROFILE_PAGE_URL_SIT1 = configReader.getTestData("TestData", "N_ProfilePage_URL_sit1")
PROFILE_PAGE_URL_SIT2 = configReader.getTestData("TestData", "N_ProfilePage_URL_sit2")
SERVICE_PLAN_TEXT = configReader.getTestData("TestData", "O_SERVICE_PLAN_TEXT")
SERVICE_PLAN_PAGE_URL = configReader.getTestData("TestData", "O_SERVICE_PLAN_URL")
SERVICE_PLAN_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_SERVICE_PLAN_URL_PREPROD")
SERVICE_PLAN_PAGE_URL_SIT1 = configReader.getTestData("TestData", "service_plan_sit1_url")
SERVICE_PLAN_PAGE_URL_SIT2 = configReader.getTestData("TestData", "service_plan_sit2_url")

HELP_PAGE_URL = configReader.getTestData("TestData", "O_HELP_PAGE_URL")
ALERT_FOR_TWO_DIFFERENT_PASSWORD = configReader.getTestData("TestData", "O_ALERT_FOR_TWO_DIFFERENT_PASSWORD")


class TestLoginAndProfile(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_SignIn_Page(self):
        log.logger.info("TC" + str(TC_LoginProfile(1)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.goToSignInPage()
            url = ele.get_current_url()
            if url == SIGNIN_PAGE_URL:
                assert url in SIGNIN_PAGE_URL
            elif url == SIGNIN_PAGE_URL_PREPROD:
                assert url in SIGNIN_PAGE_URL_PREPROD
            elif url == SIGNIN_PAGE_URL_SIT1:
                assert url in SIGNIN_PAGE_URL_SIT1
            elif url == SIGNIN_PAGE_URL_SIT2:
                assert url in SIGNIN_PAGE_URL_SIT2
            else:
                assert False
        with check:
            ele.isVisible_SignAge_Logo()
            assert True
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_SignIn_Page_UIUX(self):
        log.logger.info("TC" + str(TC_LoginProfile(2)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.goToSignInPage()
            url = ele.get_current_url()
            if url == SIGNIN_PAGE_URL:
                assert url in SIGNIN_PAGE_URL
            elif url == SIGNIN_PAGE_URL_PREPROD:
                assert url in SIGNIN_PAGE_URL_PREPROD
            elif url == SIGNIN_PAGE_URL_SIT1:
                assert url in SIGNIN_PAGE_URL_SIT1
            elif url == SIGNIN_PAGE_URL_SIT2:
                assert url in SIGNIN_PAGE_URL_SIT2
            else:
                assert False
        with check:
            ele.isVisible_SignAge_Logo()
            assert True
        with check:
            Login = ele.textOfLogin()
            assert Login == SIGNIN_PAGE_LOGIN_TEXT
        with check:
            Email = ele.textOfEmail()
            assert Email == SIGNIN_PAGE_EMAIL_TEXT
        with check:
            Password = ele.textOfPassword()
            assert Password == SIGNIN_PAGE_PASSWORD_TEXT
        with check:
            GetOTP = ele.textOfGetOTPBTN()
            assert GetOTP == SIGNIN_PAGE_GetOTP_TEXT
        with check:
            ele.isVisible_EnterEmail_Textbox()
            assert True
        with check:
            ele.isVisible_EnterPassword_Textbox()
            assert True
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_SignIn_Page_JioSignageLogo(self):
        log.logger.info("TC" + str(TC_LoginProfile(3)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.goToSignInPage()
            url = ele.get_current_url()
            if url == SIGNIN_PAGE_URL:
                assert url in SIGNIN_PAGE_URL
            elif url == SIGNIN_PAGE_URL_PREPROD:
                assert url in SIGNIN_PAGE_URL_PREPROD
            elif url == SIGNIN_PAGE_URL_SIT1:
                assert url in SIGNIN_PAGE_URL_SIT1
            elif url == SIGNIN_PAGE_URL_SIT2:
                assert url in SIGNIN_PAGE_URL_SIT2
            else:
                assert False
        with check:
            ele.isVisible_SignAge_Logo()
            assert True
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_EmailTextbox(self):
        log.logger.info("TC" + str(TC_LoginProfile(4)))
        with check:
            Home = HomePage(self.driver)
            Home.goToSignInPage().Enter_EmailAddress().verifyEmailAddressField()
            assert True
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit1.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit2.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_PasswordTextbox(self):
        log.logger.info("TC" + str(TC_LoginProfile(5)))
        with check:
            Home = HomePage(self.driver)
            Home.goToSignInPage().Enter_Password().verifyPasswordField()
            assert True
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit1.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit2.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_PasswordTextbox_showPasswordBtn(self):
        log.logger.info("TC" + str(TC_LoginProfile(6)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.goToSignInPage().Enter_Password().verifyShowPasswordBtn()
            assert ele == "text"
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit1.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit2.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_RememberMeOption(self):
        log.logger.info("TC" + str(TC_LoginProfile(7)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.goToSignInPage().Enter_EmailAddress().Enter_Password().clickOnRememberMeBtn().clickOnGetOTPBtn()
            self.driver.refresh()
            ele.verifyEmailAddressField()
            assert True
        with check:
            ele.verifyPasswordField()
            assert True
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit1.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()

        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit2.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_LoginWithValidCredential(self):
        log.logger.info("TC" + str(TC_LoginProfile(9)))
        with check:
            Home = HomePage(self.driver)
            url = Home.get_current_url()
            if url == DASHBOARD_PAGE_URL:
                assert url in DASHBOARD_PAGE_URL
            elif url == DASHBOARD_PAGE_URL_PREPROD:
                assert url in DASHBOARD_PAGE_URL_PREPROD
            elif url == DASHBOARD_PAGE_URL_SIT1:
                assert url in DASHBOARD_PAGE_URL_SIT1
            elif url == DASHBOARD_PAGE_URL_SIT2:
                assert url in DASHBOARD_PAGE_URL_SIT2
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_back_button_fromOTP_page(self):
        log.logger.info("TC" + str(TC_LoginProfile(12)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.goToSignInPage().Enter_EmailAddress_testAccount().Enter_Password_testAccount().clickOnGetOTPBtn()
            time.sleep(5)
            self.driver.back()
            url = ele.get_current_url()
            if url == SIGNIN_PAGE_URL:
                assert url in SIGNIN_PAGE_URL
            elif url == SIGNIN_PAGE_URL_PREPROD:
                assert url in SIGNIN_PAGE_URL_PREPROD
            elif url == SIGNIN_PAGE_URL_SIT1:
                assert url in SIGNIN_PAGE_URL_SIT1
            elif url == SIGNIN_PAGE_URL_SIT2:
                assert url in SIGNIN_PAGE_URL_SIT2
            else:
                assert False
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit1.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit2.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.driver.refresh()



    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_viewProfile(self):
        log.logger.info("TC" + str(TC_LoginProfile(14)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            url = ele.get_current_url()
            if url == PROFILE_PAGE_URL:
                assert url in PROFILE_PAGE_URL
            elif url == PROFILE_PAGE_URL_PREPROD:
                assert url in PROFILE_PAGE_URL_PREPROD
            elif url == PROFILE_PAGE_URL_SIT1:
                assert url in PROFILE_PAGE_URL_SIT1
            elif url == PROFILE_PAGE_URL_SIT2:
                assert url in PROFILE_PAGE_URL_SIT2
            else:
                assert False
        with check:
            UName = ele.getValueOfUserNameField()
            if UName:
                assert True
            else:
                assert False
        with check:
            Email = ele.getValueOfEmailField()
            if Email:
                assert True
            else:
                assert False
        with check:
            PhoneNum = ele.getValueOfPhoneNumberField()
            if PhoneNum:
                assert True
            else:
                assert False
        with check:
            Password = ele.getValueOfPasswordField()
            if Password:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    # def test_editUserName(self):
    #     # log.logger.info("TC" + str(TC_LoginProfile(15)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         Home.O_clickOnViewProfile().clickOnEditUNameBtn().editUserName().clickOnEditUNameSaveBtn().verifyEditedUserName()
    #         assert True
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editUserName_SAVE_CANCEL_BTN(self):
        log.logger.info("TC" + str(TC_LoginProfile(16)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            ele.clickOnEditUNameBtn().editUserName().clickOnEditUNameSaveBtn().verifyEditedUserName()
            assert True, "Save button is not working"
        with check:
            ele2 = ele.clickOnEditUNameBtn().clickOnEditUNameCancelBtn().isVisibleEDITNAME_POPUP_HEADING()
            if ele2 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editPhoneNumber_SAVE_CANCEL_BTN(self):
        log.logger.info("TC" + str(TC_LoginProfile(18)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            ele.clickOnEditPhoneNumBtn().editPhoneNum().clickOnEditPhoneNumSaveBtn().verifyEditedPhoneNum()
            assert True, "Save button is not working"
        with check:
            ele2 = ele.clickOnEditPhoneNumBtn().clickOnEditPhoneNumCancelBtn().isVisibleEDITNAME_POPUP_HEADING()
            if ele2 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editPhoneNumber_X_BTN(self):
        log.logger.info("TC" + str(TC_LoginProfile(19)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            ele2 = ele.clickOnEditPhoneNumBtn().clickOnEditPhoneNum_X_Btn().isVisibleEDITNAME_POPUP_HEADING()
            if ele2 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_twoDifferentPassword_alert(self):
        log.logger.info("TC" + str(TC_LoginProfile(21)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            alert_msg = ele.clickOnEditPasswordBtn().EnterCurrentPassword().enterNewPassword().enterNewPassword_Conf().clickOnEditPhoneNumSaveBtn().getTextFromAlertMsg()
            assert alert_msg in ALERT_FOR_TWO_DIFFERENT_PASSWORD
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editPassword_X_BTN(self):
        log.logger.info("TC" + str(TC_LoginProfile(23)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            ele2 = ele.clickOnEditPasswordBtn().clickOnEditPhoneNum_X_Btn().isVisibleEDITNAME_POPUP_HEADING()
            if ele2 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_ViewServicePlan(self):
        log.logger.info("TC" + str(TC_LoginProfile(24)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewServicePlan()
            url = ele.get_current_url()
            if url == SERVICE_PLAN_PAGE_URL:
                assert url in SERVICE_PLAN_PAGE_URL
            elif url == SERVICE_PLAN_PAGE_URL_PREPROD:
                assert url in SERVICE_PLAN_PAGE_URL_PREPROD
            elif url == SERVICE_PLAN_PAGE_URL_SIT1:
                assert url in SERVICE_PLAN_PAGE_URL_SIT1
            elif url == SERVICE_PLAN_PAGE_URL_SIT2:
                assert url in SERVICE_PLAN_PAGE_URL_SIT2
            else:
                assert False
        with check:
            title = ele.getTitleOfServicePlanPage()
            assert title in SERVICE_PLAN_TEXT
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Help_Page(self):
        log.logger.info("TC" + str(TC_LoginProfile(25)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnHelp()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = ele.get_current_url()
            assert url in HELP_PAGE_URL
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_LogoutOption(self):
        log.logger.info("TC" + str(TC_LoginProfile(26)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_ClickOnLogout()
            url = ele.get_current_url()
            if url == SIGNIN_PAGE_URL:
                assert url in SIGNIN_PAGE_URL
            elif url == SIGNIN_PAGE_URL_PREPROD:
                assert url in SIGNIN_PAGE_URL_PREPROD
            elif url == SIGNIN_PAGE_URL_SIT1:
                assert url in SIGNIN_PAGE_URL_SIT1
            elif url == SIGNIN_PAGE_URL_SIT2:
                assert url in SIGNIN_PAGE_URL_SIT2
            else:
                assert False
        with check:
            ele.isVisible_SignAge_Logo()
            assert True
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_prod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/users/sign_in")
            with open("JioSignAge_cookies_preprod.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit1.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/users/sign_in")
            with open("JioSignage_cookies_sit2.json", 'r') as file:
                cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
        self.driver.refresh()
        self.driver.refresh()



        ####additional TC#########

    @pytest.mark.FOCUSED
    def test_verifyeditusername(self):
        log.logger.info("TC" + str(TC_LoginProfile(27)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            ele1 = ele.clickOnEditUNameBtn()
            time.sleep(2)
            ele2=ele1.gettextexisitingusername()
            time.sleep(1)
            self.driver.refresh()
            ele3 =ele.clickOnEditUNameBtn().editUserName().clickOnEditUNameSaveBtn().verifyEdited_UserNameadded()
            time.sleep(2)
            ele4 = Home.O_clickOnViewProfile()
            # ele5 = ele4.clickOnEditUNameBtn()
            # ele6 = ele.gettextexisitingusername()
            self.driver.refresh()
            ele7 = ele4.clickOnEditUNameBtn().renterusername().clickOnEditUNameSaveBtn()
            time.sleep(3)
            ele8 = ele7.clickOnEditUNameBtn().verifyrenteredusername()
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editphonenumber(self):
        log.logger.info("TC" + str(TC_LoginProfile(28)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.O_clickOnViewProfile()
            ele1 = ele.clickOnEditPhoneNumBtn()
            time.sleep(2)
            ele2 = ele1.gettextexistingphonenumber()
            self.driver.refresh()
            ele3 = ele.clickOnEditPhoneNumBtn().editPhoneNum().clickOnEditPhoneNumSaveBtn().verifyEditedPhoneNumadded()
            time.sleep(2)
            ele4 = Home.O_clickOnViewProfile()
            # ele5 = ele4.clickOnEditUNameBtn()
            # ele6 = ele.gettextexisitingusername()
            self.driver.refresh()
            ele7 = ele4.clickOnEditPhoneNumBtn().renterphoneno().clickOnEditPhoneNumSaveBtn()
            time.sleep(2)
            ele8 = ele7.clickOnEditPhoneNumBtn().verifyrenteredPhonename()
            self.driver.refresh()
            self.driver.refresh()

