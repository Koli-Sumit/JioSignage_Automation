import time

import pytest
from pytest_check import check

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import configReader
from Utilities.LogUtil import Logger
import logging
from utils.TC_ContentApproval import TC_ContentApproval
contentApprovalURL = "https://digitalsignage.jio.com/v2/content_approval?pending=true"

CA_send_text = configReader.getTestData("TestData", "D_RequestApproval_CA_text")
CA_PendingApproval_text = configReader.getTestData("TestData", "D_Pending_CA_text")
CA_Rejected_text = configReader.getTestData("TestData", "D_Rejected_CA_text")
CA_Approved_text = configReader.getTestData("TestData", "D_Approved_CA_text")
env = configReader.getTestData("TestData", "Environment")

log = Logger(__name__, logging.INFO)

class TestContentApproval(BaseTest):

    @pytest.fixture(autouse=True)
    def test_switchtohead(self):
        homepage = HomePage(self.driver)
        homepage.gotoContentApproval().checkForCurrentAccountTypeProd()

    # def test_verifyContentApprovalURL(self):
    #     homepage = HomePage(self.driver)
    #     assert contentApprovalURL in homepage.gotoContentApproval().verifyContentApprovalURL()F

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifysendapproverequest(self):
        # 1
        log.logger.info("TC" + str(TC_ContentApproval(1)))
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            # ele5.clickcancelpopup()
            assert ele5 == CA_send_text
            time.sleep(2)
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().gotoContentContents()
            ele1 = ele.searchcreatedContent()
            time.sleep(2)
            getcontentname = ele1.contentcreatedread()
            # ele2 = ele1.ApproveResponse()
            time.sleep(2)
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            ele2 = ele1.conapproveresponse()
            # print(type(ele2))
            if ele2 == getcontentname:
                assert True
            else:
                assert False
        # homepage = HomePage(self.driver)
        # ele = homepage.gotoContentApproval().gotoContentContents().searchcreatedContent()
        # time.sleep(1)
        # ele1=ele.deletecreatedcontent()
        self.driver.refresh()
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifysendapproverequestforplaylist(self):
        log.logger.info("TC" + str(TC_ContentApproval(2)))
        # 2
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            # homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().gotoPlaylist().clikonaddContent()
            ele1 = ele.EnterPlaylistname().ClickRequestForApproval().EnterDetails()
            time.sleep(2)
            ele2 = homepage.gotoContentApproval()
            ele3 = ele2.searchcreatedPlaylist()
            time.sleep(2)
            ele3 = ele3.gettextsearchedplaylist()
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_contentapprovalpage(self):
        log.logger.info("TC" + str(TC_ContentApproval(3)))
        # 3
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval()
            ele1 = ele.contentApprovalscreen()
            if ele1 == 1:
                assert True
            else:
                assert False
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval()
            ele1 = ele.readPending()
            if ele1 == CA_PendingApproval_text:
                assert True
            else:
                assert False
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval()
            ele1 = ele.readApproved()
            if ele1 == CA_Approved_text:
                assert True
            else:
                assert False
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval()
            ele1 = ele.readRejected()
            if ele1 == CA_Rejected_text:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_contentnameapprovalpage(self):
        log.logger.info("TC" + str(TC_ContentApproval(4)))
        # 4
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            ele = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(3)
            ele1 = ele.gettextofsearchedcontent()
        # ele1 = ele.searchcreatedcontent().gettextofsearchedcontent()

        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_type(self):
        log.logger.info("TC" + str(TC_ContentApproval(5)))
        # 5
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            time.sleep(2)
            # getrequestername = ele3.gettextfromrequester()
            # print(getrequestername)
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            gettypetext = gotocontentapproval.gettexttypecontentapproval()
            print(gettypetext)
            if gettypetext == 'Layout':
                assert True
            else:
                assert False
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().gotoPlaylist().clikonaddContent()
            ele1 = ele.EnterPlaylistname().ClickRequestForApproval().EnterDetails()
            time.sleep(2)
            ele2 = homepage.gotoContentApproval()
            ele3 = ele2.searchcreatedPlaylist()
            time.sleep(2)
            gettypetextp = gotocontentapproval.gettexttypecontentapproval()
            print(gettypetextp)
            if gettypetextp == 'Playlist':
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_SeeStartdate(self):
        log.logger.info("TC" + str(TC_ContentApproval(6)))
        # 6
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setExpiryDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            # self.driver.refresh()
            gotocontent = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            getstartdate = gotocontent.getcontentapprovalstartdate()
            if getstartdate == '2024-04-05':
                assert True
            else:
                assert False
            # gotocontentmodifiedat=gotocontent.searchcreatedcontent().gettextofmodifiedatContentsection()
            # time.sleep(2)
            # gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            # time.sleep(2)
            # gotocontentapprovalmodifiedat = gotocontentapproval.gettextofmodifiedatContentapprovalsection()
            # if gotocontentmodifiedat == gotocontentapprovalmodifiedat:
            #     assert True
            # else:
            #     assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_SeeEnddate(self):
        # 7
        log.logger.info("TC" + str(TC_ContentApproval(7)))
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setExpiryDateContent()
            # readenddate = ele2.gettextEnddate()
            # print(readenddate)
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            getEnddateCA = gotocontentapproval.getcontentapprovalEnddate()
            # print(getEnddateCA)
            # if readenddate == getEnddateCA:
            #     assert True
            # else:
            #     assert False
            # assert getEnddateCA == '2024-04-08'
            if getEnddateCA == '2024-04-08':
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_verifyRequestedapprovaltime(self):
        log.logger.info("TC" + str(TC_ContentApproval(8)))
        # 8
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontent = homepage.gotoContentApproval().gotoContentContents()
            gotocontentmodifiedat = gotocontent.searchcreatedcontent().gettextofmodifiedatContentsection()
            time.sleep(2)
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            gotocontentapprovalmodifiedat = gotocontentapproval.gettextofmodifiedatContentapprovalsection()
            if gotocontentmodifiedat == gotocontentapprovalmodifiedat:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyRequestername(self):
        log.logger.info("TC" + str(TC_ContentApproval(9)))
        # 9
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            time.sleep(2)
            # getrequestername = ele3.gettextfromrequester()
            # print(getrequestername)
            time.sleep(1)
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            getrequesternamecontentapproval = gotocontentapproval.gettextfromContentApprovalRequester()
            # print(getrequesternamecontentapproval)
            # assert getrequestername == getrequesternamecontentapproval
            getusername = homepage.gotoContentApproval().getprofileusernameusername()
            if getusername == getrequesternamecontentapproval:
            # if getrequestername == getrequesternamecontentapproval:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifycompanyname(self):
        log.logger.info("TC" + str(TC_ContentApproval(10)))
        # 10
        with check:
            homepage = HomePage(self.driver)
            getaccountname = homepage.gotoContentApproval().getaccountname()
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            getcompanyname = gotocontentapproval.getcompanynamecontentapproval()
            if getcompanyname == getaccountname:
                assert True
            else:
                assert False
        self.driver.refresh()
        # assert getaccountname == getcompanyname

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_verifyRedandGreenExpiredcontent(self):
        log.logger.info("TC" + str(TC_ContentApproval(11)))
        # 11
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setExpiryDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vexp = gotocontentapproval.identifyGreencontent()
            # print(vexp)
            if vexp == 0:
                assert True
            else:
                assert False
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vgreen = gotocontentapproval.identifyExpiredcontent()
            # print(vgreen)
            if vgreen == 0:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_verifyapproverejectpreviewvisible(self):
        log.logger.info("TC" + str(TC_ContentApproval(12)))
        # 12
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            time.sleep(2)
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            verifyApprovesymbol = gotocontentapproval.identifyapprovesymbolvisible()
            print(verifyApprovesymbol)
            if verifyApprovesymbol == 'True':
                assert True
            else:
                assert False
        with check:
            verifyrejectsymbol = gotocontentapproval.identifyrejectsymbolvisible()
            if verifyrejectsymbol == 'True':
                assert True
            else:
                assert False
        with check:
            verifypreviewsymbol = gotocontentapproval.identifypreviewsymbolvisible()
            if verifypreviewsymbol == 'True':
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyApprovecontent(self):
        log.logger.info("TC" + str(TC_ContentApproval(13)))
        # 13
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vgreen = gotocontentapproval.approvepopup()
            time.sleep(5)
            vpop = vgreen.verifyapprovepopuptext()
            #     print(vpop)
            if "approved" in vpop:
                assert True
            else:
                assert False
        with check:
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            searchapprovedcont = gotocontentapproval.searchApprovedContent()
            if "No matching records found" in searchapprovedcont:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_RejectContent(self):
        log.logger.info("TC" + str(TC_ContentApproval(14)))
        # 14
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vreject = gotocontentapproval.verifyrejectpopup()
            time.sleep(5)
            # print(vreject)
            if "denied" in vreject:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_PreviewContent(self):
        log.logger.info("TC" + str(TC_ContentApproval(15)))
        # 15
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vpre = gotocontentapproval.verifypreviewtext()
            time.sleep(5)
            # print(vpre)
            if 'Preview Layout' in vpre:
                assert True
            else:
                assert False
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_verifyApprovedcontentlist(self):
        log.logger.info("TC" + str(TC_ContentApproval(16)))
        # 16
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vgreen = gotocontentapproval.approvepopup()
            time.sleep(5)
            vpop = vgreen.verifyapprovepopuptext()
            if "approved" in vpop:
                assert True
            else:
                assert False
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().gotoApprovedSection().searchcreatedContent()
            time.sleep(2)
            ele1 = ele.SearchCreatedcontentinApprovedsection()
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_verifyRejeclist(self):
        log.logger.info("TC" + str(TC_ContentApproval(17)))
        # 17
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vreject = gotocontentapproval.verifyrejectpopup()
            time.sleep(5)
            # print(vreject)
            if "denied" in vreject:
                assert True
            else:
                assert False
        with check:
            gotocontentapproval = homepage.gotoContentApproval().gotoRejectedsection().searchcreatedContent()
            time.sleep(2)
            serachreject = gotocontentapproval.SearchCreatedcontentinApprovedsection()
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_verifyReasonForrejected(self):
        log.logger.info("TC" + str(TC_ContentApproval(18)))
        # 18
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentApproval().readprofileusername()
            self.driver.refresh()
            ele = ele.gotoContentContents().clikonaddContent()
            ele1 = ele.EnterContentname().cancelcontentmessage()
            time.sleep(5)
            ele2 = ele1.setDateContent()
            time.sleep(5)
            ele3 = ele2.clickonRequestApproval()
            ele3 = ele3.selectuserforapproval()
            ele4 = ele3.clickonSend()
            ele5 = ele4.verifyApprovaltext()
            gotocontentapproval = homepage.gotoContentApproval().searchcreatedContent()
            time.sleep(2)
            vreject = gotocontentapproval.verifyrejectpopup()
            time.sleep(5)
            # print(vreject)
            if "denied" in vreject:
                assert True
            else:
                assert False
        with check:
            gotocontentapproval = homepage.gotoContentApproval().gotoRejectedsection().searchcreatedContent()
            time.sleep(2)
            Readreason = gotocontentapproval.readreasonOfrejected()
        self.driver.refresh()

    # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    @pytest.mark.FOCUSED
    def test_deleteallcontents(self):
        homepage = HomePage(self.driver)
        ele = homepage.gotoContentApproval().gotoContentContents().select_200_entries()
        time.sleep(3)
        ele1 = ele.deleteAllContents()
        time.sleep(3)
        ele2=ele1.gototrash()
        ele3=ele2.select_200_entries()
        ele4=ele3.cleartrash()
    # def test_cleartrash(self):
    #     homepage = HomePage(self.driver)
    #     ele = homepage.gotoContentApproval().gotoContentContents().gototrash()
    #     time.sleep(1)
    #     ele1=ele.select_200_entries()
    #     time.sleep(1)
    #     ele2=ele1.cleartrash()
