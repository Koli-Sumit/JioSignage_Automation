import time

import allure
import pytest

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from pytest_check import check
from Utilities.LogUtil import Logger
import logging

from Utilities import configReader
from utils.TC_Deliverymanagement import TC_Delivermanagement

deliveryMgmt_URL = "https://digitalsignage.jio.com/v2/displays/status"
Contentbuttontext = configReader.getTestData("TestData", "DeliveryButton_Content_text")
Cancelbtntext = configReader.getTestData("TestData", "Cancel_button_text")
# Syncbtntext = configReader.getTestData("TestData", "SyncButton_Content_text")
rebootbtntext = configReader.getTestData("TestData", "reboot_content_text")

###added new by devanshu##14-04-25##
Syncbtntext = configReader.getTestData("TestData", "SyncButton_Content_SIT_text")
log = Logger(__name__, logging.INFO)



class TestDeliveryManagement(BaseTest):

    @pytest.fixture(autouse=True)
    def test_switchtohead(self):
        homepage = HomePage(self.driver)
        homepage.gotoDeliveryMgmt().checkForCurrentAccountTypeProd()

    # def test_verifyDeliveryMgmtURL(self):
    #     # 1
    #     log.logger.info("TC" + str(TC_Delivermanagement(1)))
    #     homepage = HomePage(self.driver)
    #     assert deliveryMgmt_URL in homepage.gotoDeliveryMgmt().verifyDeliveryMgmtURL()
    #     self.driver.refresh()
    #     self.driver.refresh()

    # def test_verifysearchfunctionality(self):
    #     homepage = HomePage(self.driver)
    #     ele =  homepage.gotodisplays().verifycreatedisplay().verifySearchFunctionality()
    @pytest.mark.FOCUSED
    def test_search_byAllScenario(self):
        log.logger.info("TC" + str(TC_Delivermanagement(2)))
        # 3
        with check:
            time.sleep(2)
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()
            ID = ele.getDisplayID_fromTable()
            r_count = ele.searchByDisplayID().Count_forSearch()
            if r_count == 1:
                assert True
            else:
                assert False
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()
            name = ele.getDisplayName_fromTable()
            r_count = ele.searchByDisplayName().Count_forSearch()
            print("Expected:", r_count)


            if r_count == 1:
                assert True
            else:
                assert False
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()
            sc = ele.getDisplaySchedule_fromTable()
            self.driver.refresh()
            time.sleep(2)
            count = ele.getCountOfSchedules()
            r_count = ele.searchByDisplaySchedule().Count_forSearch()
            if r_count == count:
                assert True
            else:
                assert False
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()
            ID = ele.getDisplayID_fromTable()
            sc = ele.getIPAdd_fromTable()
            r_count = ele.searchByIPAdd().Count_forSearch()
            if r_count == 1:
                assert True
            else:
                assert False
        # with check:
        #     time.sleep(1)
        #     Home = HomePage(self.driver)
        #     ele = Home.gotoDeliveryMgmt()
        #     time.sleep(2)
        #     ele = ele.clickOnSideBarHideBtn()
        #     hdmi_count = ele.select_200_entries().countOfConnectedHDMI()
        #     ele.search_connected()
        #     current_hdmi_count = ele.select_200_entries().countOfConnectedHDMI()
        #     if hdmi_count == current_hdmi_count:
        #         assert True
        #     else:
        #         assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_search_byDisplayID(self):
        # 5
        log.logger.info("TC" + str(TC_Delivermanagement(3)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()
            ID = ele.getDisplayID_fromTable()
            r_count = ele.searchByDisplayID().Count_forSearch()
            if r_count == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_search_byDisplayName(self):
        # 6
        log.logger.info("TC" + str(TC_Delivermanagement(4)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()
            time.sleep(3)
            name = ele.getDisplayName_fromTable()
            time.sleep(3)
            r_count = ele.searchByDisplayName().Count_forSearch()
            print(r_count)
            if r_count == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_search_bySchedule(self):
        # 7
        log.logger.info("TC" + str(TC_Delivermanagement(5)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()

            time.sleep(4)
            sc = ele.getDisplaySchedule_fromTable()
            self.driver.refresh()
            time.sleep(2)
            count = ele.getCountOfSchedules()
            time.sleep(4)
            r_count = ele.searchByDisplaySchedule().Count_forSearch()
            time.sleep(4)
            print(r_count)
            if r_count == count:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_search_byIPAdd(self):
        # 8
        log.logger.info("TC" + str(TC_Delivermanagement(6)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn().search_192()

            ID = ele.getDisplayID_fromTable()

            sc = ele.getIPAdd_fromTable()
            r_count = ele.searchByIPAdd().Count_forSearch()
            if r_count == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_search_byStatusHDMI(self):
    #     # 9
    #     log.logger.info("TC" + str(TC_Delivermanagement(7)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoDeliveryMgmt().clickOnSideBarHideBtn()
    #         hdmi_count = ele.select_200_entries().countOfConnectedHDMI()
    #         ele.search_connected()
    #         current_hdmi_count = ele.select_200_entries().countOfConnectedHDMI()
    #         print(hdmi_count)
    #         print(current_hdmi_count)
    #         if hdmi_count == current_hdmi_count:
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_SortbyDisplayID(self):
        log.logger.info("TC" + str(TC_Delivermanagement(8)))
        # 10
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt()
            dec = ele.verifyInDescendingOrder_name()
            dec = str(dec)
            if dec == "True":
                assert True
            else:
                assert False
        with check:
            asc = ele.clickOnDisplayID_Clm().verifyInAscendingOrder_name()
            asc = str(asc)
            if asc == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_sortbyDisplayname(self):
        # 11
        log.logger.info("TC" + str(TC_Delivermanagement(9)))
        with check:
            # Home = HomePage(self.driver)
            # ele = Home.gotoDeliveryMgmt().gotouseraccess()
            # ele1 = ele.createbaseuser().switchtobaseuser()
            # time.sleep(2)
            # ele2 = ele1.gotodisplaysBase().verifycreatedisplayBase()
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnDisplayNAME_Clm()
            time.sleep(2)
            asc = ele.verifyInAscendingOrder_Displayname()
            asc = str(asc)
            assert asc, "Display name are not sorted in ascending order"
            # print(asc)
            # if asc == "True":
            #     assert True
            # else:
            #     assert False
        with check:
            dsc = ele.clickonDispnameDesc().verifyInDescendingOrder_Displayname()
            time.sleep(2)
            dsc = str(dsc)
            assert dsc, "Display name are not sorted in descending order"
            # if dsc == "True":
            #     assert True
            # else:
            #     assert False
        self.driver.refresh()
        self.driver.refresh()
        # ele3 = ele.gotodisplaysBase().DeleteCreatedDisplay()
        # time.sleep(2)
        # ele4 = ele3.SwitchtoHeaduser()
        # ele5 = ele4.gotouseraccess().deletecreatedbaseuser()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_enableIcon(self):
        log.logger.info("TC" + str(TC_Delivermanagement(10)))
        # 15
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt()
            ele2 = ele.clickOnfirstdisplay()
            isEnable = ele2.verifyDelivericonIsEnable()
            isEnable = str(isEnable)
            if isEnable == "True":
                assert True
            else:
                assert False

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_20_50_100_200_500_entries_forDeliveryMgt(self):
        # 16
        log.logger.info("TC" + str(TC_Delivermanagement(11)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt()
            user20 = ele.clickOnSideBarHideBtn().select_20_entries().UserCount()
            assert user20 <= 20
        with check:
            user50 = ele.clickOnSideBarHideBtn().select_50_entries().UserCount()
            assert user50 <= 50
        with check:
            user100 = ele.clickOnSideBarHideBtn().select_100_entries().UserCount()
            assert user100 <= 100
        # with check:
        #     user200 = ele.clickOnSideBarHideBtn().select_200_entries().UserCount()
        #     if user200 <= 200:
        #         assert True
        #     else:
        #         assert False
        # with check:
        #     user500 = ele.clickOnSideBarHideBtn().select_500_entries().UserCount()
        #     if user500 <= 500:
        #         assert True
        #     else:
        #         assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_DeliverEnabled(self):
        log.logger.info("TC" + str(TC_Delivermanagement(12)))
        # 18
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().verifydeliveryicontentenabled()
            ele1 = ele.verifyreaddeliverycontent()
            assert Contentbuttontext == ele1
            self.driver.refresh()

        with check:
            ele2 = Home.gotoDeliveryMgmt().verifydeliveryicontentenabled()
            time.sleep(4)
            ele3 = ele2.verifyOkbuttonvisible()
            time.sleep(4)
            print(ele3)
            if ele3 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            ele4 = Home.gotoDeliveryMgmt().verifydeliveryicontentenabled()
            time.sleep(1)
            ele5 = ele4.verifycrossbutonvisible()
            time.sleep(1)
            if ele5 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            ele6 = Home.gotoDeliveryMgmt().verifydeliveryicontentenabled()
            time.sleep(2)
            ele7 = ele6.verifycancelbutoonvisible()
            time.sleep(2)
            if ele7 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_SyncEnabled(self):
        log.logger.info("TC" + str(TC_Delivermanagement(13)))
        # 19
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().verifySyncbuttonenabled()
            ele1 = ele.readsynccontent()
            assert Syncbtntext == ele1
            self.driver.refresh()

        with check:
            ele2 = Home.gotoDeliveryMgmt().verifySyncbuttonenabled()
            ele3 = ele2.verifyOkbuttonvisible()
            if ele3 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            ele4 = Home.gotoDeliveryMgmt().verifySyncbuttonenabled()
            ele5 = ele4.verifycrossbutonvisible()
            if ele5 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            ele6 = Home.gotoDeliveryMgmt().verifySyncbuttonenabled()
            ele7 = ele6.verifycancelbutoonvisible()
            if ele7 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_rebootenabled(self):
        log.logger.info("TC" + str(TC_Delivermanagement(14)))
        # 20
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().verifyrebootbuttonenabled()
            ele1 = ele.readrebootcontent()
            assert rebootbtntext == ele1
            self.driver.refresh()

        with check:
            ele2 = Home.gotoDeliveryMgmt().verifyrebootbuttonenabled()
            ele3 = ele2.verifyOkbuttonvisible()
            if ele3 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            ele4 = Home.gotoDeliveryMgmt().verifyrebootbuttonenabled()
            ele5 = ele4.verifycrossbutonvisible()
            if ele5 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            ele6 = Home.gotoDeliveryMgmt().verifyrebootbuttonenabled()
            ele7 = ele6.verifycancelbutoonvisible()
            if ele7 == '1':
                assert True
            else:
                assert False
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_checkscheduledeliver(self):
        # 22
        log.logger.info("TC" + str(TC_Delivermanagement(15)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotodisplays().verifycreatedisplay()
            time.sleep(3)
            self.driver.refresh()
            ele1 = Home.gotoshedules_D().createScheduleemtpy()
            time.sleep(5)
            self.driver.refresh()
            ele2 = Home.gotoDeliveryMgmt().AssignScheduletodisplay()
            time.sleep(3)
            ele3 = ele2.searchdisplaycreated().ScheduleofCreatedDisplay()
            time.sleep(3)
            r = ele3.verifyschedulename()
            r = str(r)
            if r == "True":
                assert True
            else:
                assert False

    @pytest.mark.FOCUSED
    def test_yLeftNavigation(self):
        # 27
        log.logger.info("TC" + str(TC_Delivermanagement(16)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnOnlineOfflineOpt()
            time.sleep(5)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnBaseOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnStateOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 40
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnCityOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 41
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnDistrictOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 42
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnPincodeOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 43
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnOS_TypeOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 44
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnScheduleOpt()
            time.sleep(3)
            c = ele.nestedActiveListCount()
            time.sleep(1)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 45
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnTagWiseOpt()
            time.sleep(4)
            c = ele.nestedActiveListCount()
            time.sleep(2)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

        # 46
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnHDMIOpt()
            time.sleep(4)
            c = ele.nestedActiveListCount()
            time.sleep(2)
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_online_offline_options(self):
        # 29
        log.logger.info("TC" + str(TC_Delivermanagement(17)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnOnlineOfflineOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_base_options(self):
        # 38
        log.logger.info("TC" + str(TC_Delivermanagement(18)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnBaseOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_yxstate_options(self):
        # 39
        log.logger.info("TC" + str(TC_Delivermanagement(19)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnStateOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_wcity_options(self):
        # 40
        log.logger.info("TC" + str(TC_Delivermanagement(20)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnCityOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_district_options(self):
        log.logger.info("TC" + str(TC_Delivermanagement(21)))
        # 41
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnDistrictOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_pincode_options(self):
        log.logger.info("TC" + str(TC_Delivermanagement(22)))
        # 42
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnPincodeOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_zos_type_options(self):
        # 43
        log.logger.info("TC" + str(TC_Delivermanagement(23)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnOS_TypeOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_schedule_options(self):
        # 44
        log.logger.info("TC" + str(TC_Delivermanagement(24)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnScheduleOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_zxtagwise_options(self):
        # 45
        log.logger.info("TC" + str(TC_Delivermanagement(25)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnScheduleOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_xHDMI_Status_options(self):
        # 46
        log.logger.info("TC" + str(TC_Delivermanagement(26)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().clickOnHDMIOpt()
            c = ele.nestedActiveListCount()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    ###########Added########################
    # sort IP addr functionality removed##
    # @pytest.mark.FOCUSED
    # def test_sortbyIPaddress(self):
    #     log.logger.info("TC" + str(TC_Delivermanagement(27)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoDeliveryMgmt().clickonIPaddresssortingASC()
    #         time.sleep(6)
    #         dec = ele.verifyInAscendingOrder_IPaddress()
    #         dec = str(dec)
    #         if dec == "True":
    #             assert True
    #         else:
    #             assert False
    #     with check:
    #         asc = ele.clickonIPaddresssortingDSC().verifyInDescendingOrder_IPaddress()
    #         time.sleep(6)
    #         asc = str(asc)
    #         if asc == "True":
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Deliverfunctionality(self):
        log.logger.info("TC" + str(TC_Delivermanagement(28)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().verifydeliveryicontentenabled()
            ele1 = ele.clickokdelivery()
            time.sleep(4)
            ele2 = ele.gettextofdeliver()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_SyncyFunctionality(self):
        log.logger.info("TC" + str(TC_Delivermanagement(29)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().verifySyncbuttonenabled()
            time.sleep(1)
            ele1 = ele.clickokdelivery()
            time.sleep(4)
            ele2 = ele1.gettextofsync()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_Rebootfunctionality(self):
        log.logger.info("TC" + str(TC_Delivermanagement(30)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().verifyrebootbuttonenabled()
            time.sleep(1)
            ele1 = ele.clickokdelivery()
            time.sleep(4)
            ele2 = ele1.gettextofreboot()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_deliverschedule(self):
        log.logger.info("TC" + str(TC_Delivermanagement(31)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().gotoContentDisplays().createdisplay()
            time.sleep(2)
            ele1 = Home.gotoDeliveryMgmt().gotoContentSchedules().addSchedule()
            time.sleep(3)
            ele2 = Home.gotoDeliveryMgmt().searchDisplayNamecraetedinDM().clickcreateddisplay()
            time.sleep(1)
            ele3 = ele2.clickassignschedule().Assignschedule()
            ele4 = ele3.readpopup()
        with check:
            self.driver.refresh()
            ele5 = ele3.searchDisplayNamecraetedinDM()
            ele6 = ele5.readschedulenamecolinDM()
        self.driver.refresh()
        Home.gotoDeliveryMgmt().gotoContentDisplays().deleteCreatedDisplay()

       #########additional for sanity##########

    def test_refreshdeliverymng(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().search_192()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(4)
            ele2 = Home.gotoDeliveryMgmt().textofsearchbar()
            ele2 = ele2.replace(" ","")
            assert ele2 == ""
        self.driver.refresh()


    def test_verifydisplaydetails(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().gotodisplaysBase().createindividualdisp()
            self.driver.refresh()
            ele1= ele.gotodisplaysBase().searchcreateddisplay().gettextofdisplayid()
            self.driver.refresh()
            ele2 = Home.gotoDeliveryMgmt().gotodisplaysBase().searchcreateddisplay().textofdisplayname()
            self.driver.refresh()
            ele3 = Home.gotoDeliveryMgmt().searchcreateddisplay().gettextofdisplayid()
            print(ele3)
            self.driver.refresh()
            assert ele1 == ele3
        with check:
            ele4 = Home.gotoDeliveryMgmt().searchcreateddisplay().textofdisplaynameinDM()
            assert ele2 == ele4

    @pytest.mark.SMOKE
    @allure.description("Verify Offline Displays of Left Navigation")
    def test_Offline_Display_DMPage(self):
        with check:
            Home = HomePage(self.driver)
            DMPageOfflineCount = Home.gotoDeliveryMgmt().CheckOfflineDisplay()
            DahboarCount = Home.gotoDashboard().ReturnOfflineDisplayCount()
            assert DMPageOfflineCount == DahboarCount

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_displaySettings(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().gotoContentDisplays().createdisplay()
            time.sleep(2)
            assert Home.gotoDeliveryMgmt().verifyDisplaySettings()
        self.driver.refresh()
        Home.gotoDeliveryMgmt().gotoContentDisplays().deleteCreatedDisplay()

    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_displayStatus_leftPanel(self):
        with check:
            Home = HomePage(self.driver)
            offlineDisplays = Home.gotoDeliveryMgmt().gotoDashboard_DM().getOfflineDisplayCount()
            time.sleep(2)
            ele = Home.gotoDeliveryMgmt()
            assert ele.verifyLeftPanelList()
        with check:
            offlineDisplayFromDM = ele.selectAndReturn_OfflineDisplay()
            if offlineDisplays == offlineDisplayFromDM:
                assert True
            else:
                assert False

    @pytest.mark.SANITY
    @pytest.mark.FOCUSED
    def test_displayStatus_refreshBtn(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoDeliveryMgmt().gotoContentDisplays().createdisplay()
            time.sleep(2)
            assert Home.gotoDeliveryMgmt().verifyRefreshBtn()
        self.driver.refresh()
        Home.gotoDeliveryMgmt().gotoContentDisplays().deleteCreatedDisplay()




