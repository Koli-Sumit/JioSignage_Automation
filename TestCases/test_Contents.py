import logging
import time

import allure
import pytest

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from pytest_check import check

from Utilities import configReader
from Utilities.LogUtil import Logger

from utils.TC_Content import TC_Content

from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__, logging.INFO)

SPL_CHAR_WARN_MSG = configReader.getTestData("TestData", "O_CONTENT_SPL_CHAR_WARN_SIT1_MSG")
HORIZONTAL_DD = configReader.getTestData("TestData", "O_HORIZONTAL_DD")
VERTICAL_DD = configReader.getTestData("TestData", "O_VERTICAL_DD")
WARN_MSG_Only_lettersNumbers = configReader.getTestData("TestData", "O_WARN_MSG_Only_lettersNumbers")
env = configReader.getTestData("TestData", "Environment")
CA_send_text = configReader.getTestData("TestData", "D_RequestApproval_CA_text")


class TestContents(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_addNewContent_Option(self):
        with check:
            log.logger.info("TC" + str(TC_Content(1)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().createBaseAccount_SwitchToBaseUser().stayOnBaseAccount().gotoContentContents_Page()
            result = ele.verifyTooltipOfAddNewMaterialBtn()
            result = str(result)
            if result == "True":
                assert True
            else:
                assert False
        with check:
            result2 = ele.verify_AddNewMaterial_OSD()
            if result2 == 1:
                assert True
            else:
                assert False
        #self.driver.refresh()
        #self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent(self):
        with check:
            log.logger.info("TC" + str(TC_Content(2)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        #self.driver.refresh()
        #self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_addNewContent_SpecialChar(self):
        with check:
            log.logger.info("TC" + str(TC_Content(3)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_SpecialChar()
            warnMsg = ele.getTextFromWarnMsg()
            assert warnMsg == SPL_CHAR_WARN_MSG
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_VerticalHorizontal_option(self):
        with check:
            log.logger.info("TC" + str(TC_Content(4)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            r1 = ele.verifyHorizontalOption()
            assert r1 == HORIZONTAL_DD
        with check:
            r2 = ele.verifyVerticalOption()
            assert r2 == VERTICAL_DD
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_ResolutionDropdown_HorizontalSelected(self):
        with check:
            log.logger.info("TC" + str(TC_Content(5)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            r1 = ele.verifyDDOption_Horizontal()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_ResolutionDropdown_VerticalSelected(self):
        with check:
            log.logger.info("TC" + str(TC_Content(6)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            r1 = ele.verifyDDOption_Vertical()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_AddNewContent_CustomResolution(self):
        with check:
            log.logger.info("TC" + str(TC_Content(7)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            r1 = ele.verify_OtherResolution()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyAddedContent()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyEditContentPageTitle()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_slideOptions(self):
        with check:
            log.logger.info("TC" + str(TC_Content(8)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_VerifySlides()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_addNewContent_BlankSlide(self):
        with check:
            log.logger.info("TC" + str(TC_Content(9)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyBlankSlide()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()


    # # # This feature  (Document option during layout creation)is removed
    # # @pytest.mark.FOCUSED
    # # def test_addNewContent_TemplateForDocument(self):
    # #     with check:
    # #         log.logger.info("TC" + str(TC_Content(10)))
    # #         Home = HomePage(self.driver)
    # #         ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_TemplateForDocument()
    # #         r1 = ele.verifyAddedContent()
    # #         if r1 == 1:
    # #             assert True
    # #         else:
    # #             assert False
    # #     with check:
    # #         r2 = ele.verifyEditContentPageTitle()
    # #         if r2 == 1:
    # #             assert True
    # #         else:
    # #             assert False
    # #     with check:
    # #         r3 = ele.verifyBlankSlide()
    # #         if r3 == 0:
    # #             assert True
    # #         else:
    # #             assert False
    # #     ele.createdContentMoveToTrash()
    # #     self.driver.refresh()
    # #     self.driver.refresh()
    #
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_addNewContent_TemplateForPlayingVideo(self):
        with check:
            log.logger.info("TC" + str(TC_Content(17)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_TemplateForPlayingVideo()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyBlankSlide()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_TemplateForSplitScreen(self):
        with check:
            log.logger.info("TC" + str(TC_Content(21)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_TemplateForSplitScreen()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyBlankSlide()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_10_Opt(self):
        with check:
            log.logger.info("TC" + str(TC_Content(22)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_2()
            opt2 = ele.verify_Split_Opt_2()
            if opt2 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_3()
            opt3 = ele.verify_Split_Opt_3()
            if opt3 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_4()
            opt4 = ele.verify_Split_Opt_4()
            if opt4 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_5()
            opt5 = ele.verify_Split_Opt_5()
            if opt5 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_6()
            opt6 = ele.verify_Split_Opt_6()
            if opt6 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_7()
            opt7 = ele.verify_Split_Opt_7()
            if opt7 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_8()
            opt8 = ele.verify_Split_Opt_8()
            if opt8 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_9()
            opt9 = ele.verify_Split_Opt_9()
            if opt9 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_10()
            opt10 = ele.verify_Split_Opt_10()
            if opt10 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_EditOpt(self):
        with check:
            log.logger.info("TC" + str(TC_Content(26)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            r = ele.verifyEditButton_SplitScreen()
            if r == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()
    #
    # # def test_addNewContent_TemplateForSplitScreen_DeleteOpt(self):
    # #     with check:
    # #         log.logger.info("TC" + str(TC_Content(29)))
    # #         Home = HomePage(self.driver)
    # #         ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
    # #         ele.addNewContent_TemplateForSplitScreen_Opt_1()
    # #         opt1 = ele.verify_Split_Opt_1()
    # #         if opt1 == 1:
    # #             assert True
    # #         else:
    # #             assert False
    # #         time.sleep(1)
    # #     with check:
    # #         r1 = ele.verifyDeleteButton_SplitScreen()
    # #         if r1 == 0:
    # #             assert True
    # #         else:
    # #             assert False
    # #     with check:
    # #         r2 = ele.verifyAddSlide_afterDelete()
    # #         if r2 == 1:
    # #             assert True
    # #         else:
    # #             assert False
    # #     ele.createdContentMoveToTrash()
    # #     self.driver.refresh()
    # #     self.driver.refresh()
    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_SlideSelection(self):
        with check:
            log.logger.info("TC" + str(TC_Content(30)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            r1 = ele.clickOnEditButton().verify_2_Slides()
            if r1 == 2:
                assert True
            else:
                assert False
        with check:
            r2 = ele.clickOnSlide1().verifyRedlineOnSlide1()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.clickOnSlide2().verifyRedlineOnSlide2()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_AddObject(self):
        with check:
            log.logger.info("TC" + str(TC_Content(33)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            r1 = ele.clickOnEditButton().clickOnSlide1().verifyImageObject()
            if r1 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_RemoveObject_X_Btn(self):
        with check:
            log.logger.info("TC" + str(TC_Content(34)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            r1 = ele.clickOnEditButton().clickOnSlide1().verifyImageObject_X_Btn()
            if r1 == 0:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_AddObjectOnAllSlides(self):
        with check:
            log.logger.info("TC" + str(TC_Content(35)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            r1 = ele.clickOnEditButton().verifyTextObjectOn_AllSlides()
            if r1 == 2:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyPreviewOfTextObject()
            if r2 == 2:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_TemplateForSplitScreen_AddObject_TitleNumXBtn(self):
        with check:
            log.logger.info("TC" + str(TC_Content(36)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page()
            ele.addNewContent_TemplateForSplitScreen_Opt_1()
            opt1 = ele.verify_Split_Opt_1()
            if opt1 == 1:
                assert True
            else:
                assert False
            time.sleep(1)
        with check:
            r1 = ele.clickOnEditButton().clickOnSlide1().verifyImageObject()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyXBtn()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyNumbersOfSlides()
            if r3 == 2:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_VerifyTableContent(self):
        with check:
            log.logger.info("TC" + str(TC_Content(38)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.gotoContentContents_Page().verifyColumnCount()
            if r2 == 11:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_SearchByName(self):
        with check:
            log.logger.info("TC" + str(TC_Content(39)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.gotoContentContents_Page().verifySearchContentByName()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_MultiSelect(self):
        with check:
            log.logger.info("TC" + str(TC_Content(40)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfContentPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.createdContentMoveToTrash_OG()
            self.driver.refresh()
            time.sleep(1.5)
            after_count = ele2.getDataCountOfContentPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count - 2:
                ele2.deleteContentInTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_ClickOnContentName(self):
        with check:
            log.logger.info("TC" + str(TC_Content(41)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            ele.gotoContentContents_Page().clickOnContentName()
            r2 = ele.verifyAddedContent()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyEditContentPageTitle()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_ClickOnPlaylistCount(self):
        with check:
            log.logger.info("TC" + str(TC_Content(42)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False

        with check:
            ele.AssignLayoutToPlaylist()
            ele2 = ele.gotoContentContents_Page().getValueOfCreatedContent().clickOnPlaylistCount()
            time.sleep(2)
            expected_url = ele2.getUrlOfPlaylistWithValue()
            actual_url = ele2.get_current_url()
            if actual_url == expected_url:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_addNewContent_ClickOnScheduleCount(self):
        with check:
            log.logger.info("TC" + str(TC_Content(43)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            ele.AssignLayoutToSchedule()
            ele2 = ele.gotoContentContents_Page().getValueOfCreatedContent().clickOnScheduleCount()
            time.sleep(2)
            expected_url = ele2.getUrlOfScheduleWithValue()
            actual_url = ele2.get_current_url()
            print(expected_url)
            print(actual_url)
            if actual_url == expected_url:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_ClickOnPreviewFromActions(self):
        with check:
            log.logger.info("TC" + str(TC_Content(44)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            ele2 = ele.gotoContentContents_Page().getValueOfCreatedContent().clickOnPreviewFromActions()
            r2 = ele2.verifyPreviewTitle()
            r2 = str(r2)
            if r2 == "True":
                self.driver.refresh()
                time.sleep(2)
                assert True
            else:
                assert False
        self.driver.refresh()        
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_CopyFromActions(self):
        with check:
            log.logger.info("TC" + str(TC_Content(45)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            ele2 = ele.gotoContentContents_Page().getValueOfCreatedContent().createCopiedContent()
            r2 = ele2.verifyDimensions()
            r2 = str(r2)
            if r2 == "True":
                ele2.createdContentMoveToTrash()
                assert True
            else:
                assert False
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_VerifyMoreOptions(self):
        with check:
            log.logger.info("TC" + str(TC_Content(47)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r1 = ele.verify_More_MoveContent()
            if r1 == "Move Layout":
                assert True
            else:
                assert False
        with check:
            r2 = ele.verify_More_MoveToTrash()
            if r2 == "Trash":
                assert True
            else:
                assert False
        with check:
            r3 = ele.verify_More_RemoveTag()
            if r3 == "Remove Tag":
                assert True
            else:
                assert False
        with check:
            r4 = ele.verify_More_AddTag()
            if r4 == "Add Tag":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    def test_verify_More_MoveContent_Function(self):
        with check:
            log.logger.info("TC" + str(TC_Content(48)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            ele2 = ele.createNewFolder().gotoContentContents_Page().MoveContentToFolder()
            popup_msg = ele2.verifyPopupMsg_MoveContent()
            popup_msg = str(popup_msg)
            if popup_msg == "True":
                assert True
            else:
                assert False
        with check:
            r1 = ele2.clickOnMovedFolderName().verifyContentInFolder()
            if r1 == 1:
                assert True
            else:
                assert False
        ele2.deleteCreatedFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    def test_verify_More_MoveToTrash_Function(self):
        with check:
            log.logger.info("TC" + str(TC_Content(49)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            popup_msg = ele.createdContentMoveToTrash_CancelBtn().createdContentMoveToTrash_OG().getTextFromPopUp()
            if popup_msg == "Layout moved to trash ×":
                assert True
            else:
                assert False
        ele.deleteContentInTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verify_More_CopyToShared_Function(self):
        with check:
            log.logger.info("TC" + str(TC_Content(50)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().SwitchToHeadUser().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r = ele.createdContentCopyToShared_OSD_isVisible_CancelBtn()
            if r == 0:
                assert True
            else:
                assert False
        with check:
            ele.gotoContentContents_Page().clickOnSharedFolder()
            before_count = ele.getDataCountOfContentPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.clickOnHeadOrBaseFolder().createdContentCopyToShared().clickOnSharedFolder()
            self.driver.refresh()
            time.sleep(1)
            self.driver.refresh()
            after_count = ele2.getDataCountOfContentPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.deleteFromSharedFolder().createdContentMoveToTrash()
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verify_RemoveFromSharedFolder(self):
        with check:
            log.logger.info("TC" + str(TC_Content(51)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().SwitchToHeadUser().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            ele2 = ele.clickOnHeadOrBaseFolder().createdContentCopyToShared().clickOnSharedFolder()
            self.driver.refresh()
            time.sleep(1)
            self.driver.refresh()
            before_count = ele.getDataCountOfContentPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2.deleteFromSharedFolder_single()
            after_count = ele2.getDataCountOfContentPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count - 1:
                ele2.createdContentMoveToTrash()
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()
##########################partition#######################################################
    @pytest.mark.FOCUSED
    def test_verify_More_Add_Tag_RadioBtn(self):
        with check:
            log.logger.info("TC" + str(TC_Content(52)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r1 = ele.verify_more_AddTag_RadioBtn()
            if r1 == 2:
                assert True
            else:
                assert False
        # self.driver.back()
        ele.createdContentMoveToTrash()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    def test_verify_More_Add_New_Tag(self):
        with check:
            log.logger.info("TC" + str(TC_Content(53)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r1 = ele.verify_AddNewTag_WarnMsg()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        with check:
            r2 = ele.verify_AddNewTag_popup()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        with check:
            r3 = ele.clickOnTagBtn().verifyAddedTag()
            r3 = str(r3)
            print(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.closetagoption().createdContentMoveToTrash()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verify_More_Add_Existing_Tag(self):
        with check:
            log.logger.info("TC" + str(TC_Content(54)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r2 = ele.verify_AddNewTag_popup()
            assert r2
        with check:
            time.sleep(5)
            r3 = ele.addNewContent().gotoContentContents_Page().verify_AddExistingTag_popup()
            assert r3
        ele.createdContentMoveToTrash()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    def test_verify_More_Add_New_Tag_2Tags(self):
        with check:
            log.logger.info("TC" + str(TC_Content(55)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r1 = ele.verify_AddNewTag_WarnMsg()
            if r1 == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        with check:
            r2 = ele.verify_AddNewTag_popup()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
            time.sleep(2)
        with check:
            r3 = ele.verify_AddNewTag_popup()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
            time.sleep(2)
        with check:
            r4 = ele.getTextTagBtn()
            if r4 == "2":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verify_More_Remove_New_Tag(self):
        with check:
            log.logger.info("TC" + str(TC_Content(56)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
        with check:
            r2 = ele.verify_AddNewTag_popup()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        with check:
            r3 = ele.verify_RemoveTag_popup()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    def test_verify_More_Remove_Tag_2Tags(self):
        with check:
            log.logger.info("TC" + str(TC_Content(57)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent().gotoContentContents_Page()
            r2 = ele.verify_AddNewTag_popup()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
            time.sleep(2)
        with check:
            r3 = ele.verify_AddNewTag_popup()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
            ele.verify_RemoveTag_popup_2Tag()
        with check:
            r4 = ele.getTextTagBtn()
            if r4 == "0":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_Content_CreateFolder_WarnMsg_SpecialCharacter(self):
        log.logger.info("TC" + str(TC_Content(58)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().createNewFolder_SplChar()
            warnMsg = ele.getTextFromWarningMsg()
            assert warnMsg == WARN_MSG_Only_lettersNumbers
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewContent_InRootFolder(self):
        with check:
            log.logger.info("TC" + str(TC_Content(59)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_xaddNewContent_InCreatedFolder(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Content(60)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().createNewFolder()
            r1 = ele.verifyFolderIsCreated()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            ele2 = ele.addNewContent_folder()
            Home.gotoContentContents()
            r2 = ele2.verifyAddedContentInTable()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_SearchContentInTrashFolder(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(61)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            ele2 = ele.createdContentMoveToTrash_OG().ClickOnTrashFolder()
            r1 = ele2.verifySearchContentByName()
            if r1 == 1:
                ele.deleteContentInTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_TrashFolder_ClickOnPreviewFromActions(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(62)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            ele2 = ele.gotoContentContents_Page().getValueOfCreatedContent().createdContentMoveToTrash_OG().ClickOnTrashFolder().clickOnPreviewFromActions()
            r2 = ele2.verifyPreviewTitle()
            r2 = str(r2)
            if r2 == "True":
                self.driver.refresh()
                time.sleep(2)
                ele.deleteContentInTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_RestoreContentFromTrashFolder(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(63)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            ele2 = ele.createdContentMoveToTrash_OG().restoreDeletedAllFiles()
            r1 = ele2.verifyAddedContentInTable()
            if r1 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_DeleteCompletelyContentFromTrashFolder(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(64)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            ele2 = ele.createdContentMoveToTrash().ClickOnTrashFolder()
            r1 = ele2.verifyAddedContentInTable()
            if r1 == 0:
                assert True
            else:
                assert False
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_zyeditContent_BlankSlide(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(65)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditContentPageTitle()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyBlankSlide()
            if r3 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editContent_ExistingContent(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(66)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_folder()
            # ele2 = ele.clickOnAddedContentNameInTable()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.editContent()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    def test_editContent_SharedFolder(self):
        self.driver.refresh()
        log.logger.info("TC" + str(TC_Content(67)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG().clickOnUpload_forMP4().addMaterialToSharedFolder().clickOnSharedFolderBtn()
            ele3 = ele2.gotoContentContents_Page().addNewContent()
            r = ele3.verifySharedFolderOnEditContentPage()
            if r == 1:
                assert True
            else:
                assert False
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        ele3.createdMaterialDeleteCompletely().createdContentMoveToTrash().switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContentPage_PreviewOption(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(69)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyPreviewFromEditContentPage()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        # self.driver.back()
        self.driver.refresh()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_editContent_SaveButton(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(70)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyDisabledSaveBtn()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            # r2 = ele.editContent()
            r2 = ele.editContentSIT()
            if r2 == 1:
                assert True
            else:
                assert False
        # self.driver.back()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_CloseButton(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(71)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent_folder()
            r1 = ele.verifyContentNameInTable()
            if r1 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()
###Manuall NP
    # @pytest.mark.FOCUSED
    # def test_editContent_Add20Slides(self):
    #     self.driver.refresh()
    #     with check:
    #         log.logger.info("TC" + str(TC_Content(72)))
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
    #         r1 = ele.verifyAddedContent()
    #         if r1 == 1:
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         r2 = ele.editContent_verifyDisabledAddSlideBtn()
    #         if r2 == 1:
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         r3 = ele.verify20SlidesDuration()
    #         if r3 == 1:
    #             assert True
    #         else:
    #             assert False
    #     if configReader.getTestData("TestData", "Environment") == "prod":
    #         self.driver.get("https://digitalsignage.jio.com/v2/contents")
    #     elif configReader.getTestData("TestData", "Environment") == "pre-prod":
    #         self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
    #     elif env == "sit1":
    #         self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
    #     elif env == "sit2":
    #         self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
    #     ele.createdContentMoveToTrash()
    #     self.driver.refresh()
    #     self.driver.refresh()
    # # ##Manually NP
    # @pytest.mark.FOCUSED
    # def test_editContent_DeleteButton(self):
    #     self.driver.refresh()
    #     with check:
    #         log.logger.info("TC" + str(TC_Content(73)))
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
    #         r1 = ele.verifyDeleteButton_BlankSheet()
    #         r1 = ele.editContentSIT()
    #         if r1 == 0:
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         r2 = ele.verifyDisabledSaveBtn()
    #         if r2 == 1:
    #             assert True
    #         else:
    #             assert False
    #     ele.createdContentMoveToTrash()
    #     self.driver.refresh()
    #     self.driver.refresh()

    # ##Manually Np
    # @pytest.mark.DEMO
    # @pytest.mark.FOCUSED
    # def test_editContent_Add20Slides_CopyBtn(self):
    #     self.driver.refresh()
    #     with check:
    #         log.logger.info("TC" + str(TC_Content(74)))
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
    #         r1 = ele.verifyAddedContent()
    #         if r1 == 1:
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         r2 = ele.editContent_verifyDisabledCopyBtn()
    #         if r2 == 21:
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         r3 = ele.verify20SlidesDuration()
    #         if r3 == 1:
    #             assert True
    #         else:
    #             assert False
    #     if configReader.getTestData("TestData", "Environment") == "prod":
    #         self.driver.get("https://digitalsignage.jio.com/v2/contents")
    #     elif configReader.getTestData("TestData", "Environment") == "pre-prod":
    #         self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
    #     ele.createdContentMoveToTrash()
    #     self.driver.refresh()
    #     self.driver.refresh()

    ####Manually 1 step NP
    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_editContent_PlayTime(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(76)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyAddedContent()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.editContent_verifyPlaytime_1Slide()
            if r2 == 1:
                assert True
            else:
                assert False
              ##Manually step NP
        # with check:
        #     r3 = ele.editContent_verifyPlaytime_20Slides()
        #     if r3 == 1:
        #         assert True
        #     else:
        #         assert False
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_EditBtn(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(79)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r = ele.verifyEditBtnFromEditContentOSD()
            if r == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_Preview_Save_Back_Close_Btn(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(80)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r = ele.verifyPreview_Save_Back_Close_Btn()
            if r == 4:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_BackBtn(self):
        self.driver.refresh()
        with check:
            log.logger.info("TC" + str(TC_Content(81)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyBackBtnFromEditContentOSD_WithoutChanges()
            if r1 == 0:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyBackBtnFromEditContentOSD_WithChanges()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_SaveButton_withChanges(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(82)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyDisabledSaveBtn()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifySaveBtnFromEditContentOSD_WithChanges()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()



#####################need to discuss###############preview issue############
    @pytest.mark.FOCUSED
    def test_editSlidePage_PreviewOption(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(83)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifySaveBtnFromEditContentOSD_WithChanges()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyPreviewFromEditSlidePage()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        time.sleep(2)
        # self.driver.back()
        time.sleep(2)
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editSlidePage_CloseBtn(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(84)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyCloseBtnFromEditContentOSD_WithoutChanges()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyCloseBtnFromEditContentOSD_WithChanges()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editSlidePage_AddObject(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(87)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyNumberOfObjects()
            # if r1 == 22:
            ###23 objects as per new ui
            if r1 == 21:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyTooltipOfObjects()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

# # #  ###need discussion
    @pytest.mark.FOCUSED
    def test_editSlidePage_AddObject_AddText(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(88)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddText()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyPreviewFromEditSlidePage()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editSlidePage_DeleteAddedObject(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(90)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddImage()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyDelete_AddedImage()
            if r2 == 0:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editSlidePage_CopyAddedObject(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(91)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddText()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyCopy_AddedText()
            if r2 == 2:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddImage(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(92)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddImage__()
            if r1 == 1:
                assert True
            else:
                assert False
#######need discussion#################################
        with check:
            r2 = ele.verifyPreviewFromEditSlidePage()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editSlidePage_DeleteAddedObject_Video(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(93)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddVideo()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditInfoWhile_AddVideo()
            if r2 == 1:
                assert True
            else:
                assert False
        with check:
            r3 = ele.verifyDelete_AddedVideo()
            if r3 == 0:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddOnscreenText(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(94)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddOnscreenText()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditInfoWhile_AddOnscreenText()
            if r2 == 1:
                assert True
            else:
                assert False
    ###############step removed code issue############
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddRssFeed(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(95)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddRssFeed()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyEditInfoWhile_AddRssFeed()
            if r2 == 1:
                assert True
            else:
                assert False
    #############step removed code issue###############
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddYoutube(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(96)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddYoutube()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyDelete_AddedYoutube()
            if r2 == 0:
                assert True
            else:
                assert False
        ###step removed code issue###
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddGoogle(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(97)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddGoogle()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyDelete_AddedGoogle()
            if r2 == 0:
                assert True
            else:
                assert False
        #####step removed code issue####
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddShape(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(98)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddShape()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyDelete_AddedShape()
            if r2 == 0:
                assert True
            else:
                assert False
    #####step removdd code issue####
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddJioSaavan(self):
        self.driver.refresh()
        with check:
            # log.logger.info("TC" + str(TC_Content(99)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddJioSaavan()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyDelete_AddedJioSaavan()
            if r2 == 0:
                assert True
            else:
                assert False
    #####code issue step removed####
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddInstagram(self):
        with check:
            # log.logger.info("TC" + str(TC_Content(100)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddInstagram()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verifyDelete_AddedInstagram()
            if r2 == 0:
                assert True
            else:
                assert False
        ###step removed code issue###
        with check:
            r3 = ele.verifyPreviewFromEditSlidePage()
            r3 = str(r3)
            if r3 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_Duration_IncreaseDecrease(self):
        with check:
            # log.logger.info("TC" + str(TC_Content(101)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verify_IncreaseDuration()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele.verify_DecreaseDuration()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_editContent_TransitionEffectOption(self):
        with check:
            # log.logger.info("TC" + str(TC_Content(103)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verify_TransitionEffectSlide1()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            ele2 = ele.goToEditContentPage()
            r2 = ele2.verify_TransitionEffectSlide2()
            if r2 == 1:
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_editContent_BackgroundColour(self):
        with check:
            # log.logger.info("TC" + str(TC_Content(109)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyBgColour()
            assert r1
        with check:
            r2 = ele.verifyDeselectBgColour()
            assert r2
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.failtc
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_editSlidePage_AddObject_AddText_Custom(self):
        with check:
            # log.logger.info("TC" + str(TC_Content(176)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount().gotoContentContents_Page().addNewContent()
            r1 = ele.verifyObject_AddText_Custom()
            print("test output",r1)
            if r1 == "~!@#$%^&*()_+`1234567890-=qwertyuiop[]\{}|QWERTYUIOPASDFGHJKL:asdfghjkl;'zxcvbnm,./ZXCVBNM<>?":
                assert True
            else:
                assert False
        ###step removed preview issue ####
        with check:
            r2 = ele.verifyPreviewFromEditSlidePage_Custom()
            r2 = str(r2)
            if r2 == "True":
                assert True
            else:
                assert False
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    # def test_verifyPlayLogPage(self):
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentContents().gotoReportsPlaylogs_omkar()


    @pytest.mark.SMOKE
    @allure.description("Verify Usage count for playlist, Schedule @ Layout -> Roots")
    def test_UsageCount(self):
        Home = HomePage(self.driver)
        countbefore = Home.gotoContentContents().addNewContent().gotocontentlink().InitialUsageCount()
        with check:
            assert countbefore == "Playlist: 0\nSchedule: 0"
        with check:
            countafter = Home.gotoContentContents().AssignLayoutToPlaylist().AssignLayoutToSchedule().VerifyUsageCount()
            assert int(countafter[0]) == 1
            assert int(countafter[1]) == 1


    @pytest.mark.SMOKE
    @allure.description("Verify content Name, Folder, duration, details, content logs @ Layout -> Roots")
    def test_LayoutDetails(self):
        Home = HomePage(self.driver)
        with check:
            assert Home.gotoContentContents().addNewContent().LayoutHeaderDetails()
        with check:
            assert Home.gotoContentContents().CreatedLayoutDetails()
    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_WithVideoObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            Home.gotoContentContents().stayOnBaseAccount()
            ele = Home.gotoContentMaterialsForContents()
            ele.Uploadmedia_video()
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateForVideo_3min()
            assert ele.verifyObject_videoObject()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.SANITY
    @pytest.mark.FOCUSED
    def test_addNewContent_WithMultiSlideObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            Home.gotoContentContents().stayOnBaseAccount()
            ele = Home.gotoContentMaterialsForContents()
            ele.Uploadmedia1()
            ele.Uploadmedia2()
            ele.Uploadmedia3()
            time.sleep(2)
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateForImagesMultiSlide()
            assert ele.verifyMultiSlide()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_WithFTPObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount()
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateFor_FTPObj()
            assert ele.verifyFTPObj()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_WithExternalWebpageObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount()
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateFor_ExternalWebpageObj()
            assert ele.verifyExternalWebpage()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_WithButtonObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount()
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateFor_ButtonObj()
            assert ele.verifyButtonObj()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_WithButtonBoxObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount()
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateFor_ButtonBoxObj()
            assert ele.verifyButtonBoxObj()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewContent_WithClockObject(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentContents().stayOnBaseAccount()
            ele.gotoContentContents_Page().CreateLayoutWithBlankTemplateFor_ClockObj()
            assert ele.verifyClockObj()
        ele.createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

