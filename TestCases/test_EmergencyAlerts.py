import logging

import pytest
from pytest_check import check

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
import time

from Utilities import configReader
from Utilities.LogUtil import Logger
from utils.TC_EmergencyAlerts import TC_EmergencyAlert

EA_URL = "https://digitalsignage.jio.com/v2/emergency_alerts"
EDitBldMaintainence_URL = configReader.getTestData("TestData", "Edit_buildingMaintenance_prod_URL")
EA_OK_btn_blgmain_text = configReader.getTestData("TestData", "D_okbtn_edit_EA_text")
EA_dragtxt_blgmain_text = configReader.getTestData("TestData", "D_dragndrop_editEA_text")
log = Logger(__name__, logging.INFO)



class TestEmergencyAlerts(BaseTest):
    @pytest.fixture(autouse=True)
    def test_switchtohead(self):
        homepage = HomePage(self.driver)
        homepage.gotoEmergencyAlerts().checkForCurrentAccountTypeProd()
        self.driver.refresh()

    # def test_verifyEmerAlertURL(self):
    #     homepage = HomePage(self.driver)
    #     assert EA_URL in homepage.gotoEmergencyAlerts().verifyURL()
    #     self.driver.refresh()
    @pytest.mark.FOCUSED
    def test_Opendropdown(self):
        # 2
        log.logger.info("TC" + str(TC_EmergencyAlert(1)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.clicktimedropdown()
            time.sleep(2)
            ele2 = ele1.visibleonehour()
            if ele2 == 'True':
                assert True
            else:
                assert False
        with check:
            ele3 = ele1.visiblesixhour()
            if ele3 == 'True':
                assert True
            else:
                assert False
        with check:
            ele4 = ele1.visibletwentyfourhour()
            if ele4 == 'True':
                assert True
            else:
                assert False
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_selecttimeduration(self):
        # 2
        log.logger.info("TC" + str(TC_EmergencyAlert(2)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            time.sleep(1)
            get = ele.gettextfromdropdownbeforechange()
            print(get)
            time.sleep(2)
            ele1 = ele.clicktimedropdown()
            time.sleep(1)
            ele2 = ele1.selecttimedurationonehour()
            time.sleep(1)
            ele3 = ele2.gettextdropdown()
            assert ele3 != get
            print(ele3)
            self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyfilter(self):
        # 7
        log.logger.info("TC" + str(TC_EmergencyAlert(3)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts().FindlenghthDisplayIDcol()
            ele1 = ele.clickonFilter()
            time.sleep(2)
            ele2 = ele1.FindlengthAfterFilterAppliedDisplayIDcol()
            if ele == 0:
                assert False
            else:
                assert True
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifySorting(self):
        # 8
        log.logger.info("TC" + str(TC_EmergencyAlert(4)))
        with check:
            Home = HomePage(self.driver)
            ele1 = Home.gotoEmergencyAlerts()
            # ele = Home.gotoEmergencyAlerts().switchtobaseuser()
            # time.sleep(2)
            # ele1 =ele.gotoEmergencyAlerts_EA()
            #
            ele2 = ele1.clickonDisplayIDsorting()
            asc = ele2.verifyInAscendingOrder_namee()
            asc = str(asc)
            assert asc, "Display ID are not sorted in ascending order"
            # if asc == 'True':
            #     assert True
            # else:
            #     assert False
        with check:
            time.sleep(2)
            # asc = ele.clickonDisplayIDsorting().
            Dsc = ele1.clickonDisplayIDsortingDSC()
            dsc = Dsc.verifyInDescendingOrder_name()
            dsc = str(dsc)
            assert dsc, "Display ID are not sorted in descending order"
            # if dsc == "True":
            #     assert True
            # else:
            #     assert False
        self.driver.refresh()
        self.driver.refresh()

        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.clickonDisplaynameSorting()
            time.sleep(1)
            asc = ele1.verifyInAscendingOrder_Dispnamee()
            time.sleep(1)
            asc = str(asc)
            assert asc, "Display names are not sorted in ascending order"
            # if asc == "True":
            #     assert True
            # else:
            #     assert False
        # with check:
        #     clk = ele.clickondispnamedscsort()
        #     dsc = clk.verifyInDescendingOrder_Dispname()
        #     dsc = str(dsc)
        #     assert dsc, "Display names are not sorted in descending order"
        #     # if dsc == "True":
        #     #     assert True
        #     # else:
        #     #     assert False
        # self.driver.refresh()
        # self.driver.refresh()
    
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.clickonDisplayStatesorting()
            asc = ele1.verifyInAscendingOrder_DispState()
            asc = str(asc)
            assert asc, "Display states are not sorted in ascending order"
            # if asc == "True":
            #     assert True
            # else:
            #     assert False
        # with check:
        #     clk = ele.clickonDisplaystatedscsorting()
        #     dsc = clk.verifyInDescendingOrder_DispState()
        #     dsc = str(dsc)
        #     assert dsc, "Display states are not sorted in descending order"
        #     # if dsc == "True":
        #     #     assert True
        #     # else:
        #     #     assert False

        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.clickonDisplaycitySorting()
            asc = ele.verifyInAscendingOrder_DispCity()
            asc = str(asc)
            assert asc, "Display cities are not sorted in ascending order"
            # if asc == "True":
            #     assert True
            # else:
            #     assert False
        # with check:
        #     clk = ele.clickonDisplaycitysortingdesc()
        #     dsc = clk.verifyInDescendingOrder_DispCity()
        #     dsc = str(dsc)
        #     assert dsc, "Display cities are not sorted in descending order"
        #     # if dsc == "True":
        #     #     assert True
        #     # else:
        #     #     assert False
        # self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_clickoncheckbox(self):
        # 9
        log.logger.info("TC" + str(TC_EmergencyAlert(5)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.checkDeliverButton()
            if ele1 == 'True':
                ele2 = ele.clickonbuildingmaintenance().clickonFirstdisplay().checkDeliverButton()
                if ele2 == "False":
                    assert True
                else:
                    assert False
            else:
                assert False
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyDisplayID(self):
        # 10
        log.logger.info("TC" + str(TC_EmergencyAlert(6)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts().gotodisplays()
            ele1 = ele.getDisplayIDs_fromDisplayPage()
            ele2 = ele1.gotoEmergencyAlerts_EA().getDisplayIDs_fromEmergencyAlertPage()
            ele2.verifyDisplayIDs()
            assert True
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyDisplayName(self):
        # 11
        log.logger.info("TC" + str(TC_EmergencyAlert(7)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele = ele.gotodisplays()
            ele1 = ele.getDisplayNames_fromDisplayPage()
            time.sleep(1)
            ele2 = ele1.gotoEmergencyAlerts_EA().getDisplayNames_fromEmergencyAlertPage()
            ele2.verifyDisplayNames()
            assert True
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifydisplaystate(self):
        # 12
        log.logger.info("TC" + str(TC_EmergencyAlert(8)))
        with check:
            Home = HomePage(self.driver)
            # ele = Home.gotoEmergencyAlerts().switchtobaseuser()
            ele = Home.gotoEmergencyAlerts()
            time.sleep(2)
            ele1 = ele.gotodisplays().clickodisplayneditbutton().getvaluestate()
            print(type(ele1))
            self.driver.refresh()
            ele2 = ele.gotodisplays().clickodisplayneditbutton().geteditdisplayname()
            self.driver.refresh()
            ele2 = Home.gotoEmergencyAlerts().searchinEA()
            time.sleep(5)
            ele3 = ele2.getemgstatedisplay()
            print(ele3)
            assert ele1 == ele3
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifydisplaycity(self):
        # 13
        log.logger.info("TC" + str(TC_EmergencyAlert(9)))
        with check:
            Home = HomePage(self.driver)
            # ele = Home.gotoEmergencyAlerts().switchtobaseuser()
            ele = Home.gotoEmergencyAlerts()
            time.sleep(2)
            ele1 = ele.gotodisplays().clickodisplayneditbutton().getvalueCity()
            print(type(ele1))
            self.driver.refresh()
            ele2 = ele.gotodisplays().clickodisplayneditbutton().geteditdisplayname()
            self.driver.refresh()
            ele2 = Home.gotoEmergencyAlerts().searchinEA()
            time.sleep(2)
            ele3 = ele2.getemgcitydisplay()
            print(ele3)
            assert ele1 == ele3
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_Emgalert_20_50_100_200_500(self):
        # 14
        log.logger.info("TC" + str(TC_EmergencyAlert(10)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            user20 = ele.clickOnSideBarHideBtn().UserCount()
            if user20 <= 20:
                assert True
            else:
                assert False
        with check:
            user50 = ele.clickOnSideBarHideBtn().select_50_entries().UserCount()
            if user50 <= 50:
                assert True
            else:
                assert False
        with check:
            user100 = ele.clickOnSideBarHideBtn().select_100_entries().UserCount()
            if user100 <= 100:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()        
            ###functionality removed###
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
        

    # @pytest.mark.FOCUSED
    # def test_chooseanytemplate(self):
    #     # 17
    #     log.logger.info("TC" + str(TC_EmergencyAlert(11)))
    #     with check:
    #         ##bldgmain
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoEmergencyAlerts()
    #         ele1 = ele.clickonbuildingmaintenance().clickonEditBuildingMaintenance()
    #         time.sleep(5)
    #         ele2 = ele1.verifyeditbldgmaintenanceokbtn()
    #         time.sleep(10)
    #         # print(ele2)
    #         # assert ele2 == EA_OK_btn_blgmain_text
    #         assert ele2 == 1
    #     with check:
    #         ele3 = ele1.verifyeditpagemaintenancedragtext()
    #         assert ele3 == "Building In Maintenance"
    #         # ele3 = ele.verifyeditpagemaintenancedragtext()
    #         # assert ele3 == EA_dragtxt_blgmain_text

        # self.driver.refresh()
        # ##firealert
        # with check:
        #     Home = HomePage(self.driver)
        #     ele = Home.gotoEmergencyAlerts()
        #     ele1 = ele.clickonfirealert().clickoneditfirealert()
        #     time.sleep(5)
        #     ele2 = ele1.verifyeditbldgmaintenanceokbtn()
        #     time.sleep(3)
        #     # print(ele2)
        #     # assert ele2 == EA_OK_btn_blgmain_text
        #     assert ele2 == 1
        # with check:
        #     ele3 = ele.verifyeditpagemaintenancedragtext()
        #     # assert ele3 == EA_dragtxt_blgmain_text
        #     assert ele3 == "Fire Alert"
        # self.driver.refresh()
        # self.driver.refresh()
        # ##heavyrain
        # with check:
        #     Home = HomePage(self.driver)
        #     ele = Home.gotoEmergencyAlerts()
        #     time.sleep(3)
        #     ele1 = ele.clickonHeavyrain().clickoneditheavyrain()
        #     time.sleep(5)
        #     ele2 = ele1.verifyeditbldgmaintenanceokbtn()
        #     time.sleep(3)
        #     print(ele2)
        #     assert ele2 == EA_OK_btn_blgmain_text
        # with check:
        #     ele3 = ele.verifyeditp-agemaintenancedragtext()
        #     print(ele3)
        #     assert ele3 == EA_dragtxt_blgmain_text
        # self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_verifyediticonBuildingMaintenance(self):
    #     # 18
    #     log.logger.info("TC" + str(TC_EmergencyAlert(12)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoEmergencyAlerts()
    #         ele1 = ele.clickonbuildingmaintenance().clickonEditBuildingMaintenance()
    #         time.sleep(5)
    #         ele2 = ele1.verifyeditbldgmaintenanceokbtn()
    #         time.sleep(10)
    #         # print(ele2)
    #         # assert ele2 == EA_OK_btn_blgmain_text
    #         assert ele2 == 1
    #     with check:
    #         ele3 = ele.verifyeditpagemaintenancedragtext()
    #         # assert ele3 == EA_dragtxt_blgmain_text
    #         assert ele3 == "Building In Maintenance"
    #     self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_verifyediticonHeavyrain(self):
    #     # 19
    #     log.logger.info("TC" + str(TC_EmergencyAlert(13)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoEmergencyAlerts()
    #         time.sleep(3)
    #         ele1 = ele.clickonHeavyrain().clickoneditheavyrain()
    #         time.sleep(5)
    #         ele2 = ele1.verifyeditbldgmaintenanceokbtn()
    #         time.sleep(3)
    #         print(ele2)
    #         # assert ele2 == EA_OK_btn_blgmain_text
    #         assert ele2 == 1
    #     with check:
    #         ele3 = ele.verifyeditpagemaintenancedragtext()
    #         # assert ele3 == EA_dragtxt_blgmain_text
    #         assert ele3  == "Heavy Rain"
    #     self.driver.refresh()
    #     self.driver.refresh()

    # @pytest.mark.FOCUSED
    # def test_verifyeditFireicon(self):
    #     # 20
    #     log.logger.info("TC" + str(TC_EmergencyAlert(14)))
    #     with check:
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoEmergencyAlerts()
    #         time.sleep(5)
    #         ele1 = ele.clickonfirealert().clickoneditfirealert()
    #         time.sleep(10)
    #         ele2 = ele1.verifyeditbldgmaintenanceokbtn()
    #         time.sleep(5)
    #         # print(ele2)
    #         # assert ele2 == EA_OK_btn_blgmain_text
    #         assert ele2 == 1
    #     with check:
    #         ele3 = ele.verifyeditpagemaintenancedragtext()
    #         # assert ele3 == EA_dragtxt_blgmain_text
    #         assert ele3 == "Fire Alert"
    #     self.driver.refresh()
    #     self.driver.refresh()

    ###########sanity additional############

    def test_deliveralert(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.checkDeliverButton()
            if ele1 == 'True':
                ele2 = ele.clickonbuildingmaintenance().clickonFirstdisplay().clickondeliverbutton()
                ele3 = ele2.readpopup()
                time.sleep(5)
                assert ele3 == "Alert delivered successfully ×"
            else:
                assert False
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.checkDeliverButton()
            if ele1 == 'True':
                ele2 = ele.clickonfirealert().clickonFirstdisplay().clickondeliverbutton()
                ele3 = ele2.readpopup()
                time.sleep(5)
                assert ele3 == "Alert delivered successfully ×"
            else:
                assert False
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoEmergencyAlerts()
            ele1 = ele.checkDeliverButton()
            if ele1 == 'True':
                ele2 = ele.clickonHeavyrain().clickonFirstdisplay().clickondeliverbutton()
                ele3 = ele2.readpopup()
                time.sleep(5)
                assert ele3 == "Alert delivered successfully ×"
            else:
                assert False

