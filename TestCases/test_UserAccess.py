import logging
import time

import allure

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import configReader
from Utilities.LogUtil import Logger
from pytest_check import check
import pytest
from utils.TC_UserAccess import TC_UserAccess

log = Logger(__name__, logging.INFO)

USER_MGT_PAGE_URL = configReader.getTestData("TestData", "O_USER_MGT_URL")
USER_MGT_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_USER_MGT_URL_PREPROD")
USER_MGT_PAGE_URL_SIT1 = configReader.getTestData("TestData", "O_USER_MGT_URL_SIT1")
USER_MGT_PAGE_URL_SIT2 = configReader.getTestData("TestData", "O_USER_MGT_URL_SIT2")
USER_MGT_SUBTITLE = configReader.getTestData("TestData", "O_USER_MGT_SUBTITLE")
USER_MGT_DuplicateMobileNum_Alert = configReader.getTestData("TestData", "O_USER_MGT_DuplicateMobileNum_Alert")
USER_MGT_DuplicateEmail_Alert = configReader.getTestData("TestData", "O_USER_MGT_DuplicateEMAIL_Alert")
ALL_PERMISSIONS_TEXT = configReader.getTestData("TestData", "O_ALL_PERMISSIONS_TEXT")
PERMISSIONS_1_3_TEXT = configReader.getTestData("TestData", "O_1_3_PERMISSIONS_TEXT")
PERMISSIONS_1_2_3_TEXT = configReader.getTestData("TestData", "O_1_2_3_permissions_TEXT")
PERMISSIONS_1_3_4_TEXT = configReader.getTestData("TestData", "O_1_3_4_PERMISSIONS_TEXT")
PERMISSIONS_1_TEXT = configReader.getTestData("TestData", "O_1_PERMISSIONS_TEXT")
PERMISSIONS_3_TEXT = configReader.getTestData("TestData", "O_3_PERMISSIONS_TEXT")

BASE_MGT_PAGE_URL = configReader.getTestData("TestData", "O_BASE_MGT_URL")
BASE_MGT_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_BASE_MGT_URL_PREPROD")
BASE_MGT_PAGE_URL_SIT1 = configReader.getTestData("TestData", "O_BASE_MGT_URL_SIT1")
BASE_MGT_PAGE_URL_SIT2 = configReader.getTestData("TestData", "O_BASE_MGT_URL_SIT2")
BASE_MGT_ACCOUNT_ID_COLOUR = configReader.getTestData("TestData", "O_BASE_MGT_ACCOUNT_ID_TEXT_COLOUR")
BASE_MGT_SCHEDULE_COLOUR = configReader.getTestData("TestData", "O_BASE_MGT_SCHEDULE_TEXT_COLOUR")

ROLE_MGT_PAGE_URL = configReader.getTestData("TestData", "O_ROLE_MGT_URL")
ROLE_MGT_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_ROLE_MGT_URL_PREPROD")
ROLE_MGT_PAGE_URL_SIT1 = configReader.getTestData("TestData", "O_ROLE_MGT_URL_SIT1")
ROLE_MGT_PAGE_URL_SIT2 = configReader.getTestData("TestData", "O_ROLE_MGT_URL_SIT2")
ROLE_MGT_SUBTITLE = configReader.getTestData("TestData", "O_ROLE_MGT_SUBTITLE")
ASSIGN_PERMISSION_WARN_MSG = configReader.getTestData("TestData", "O_ROLE_MGT_ASSIGN_PERMISSION_WARN_MSG")
ROLE_MGT_MATERIAL_PERMISSION_TEXT = configReader.getTestData("TestData", "O_ROLE_MGT_MATERIAL_PERMISSION_TEXT")


class TestUserAccess(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    @pytest.fixture(autouse=True)
    def test_switchtohead(self):
        homepage = HomePage(self.driver)
        homepage.checkForCurrentAccountTypeProd()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyUserMgt_UIUX(self):
        log.logger.info("TC" + str(TC_UserAccess(1)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            url = ele.verifyUserMgmtURL()
            if url == USER_MGT_PAGE_URL:
                assert url in USER_MGT_PAGE_URL
            elif url == USER_MGT_PAGE_URL_PREPROD:
                assert url in USER_MGT_PAGE_URL_PREPROD
            elif url == USER_MGT_PAGE_URL_SIT1:
                assert url in USER_MGT_PAGE_URL_SIT1
            elif url == USER_MGT_PAGE_URL_SIT2:
                assert url in USER_MGT_PAGE_URL_SIT2
            else:
                assert False
        with check:
            sTitle = ele.getSubTitleOfUserMgtPage()
            assert sTitle in "Add, delete, and modify users." or "Add, Delete and Modify User."
        with check:
            ele2 = ele.isVisibleAddUserOpt()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleSearchBar()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleNameCLM()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleEmailCLM()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleRoleCLM()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisiblePermissionCLM()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleActStatusCLM()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleActionCLM()
            if ele2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    # @pytest.mark.DEMO
    # @pytest.mark.FOCUSED
    # def test_verify_DuplicateMobileNum_Alert(self):
    #     log.logger.info("TC" + str(TC_UserAccess(7)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoUAUserMgmt().addNewUser()
    #         ele2 = ele.clickOnAddUser().enterUserName_additional(
    #         ).enterEmailAddress_additional().enterConfEmailAddress_additional().enterPhoneNumber_same()
    #         alert = ele2.clickOnAddOpt().verifyAlertDuplicateMobileNum()
    #         assert alert in USER_MGT_DuplicateMobileNum_Alert
    #     ele.deleteCreatedUser()
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verify_DuplicateEmail_Alert(self):
        log.logger.info("TC" + str(TC_UserAccess(8)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser()
            ele2 = ele.clickOnAddUser().enterUserName_additional(
            ).enterEmailAddress_same().enterConfEmailAddress_same().enterPhoneNumber_additional()
            alert = ele2.clickOnAddOpt().verifyAlertDuplicateEmail()
            assert alert in USER_MGT_DuplicateEmail_Alert
        #ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_verify_AddUserWithExistingName(self):
        log.logger.info("TC" + str(TC_UserAccess(9)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser()
            ele2 = ele.clickOnAddUser().enterUserName_same(
            ).enterEmailAddress_additional().enterConfEmailAddress_additional().enterPhoneNumber_additional()
            ele2.clickOnAddOpt().verifyUserWithExistingName()
            assert True
        ele.deleteCreatedUser()
        ele.deleteCreatedUser_additional()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verify_AddUser_CancelBtn(self):
        log.logger.info("TC" + str(TC_UserAccess(10)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            existing_user_count = ele.UserCount()
            ele.addNewUser_cancelBtn()
            current_user_count = ele.UserCount()
            if existing_user_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()


    # @pytest.mark.DEMO
    # @pytest.mark.FOCUSED
    # def test_userType_selection(self):
    #     log.logger.info("TC" + str(TC_UserAccess(11)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoUAUserMgmt().addNewUser_contractorUser().clickOnCheckbox2()
    #         chk1 = ele.isDisableCheckbox1()
    #         if chk1 == "True":
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         chk3 = ele.isDisableCheckbox3()
    #         if chk3 == "True":
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         ele2 = ele.clickOnAddOpt()
    #         all_permissions = ele2.getPermissions_CreatedUsers()
    #         assert all_permissions == ALL_PERMISSIONS_TEXT
    #     ele.deleteCreatedUser()
    #     self.driver.refresh()
    #     self.driver.refresh()
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoUAUserMgmt().addNewUser_editorUser()
    #         chk2 = ele.isDisableCheckbox2()
    #         if chk2 == "True":
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         chk4 = ele.isDisableCheckbox4()
    #         if chk4 == "True":
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         ele2 = ele.clickOnAddOpt()
    #         editor_permissions = ele2.getPermissions_CreatedUsers()
    #         assert editor_permissions == PERMISSIONS_1_3_TEXT
    #     ele.deleteCreatedUser()
    #     self.driver.refresh()
    #     self.driver.refresh()
    #     with check:
    #         Home = HomePage(self.driver)
    #         Home.gotoUAUserMgmt().addNewUser_advertiserUser().isOptionsAvailableInDropdown_advertiserTag()
    #         assert True
    #     self.driver.refresh()
    #     self.driver.refresh()
    #     with check:
    #         Home = HomePage(self.driver)
    #         Home.gotoUAUserMgmt().addNewUser_customUser().isOptionsAvailableInDropdown_customerRole()
    #         assert True
    #     self.driver.refresh()
    #     self.driver.refresh()


    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_searchFunction(self):
        log.logger.info("TC" + str(TC_UserAccess(12)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser().searchUserName()
            u_count = ele.UserCount_forSearch()
            if u_count == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_searchFunction_ByAllScenario(self):
        log.logger.info("TC" + str(TC_UserAccess(13)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser().searchUserName()
            u_count = ele.UserCount_forSearch()
            if u_count == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedUser()
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser().searchEmailAddress()
            u_count = ele.UserCount_forSearch()
            if u_count == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedUser()
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            admin_count = ele.countOfAdminUsers()
            ele.searchRole_admin()
            current_user_count = ele.UserCount_forSearch()
            if admin_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            admin_count = ele.countOfPermission_Selected()
            ele.search_permission()
            current_user_count = ele.UserCount_forSearch()
            if admin_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            admin_count = ele.countOfActive_status()
            ele.search_active()
            current_user_count = ele.UserCount_forSearch()
            if admin_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_searchFunction_ByUserName(self):
        log.logger.info("TC" + str(TC_UserAccess(14)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser().searchUserName()
            u_count = ele.UserCount_forSearch()
            if u_count == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_searchFunction_ByEmail(self):
        log.logger.info("TC" + str(TC_UserAccess(15)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser().searchEmailAddress()
            u_count = ele.UserCount_forSearch()
            if u_count == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_searchFunction_ByRole(self):
        log.logger.info("TC" + str(TC_UserAccess(16)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            admin_count = ele.countOfAdminUsers()
            ele.searchRole_admin()
            current_user_count = ele.UserCount_forSearch()
            if admin_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_searchFunction_ByPermission(self):
        log.logger.info("TC" + str(TC_UserAccess(17)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            admin_count = ele.countOfPermission_Selected()
            ele.search_permission()
            current_user_count = ele.UserCount_forSearch()
            print(current_user_count)
            print(admin_count)
            if admin_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_searchFunction_ByActivationStatus(self):
        log.logger.info("TC" + str(TC_UserAccess(18)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            admin_count = ele.countOfActive_status()
            ele.search_active()
            current_user_count = ele.UserCount_forSearch()
            if admin_count == current_user_count:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_sort_byName(self):
        log.logger.info("TC" + str(TC_UserAccess(19)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            r1 = ele.verifyInDescendingOrder_name()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnNameClm()
            r2 = ele2.verifyInAscendingOrder_name()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_sort_byEmail(self):
        log.logger.info("TC" + str(TC_UserAccess(20)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().clickOnEmailClm()
            r1 = ele.verifyInAscendingOrder_email()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnEmailClm()
            r2 = ele2.verifyInDescendingOrder_email()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_sort_byRole(self):
        log.logger.info("TC" + str(TC_UserAccess(21)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().clickOnRoleClm()
            r1 = ele.verifyInAscendingOrder_role()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnRoleClm()
            r2 = ele2.verifyInDescendingOrder_role()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_sort_byPermission(self):
        log.logger.info("TC" + str(TC_UserAccess(22)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().clickOnPermissionClm()
            r1 = ele.verifyInAscendingOrder_permission()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnPermissionClm()
            r2 = ele2.verifyInDescendingOrder_permission()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_sort_byActivationStatus(self):
        log.logger.info("TC" + str(TC_UserAccess(23)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().clickOnActivationStatusClm()
            r1 = ele.verifyInAscendingOrder_ActivationStatus()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnActivationStatusClm()
            r2 = ele2.verifyInDescendingOrder_ActivationStatus()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()


    def test_addUserPage_checkboxes_contractorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(26)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_contractorUser().clickOnCheckbox2()
            chk1 = ele.isDisableCheckbox1()
            if chk1 == "True":
                assert True
            else:
                assert False
        with check:
            chk3 = ele.isDisableCheckbox3()
            if chk3 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnAddOpt()
            all_permissions = ele2.getPermissions_CreatedUsers()
            assert all_permissions == ALL_PERMISSIONS_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    def test_addUserPage_checkboxes_editorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(27)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_editorUser()
            chk2 = ele.isDisableCheckbox2()
            if chk2 == "True":
                assert True
            else:
                assert False
        # with check:
        #     chk4 = ele.isDisableCheckbox4()
        #     if chk4 == "True":
        #         assert True
        #     else:
        #         assert False
        with check:
            ele2 = ele.clickOnAddOpt()
            editor_permissions = ele2.getPermissions_CreatedUsers()
            assert editor_permissions == PERMISSIONS_1_3_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()


    def test_addUserPage_checkboxes_advertiserUser(self):
        log.logger.info("TC" + str(TC_UserAccess(28)))
        with check:
            Home = HomePage(self.driver)
            Home.gotoUAUserMgmt().addNewUser_advertiserUser().isOptionsAvailableInDropdown_advertiserTag()
            assert True
        self.driver.refresh()
        self.driver.refresh()

    def test_addUserPage_checkboxes_customUser(self):
        log.logger.info("TC" + str(TC_UserAccess(29)))
        with check:
            Home = HomePage(self.driver)
            Home.gotoUAUserMgmt().addNewUser_customUser().isOptionsAvailableInDropdown_customerRole()
            assert True
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_20_50_100_200_500_entries(self):
        log.logger.info("TC" + str(TC_UserAccess(30)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            user20 = ele.UserCount()
            if user20 <= 20:
                assert True
            else:
                assert False
        with check:
            user50 = ele.select_50_entries().UserCount()
            if user50 <= 50:
                assert True
            else:
                assert False
        with check:
            user100 = ele.select_100_entries().UserCount()
            if user100 <= 100:
                assert True
            else:
                assert False
        # with check:
        #     user200 = ele.select_200_entries().UserCount()
        #     if user200 <= 200:
        #         assert True
        #     else:
        #         assert False
        # with check:
        #     user500 = ele.select_500_entries().UserCount()
        #     if user500 <= 500:
        #         assert True
        #     else:
        #         assert False
        self.driver.refresh()
        self.driver.refresh()

    def test_checkboxes_1_2_3_4_contractorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(32)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_contractorUser().clickOnCheckbox2().clickOnAddOpt()
            all_permissions = ele.getPermissions_CreatedUsers()
            assert all_permissions == ALL_PERMISSIONS_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    def test_checkboxes_1_2_3_contractorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(33)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_contractorUser().clickOnCheckbox2().clickOnCheckbox4().clickOnAddOpt()
            permissions_1_2_3 = ele.getPermissions_CreatedUsers()
            assert permissions_1_2_3 == PERMISSIONS_1_2_3_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    def test_checkboxes_1_3_4_contractorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(34)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_contractorUser().clickOnAddOpt()
            permissions_1_3_4 = ele.getPermissions_CreatedUsers()
            assert permissions_1_3_4 == PERMISSIONS_1_3_4_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    def test_checkboxes_1_3_editorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(35)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_editorUser().clickOnAddOpt()
            permissions_1_3 = ele.getPermissions_CreatedUsers()
            assert permissions_1_3 == PERMISSIONS_1_3_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    def test_checkboxes_1_editorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(36)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_editorUser().clickOnCheckbox3().clickOnAddOpt()
            permissions_1 = ele.getPermissions_CreatedUsers()
            assert permissions_1 == PERMISSIONS_1_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    def test_checkboxes_3_editorUser(self):
        log.logger.info("TC" + str(TC_UserAccess(37)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser_editorUser().clickOnCheckbox1().clickOnAddOpt()
            permissions_3 = ele.getPermissions_CreatedUsers()
            assert permissions_3 == PERMISSIONS_3_TEXT
        ele.deleteCreatedUser()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyBaseMgt_UIUX(self):
        log.logger.info("TC" + str(TC_UserAccess(38)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt()
            url = ele.verifyBaseMgmtURL()
            if url == BASE_MGT_PAGE_URL:
                assert url in BASE_MGT_PAGE_URL
            elif url == BASE_MGT_PAGE_URL_PREPROD:
                assert url in BASE_MGT_PAGE_URL_PREPROD
            elif url == BASE_MGT_PAGE_URL_SIT1:
                assert url in BASE_MGT_PAGE_URL_SIT1
            elif url == BASE_MGT_PAGE_URL_SIT2:
                assert url in BASE_MGT_PAGE_URL_SIT2
            else:
                assert False
        with check:
            ele1 = ele.isVisibleSearchBar()
            if ele1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.isVisibleTrashBtn()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele3 = ele.isVisibleAddNewBaseBtn()
            if ele3 == "True":
                assert True
            else:
                assert False
        with check:
            ele4 = ele.isVisibleAddNewBaseBtn_PlusIcon()
            if ele4 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_AddNewBaseAccount(self):
        log.logger.info("TC" + str(TC_UserAccess(39)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().addNewBaseAccount()
            baseAccountName = ele.isVisible_baseAccountName()
            baseAccountName = str(baseAccountName)
            if baseAccountName == "True":
                assert True
            else:
                assert False
        with check:
            acc_id_text_colour = ele.accountID_text_colour()
            assert acc_id_text_colour == BASE_MGT_ACCOUNT_ID_COLOUR
        with check:
            schedule_text_colour = ele.schedule_text_colour()
            assert schedule_text_colour == BASE_MGT_SCHEDULE_COLOUR
        ele.deleteCreatedBaseAccount()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_AddNewBaseAccount_CancelBtn(self):
        log.logger.info("TC" + str(TC_UserAccess(41)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt()
            default_accounts_count = ele.getBaseAccountsCount()
            ele2 = ele.addNewBaseAccount_CancelBtn()
            accounts_count = ele2.getBaseAccountsCount()
            assert default_accounts_count == accounts_count
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Edit_Delete_Opt_Availability(self):
        log.logger.info("TC" + str(TC_UserAccess(42)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().clickOn_FIRST_ACC_THREE_DOT()
            editBtn = ele.isVisibleEditBTN()
            if editBtn == "True":
                assert True
            else:
                assert False
        with check:
            deleteBtn = ele.isVisibleDeleteBTN()
            if deleteBtn == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_EditBaseAccount(self):
        log.logger.info("TC" + str(TC_UserAccess(43)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().addNewBaseAccount()
            acc_id = ele.get_accountID_ofCreatedBaseAccount()
            schedule_status = ele.get_schedule_status_ofCreatedBaseAccount()
            ele2 = ele.editCreatedBaseAccount()
            baseAccountName_edited = ele2.isVisible_baseAccountName_edited()
            baseAccountName_edited = str(baseAccountName_edited)
            if baseAccountName_edited == "True":
                assert True
            else:
                assert False
        with check:
            id_afterEdit = ele2.get_accountID_ofCreatedBaseAccount_afterEdit()
            assert acc_id in id_afterEdit
        with check:
            schedule_status_afterEdit = ele2.get_schedule_status_ofCreatedBaseAccount_afterEdit()
            assert schedule_status in schedule_status_afterEdit
        ele2.deleteCreatedBaseAccount_edited()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_deleteAccountFunction(self):
        log.logger.info("TC" + str(TC_UserAccess(44)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().addNewBaseAccount().deleteCreatedBaseAccount()
            ele2 = ele.verifyDeletedAccountOnBaseMgtPage()
            ele2 = str(ele2)
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele3 = ele.clickOnTrashBtn().verifyDeletedAccountOnTrashPage()
            ele3 = str(ele3)
            if ele3 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_deleteAccountFunction_restoreFromTrashPage(self):
        log.logger.info("TC" + str(TC_UserAccess(45)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().addNewBaseAccount().deleteCreatedBaseAccount()
            ele2 = ele.verifyDeletedAccountOnBaseMgtPage()
            ele2 = str(ele2)
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele3 = ele.clickOnTrashBtn().verifyDeletedAccountOnTrashPage()
            ele3 = str(ele3)
            if ele3 == "True":
                assert True
            else:
                assert False
        with check:
            ele4 = ele.restoreDeletedBaseAccount()
            ele7 = ele4.gotoUABaseMgmt_page().verifyRestoredAccountOnBaseMgtPage()
            ele7 = str(ele7)
            if ele7 == "True":
                assert True
            else:
                assert False
        ele4.deleteCreatedBaseAccount()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyRoleMgt_UIUX(self):
        log.logger.info("TC" + str(TC_UserAccess(46)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt()
            url = ele.verifyRoleMgmtURL()
            if url == ROLE_MGT_PAGE_URL:
                assert url in ROLE_MGT_PAGE_URL
            elif url == ROLE_MGT_PAGE_URL_PREPROD:
                assert url in ROLE_MGT_PAGE_URL_PREPROD
            elif url == ROLE_MGT_PAGE_URL_SIT1:
                assert url in ROLE_MGT_PAGE_URL_SIT1
            elif url == ROLE_MGT_PAGE_URL_SIT2:
                assert url in ROLE_MGT_PAGE_URL_SIT2
            else:
                assert False
        with check:
            sTitle = ele.getSubTitleOfRoleMgtPage()
            assert sTitle in "Add, remove, and modify roles." or "Add, Delete and Modify Role."
        with check:
            ele2 = ele.isVisibleSearchBar()
            if ele2 == "True":
                assert True
            else:
                assert False
        with check:
            ele3 = ele.isVisibleAddNewRoleBtn()
            if ele3 == "True":
                assert True
            else:
                assert False
        with check:
            ele4 = ele.isVisibleNameClm()
            if ele4 == "True":
                assert True
            else:
                assert False
        with check:
            ele5 = ele.isVisiblePermissionsClm()
            if ele5 == "True":
                assert True
            else:
                assert False
        with check:
            ele6 = ele.isVisibleUsersClm()
            if ele6 == "True":
                assert True
            else:
                assert False
        with check:
            ele7 = ele.isVisibleActionClm()
            if ele7 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    # def test_addNewRole_WithoutName(self):
    # log.logger.info("TC" + str(TC_UserAccess(48)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_UserCheckbox().clickOnPopup_AddBtn().getPOPUP()
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewRole_WithoutAnyPermission(self):
        log.logger.info("TC" + str(TC_UserAccess(49)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName().clickOnPopup_AddBtn()
            warn_msg = ele.getTextFromWarnMsg()
            assert warn_msg in ASSIGN_PERMISSION_WARN_MSG
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Role_available_for_selection_under_User_Management(self):
        log.logger.info("TC" + str(TC_UserAccess(50)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole()
            permissions_onRoleMgtPage = ele.getPermissions_CreatedRole()
            ele2 = ele.gotoUAUserMgmt_O().addNewUser_customUser().clickOnPermissions_link()
            permissions_onUserMgtPage = ele2.getPermissions_CreatedUsers_custom()
            permissions_onUserMgtPage = permissions_onUserMgtPage.replace(" ", "")
            permissions_onRoleMgtPage = permissions_onRoleMgtPage.replace(" ", "")
            assert permissions_onUserMgtPage in permissions_onRoleMgtPage
        ele2.gotoUAUserMgmt_O().deleteCreatedUser().gotoUARoleMgmt_O().deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_editRoleName(self):
        log.logger.info("TC" + str(TC_UserAccess(51)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().editRole()
            result = ele.verifyEditedName()
            if result == "True":
                assert True
            else:
                assert False
            ele.deleteEditedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editPermissions(self):
        log.logger.info("TC" + str(TC_UserAccess(52)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().editPermission()
            permissions_onRoleMgtPage = ele.getPermissions_CreatedRole()
            assert permissions_onRoleMgtPage in "View Media, Upload/Create/Edit Media, Move Media/Copy to Shared, Move to Trash, Restore Media, Delete Completely"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Search_ByNamePermissionUser(self):
        log.logger.info("TC" + str(TC_UserAccess(53)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().searchCreatedRole_byName()
            row_count = ele.getRowCount()
            if row_count == 1:
                assert True
            else:
                assert False
        with check:
            r1 = ele.verifyFirstRow_Name()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedRole()
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole()
            count_before_search = ele.getCount_customPermission()
            ele2 = ele.searchCreatedRole_byPermission()
            count_after_search = ele2.getCount_customPermission()
            assert count_before_search == count_after_search
        self.driver.refresh()
        ele.deleteCreatedRole()
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().verify_searchByUser1()
            if ele == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Search_ByName(self):
        log.logger.info("TC" + str(TC_UserAccess(55)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().searchCreatedRole_byName()
            row_count = ele.getRowCount()
            if row_count == 1:
                assert True
            else:
                assert False
        with check:
            r1 = ele.verifyFirstRow_Name()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Search_ByPermissions(self):
        log.logger.info("TC" + str(TC_UserAccess(56)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole()
            count_before_search = ele.getCount_customPermission()
            ele2 = ele.searchCreatedRole_byPermission()
            count_after_search = ele2.getCount_customPermission()
            assert count_before_search == count_after_search
        self.driver.refresh()
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Search_ByUser1(self):
        log.logger.info("TC" + str(TC_UserAccess(57)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().verify_searchByUser1()
            if ele == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_RoleMgt_sort_byName(self):
        log.logger.info("TC" + str(TC_UserAccess(58)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt()
            r1 = ele.verifyInDescendingOrder_name()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnNameClm()
            r2 = ele2.verifyInAscendingOrder_name()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_RoleMgt_sort_byPermission(self):
        log.logger.info("TC" + str(TC_UserAccess(59)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnPermissionClm()
            r1 = ele.verifyInAscendingOrder_permission()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnPermissionClm()
            r2 = ele2.verifyInDescendingOrder_permission()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_RoleMgt_sort_byUser(self):
        log.logger.info("TC" + str(TC_UserAccess(60)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnUserClm()
            r1 = ele.verifyInAscendingOrder_user()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOnUserClm()
            r2 = ele2.verifyInDescendingOrder_user()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_deleteRoleFunction(self):
        log.logger.info("TC" + str(TC_UserAccess(61)))
        with (check):
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().select_100_entries()
            count_before_delete = ele.getRoleAccountsCount()
            ele2 = ele.deleteCreatedRole()
            self.driver.refresh()
            self.driver.refresh()
            ele3 = ele2.select_100_entries()
            count_after_delete = ele3.getRoleAccountsCount()
            print(count_before_delete)
            print(count_after_delete)
            if count_after_delete == count_before_delete - 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_20_50_100_200_500_entries_RoleMGT_Page(self):
        log.logger.info("TC" + str(TC_UserAccess(62)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt()
            user20 = ele.getRoleAccountsCount()
            if user20 <= 20:
                assert True
            else:
                assert False
        with check:
            user50 = ele.select_50_entries().getRoleAccountsCount()
            if user50 <= 50:
                assert True
            else:
                assert False
        with check:
            user100 = ele.select_100_entries().getRoleAccountsCount()
            if user100 <= 100:
                assert True
            else:
                assert False
        # with check:
        #     user200 = ele.select_200_entries().getRoleAccountsCount()
        #     if user200 <= 200:
        #         assert True
        #     else:
        #         assert False
        # with check:
        #     user500 = ele.select_500_entries().getRoleAccountsCount()
        #     if user500 <= 500:
        #         assert True
        #     else:
        #         assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_userCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(64)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_UserCheckbox()
            result = ele.elementOfUserCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfUser_Sub1_Checkbox().is_selected()
            r2 = ele.elementOfUser_Sub2_Checkbox().is_selected()
            r3 = ele.elementOfUser_Sub3_Checkbox().is_selected()
            r4 = ele.elementOfUser_Sub4_Checkbox().is_selected()
            r5 = ele.elementOfUser_Sub5_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_UserCheckbox()
            r1 = ele2.elementOfUser_Sub1_Checkbox().is_selected()
            r2 = ele2.elementOfUser_Sub2_Checkbox().is_selected()
            r3 = ele2.elementOfUser_Sub3_Checkbox().is_selected()
            r4 = ele2.elementOfUser_Sub4_Checkbox().is_selected()
            r5 = ele2.elementOfUser_Sub5_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            if r1 == "False" and r2 == "False" and r3 == "False" and r4 == "False" and r5 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_userCheckbox_ViewUser(self):
        log.logger.info("TC" + str(TC_UserAccess(65)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserSub1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "View User"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_userCheckbox_CreateEditUser(self):
        log.logger.info("TC" + str(TC_UserAccess(66)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserSub2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Create/Edit User"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_userCheckbox_EditUpdateUser(self):
        log.logger.info("TC" + str(TC_UserAccess(67)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserSub3_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Edit/Update User"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_userCheckbox_DeleteUser(self):
        log.logger.info("TC" + str(TC_UserAccess(68)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserSub4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Delete User"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_userCheckbox_EnableDisableUser(self):
        log.logger.info("TC" + str(TC_UserAccess(69)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserSub5_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Enable/Disable User"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(70)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_MaterialCheckbox()
            result = ele.elementOfMaterialCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfMaterial_Opt1_Checkbox().is_selected()
            r2 = ele.elementOfMaterial_Opt2_Checkbox().is_selected()
            r3 = ele.elementOfMaterial_Opt3_Checkbox().is_selected()
            r4 = ele.elementOfMaterial_Opt4_Checkbox().is_selected()
            r5 = ele.elementOfMaterial_Opt5_Checkbox().is_selected()
            r6 = ele.elementOfMaterial_Opt6_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True" and r6 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_MaterialCheckbox()
            r1 = ele2.elementOfMaterial_Opt1_Checkbox().is_selected()
            r2 = ele2.elementOfMaterial_Opt2_Checkbox().is_selected()
            r3 = ele2.elementOfMaterial_Opt3_Checkbox().is_selected()
            r4 = ele2.elementOfMaterial_Opt4_Checkbox().is_selected()
            r5 = ele2.elementOfMaterial_Opt5_Checkbox().is_selected()
            r6 = ele2.elementOfMaterial_Opt6_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            if r1 == "False" and r2 == "False" and r3 == "False" and r4 == "False" and r5 == "False" and r6 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_ViewMaterials(self):
        log.logger.info("TC" + str(TC_UserAccess(71)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_MaterialOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "View Media"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_Upload_Create_Edit_Material(self):
        log.logger.info("TC" + str(TC_UserAccess(72)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_MaterialOpt2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Upload/Create/Edit Material" or "Upload/Create/Edit Media"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_Move_Material_Copy_To_Shared(self):
        log.logger.info("TC" + str(TC_UserAccess(73)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_MaterialOpt3_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move Media/Copy to Shared"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_Move_To_Trash(self):
        log.logger.info("TC" + str(TC_UserAccess(74)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_MaterialOpt4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move to Trash"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_Restore_Material(self):
        log.logger.info("TC" + str(TC_UserAccess(75)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_MaterialOpt5_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Restore Media"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialCheckbox_Delete_Completely(self):
        log.logger.info("TC" + str(TC_UserAccess(76)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_MaterialOpt6_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Delete Completely"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(77)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_ContentCheckbox()
            result = ele.elementOfContentCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfContent_Opt1_Checkbox().is_selected()
            r2 = ele.elementOfContent_Opt2_Checkbox().is_selected()
            r3 = ele.elementOfContent_Opt3_Checkbox().is_selected()
            r4 = ele.elementOfContent_Opt4_Checkbox().is_selected()
            r5 = ele.elementOfContent_Opt5_Checkbox().is_selected()
            r6 = ele.elementOfContent_Opt6_Checkbox().is_selected()
            r7 = ele.elementOfContent_Opt7_Checkbox().is_selected()
            r8 = ele.elementOfContent_Opt8_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            r7 = str(r7)
            r8 = str(r8)
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True" and r6 == "True" and r7 == "True" and r8 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_ContentCheckbox()
            r1 = ele2.elementOfContent_Opt1_Checkbox().is_selected()
            r2 = ele2.elementOfContent_Opt2_Checkbox().is_selected()
            r3 = ele2.elementOfContent_Opt3_Checkbox().is_selected()
            r4 = ele2.elementOfContent_Opt4_Checkbox().is_selected()
            r5 = ele2.elementOfContent_Opt5_Checkbox().is_selected()
            r6 = ele2.elementOfContent_Opt6_Checkbox().is_selected()
            r7 = ele.elementOfContent_Opt7_Checkbox().is_selected()
            r8 = ele.elementOfContent_Opt8_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            r7 = str(r7)
            r8 = str(r8)
            if r1 == "False" and r2 == "False" and r3 == "False" and r4 == "False" and r5 == "False" and r6 == "False" and r7 == "False" and r8 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_View_Content(self):
        log.logger.info("TC" + str(TC_UserAccess(78)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ContentOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "View Layout"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_Create_Edit_Content(self):
        log.logger.info("TC" + str(TC_UserAccess(79)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ContentOpt2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Create/Edit Layout"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_MoveContentCopyToShared(self):
        log.logger.info("TC" + str(TC_UserAccess(80)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ContentOpt3_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move Layout/Copy to Shared"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_MoveToTrash(self):
        log.logger.info("TC" + str(TC_UserAccess(81)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ContentOpt4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move to Trash"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_RestoreContent(self):
        log.logger.info("TC" + str(TC_UserAccess(82)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ContentOpt5_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Restore Layout"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_contentCheckbox_DeleteCompletely(self):
        log.logger.info("TC" + str(TC_UserAccess(83)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ContentOpt6_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Delete Completely"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(84)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_PlaylistCheckbox()
            result = ele.elementOfPlaylistCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfPlaylist_Opt1_Checkbox().is_selected()
            r2 = ele.elementOfPlaylist_Opt2_Checkbox().is_selected()
            r3 = ele.elementOfPlaylist_Opt3_Checkbox().is_selected()
            r4 = ele.elementOfPlaylist_Opt4_Checkbox().is_selected()
            r5 = ele.elementOfPlaylist_Opt5_Checkbox().is_selected()
            r6 = ele.elementOfPlaylist_Opt6_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True" and r6 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_PlaylistCheckbox()
            r1 = ele2.elementOfPlaylist_Opt1_Checkbox().is_selected()
            r2 = ele2.elementOfPlaylist_Opt2_Checkbox().is_selected()
            r3 = ele2.elementOfPlaylist_Opt3_Checkbox().is_selected()
            r4 = ele2.elementOfPlaylist_Opt4_Checkbox().is_selected()
            r5 = ele2.elementOfPlaylist_Opt5_Checkbox().is_selected()
            r6 = ele2.elementOfPlaylist_Opt6_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            if r1 == "False" and r2 == "False" and r3 == "False" and r4 == "False" and r5 == "False" and r6 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_View_Playlist(self):
        log.logger.info("TC" + str(TC_UserAccess(85)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlaylistOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "View Playlist"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_Create_Edit_Playlist(self):
        log.logger.info("TC" + str(TC_UserAccess(86)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlaylistOpt2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Create/Edit Playlist"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_MovePlaylist(self):
        log.logger.info("TC" + str(TC_UserAccess(87)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlaylistOpt3_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move Playlist" or "Move Playlist/Copy to Shared"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_MoveToTrash(self):
        log.logger.info("TC" + str(TC_UserAccess(88)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlaylistOpt4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move to Trash"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_RestorePlaylist(self):
        log.logger.info("TC" + str(TC_UserAccess(89)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlaylistOpt5_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Restore Playlist"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_playlistCheckbox_DeleteCompletely(self):
        log.logger.info("TC" + str(TC_UserAccess(90)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlaylistOpt6_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Delete Completely"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(91)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_ScheduleCheckbox()
            result = ele.elementOfScheduleCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfSchedule_Opt1_Checkbox().is_selected()
            r2 = ele.elementOfSchedule_Opt2_Checkbox().is_selected()
            r3 = ele.elementOfSchedule_Opt3_Checkbox().is_selected()
            r4 = ele.elementOfSchedule_Opt4_Checkbox().is_selected()
            r5 = ele.elementOfSchedule_Opt5_Checkbox().is_selected()
            r6 = ele.elementOfSchedule_Opt6_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True" and r6 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_ScheduleCheckbox()
            r1 = ele2.elementOfSchedule_Opt1_Checkbox().is_selected()
            r2 = ele2.elementOfSchedule_Opt2_Checkbox().is_selected()
            r3 = ele2.elementOfSchedule_Opt3_Checkbox().is_selected()
            r4 = ele2.elementOfSchedule_Opt4_Checkbox().is_selected()
            r5 = ele2.elementOfSchedule_Opt5_Checkbox().is_selected()
            r6 = ele2.elementOfSchedule_Opt6_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            if r1 == "False" and r2 == "False" and r3 == "False" and r4 == "False" and r5 == "False" and r6 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_View_Schedule(self):
        log.logger.info("TC" + str(TC_UserAccess(92)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "View Schedule"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_Create_Edit_Schedule(self):
        log.logger.info("TC" + str(TC_UserAccess(93)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Create/Edit Schedule"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_MoveSchedule(self):
        log.logger.info("TC" + str(TC_UserAccess(94)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt3_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move Schedule"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_MoveToTrash(self):
        log.logger.info("TC" + str(TC_UserAccess(95)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move to Trash"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_RestoreSchedule(self):
        log.logger.info("TC" + str(TC_UserAccess(96)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt5_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Restore Schedule"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_scheduleCheckbox_DeleteCompletely(self):
        log.logger.info("TC" + str(TC_UserAccess(97)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt6_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Delete Completely"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(98)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_DisplayAndDeliveryCheckbox()
            result = ele.elementOfDisplayAndDeliveryCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfDisplayAndDelivery_Opt1_Checkbox().is_selected()
            r2 = ele.elementOfDisplayAndDelivery_Opt2_Checkbox().is_selected()
            r3 = ele.elementOfDisplayAndDelivery_Opt3_Checkbox().is_selected()
            r4 = ele.elementOfDisplayAndDelivery_Opt4_Checkbox().is_selected()
            r5 = ele.elementOfDisplayAndDelivery_Opt5_Checkbox().is_selected()
            r6 = ele.elementOfDisplayAndDelivery_Opt6_Checkbox().is_selected()
            r7 = ele.elementOfDisplayAndDelivery_Opt7_Checkbox().is_selected()
            r8 = ele.elementOfDisplayAndDelivery_Opt8_Checkbox().is_selected()
            r9 = ele.elementOfDisplayAndDelivery_Opt9_Checkbox().is_selected()
            r10 = ele.elementOfDisplayAndDelivery_Opt9_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            r7 = str(r7)
            r8 = str(r8)
            r9 = str(r9)
            r10 = str(r10)
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True" and r6 == "True" and r7 == "True" and r8 == "True" and r9 == "True" and r10 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_DisplayAndDeliveryCheckbox()
            r1 = ele2.elementOfDisplayAndDelivery_Opt1_Checkbox().is_selected()
            r2 = ele2.elementOfDisplayAndDelivery_Opt2_Checkbox().is_selected()
            r3 = ele2.elementOfDisplayAndDelivery_Opt3_Checkbox().is_selected()
            r4 = ele2.elementOfDisplayAndDelivery_Opt4_Checkbox().is_selected()
            r5 = ele2.elementOfDisplayAndDelivery_Opt5_Checkbox().is_selected()
            r6 = ele2.elementOfDisplayAndDelivery_Opt6_Checkbox().is_selected()
            r7 = ele2.elementOfDisplayAndDelivery_Opt7_Checkbox().is_selected()
            r8 = ele2.elementOfDisplayAndDelivery_Opt8_Checkbox().is_selected()
            r9 = ele2.elementOfDisplayAndDelivery_Opt9_Checkbox().is_selected()
            r10 = ele.elementOfDisplayAndDelivery_Opt9_Checkbox().is_selected()
            r1 = str(r1)
            r2 = str(r2)
            r3 = str(r3)
            r4 = str(r4)
            r5 = str(r5)
            r6 = str(r6)
            r7 = str(r7)
            r8 = str(r8)
            r9 = str(r9)
            r10 = str(r10)
            if r1 == "False" and r2 == "False" and r3 == "False" and r4 == "False" and r5 == "False" and r6 == "False" and r7 == "False" and r8 == "False" and r9 == "False" and r10 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_View_Display(self):
        log.logger.info("TC" + str(TC_UserAccess(99)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "View Display"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_Create_Edit_Display(self):
        log.logger.info("TC" + str(TC_UserAccess(100)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Create/Edit Display"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_MoveScheduleAssignSchedule(self):
        log.logger.info("TC" + str(TC_UserAccess(101)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt3_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move Display/Assign Schedule"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_DisplayAndDeliveryCheckbox_MoveToTrash(self):
    #     log.logger.info("TC" + str(TC_UserAccess(102)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
    #         ).clickOn_DisplayAndDeliveryOpt4_Checkbox().clickOnPopup_AddBtn()
    #         permissions = ele.getPermissions_CreatedRole()
    #         assert permissions == "Move to Trash"
    #     ele.deleteCreatedRole()
    #     self.driver.refresh()
    #     self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_DisplayAndDeliveryCheckbox_RestoreDisplay(self):
    #     log.logger.info("TC" + str(TC_UserAccess(103)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
    #         ).clickOn_DisplayAndDeliveryOpt5_Checkbox().clickOnPopup_AddBtn()
    #         permissions = ele.getPermissions_CreatedRole()
    #         assert permissions == "Restore Display"
    #     ele.deleteCreatedRole()
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_DeleteCompletely(self):
        log.logger.info("TC" + str(TC_UserAccess(104)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Delete Completely"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_Deliver(self):
        log.logger.info("TC" + str(TC_UserAccess(105)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt5_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Deliver"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_Sync(self):
        log.logger.info("TC" + str(TC_UserAccess(106)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt6_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Sync"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DisplayAndDeliveryCheckbox_Reboot(self):
        log.logger.info("TC" + str(TC_UserAccess(107)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt7_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Reboot"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_PlayLogCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(108)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_PlayLogCheckbox()
            result = ele.elementOfPlayLogCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfPlayLog_Opt1_Checkbox().is_selected()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_PlayLogCheckbox()
            r1 = ele2.elementOfPlayLog_Opt1_Checkbox().is_selected()
            r1 = str(r1)
            if r1 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_PlayLogCheckbox_Generate_Played_Log_Reports(self):
        log.logger.info("TC" + str(TC_UserAccess(109)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_PlayLogOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Generate Played Log Reports"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_UserActivityLogCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(110)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_UserActivityLogCheckbox()
            result = ele.elementOfUserActivityLogCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfUserActivityLog_Opt1_Checkbox().is_selected()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_UserActivityLogCheckbox()
            r1 = ele2.elementOfUserActivityLog_Opt1_Checkbox().is_selected()
            r1 = str(r1)
            if r1 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_UserActivityLogCheckbox_Generate_Played_Log_Reports(self):
        log.logger.info("TC" + str(TC_UserAccess(111)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserActivityLogOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Generate User Activity Log Reports"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EmergencyAlertCheckbox_Checked_Unchecked(self):
        log.logger.info("TC" + str(TC_UserAccess(112)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().clickOn_EmergencyAlertLogCheckbox()
            result = ele.elementOfEmergencyAlertLogCheckbox().is_selected()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele.elementOfEmergencyAlertLog_Opt1_Checkbox().is_selected()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        with check:
            ele2 = ele.clickOn_EmergencyAlertLogCheckbox()
            r1 = ele2.elementOfEmergencyAlertLog_Opt1_Checkbox().is_selected()
            r1 = str(r1)
            if r1 == "False":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EmergencyAlertLogCheckbox_Generate_Played_Log_Reports(self):
        log.logger.info("TC" + str(TC_UserAccess(113)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_EmergencyAlertLogOpt1_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Emergency alert"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()

    #####

    def test_UserAccessDropdown(self):
        # log.logger.info("TC" + str(TC_UserAccess()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt()
            c1 = ele.verify_UM_option()
            c2 = ele.verify_BM_option()
            c3 = ele.verify_RM_option()
            r1 = c1 + c2 + c3
            if r1 == 3:
                assert True
            else:
                assert False
        with check:
            ele2 = ele.createBaseAccount_SwitchToBaseUser()
            c4 = ele2.verify_UM_option()
            c5 = ele2.verify_BM_option()
            c6 = ele2.verify_RM_option()
            r2 = c4 + c5 + c6
            if r2 == 1:
                assert True
            else:
                assert False
        ele.SwitchToHeadUser()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.SMOKE
    def test_UserAccess_Search(self):
        self.test_searchFunction_ByUserName()
        time.sleep(2)
        self.test_BaseMgt_Search()
        time.sleep(2)
        self.test_Search_ByName()


    def test_BaseMgt_Search(self):
        # log.logger.info("TC" + str(TC_UserAccess()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().addNewBaseAccount()
            baseAccountName = ele.isVisible_baseAccountName()
            baseAccountName = str(baseAccountName)
            if baseAccountName == "True":
                assert True
            else:
                assert False
        with check:
            r = ele.verifyBaseSearchBar()
            if r == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedBaseAccount()
        self.driver.refresh()
        self.driver.refresh()


    def test_deleteBaseAccount(self):
        # log.logger.info("TC" + str(TC_UserAccess()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUABaseMgmt().addNewBaseAccount()
            baseAccountName = ele.isVisible_baseAccountName()
            baseAccountName = str(baseAccountName)
            if baseAccountName == "True":
                assert True
            else:
                assert False
        with check:
            r = ele.deleteCreatedBaseAccount().verifyBaseSearchBar()
            if r == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()


    def test_addNewRole(self):
        # log.logger.info("TC" + str(TC_UserAccess()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserOptions().clickOnPopup_AddBtn()
            r = ele.verifyAddedRole()
            if r == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()


    def test_createCustomRole(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserSub2_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Create/Edit User"
        ele.deleteCreatedRole()
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_ScheduleOpt4_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Move to Trash"
        ele.deleteCreatedRole()
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_DisplayAndDeliveryOpt7_Checkbox().clickOnPopup_AddBtn()
            permissions = ele.getPermissions_CreatedRole()
            assert permissions == "Reboot"
        ele.deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()


    def test_NumberOfUserAssociatedWithSelectedRole(self):
        # log.logger.info("TC" + str(TC_UserAccess()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().gotoUAUserMgmt_O().addNewUser_customUser().gotoUARoleMgmt_O()
            r = ele.verifyUserCountAssociatedWithRole()
            if r == "1":
                assert True
            else:
                assert False
        ele.gotoUAUserMgmt_O().deleteCreatedUser().gotoUARoleMgmt_O().deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()


    def test_deleteRole(self):
        # log.logger.info("TC" + str(TC_UserAccess()))
        with (check):
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().clickOnAddNewRoleBtn().enterRoleName(
            ).clickOn_UserOptions().clickOnPopup_AddBtn()
            ele2 = ele.deleteCreatedRole()
            r = ele2.verifyAddedRole()
            if r == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.SMOKE
    @allure.description("Verify able to switch between head and base user")
    def test_HeadToBase_and_BaseToHead(self):
        with check:
            Home = HomePage(self.driver)
            Home.gotoDashboard().switchToHead()
            HeadName = Home.gotoUAUserMgmt().ReturnHeadName()
            assert Home.gotoUAUserMgmt().CheckAndSwitchToBase()
        with check:
            ActaulHeadname = Home.gotoUAUserMgmt().CheckAndSwitchToHead()
            assert ActaulHeadname == HeadName

    @pytest.mark.SMOKE
    @allure.description("Verify able to search the base")
    def test_SearchBase(self):
        with check:
            Home = HomePage(self.driver)
            Home.gotoDashboard().switchToHead()
            assert Home.gotoUAUserMgmt().SearchBase()
        with check:
            Home.gotoUAUserMgmt().SearchBaseWithRandomName()
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    @allure.description("Verify able to delete the user account")
    def test_UM_deleteUser(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUAUserMgmt().addNewUser().deleteCreatedUser()
            assert ele.verifyUserDeleted()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.SANITY
    @pytest.mark.FOCUSED
    @allure.description("Verify able to delete the role")
    def test_RM_deleteRole(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().select_100_entries()
            count_before_delete = ele.getRoleAccountsCount()
            ele2 = ele.deleteCreatedRole()
            self.driver.refresh()
            self.driver.refresh()
            ele3 = ele2.select_100_entries()
            count_after_delete = ele3.getRoleAccountsCount()
            print(count_before_delete)
            print(count_after_delete)
            if count_after_delete == count_before_delete - 1:
                assert True
            else:
                assert False
        with check:
            assert ele.verifyRoleDeleted()
        self.driver.refresh()
        self.driver.refresh()
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    @allure.description("Verify able to create custom user")
    def test_UM_createCustomUser(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoUARoleMgmt().addNewRole().gotoUAUserMgmt_O().addNewUser_customUser().gotoUARoleMgmt_O()
            r = ele.verifyUserCountAssociatedWithRole()
            if r == "1":
                assert True
            else:
                assert False
        with check:
            assert ele.gotoUAUserMgmt_O().verifyCustomUser()
        ele.deleteCreatedUser().gotoUARoleMgmt_O().deleteCreatedRole()
        self.driver.refresh()
        self.driver.refresh()