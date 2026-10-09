import logging
import time

import pytest
from pytest_check import check

from TestCases.BaseTest import BaseTest
from Pages.HomePage import HomePage
from Utilities import configReader
from Utilities.LogUtil import Logger
from utils.TC_Schedules import TC_Schedules

log = Logger(__name__, logging.INFO)

time_list = ['12am', '1am', '2am', '3am', '4am', '5am', '6am', '7am', '8am', '9am', '10am', '11am', '12pm', '1pm',
             '2pm', '3pm', '4pm', '5pm', '6pm', '7pm', '8pm', '9pm', '10pm', '11pm']
new_time = ['12am', '12:30am', '1am', '1:30am', '2am', '2:30am', '3am', '3:30am', '4am', '4:30am', '5am', '5:30am',
            '6am', '6:30am', '7am', '7:30am', '8am', '8:30am', '9am', '9:30am', '10am', '10:30am', '11am', '11:30am',
            '12pm', '12:30pm', '1pm', '1:30pm', '2pm', '2:30pm', '3pm', '3:30pm', '4pm', '4:30pm', '5pm', '5:30pm',
            '6pm', '6:30pm', '7pm', '7:30pm', '8pm', '8:30pm', '9pm', '9:30pm', '10pm', '10:30pm', '11pm', '11:30pm']
time_list_5 = ['12am', '12:15am', '12:30am', '12:45am', '1am', '1:15am', '1:30am', '1:45am', '2am', '2:15am', '2:30am',
               '2:45am', '3am', '3:15am', '3:30am', '3:45am', '4am', '4:15am', '4:30am', '4:45am', '5am', '5:15am',
               '5:30am', '5:45am', '6am', '6:15am', '6:30am', '6:45am', '7am', '7:15am', '7:30am', '7:45am', '8am',
               '8:15am', '8:30am', '8:45am', '9am', '9:15am', '9:30am', '9:45am', '10am', '10:15am', '10:30am',
               '10:45am', '11am', '11:15am', '11:30am', '11:45am', '12pm', '12:15pm', '12:30pm', '12:45pm', '1pm',
               '1:15pm', '1:30pm', '1:45pm', '2pm', '2:15pm', '2:30pm', '2:45pm', '3pm', '3:15pm', '3:30pm', '3:45pm',
               '4pm', '4:15pm', '4:30pm', '4:45pm', '5pm', '5:15pm', '5:30pm', '5:45pm', '6pm', '6:15pm', '6:30pm',
               '6:45pm', '7pm', '7:15pm', '7:30pm', '7:45pm', '8pm', '8:15pm', '8:30pm', '8:45pm', '9pm', '9:15pm',
               '9:30pm', '9:45pm', '10pm', '10:15pm', '10:30pm', '10:45pm', '11pm', '11:15pm', '11:30pm', '11:45pm']


class TestSchedules(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    # working
    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_verifyAddSchedule(self):
        log.logger.info(str(TC_Schedules(1)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        schedule = homepage.gotoContentSchedules().addScheduleWith5Char()
        if schedule == "1":
            assert True
        else:
            assert False
        homepage.openSchedulePage().delete_sch1()

    # working
    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyAddScheduleWithAllChar(self):
        log.logger.info(str(TC_Schedules(2)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        schedule = homepage.gotoContentSchedules().addSchedulesWithMaxChar()
        if schedule == "1":
            assert True
        else:
            assert False
        homepage.openSchedulePage().delete_sch2()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyScheduleNameWithSP(self):
        log.logger.info(str(TC_Schedules(3)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        msg = homepage.gotoContentSchedules().addScheduleNameWithSpecialChar()
        assert "Only letters, numbers, spaces and _ are allowed." in msg

    @pytest.mark.FOCUSED
    def test_verifyCustomizeSchedulePage(self):
        log.logger.info(str(TC_Schedules(4)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        with check:
            assert homepage.gotoContentSchedules().scheduleNameOnCustomizePage() is not None
        with check:
            assert homepage.gotoContentSchedules().getEditScheduleOptions() is not None
        homepage.openSchedulePage().delete_sch3()
        homepage.openSchedulePage().delete_sch4()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyCancelOptionOnAddSchedule(self):
        log.logger.info(str(TC_Schedules(5)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        schedule = homepage.gotoContentSchedules().cancelOptionOnAddSchedule()
        if schedule == "0":
            assert True
        else:
            assert False

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnAddSchedule(self):
        log.logger.info(str(TC_Schedules(6)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        schedule = homepage.gotoContentSchedules().closeOptionOnAddSchedule()
        if schedule == "0":
            assert True
        else:
            assert False

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyEditScheduleName(self):
        log.logger.info(str(TC_Schedules(7)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().editScheduleNameOnEditPage()
        # homepage.openSchedulePage().delete_sch5()
        homepage.openSchedulePage().delete_sch6()

    @pytest.mark.FOCUSED
    def test_verifyUpdateScheduleName(self):
        log.logger.info(str(TC_Schedules(8)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "Schedule name updated successfully." == homepage.gotoContentSchedules().UpdateScheduleNameOnEditPage()
        homepage.openSchedulePage().delete_sch8()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyScheduleTime(self):
        log.logger.info(str(TC_Schedules(9)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().createScheduleForCount()
        # 1 Hrs
        with check:
            assert time_list == homepage.gotoSchedules().verify1hrDuration()
            assert 24 == homepage.gotoSchedules().verify1hrDurationCount()
        # 30 Min
        with check:
            assert time_list == homepage.gotoSchedules().verify30MinDuration()
            assert 48 == homepage.gotoSchedules().verify30MinDurationCount()
        # 15 Min
        with check:
            assert new_time == homepage.gotoSchedules().verify15MinDuration()
            assert 96 == homepage.gotoSchedules().verify15MinDurationCount()
        # 10 Min
        with check:
            assert new_time == homepage.gotoSchedules().verify10MinDuration()
            assert 144 == homepage.gotoSchedules().verify10MinDurationCount()
        # 05 Min
        with check:
            assert time_list_5 == homepage.gotoSchedules().verify05MinDuration()
            assert 288 == homepage.gotoSchedules().verify05MinDurationCount()
        homepage.openSchedulePage().delete_scheduleForCount()

    @pytest.mark.FOCUSED
    def test_verifyPreviousWeekOption(self):
        with check:
            log.logger.info(str(TC_Schedules(13)))
            homepage = HomePage(self.driver)
            homepage.gotoSchedules().switchToHead()
            current_week = homepage.gotoContentSchedules().getCurrentWeek()
            previous_week = homepage.gotoSchedules().getPreviousWeek()
            assert current_week != previous_week
        homepage.openSchedulePage().delete_sc_name()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyNextWeekOption(self):
        with check:
            log.logger.info(str(TC_Schedules(14)))
            homepage = HomePage(self.driver)
            homepage.gotoSchedules().switchToHead()
            time.sleep(3)
            self.driver.refresh()
            time.sleep(1)
            current_week = homepage.gotoContentSchedules().getCurrentWeek_()
            next_week = homepage.gotoSchedules().getNextWeek()
            assert current_week != next_week
        homepage.openSchedulePage().delete_sc_name20()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyTodayOption(self):
        log.logger.info(str(TC_Schedules(15)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        next_week = homepage.gotoContentSchedules().getCurrentWeekDate()
        today = homepage.gotoSchedules().clickToday()
        assert next_week != today
        homepage.openSchedulePage().delete_sch_name()

    @pytest.mark.FOCUSED
    def test_verifyContentSearch(self):
        log.logger.info(str(TC_Schedules(16)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c1()
        print("MANUAL TESTING IS REQUIRED")
        # with check:
        #     assert 1 == homepage.gotoContentSchedules().searchForContent()
        # with check:
        #     assert "Not Requested" == homepage.gotocs().getApprovalStatus()
        # with check:
        #     duration = homepage.gotocs().getDuration()
        #     print(duration)
        #     assert "00:00:10 Not Requested" in duration
        homepage.openSchedulePage().delete_xxx()
        homepage.gotocs().delete_content_c1()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_verifyDragDrop(self):
        log.logger.info(str(TC_Schedules(18)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c2()
        ItemCountBeforeDrag = homepage.gotoContentSchedules().checkItemCountBeforeDrag()
        ItemCountAfterDrag = homepage.gotoContentSchedules().verifyDragDrop()
        assert ItemCountBeforeDrag != ItemCountAfterDrag
        homepage.openSchedulePage().delete_dra_drop_schedule()
        homepage.gotocs().delete_content_c2()

    @pytest.mark.FOCUSED
    def test_verifyEditScheduleOnDragContent(self):
        log.logger.info(str(TC_Schedules(19)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c3()
        assert "Edit Schedule Details" == homepage.gotoContentSchedules().verifyEditScheduleOnDragContent()
        homepage.openSchedulePage().delete_dra_drop_schedule1()
        homepage.gotocs().delete_content_c3()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyStartTime(self):
        log.logger.info(str(TC_Schedules(21)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c4()
        homepage.gotoContentSchedules().verifyStartTime()
        homepage.openSchedulePage().delete_dra_drop_schedule2()
        homepage.gotocs().delete_content_c4()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyEndTime(self):
        log.logger.info(str(TC_Schedules(22)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c5()
        homepage.gotoContentSchedules().verifyEndTime()
        homepage.openSchedulePage().delete_dra_drop_schedule3()
        homepage.gotocs().delete_content_c5()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyRepeatCheckBox(self):
        log.logger.info(str(TC_Schedules(23)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c6()
        assert "Start DateEnd Date" == homepage.gotoContentSchedules().verifyRepeatCheckBox()
        homepage.openSchedulePage().delete_dra_drop_schedule4()
        homepage.gotocs().delete_content_c6()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyStartDate(self):
        log.logger.info(str(TC_Schedules(24)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c7()
        homepage.gotoContentSchedules().verifyStartDate()
        homepage.openSchedulePage().delete_dra_drop_schedule5()
        homepage.gotocs().delete_content_c7()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyEndDate(self):
        log.logger.info(str(TC_Schedules(25)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c8()
        homepage.gotoContentSchedules().verifyEndDate()
        homepage.openSchedulePage().delete_dra_drop_schedule6()
        homepage.gotocs().delete_content_c8()

    @pytest.mark.FOCUSED
    def test_verifySaveSchedule(self):
        log.logger.info(str(TC_Schedules(26)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c9()
        homepage.gotoContentSchedules().verifySaveSchedule()
        homepage.openSchedulePage().delete_dra_drop_schedule7()
        homepage.gotocs().delete_content_c9()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyCancelOptionOnSchedule(self):
        log.logger.info(str(TC_Schedules(27)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c10()
        homepage.gotoContentSchedules().verifyCancelSchedule()
        homepage.openSchedulePage().delete_dra_drop_schedule8()
        homepage.gotocs().delete_content_c10()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyDeleteOptionOnSchedule(self):
        log.logger.info(str(TC_Schedules(28)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContent_c11()
        homepage.gotoContentSchedules().verifyDeleteSchedule()
        homepage.openSchedulePage().delete_dra_drop_schedule10()
        homepage.gotocs().delete_content_c11()

    @pytest.mark.FOCUSED
    def test_verifyDragAndDropFromFolder(self):
        log.logger.info(str(TC_Schedules(30)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContentInFolder()
        assert "Item count : 1" or "Item count : 1"  == homepage.gotoContentSchedules().verifyDragAndDropFromFolder()
        homepage.openSchedulePage().delete_schedule090()
        homepage.gotocs().delete_content_c12()

    @pytest.mark.FOCUSED
    def test_verifyCurrentDate(self):
        log.logger.info(str(TC_Schedules(32)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "True" == homepage.gotoContentSchedules().verifyCurrentDate()

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnEditSchedule(self):
        global url
        log.logger.info(str(TC_Schedules(34)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        if configReader.getTestData("TestData", "Environment") == "prod":
            url = configReader.getTestData("TestData", "total_schedules_prod_url")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            url = configReader.getTestData("TestData", "total_schedules_preprod_url")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            url = configReader.getTestData("TestData", "total_schedules_SIT1_url")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            url = configReader.getTestData("TestData", "total_schedules_SIT2_url")
        assert url == homepage.gotoContentSchedules().verifyCloseOptionOnEditSchedule()
        homepage.openSchedulePage().delete_scheduleName_7()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_verifyAddTrigger(self):
        log.logger.info(str(TC_Schedules(38)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "Add Trigger" == homepage.gotoContentSchedules().verifyAddTrigger()
        homepage.openSchedulePage().delete_sch_9()

    @pytest.mark.FOCUSED
    def test_verifyCancelOptionOnAddTrigger(self):
        log.logger.info(str(TC_Schedules(40)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "No data available in table" in homepage.gotoContentSchedules().verifyCancelOptionOnAddTrigger()
        homepage.openSchedulePage().delete_sch_10()

    # @pytest.mark.FOCUSED
    # def test_AddTrigger(self):
    #     log.logger.info(str(TC_Schedules(41)))
    #     homepage = HomePage(self.driver)
    #     homepage.gotoSchedules().switchToHead()
    #     assert "1" in homepage.gotoSchedules().createTrigger()
    #     homepage.openSchedulePage().delete_sc_cont_name()

    @pytest.mark.FOCUSED
    def test_verifyHeadFolderInSchedule(self):
        log.logger.info(str(TC_Schedules(47)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        Schedules_Root = homepage.gotoContentSchedules().verifyHeadFolder()
        Schedule_Trashed = homepage.gotoContentSchedules().verifyHeadTrashFolder()
        print(Schedules_Root)
        print(Schedule_Trashed)
        assert Schedules_Root != Schedule_Trashed

    @pytest.mark.FOCUSED
    def test_verifyTrashedSchedule(self):
        log.logger.info(str(TC_Schedules(48)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "1" == homepage.gotoContentSchedules().verifyTrashedSchedule()
        homepage.openSchedulePage().delete_sch_n()

    @pytest.mark.FOCUSED
    def test_verifySearchScheduleInTrashed(self):
        log.logger.info(str(TC_Schedules(49)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert 1 == homepage.gotoContentSchedules().SearchScheduleInsideTrashed()
        homepage.openSchedulePage().delete_schedule_nm()

    @pytest.mark.FOCUSED
    def test_verifyCheckOptionOnScheduleTrashed(self):
        log.logger.info(str(TC_Schedules(50)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert 1 == homepage.gotoContentSchedules().verifyCheckOptionOnScheduleTrashed()
        homepage.openSchedulePage().delete_schedule30()

    @pytest.mark.FOCUSED
    def test_verifyMoreOptionInsideTrash(self):
        log.logger.info(str(TC_Schedules(51)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "RestoreDelete Completely" == homepage.gotoContentSchedules().moreOptionTrashed()
        homepage.openSchedulePage().delete_schedule_n()

    @pytest.mark.FOCUSED
    def test_verifyRestoreSchedule(self):
        log.logger.info(str(TC_Schedules(53)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().restoreSchedule()
        homepage.openSchedulePage().delete_scheduleName_8()

    @pytest.mark.FOCUSED
    def test_verifyCancelOnRestoreSchedule(self):
        log.logger.info(str(TC_Schedules(54)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "1" == homepage.gotoContentSchedules().CancelOnRestoreSchedule()
        homepage.openSchedulePage().delete_s_Name()

    @pytest.mark.FOCUSED
    def test_verifyCloseOnRestoreSchedule(self):
        log.logger.info(str(TC_Schedules(55)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "1" == homepage.gotoContentSchedules().CloseOnRestoreSchedule()
        homepage.openSchedulePage().delete_sch_newName()

    @pytest.mark.FOCUSED
    def test_verifyCompleteDeleteSchedule(self):
        log.logger.info(str(TC_Schedules(56)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "0" in homepage.gotoContentSchedules().verifyCompleteDeleteSchedule()

    @pytest.mark.FOCUSED
    def test_verifyOkButtonOnDeleteSchedule(self):
        log.logger.info(str(TC_Schedules(57)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "0" in homepage.gotoContentSchedules().verifyCompleteDeleteSchedule()

    @pytest.mark.FOCUSED
    def test_verifyCancelButtonOnDeleteSchedule(self):
        log.logger.info(str(TC_Schedules(58)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "1" in homepage.gotoContentSchedules().verifyCancelOnCompleteDeleteSchedule()

    @pytest.mark.FOCUSED
    def test_verifyCloseButtonOnDeleteSchedule(self):
        log.logger.info(str(TC_Schedules(59)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "1" in homepage.gotoContentSchedules().verifyCloseButtonOnDeleteSchedule()
        homepage.openSchedulePage().delete_schedule_1()

    @pytest.mark.FOCUSED
    def test_verifyScrollInTrashed(self):
        log.logger.info(str(TC_Schedules(61)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().scrollTrash()

    @pytest.mark.FOCUSED
    def test_trashedSchedule(self):
        log.logger.info(str(TC_Schedules(62)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().trashedSchedule()
        with check:
            entries_20 = homepage.gotoSchedules().get20Entries()
            assert entries_20 is not None
        with check:
            entries_50 = homepage.gotoSchedules().get50Entries()
            assert entries_50 is not None
        with check:
            entries_100 = homepage.gotoSchedules().get100Entries()
            assert entries_100 is not None
        # with check:
        #     entries_200 = homepage.gotoSchedules().get200Entries()
        #     assert entries_200 is not None
        # with check:
        #     entries_500 = homepage.gotoSchedules().get500Entries()
        #     assert entries_500 is not None

    @pytest.mark.FOCUSED
    def test_verifyNextButtonOnTrashed(self):
        log.logger.info(str(TC_Schedules(63)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().createMultipleSchedule(30)
        homepage.gotoContentSchedules().deleteAllSchedules()
        sch_count = homepage.gotoContentSchedules().getScheduleTrashedCount()
        sch_cnt_next = homepage.gotoSchedules().verifyNextOptionOnTrashed()
        assert sch_count != sch_cnt_next
        homepage.openSchedulePage().deleteLast20Entries()

    @pytest.mark.FOCUSED
    def test_verifyPreviousButtonOnTrashed(self):
        log.logger.info(str(TC_Schedules(63)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().createMultipleSchedule(30)
        sch_count = homepage.gotoContentSchedules().getScheduleTrashedCount()
        sch_cnt_next = homepage.gotoSchedules().verifyPreviousOptionOnScheduleTrashed()
        assert sch_count != sch_cnt_next
        homepage.openSchedulePage().deleteLast20Entries()

    @pytest.mark.FOCUSED
    def test_verifyCreateFolder(self):
        log.logger.info(str(TC_Schedules(65)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "Root" in homepage.gotoContentSchedules().createFolder_new()

    @pytest.mark.FOCUSED
    def test_verifyAllCharInCreateFolder(self):
        log.logger.info(str(TC_Schedules(66)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "Root" in homepage.gotoContentSchedules().verifyAllCharInCreateFolder()

    @pytest.mark.FOCUSED
    def test_verifySCInCreateFolder(self):
        log.logger.info(str(TC_Schedules(67)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        with check:
            msg = homepage.gotoContentSchedules().verifySCInCreateFolder()
            assert "Only letters, number, spaces and _ allowed" in msg
        self.driver.refresh()
        with check:
            cnt = homepage.gotoContentSchedules().verifySCDotInCreateFolder()
            if cnt == "1":
                assert True
            else:
                assert False

    @pytest.mark.FOCUSED
    def test_verifyAddButtonOnCreateFolder(self):
        log.logger.info(str(TC_Schedules(68)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "Root" in homepage.gotoContentSchedules().createFolder_new1()

    @pytest.mark.FOCUSED
    def test_verifyCancelButtonOnCreateFolder(self):
        log.logger.info(str(TC_Schedules(69)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        cn = homepage.gotoContentSchedules().verifyCancelButtonOnCreateFolder()
        if cn == "0":
            assert True
        else:
            assert False

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnCreateFolder(self):
        log.logger.info(str(TC_Schedules(70)))
        global url
        if configReader.getTestData("TestData", "Environment") == "prod":
            url = configReader.getTestData("TestData", "total_schedules_prod_url")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            url = configReader.getTestData("TestData", "total_schedules_preprod_url")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            url = configReader.getTestData("TestData", "total_schedules_sit1_url")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            url = configReader.getTestData("TestData", "total_schedules_sit2_url")
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert url in homepage.gotoContentSchedules().verifyCloseOptionOnCreateFolder()

    @pytest.mark.FOCUSED
    def test_verifyFolders(self):
        log.logger.info(str(TC_Schedules(71)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert homepage.gotoContentSchedules().verifyFolders() is not None

    @pytest.mark.FOCUSED
    def test_selectFolderFromDropdown(self):
        log.logger.info(str(TC_Schedules(72)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().folder()
        searched_fName = homepage.gotoContentSchedules().selectFolderFromDropdown()
        assert "1" in searched_fName

    @pytest.mark.FOCUSED
    def test_selectFolderFromDropdownAndOpen(self):
        log.logger.info(str(TC_Schedules(73)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        folder_names = homepage.gotoContentSchedules().new_folder()
        se_fName = homepage.gotoContentSchedules().selectFolderFromDropdownAndOpen()
        print(folder_names)
        print(se_fName)
        time.sleep(5)
        assert folder_names == se_fName

    @pytest.mark.FOCUSED
    def test_verifyScheduleSearch(self):
        log.logger.info(str(TC_Schedules(74)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().verifySearchSchedule()
        homepage.openSchedulePage().delete_sc_name1()

    @pytest.mark.FOCUSED
    def test_verifyFilterSearch(self):
        log.logger.info(str(TC_Schedules(75)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        with check:
            assert 1 == homepage.gotoContentSchedules().verifyFilterSearch()
        with check:
            homepage.gotoSchedules().verifyFilterSearchName()
        homepage.openSchedulePage().delete_sc_name2()

    @pytest.mark.FOCUSED
    def test_verifyCheckOptionOnSchedule(self):
        log.logger.info(str(TC_Schedules(77)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert 1 == homepage.gotoContentSchedules().verifyCheckOptionOnSchedule()

    @pytest.mark.FOCUSED
    def test_verifyClickOnScheduleName(self):
        log.logger.info(str(TC_Schedules(78)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert homepage.gotoContentSchedules().verifyClickOnScheduleName() is not None

    # @pytest.mark.FOCUSED
    # def test_verifyDragDropForExistingSchedule(self):
    #     log.logger.info(str(TC_Schedules(78)))
    #     homepage = HomePage(self.driver)
    #     homepage.gotoSchedules().switchToHead()
    #     homepage.gotoSchedules().createContentInBase()
    #     assert "Item count : 2" == homepage.gotoContentSchedules().verifyDragDropForExistingSchedule()

    @pytest.mark.FOCUSED
    def test_EditSchedule(self):
        log.logger.info(str(TC_Schedules(80)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContentInBase()
        assert "Edit Schedule Details" == homepage.gotoContentSchedules().EditExistingSchedule()

    @pytest.mark.FOCUSED
    def test_verifyUpdateTime(self):
        log.logger.info(str(TC_Schedules(81)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().createContentInBase()
        old_time = homepage.gotoContentSchedules().createScheduleForTime()
        new_times = homepage.gotoSchedules().verifyTime()
        assert old_time != new_times

    @pytest.mark.FOCUSED
    def test_verifyEditSchedule(self):
        log.logger.info(str(TC_Schedules(84)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        assert "1" in homepage.gotoContentSchedules().editSchedule()

    @pytest.mark.FOCUSED
    def test_AllCharInEditSchedule(self):
        log.logger.info(str(TC_Schedules(85)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        old_schedule_name = homepage.gotoContentSchedules().AddSchedule1()
        new_schedule_name = homepage.gotoContentSchedules().rename_schedule_with_all_char()
        assert old_schedule_name != new_schedule_name

    @pytest.mark.FOCUSED
    def test_sc_editSchedule(self):
        log.logger.info(str(TC_Schedules(86)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        message = homepage.gotoContentSchedules().rename_schedule_with_sc()
        assert "Only letters, numbers, spaces and _ are allowed." in message

    @pytest.mark.FOCUSED
    def test_verifySaveButtonOnEditSchName(self):
        log.logger.info(str(TC_Schedules(87)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        schedule_name = homepage.gotoContentSchedules().AddEditSchedule()
        up_schedule_name = homepage.gotoContentSchedules().rename_schedule_with_all_char2()
        assert schedule_name != up_schedule_name

    @pytest.mark.FOCUSED
    def test_verifyCancelOptionOnEditScheduleName(self):
        log.logger.info(str(TC_Schedules(88)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        name = homepage.gotoContentSchedules().AddEditSchedule3()
        n_name = homepage.gotoContentSchedules().cancel_option_on_edit_scheduleName()
        assert name == n_name

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnEditScheduleName(self):
        log.logger.info(str(TC_Schedules(89)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        name = homepage.gotoContentSchedules().AddEditSchedule5()
        n_name = homepage.gotoContentSchedules().close_option_on_edit_scheduleName()
        assert name == n_name

    @pytest.mark.FOCUSED
    def test_DuplicateSchedule(self):
        log.logger.info(str(TC_Schedules(93)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().createNewSchedule()
        assert "Name already exist" in homepage.gotoContentSchedules().DuplicateSchedule()

    @pytest.mark.FOCUSED
    def test_verifyNumberOfScheduleEntries(self):
        log.logger.info(str(TC_Schedules(96)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        sch_count = homepage.gotoContentSchedules().getScheduleCount()
        log.logger.info("sch_count : " + sch_count)
        with check:
            entries_20 = homepage.gotoSchedules().get20Entries().UserCount()
            if entries_20 <= 20:
                assert True
            else:
                assert False
        with check:
            entries_50 = homepage.gotoSchedules().get50Entries().UserCount()
            if entries_50 <= 50:
                assert True
            else:
                assert False
        with check:
            entries_100 = homepage.gotoSchedules().get100Entries().UserCount()
            if entries_100 <= 100:
                assert True
            else:
                assert False
        # with check:
        #     entries_200 = homepage.gotoSchedules().get200Entries().UserCount()
        #     if entries_200 <= 200:
        #         assert True
        #     else:
        #         assert False
        #     entries_500 = homepage.gotoSchedules().get500Entries()
        #     assert entries_200 != entries_500 or entries_200 == entries_500


    @pytest.mark.FOCUSED
    def test_verifyNextOptionOnSchedule(self):
        log.logger.info(str(TC_Schedules(97)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        sch_count = homepage.gotoContentSchedules().get10Entries().getScheduleCount()
        sch_cnt_next = homepage.gotoSchedules().verifyNextOption()
        assert sch_count != sch_cnt_next


    @pytest.mark.FOCUSED
    def test_verifyPreviousOptionOnSchedule(self):
        log.logger.info(str(TC_Schedules(98)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        sch_count = homepage.gotoContentSchedules().get10Entries().moreSchedules()
        sch_cnt_back = homepage.gotoSchedules().verifyPreviousOptionOnSchedule()
        assert sch_count != sch_cnt_back

    @pytest.mark.FOCUSED
    def test_verifyCopySchedule(self):
        log.logger.info(str(TC_Schedules(99)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().createFolder1()
        homepage.gotoSchedules().CreateScheduleInsideFolder1()
        CopiedScheduleName = homepage.gotoContentSchedules().copyScheduleInsideFolder()
        assert "2" == CopiedScheduleName

    @pytest.mark.FOCUSED
    def test_verifyFolderNameOfSchedule(self):
        log.logger.info(str(TC_Schedules(100)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        name = homepage.gotoContentSchedules().createFolder()
        f_name = homepage.gotoSchedules().CreateScheduleInsideFolder()
        assert name == f_name


    @pytest.mark.FOCUSED
    def test_verifyStartEndTimeOnSchedule(self):
        log.logger.info(str(TC_Schedules(103)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoContentSchedules().verifyStartEndTimeOnSchedule()

    @pytest.mark.FOCUSED
    def test_verifyItemCount(self):
        log.logger.info(str(TC_Schedules(104)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        ItemCountBeforeDrag = homepage.gotoContentSchedules().before_checkItemCount()
        ItemCountAfterDrag = homepage.gotoContentSchedules().verifyCountAfterDrag()
        assert ItemCountBeforeDrag != ItemCountAfterDrag

    @pytest.mark.FOCUSED
    def test_verifyModifiedAt(self):
        log.logger.info(str(TC_Schedules(106)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        added_date = homepage.gotoContentSchedules().getModifiedDateOfSchedule()
        updated_date = homepage.gotoContentSchedules().getModifiedUpdatedDateOfSchedule()
        assert added_date != updated_date

    @pytest.mark.FOCUSED
    def test_verifyScroll(self):
        log.logger.info(str(TC_Schedules(107)))
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().scroll()

    # # def test_drag_play(self):
    # #     homepage = HomePage(self.driver)
    # #     homepage.gotoSchedules().createBaseAccount()
    # #     homepage.gotoSchedules().switchToBase()
    # #     homepage.gotoSchedules().createContentInBase()
    # #     homepage.gotoSchedules().createPlaylist()

    ############additional Focused############
    @pytest.mark.FOCUSED
    def test_addtrigger(self):
        with check:
            log.logger.info(str(TC_Schedules(108)))
            homepage = HomePage(self.driver)
            # ele = homepage.gotoSchedules().createBaseAccount().switchToNewBasetrigeer()
            ele1 = homepage.gotoContentContents_S().createContentfortrigger().cancel().setDateContent()
            ele2 = ele1.gotoContentContents_SS().verifycreateTrigger()
            ele3 = ele2.gettextofpopup()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addtriggerRepeat(self):
        with check:
            log.logger.info(str(TC_Schedules(109)))
            homepage = HomePage(self.driver)
            ele1 = homepage.gotoContentContents_S().createContentfortrigger_().cancel().setDateContent()
            ele2 = ele1.gotoContentContents_SS().verifycreateRepeatTrigger()
            ele3 = ele2.gettextofpopup_()
        self.driver.refresh()
        self.driver.refresh()

    ###SANITY###############

    def test_starttimeditablesanity(self):
        self.test_verifyStartTime()
        time.sleep(3)
        self.test_verifyUpdateTime()
        time.sleep(3)
        self.test_verifyStartEndTimeOnSchedule()

    def test_Endtimeeditablesanity(self):
        self.test_verifyEndTime()
        time.sleep(2)
        self.test_verifyUpdateTime()
        time.sleep(2)
        self.test_verifyStartEndTimeOnSchedule()

    def test_verifystartenddateonrepeatschedule(self):
        self.test_verifyStartDate()
        time.sleep(3)
        self.test_verifyEndDate()
        time.sleep(3)
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_previewOption(self):
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().addNewContent1()
        assert homepage.gotoContentSchedules().createScheduleForPreviewOption().verifyPreviewOption()
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_replaceOption(self):
        homepage = HomePage(self.driver)
        homepage.gotoSchedules().switchToHead()
        homepage.gotoSchedules().addNewContent1().addNewContent2()
        assert homepage.gotoContentSchedules().createScheduleForReplaceOption().verifyReplaceOption()
