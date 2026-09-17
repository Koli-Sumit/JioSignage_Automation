import time
import logging

import pytest
from pytest_check import check
from TestCases.BaseTest import BaseTest
from Pages.HomePage import HomePage
from Utilities import configReader
from Utilities.LogUtil import Logger
from utils.TC_Displays import TC_Displays

log = Logger(__name__, logging.INFO)

# WARN_MSG_MISMATCH_PASSWORD = configReader.getTestData("TestData", "O_WARN_MSG_MISMATCH_PASSWORD")
WARN_MSG_LESS_CHAR_PASSWORD = configReader.getTestData("TestData", "O_WARN_MSG_LESS_CHAR_PASSWORD")
WARN_MSG_Only_letters = configReader.getTestData("TestData", "O_WARN_MSG_Only_letters")
WARN_MSG_Only_lettersNumbers = configReader.getTestData("TestData", "O_WARN_MSG_Only_lettersNumbers")
DISPLAY_PAGE_URL = configReader.getTestData("TestData", "O_DISPLAY_URL")
DISPLAY_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_DISPLAY_URL_PREPROD")
SCHEDULE_SUCCESSFULLY_UPDATED_POPUP = configReader.getTestData("TestData", "O_SCHEDULE_SUCCESSFULLY_UPDATED_POPUP")
###additional####Date:07-04-2024####
WARN_MSG_MISMATCH_PASSWORD = configReader.getTestData("TestData", "O_WARN_MSG_MISMATCH_SIT1_PASSWORD")


class TestDisplays(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    @pytest.fixture(autouse=True)
    def test_switchtohead(self):
        homepage = HomePage(self.driver)
        homepage.gotoContentDisplays().checkForCurrentAccountTypeProd()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_AddNewDisplayPopup_isVisible(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(1)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnAddNewDisplay()
            r1 = ele.isVisible_DisplayName()
            r2 = ele.isVisible_Password()
            r3 = ele.isVisible_ConfPassword()
            r4 = ele.isVisible_State()
            r5 = ele.isVisible_City()
            r6 = ele.isVisible_District()
            r7 = ele.isVisible_Pincode()
            r8 = ele.isVisible_StoreAddress()
            r9 = ele.isVisible_SyncRole()
            r10 = ele.isVisible_MobileNumber()
            if r1 == "True" and r2 == "True" and r3 == "True" and r4 == "True" and r5 == "True" and r6 == "True" and r7 == "True" and r8 == "True" and r9 == "True" and r10 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_AddNewDisplayPopup_CancelBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(3)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnAddNewDisplay().clickOnPopupCancelBtn_AddNewDisplay(
            ).isVisibleAddDisplayPopup()
            if ele == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_ShowPasswordOption(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(4)))
        with check:
            Home = HomePage(self.driver)
            textbox_type = Home.gotoContentDisplays().clickOnAddNewDisplay().enterDisplayPassword().clickOnShowPasswordBtn().isVisiblePassword()
            if textbox_type == "text":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_selectState_selectCity(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(5)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnAddNewDisplay().selectStateAs_Karnataka()
            selectedState = ele.getTextFromStateDropdown()
            if selectedState == "Karnataka":
                assert True
            else:
                assert False
        with check:
            selectedCity = ele.selectCityAs_Bengaluru().getTextFromSCityDropdown()
            if selectedCity == "Bengaluru":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_WarnMsg_MismatchPassword(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(6)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnAddNewDisplay().enterDisplayName().enterDisplayPassword(
            ).enterDisplayPassword_mismatch().clickOnPopupAddBtn()
            # warnMsg = ele.getTextFromWarningMsg()
            warnMsg = ele.returnpasswordmissmatchtext()
            # print(warnMsg)
            assert warnMsg == WARN_MSG_MISMATCH_PASSWORD
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_WarnMsg_PasswordMin6Character(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(7)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnAddNewDisplay().enterDisplayName().enterDisplayPassword_4char(
            ).enterDisplayPassword_Conf_4char().clickOnPopupAddBtn()
            # warnMsg = ele.getTextFromWarningMsg()
            warnMsg = ele.returnmin6charwarningmsg()
            # print(warnMsg)
            assert warnMsg == WARN_MSG_LESS_CHAR_PASSWORD
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_WarnMsg_District_Numbers(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(8)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnAddNewDisplay().enterDisplayName().enterDisplayPassword(
            ).enterDisplayPassword_Conf().enterDisplayDistrict_numbers().clickOnPopupAddBtn()
            warnMsg = ele.getTextFromWarningMsg()
            assert warnMsg == WARN_MSG_Only_letters

        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_AddTagPopup_CancelBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(10)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().goToAddNewTagPage_ForCreatedDisplay()
            result = ele.isVisibleAddTagPopup()
            self.driver.refresh()
            ele.deleteCreatedDisplay()
            if result == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_RemoveTagPopup_CancelBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(14)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().goToRemoveTagPage_ForCreatedDisplay()
            result = ele.isVisibleAddTagPopup()
            self.driver.refresh()
            ele.deleteCreatedDisplay()
            if result == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeleteCompletelyPopup_CancelBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(16)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().goToDeleteCompletelyPage_ForCreatedDisplay()
            self.driver.refresh()
            ele.deleteCreatedDisplay_Cancel()
            assert ele.verifyDisplayNotDeleted()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_CreateFolderScreen(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(18)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().goToCreateFolderPage__()
            result = ele.isVisibleCreateFolderPopup()
            self.driver.refresh()
            if result == 2:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_CreateFolder_EnterAllCharacter(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(19)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewFolder()
            r1 = ele.verifyFolderIsCreated()
            if r1 == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_CreateFolder_WarnMsg_SpecialCharacter(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(20)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewFolder_SplChar()
            # warnMsg = ele.getTextFromWarningMsg()
            warnMsg = ele.returninvalidfolderstring()
            assert warnMsg == WARN_MSG_Only_lettersNumbers
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_CreateFolderScreen_CancelBtn(self):
        log.logger.info("TC" + str(TC_Displays(22)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().goToCreateFolderPage()
            result = ele.isVisibleCreateFolderPopup()
            self.driver.refresh()
            if result == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_CreateFolderScreen_X_Btn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(23)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().goToCreateFolderPage_X_BTN()
            result = ele.isVisibleCreateFolderPopup()
            self.driver.refresh()
            if result == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_HeadFolderBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(24)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().selectFirstFolderFromDropdown().clickOnHeadFolderBtn()
            time.sleep(2)
            url = ele.get_current_url()
            if url == DISPLAY_PAGE_URL:
                assert url in DISPLAY_PAGE_URL
            elif url == DISPLAY_PAGE_URL_PREPROD:
                assert url in DISPLAY_PAGE_URL_PREPROD
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_selectFolderFromDropdown(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(25)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().selectFirstFolderFromDropdown()
            time.sleep(2)
            result = ele.verifyFolderIsSelected()
            if result == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_selectFolderFromDropdown_BySearchBar(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(26)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewFolder()
            time.sleep(3)
            self.driver.refresh()
            self.driver.refresh()
            time.sleep(1)
            ele.selectFirstFolderFromDropdown_SearchBar()
            time.sleep(2)
            result = ele.verifyFolderIsSelected()
            if result == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_RadioBTNs(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(27)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn()
            r1 = ele.isVisibleDeliverInstantlyRadioBTNs()
            if r1 == 4:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_SearchBar(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(28)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().clickOnDeliverInstantlyBtn()
            r1 = ele.searchCreatedDisplayNameOnDeliverInstantlyPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_CheckBox(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(29)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().clickOnDeliverInstantlyBtn()
            r1 = ele.selectCheckboxOfCreatedDisplayNameOnDeliverInstantlyPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_MultipleCheckBoxes(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(30)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn()
            r1 = ele.selectMultipleCheckboxesOfCreatedDisplayNameOnDeliverInstantlyPage()
            if r1 == 2:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_Folder_SearchBar(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(31)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Folder()
            r1 = ele.searchCreatedFolderNameOnDeliverInstantlyPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_Folder_CheckBox(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(32)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Folder()
            r1 = ele.selectCheckboxOfCreatedFolderNameOnDeliverInstantlyPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_Folder_MultipleCheckBoxes(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(33)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Folder()
            r1 = ele.selectMultipleCheckboxesOfCreatedFolderNameOnDeliverInstantlyPage()
            if r1 == 2:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_Base_SearchBar(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(34)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Base()
            r1 = ele.searchCreatedBaseNameOnDeliverInstantlyPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_Base_CheckBox(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(35)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Base()
            r1 = ele.selectCheckboxOfCreatedBaseNameOnDeliverInstantlyPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_Base_MultipleCheckBoxes(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(36)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Base()
            r1 = ele.selectMultipleCheckboxesOfCreatedBaseNameOnDeliverInstantlyPage()
            if r1 == 2:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_DeliverInstantlyPage_Tag_SearchBar(self):
    #     self.driver.refresh()
    #     log.logger.info("TC" + str(TC_Displays(37)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Tag()
    #         r1 = ele.searchCreatedTagNameOnDeliverInstantlyPage()
    #         if r1 == 1:
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_DeliverInstantlyPage_Tag_CheckBox(self):
    #     self.driver.refresh()
    #     log.logger.info("TC" + str(TC_Displays(38)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Tag()
    #         r1 = ele.selectCheckboxOfCreatedTagNameOnDeliverInstantlyPage()
    #         if r1 == 1:
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_DeliverInstantlyPage_Tag_MultipleCheckBoxes(self):
    #     self.driver.refresh()
    #     log.logger.info("TC" + str(TC_Displays(39)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOnRadioBtn_Tag()
    #         r1 = ele.selectMultipleCheckboxesOfCreatedTagNameOnDeliverInstantlyPage()
    #         if r1 == 2:
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_X_ICON_SELECTED_DISPLAY(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(44)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn()
            r1 = ele.clickOn_X_ICON_SELECTED_DISPLAY()
            if r1 == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverInstantlyPage_X_ICON(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(45)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDeliverInstantlyBtn().clickOn_X_ICON_DELIVER_INSTANTLY_PAGE()
            time.sleep(2)
            r1 = ele.isVisibleDeliverInstantlyPage()
            if r1 == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_DisplayDetailsPage(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(61)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            time.sleep(3)
            r1 = ele.verifyDisplayDetailsPage()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.gotoContentDisplays_Page().deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    # NA as per new UI changes 7.0 to 7.1
    # def test_DisplayDetailsPage_closeBtn(self):
    #     self.driver.refresh()
    #     log.logger.info("TC" + str(TC_Displays(62)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentDisplays().createNewDisplay()
    #         time.sleep(2)
    #         r1 = ele.verifyDisplayDetailsPage_closeBtn()
    #         if r1 == 0:
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     ele.deleteCreatedDisplay()
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_UpdateSchedule(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(63)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnSchedule()
            successful_msg = ele.getTextFromSuccessPopup()
            assert successful_msg == SCHEDULE_SUCCESSFULLY_UPDATED_POPUP
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_MoveToDisplay_closeBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(65)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            r = ele.verifyMoveToDisplayPage_closeBtn()
            if r == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_closeBtn(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(67)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            r = ele.verifyEditDisplayPage_closeBtn()
            if r == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeDisplayName(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(68)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditDisplayName()
            r = ele.verifyEditedDisplayName()
            if r == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay_edited()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeStateName(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(69)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditStateName()
            r = ele.getStateName()
            if r == "Karnataka":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeCityName(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(70)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditCityName()
            r = ele.getCityName()
            print(r)
            if r == "Bengaluru":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeDistrictName(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(71)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditDistrictName()
            r = ele.getDistrictName()
            if r == "Thane":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangePincodeName(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(72)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditPincode()
            r = ele.getPincode()
            if r == "400001":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeStoreAddress(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(73)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditStoreAddress()
            r = ele.getStoreAddress()
            if r == "Sample Store Address":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeSyncRole(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(74)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditSyncRole()
            r = ele.getSyncRole()
            if r == "Slave":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_EditDisplayPage_ChangeMobileNumber(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(75)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().EditMobileNumber()
            r = ele.getMobileNumber()
            if r == "1234567890":
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_TagListPage(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(79)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            r = ele.verifyTagListPage()
            if r == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_bulkCreate(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(80)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().bulkUpload_Display()
            time.sleep(2)
            self.driver.refresh()
            r = ele.verifyDisplayAddedFromBulkUpload()
            r = str(r)
            if r == "True":
                assert True
            else:
                assert False
        time.sleep(2)
        self.driver.refresh()
        ele.deleteCreatedDisplay_byBulkUpload()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Sort_byDisplayID(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(81)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays()
            dec = ele.verifyInDescendingOrder_id()
            dec = str(dec)
            if dec == "True":
                assert True
            else:
                assert False
        with check:
            asc = ele.clickOnDisplayID_Clm().verifyInAscendingOrder_id()
            asc = str(asc)
            if asc == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_sort_byDisplayName(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(82)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().gotouseraccess()
            ele1 = ele.createbaseuser().switchtobaseuser()
            time.sleep(2)
            ele2 = ele1.gotodisplaysBase().verifycreatedisplayBase()
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().clickOnDisplayNAME_Clm()
            dec = ele.verifyInAscendingOrder_Displayname()
            dec = str(dec)
            if dec == "True":
                assert True
            else:
                assert False
        with check:
            asc = ele.clickOnDisplayNAME_Clm().verifyInDescendingOrder_Displayname()
            asc = str(asc)
            if asc == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()
        ele3 = ele.gotodisplaysBase().DeleteCreatedDisplay()
        time.sleep(2)
        ele4 = ele3.SwitchtoHeaduser()
        ele5 = ele4.gotouseraccess().deletecreatedbaseuser()

    @pytest.mark.FOCUSED
    def test_searchBar_functionality(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(83)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            r = ele.searchDisplayName()
            if r == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_searchBar_display_nameAndId(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(84)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().getCreatedDisplayId()
            r1 = ele.searchDisplayName()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            self.driver.refresh()
            r2 = ele.searchDisplayId()
            if r2 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_20_50_100_200_500_entriesOfDisplays(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(85)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().select_20_entries()
            user20 = ele.UserCount()
            assert user20 <= 20, f"User count {user20} is not 20"
        with check:
            user50 = ele.select_50_entries().UserCount()
            assert user50 <= 50, f"User count {user50} is not 500"
        with check:
            user100 = ele.select_100_entries().UserCount()
            assert user100 <= 100, f"User count {user100} is not 100"
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

    # def test_alert(self):
    #     # log.logger.info("TC" + str(TC_Displays(62)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentDisplays().createNewDisplay()

    # self.driver.switch_to.alert()
    # alert = self.driver.execute_script("return window.alert.toString();")
    # print(alert)
    # alert = self.driver.switch_to.alert

    # time.sleep(2)
    # r1 = ele.verifyDisplayDetailsPage_closeBtn()
    # if r1 == 0:
    #     assert True
    # else:
    #     assert False
    # self.driver.refresh()
    # ele.deleteCreatedDisplay()
    # self.driver.refresh()
    # self.driver.refresh()

###added##
    @pytest.mark.FOCUSED
    def test_movedisplay(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(86)))
        ###64
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewFolder()
            time.sleep(2)
            ele1 = Home.gotoContentDisplays().createNewDisplay().searchDisplayNamecraeted().clickonfirstcheckbox().clickmore()
            ele2 = ele1.clickonMove().selectcreatedfolder()
            time.sleep(2)
            ele3 = Home.gotoContentDisplays()
            time.sleep(2)
            ele4 = ele3.selectFirstFolderFromDropdown_SearchBar()
            time.sleep(2)
            ele5 = ele4.verifydisplaynameinfolder()
        self.driver.refresh()
        self.driver.refresh()

    # def test_searchFunctionality(self):
    #     ##83
    #     Home = HomePage(self.driver)
    #     ele = Home.gotoContentDisplays().createNewDisplay()
    #     time.sleep(2)
    #     ele1 = ele.searchDisplayNamecraeted().verifydisplaynameinfolder()

    @pytest.mark.FOCUSED
    def test_Editdisplay(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(87)))
        ###39
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            ele1= ele.EditDisplayNameedit().gettextofeditdisplay()
        self.driver.refresh()
        ele.deleteCreatedDisplay_edited()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_migratedisplay(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(88)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            # ele1 = Home.gotouseraccess()
            ele1= Home.gotoContentDisplays().gotouseraccess()
            time.sleep(2)
            ele2 = ele1.createbaseuser()
            time.sleep(2)
            ele3 = Home.gotoContentDisplays().searchDisplayNamecraeted().clickonmigrate()
            ele4 = ele3.selectbasetomigratedisplay()
            time.sleep(3)
            Home.gotoContentDisplays().switchtobaseuser()
            time.sleep(3)
            ele5 = Home.gotoContentDisplays().searchDisplayNamecraeted().verifydisplaynameinfolder()
            time.sleep(3)
            Home.gotoContentDisplays().deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_deleteschedulefordisplay(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(89)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().gotoContentSchedules().addSchedule()
            time.sleep(1)
            self.driver.refresh()
            ele1 = Home.gotoContentDisplays().createNewDisplay()
            time.sleep(2)
            ele2 = ele1.searchDisplayNamecraeted()
            time.sleep(1)
            ele3 = ele2.clickonfirstcheckbox()
            time.sleep(1)
            ele4 = ele3.clickonscheduleicon().Assignschedule()
            time.sleep(1)
            ele5 = ele4.searchDisplayNamecraeted().readScheuleofdisplay()
            time.sleep(2)
            ele6 = ele5.gotoContentSchedules().searchcreatedschedule().deletecreatedschedule()
            time.sleep(2)
            ele7 = Home.gotoContentDisplays().searchDisplayNamecraeted()
            ele8 = ele7.readScheuleofdisplay()
            if ele5 == ele8:
                assert False
            else:
                assert True
            Home.gotoContentDisplays().deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_changepasswordfordisplay(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Displays(90)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            time.sleep(2)
            ele1 = ele.searchDisplayNamecraeted()
            time.sleep(1)
            ele2= ele1.clickoneditpassword()
            time.sleep(1)
            ele3 = ele2.enterDisplayPasswordnew()
            time.sleep(1)
            ele4=ele3.enterDisplayPassword_Confnew()
            time.sleep(1)
            ele5=ele4.clickonsavepassword()
            ele6=ele5.gettextofeditdisplay().printtext()
            if ele6 == "Display updated successfully. ×":
                assert True
            else:
                assert False
        ele5.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

###Sanity


    def test_addNewDisplay(self):
        self.driver.refresh()
        # log.logger.info("TC" + str(TC_Displays()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay()
            r1 = ele.verifyAddedDisplay()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    def test_deleteAddedDisplay(self):
        self.driver.refresh()
        # log.logger.info("TC" + str(TC_Displays()))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().deleteCreatedDisplay()
            r1 = ele.verifyAddedDisplay()
            if r1 == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_DeleteCompletelyDisplay(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().goToDeleteCompletelyPage_ForCreatedDisplay()
            self.driver.refresh()
            ele.deleteCreatedDisplay()
            assert ele.verifyDisplayDeleted()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.SANITY
    @pytest.mark.FOCUSED
    def test_scheduleDisplayHistory(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().gotoContentSchedules().addSchedule()
            time.sleep(1)
            self.driver.refresh()
            ele1 = Home.gotoContentDisplays().createNewDisplay().clickonfirstcheckbox().clickonscheduleicon().Assignschedule()
            assert ele1.verifyScheduleHistory()
        self.driver.refresh()
        Home.gotoContentDisplays().deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_displayLogs_CreatedDisplay(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele1 = Home.gotoContentDisplays().createNewDisplay()
            self.driver.refresh()
            assert ele1.verifyDisplayLogs()
        self.driver.refresh()
        Home.gotoContentDisplays().deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.SANITY
    @pytest.mark.FOCUSED
    def test_Display_moveDisplay(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewFolder()
            ele1 = Home.gotoContentDisplays().createNewDisplay().searchDisplayNamecraeted().clickonfirstcheckbox().clickmore().clickonMove().selectcreatedfolder()
            ele2 = Home.gotoContentDisplays().selectFirstFolderFromDropdown_SearchBar()
            assert ele2.verifyDisplayInfolder()
        self.driver.refresh()
        Home.gotoContentDisplays().deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_Display_AddTag(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().addTagToCreateDisplay()
            result = ele.verifyAddedTag()
            self.driver.refresh()
            ele.deleteCreatedDisplay()
            if result:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()
#added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_Display_RemoveTag(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentDisplays().createNewDisplay().addTagToCreateDisplay()
            assert ele.verifyAddedTag()
        with check:
            self.driver.refresh()
            assert ele.removeTagToCreateDisplay().verifyRemovedTag()
        ele.deleteCreatedDisplay()
        self.driver.refresh()
        self.driver.refresh()

    # @pytest.mark.FOCUSED
    # @pytest.mark.SANITY
    # def test_raiseTicket(self):
    #     with check:
    #         homepage = HomePage(self.driver)
    #         homepage.gotoContentDisplays().switchToHead()
    #         self.driver.refresh()
    #         db = homepage.gotoContentDisplays()
    #         db.goToRaiseTicket().fillRaiseTicketInfoAndSubmit()
    #         assert db.verifyTicketIsRaised(), "Not able to raise ticket"
