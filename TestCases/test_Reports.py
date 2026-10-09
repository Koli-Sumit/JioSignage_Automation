import logging
import time
import pytest
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from pytest_check import check
from Utilities.LogUtil import Logger
from utils.TC_Content import TC_Content

log = Logger(__name__, logging.INFO)

class TestReports(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_UserActivityLogs_DisplayCreated(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoReports_UserActivityLogs().gotoDisplayPage().createNewDisplay()
            assert Home.gotoReports_UserActivityLogs().verifyActivityLog_DisplayCreated()
        self.driver.refresh()
        ele.gotoDisplayPage().deleteCreatedDisplay()

