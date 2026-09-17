import json
import logging

import allure
import pytest
import time
from pytest_check import check

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import configReader
from Utilities.LogUtil import Logger
from utils.TC_Dashboard import TC_Dashboard

log = Logger(__name__, logging.INFO)

WelcomeHeading = "Track, analyze and report all content displayed on the display."
display_count = configReader.getTestData("TestData", "Display_Count")
jio_Help_URL = configReader.getTestData("TestData", "help_url")
env = configReader.getTestData("TestData", "Environment")



class TestDashboard(BaseTest):
    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()
        homepage = HomePage(self.driver)



    # @pytest.fixture(scope="class", autouse=True)
    # def test_emptyTrash(self):
    #     self.driver.refresh()
    #     homepage = HomePage(self.driver)
    #     homepage.goToDash().clearTrashImages().clearTrashAudios().clearTrashDocuments().clearTrashVideos()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifySignageWelcomePage(self):
        log.logger.info(str(TC_Dashboard(2)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert "True" in homepage.verifySignageHome()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyWelcomeHeading(self):
        log.logger.info(str(TC_Dashboard(4)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert WelcomeHeading in homepage.gotoDashboard().verifyWelcomeMsg()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_signageLogo(self):
        log.logger.info(str(TC_Dashboard(5)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert WelcomeHeading in homepage.clickOnSignageHome().verifyWelcomeMsg()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyDisplayCount(self):
        log.logger.info(str(TC_Dashboard(6)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert homepage.gotoDashboard().verifyDisplayCount() is not None

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyUsedDisplayCount(self):
        log.logger.info(str(TC_Dashboard(8)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        # code changes by shivaji -- added getDisplayOnDash()
        used_display = homepage.gotoDashboard().getDisplayOnDash().get_used_display_count()
        log.logger.info("used_display : " + str(used_display))
        display_dashboard = homepage.gotoDashboard().verifyUsedDisplayCount()
        log.logger.info("display_dashboard : " + str(display_dashboard))
        assert used_display == display_dashboard
        homepage.goToDash().delete_display_1()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyUsedStorage(self):
        log.logger.info(str(TC_Dashboard(11)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        storage = homepage.gotoDashboard().getUsedServerStorage()
        used_storage = homepage.gotoDashboard().verifyUsedStorage()
        assert storage == used_storage

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyStorageLink(self):
        log.logger.info(str(TC_Dashboard(15)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert "Service Plan" in homepage.gotoDashboard().redirectToStorage()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verify_serverUsage(self):
        log.logger.info(str(TC_Dashboard(16)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        total_storage = homepage.gotoDashboard().getTotalServerStorage()
        with check:
            assert total_storage != "0"
        used_storage = homepage.gotoDashboard().getUsedServerStorage()
        with check:
            assert used_storage != "0"
        with check:
            per_value = homepage.gotoDashboard().getUsedStoragePerValue()
            per_storage_usage = round(int(used_storage) / int(total_storage) * 100)
            f_storage = str(per_storage_usage) + "%"
            assert per_value == f_storage

    @pytest.mark.FOCUSED
    def test_verify_media_uploaded_location(self):
        log.logger.info(str(TC_Dashboard(17)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        isvisible = homepage.gotoDashboard().verifyMediaUploadLoc()
        if isvisible == "True":
            assert True
        else:
            assert False

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyUploadedImagesCount(self):
        log.logger.info(str(TC_Dashboard(19)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashImages()
        with check:
            # code change by shivaji
            images_count_on_dash = homepage.gotoDashboard().uploadImageForTesting().getTotalImagesCountOnDash()
            images_count_on_page = homepage.gotoDashboard().getImgCount()
            assert int(images_count_on_dash) == int(images_count_on_page)
        # with check:
        #     assert int(images_count) == homepage.gotoDashboard().getJpegPngImagesCount()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyUploadedVideoCount(self):
        log.logger.info(str(TC_Dashboard(20)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashVideos()
        with check:
            videos_count_on_dash = homepage.gotoDashboard().uploadVideoForTesting().getTotalVideosCount()
            videos_count_on_page = homepage.gotoDashboard().getVideoCount()
            assert int(videos_count_on_dash) == int(videos_count_on_page)
        with check:
            assert int(videos_count_on_dash) == homepage.gotoDashboard().getVideos()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyUploadedDocCount(self):
        log.logger.info(str(TC_Dashboard(21)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashDocuments()
        with check:
            doc_count_on_dash = homepage.gotoDashboard().uploadDocForTesting().getTotalDocCount()
            doc_count_on_page = homepage.gotoDashboard().getDocumentCount()
            assert int(doc_count_on_dash) == int(doc_count_on_page)
        # with check:
        #     assert int(doc_count_on_dash) == homepage.gotoDashboard().getDoc()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyUploadAudioCount(self):
        log.logger.info(str(TC_Dashboard(22)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashAudios()
        with check:
            audio_count = homepage.gotoDashboard().uploadAudioForTesting().getTotalAudioCount()
            totalRows = homepage.gotoDashboard().getAudioCounts()
            assert int(audio_count) == int(totalRows)
        # with check:
        #     assert int(audio_count) == homepage.gotoDashboard().getAudio()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_verifyImageUpload(self):
        log.logger.info(str(TC_Dashboard(23)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashImages()
        with check:
            homepage.gotoDashboard().checkForImage()
            image_count_before_upload = homepage.gotoDashboard().getImgCount()
            image_count_after_upload = homepage.gotoDashboard().verifyImageUpload()
            assert image_count_before_upload < image_count_after_upload
        homepage.goToDash().delImage()

    @pytest.mark.FOCUSED
    def test_verifyDeleteImage(self):
        log.logger.info(str(TC_Dashboard(24)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashImages()
        with check:
            homepage.gotoDashboard().check_if_image_present()
            image_count_before_delete = homepage.ClickDashboard().getImgCount()
            image_count_after_delete = homepage.ClickDashboard().deleteImage()
            assert image_count_before_delete > image_count_after_delete

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_verifyVideoUpload(self):
        log.logger.info(str(TC_Dashboard(25)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashVideos()
        with check:
            homepage.gotoDashboard().checkForVideo()
            video_count_before_upload = homepage.gotoDashboard().getVideoRow()
            video_count_after_upload = homepage.gotoDashboard().uploadVideo()
            assert video_count_before_upload < video_count_after_upload
        homepage.goToDash().delVideo()

    @pytest.mark.FOCUSED
    def test_verifyVideoCountAfterDelete(self):
        log.logger.info(str(TC_Dashboard(26)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashVideos()
        homepage.gotoDashboard().checkForVideo_ifPresent()
        video_count_before_delete = homepage.gotoDashboard().getVideoCount()
        video_count_after_delete = homepage.gotoDashboard().deleteVideo()
        assert video_count_before_delete > video_count_after_delete

    @pytest.mark.FOCUSED
    def test_verifyUploadAudioContent(self):
        log.logger.info(str(TC_Dashboard(27)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashAudios()
        with check:
            homepage.gotoDashboard().checkForAudioFile()
            audio_count_before_upload = homepage.gotoDashboard().getAudioCount()
            audio_count_after_upload = homepage.gotoDashboard().verifyAudioUpload()
            assert audio_count_before_upload < audio_count_after_upload
        homepage.goToDash().delAudio()

    @pytest.mark.FOCUSED
    def test_verifyDeleteAudio(self):
        log.logger.info(str(TC_Dashboard(28)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().checkForAudioFile()
        homepage.gotoDashboard().checkForAudio_ifPresent()
        audio_count_before_delete = homepage.gotoDashboard().getAudioCount()
        audio_count_after_delete = homepage.gotoDashboard().deleteAudio()
        assert audio_count_before_delete > audio_count_after_delete

    @pytest.mark.FOCUSED
    def test_verifyUploadDocContent(self):
        log.logger.info(str(TC_Dashboard(29)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashDocuments()
        with check:
            homepage.gotoDashboard().checkForDoc_ifPresent()
            doc_count_before_upload = homepage.gotoDashboard().getDocCount()
            log.logger.info("doc_count_before_upload " + doc_count_before_upload)
            doc_count_after_upload = homepage.gotoDashboard().verifyDocumentUpload()
            log.logger.info("doc_count_after_upload " + doc_count_after_upload)
            assert doc_count_before_upload < doc_count_after_upload
        homepage.goToDash().delDoc()

    @pytest.mark.FOCUSED
    def test_verifyDeleteDocument(self):
        log.logger.info(str(TC_Dashboard(30)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().clearTrashDocuments()
        homepage.gotoDashboard().checkForDoc_isPresent().DocUpload()
        doc_count_before_delete = homepage.gotoDashboard().getDocCount()
        log.logger.info("doc_count_before_delete : " + doc_count_before_delete)
        doc_count_after_delete = homepage.gotoDashboard().deleteDocument()
        log.logger.info("doc_count_after_delete : " + doc_count_after_delete)
        assert doc_count_before_delete != doc_count_after_delete

    # @pytest.mark.FOCUSED
    # def test_contentBox_location(self):
    #     log.logger.info(str(TC_Dashboard(31)))
    #     homepage = HomePage(self.driver)
    #     homepage.gotoDashboard().switchToHead()
    #     isvisible = homepage.gotoDashboard().verifyMediaUploadLoc()
    #     if isvisible == "True":
    #         assert True
    #     else:
    #         assert False

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_getContentCount(self):
        log.logger.info(str(TC_Dashboard(32)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        total_content = homepage.gotoDashboard().getAllContentCount()
        total_content_dash = homepage.gotoDashboard().getContentCountOnDash()
        assert total_content == total_content_dash

    @pytest.mark.FOCUSED
    def test_verify_7_days_expire_content(self):
        log.logger.info(str(TC_Dashboard(35)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().createContent2()
        size = homepage.gotoDashboard().get_7Days_content()
        log.logger.info("Size is : " + str(size))
        content_dash = homepage.gotoDashboard().verify_7Days_content()
        log.logger.info("Size is : " + str(content_dash))
        assert int(size) == int(content_dash)
        homepage.goToDash().deleteContent()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verify_expired_content(self):
        log.logger.info(str(TC_Dashboard(36)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().createContent1()
        size = homepage.gotoDashboard().get_expired_content()
        content_dash = homepage.gotoDashboard().verify_expired_content()
        assert int(size) == int(content_dash)
        homepage.goToDash().deleteContent()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verify_7_days_expire_content_url(self):
        log.logger.info(str(TC_Dashboard(37)))
        global URL
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        homepage.goToDash().createContent3()
        with check:
            if configReader.getTestData("TestData", "Environment") == "prod":
                URL = configReader.getTestData("TestData", "content_expire_7_days_prod_url")
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                URL = configReader.getTestData("TestData", "content_expire_7_days_preprod_url")
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                URL = configReader.getTestData("TestData", "content_expire_7_days_sit1_url")
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                URL = configReader.getTestData("TestData", "content_expire_7_days_sit2_url")
            current_url = homepage.gotoDashboard().verify_7_days_content_expire_url()
            assert URL == current_url
        with check:
            size = homepage.gotoDashboard().get_7Days_content()
            content_dash = homepage.gotoDashboard().verify_7Days_content()
            assert int(size) == int(content_dash)
        homepage.goToDash().deleteContent()

    @pytest.mark.FOCUSED
    def test_verify_expired_content_url(self):
        log.logger.info(str(TC_Dashboard(38)))
        global expired_url
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            if configReader.getTestData("TestData", "Environment") == "prod":
                expired_url = configReader.getTestData("TestData", "content_expired_prod_url")
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                expired_url = configReader.getTestData("TestData", "content_expired_preprod_url")
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                expired_url = configReader.getTestData("TestData", "content_expired_sit1_url")
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                expired_url = configReader.getTestData("TestData", "content_expired_sit2_url")
            get_current_url = homepage.gotoDashboard().verify_content_expired_url()
            assert expired_url == get_current_url
        with check:
            size = homepage.gotoDashboard().get_expired_content()
            content_dash = homepage.gotoDashboard().verify_expired_content()
            assert size == content_dash

    @pytest.mark.FOCUSED
    def test_verify_content_count_after_add(self):
        log.logger.info(str(TC_Dashboard(41)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        total_content = homepage.gotoDashboard().getAllContentCount()
        total_content_after_add = homepage.gotoDashboard().verifyContentAfterAdd()
        assert total_content < total_content_after_add

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_PlaylistBox_location(self):
        log.logger.info(str(TC_Dashboard(42)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        isvisible = homepage.gotoDashboard().verifyPlaylistLoc()
        if isvisible == "True":
            assert True
        else:
            assert False

    ########### add code to add playlist ########
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verify_PlaylistCount(self):
        log.logger.info(str(TC_Dashboard(43)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        count_text = homepage.gotoDashboard().getPlaylistCount()
        count = homepage.gotoDashboard().getPlaylistDetail()
        assert count_text == count

    # def test_verifyTotalMediaCount(self):
    #     log.logger.info(str(TC_Dashboard(18)))
    #     homepage = HomePage(self.driver)
    #     homepage.gotoDashboard().switchToHead()
    #     mc = homepage.gotoDashboard().getTotalUploadedCount()
    #     with check:
    #         material_count = homepage.gotoDashboard().get_allMaterialCount()
    #         assert material_count == mc
    #     with check:
    #         total_material_count = homepage.gotoDashboard().allContentMaterialCount()
    #         assert total_material_count == mc
    @pytest.mark.FOCUSED
    def test_stateWIseDisplay_location(self):
        log.logger.info(str(TC_Dashboard(68)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        isvisible = homepage.gotoDashboard().verifyStateWiseDisplayLoc()
        if isvisible == "True":
            assert True
        else:
            assert False

    @pytest.mark.FOCUSED
    def test_TagWIseDisplay_location(self):
        log.logger.info(str(TC_Dashboard(56)))
        homepage = HomePage(self.driver)
        isvisible = homepage.gotoDashboard().verifyTagWiseDisplayLoc()
        if isvisible == "True":
            assert True
        else:
            assert False

    @pytest.mark.FOCUSED
    def test_verifyUsedRemainingLicense(self):
        log.logger.info(str(TC_Dashboard(9)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        licence1 = homepage.gotoDashboard().verifyUsedRemainingLicense()
        licence2 = homepage.gotoDashboard().getDisplayCountOnDash()
        assert licence1 == licence2

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyUsedRemainStorage(self):
        log.logger.info(str(TC_Dashboard(10)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        storage1 = homepage.gotoDashboard().verifyStorageDetails()
        storage2 = homepage.gotoDashboard().getStorageOnDash()
        assert storage1 == storage2

    @pytest.mark.FOCUSED
    def test_verifyDisplayStatusLocation(self):
        log.logger.info(str(TC_Dashboard(46)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        isvisible = homepage.gotoDashboard().verifyDisplayStatusLocation()
        if isvisible == "True":
            assert True
        else:
            assert False

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyDisplayStatusCount(self):
        log.logger.info(str(TC_Dashboard(47)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        total_used_license = homepage.gotoDashboard().getTotalLicense()
        total_used_display = homepage.gotoDashboard().verifyDisplayStatusCount()
        assert total_used_license == total_used_display, "Display count is mismatching on display status box"
    

    @pytest.mark.FOCUSED
    def test_verifyOnlineOfflineDisplay(self):
        log.logger.info(str(TC_Dashboard(49)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            online_display_count_at_DM = homepage.gotoDashboard().getOnlineDisplayAtDM()
            online_display_count_at_DB = homepage.gotoDashboard().getOnlineDisplayCount()
            assert online_display_count_at_DM == online_display_count_at_DB
        with check:
            offline_display_count_at_DM = homepage.gotoDashboard().getOfflineDisplayAtDM()
            offline_display_count_at_DB = homepage.gotoDashboard().getOfflineDisplayCount()
            assert offline_display_count_at_DM == offline_display_count_at_DB

    @pytest.mark.FOCUSED
    def test_verifySchedulesLocation(self):
        log.logger.info(str(TC_Dashboard(50)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        isvisible = homepage.gotoDashboard().verifySchedulesLocation()
        if isvisible == "True":
            assert True
        else:
            assert False

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifyTotalSchedules(self):
        log.logger.info(str(TC_Dashboard(51)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        total_scheduled = homepage.gotoDashboard().getTotalSchedules()
        schedule_count_on_DB = homepage.gotoDashboard().getScheduleCountOnDashboard()
        assert total_scheduled == schedule_count_on_DB

    @pytest.mark.FOCUSED
    def test_JioHelp(self):
        log.logger.info(str(TC_Dashboard(110)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert jio_Help_URL == homepage.gotoDashboard().verifyJioHelp()

    @pytest.mark.FOCUSED
    def test_verifyFAQ(self):
        log.logger.info(str(TC_Dashboard(112)))
        global faq_url
        if configReader.getTestData("TestData", "Environment") == "prod":
            faq_url = configReader.getTestData("TestData", "faq_prod_url")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            faq_url = configReader.getTestData("TestData", "faq_preprod_url")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            faq_url = configReader.getTestData("TestData", "faq_sit1_url")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            faq_url = configReader.getTestData("TestData", "faq_sit2_url")
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            assert faq_url == homepage.gotoDashboard().verifyFAQ()
        with check:
            if configReader.getTestData("TestData", "Environment") == "prod" or\
                    configReader.getTestData("TestData", "Environment") == "pre-prod":
                result = homepage.gotoDashboard().verifyFAQOptions()
                assert result[0] == "JioSignage"
                assert result[1] == "Display"
                assert result[2] == "Trouble Shooting"
                #assert result[3] == "Layout"
                assert result[3] in ["Layout", "Content"]
                assert result[4] == "Proof of Play"
           

    @pytest.mark.FOCUSED
    def test_JioHelpOnProfile(self):
        log.logger.info(str(TC_Dashboard(110)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert jio_Help_URL == homepage.gotoDashboard().verifyJioHelpOnProfile()

    @pytest.mark.FOCUSED
    def test_verifyUpdateMismatchPas(self):
        log.logger.info(str(TC_Dashboard(106)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        message = homepage.gotoDashboard().verifyUpdateMismatchPass()
        assert message == "doesn't match confirmation"

    @pytest.mark.FOCUSED
    def test_verifyCrossOnEditPassword(self):
        log.logger.info(str(TC_Dashboard(108)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert "" == homepage.gotoDashboard().verifyCrossOnEditPassword()

    @pytest.mark.FOCUSED
    def test_verifyCrossOnEditPhoneNum(self):
        log.logger.info(str(TC_Dashboard(104)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        assert "" == homepage.gotoDashboard().verifyCrossOnEditPhoneNum()

    # @pytest.mark.FOCUSED
    # # @pytest.mark.skipif(env == 'prod', reason="Content approval is disable for Prod")
    # def test_verifyApprovedContentCount(self):
    #     log.logger.info(str(TC_Dashboard(33)))
    #     homepage = HomePage(self.driver)
    #     homepage.gotoDashboard().switchToHead()
    #     approved_count = homepage.gotoDashboard().verifyApprovedContentCount()
    #     approved_count_ds = homepage.gotoDashboard().ApprovedContentCount()
    #     #MANUAL TESTING REQUIRED
    #     assert approved_count_ds == approved_count

    # @pytest.mark.FOCUSED
    # def test_verifyPendingApprovalContentCount(self):
    #     log.logger.info(str(TC_Dashboard(40)))
    #     homepage = HomePage(self.driver)
    #     homepage.gotoDashboard().switchToHead()
    #     pending_approval_count = homepage.gotoDashboard().verifyPendingApprovedContentCount()
    #     pending_count_ds = homepage.gotoDashboard().verifyPendingContentCount()
    #     assert pending_approval_count == pending_count_ds

    @pytest.mark.FOCUSED
    def test_verifyProfileOptions(self):
        log.logger.info(str(TC_Dashboard(99)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        profile = homepage.gotoDashboard().verifyProfileOptions()
        assert profile is not None

    @pytest.mark.FOCUSED
    def test_verifyServicePlan(self):
        log.logger.info(str(TC_Dashboard(109)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            service_plan = homepage.gotoDashboard().verifyServicePlan()
            assert service_plan is not None
        with check:
            server_usage = homepage.gotoDashboard().verifyServerUsagePlan()
            assert server_usage is not None
        with check:
            display_status = homepage.gotoDashboard().verifyDisplayStatusPlan()
            assert display_status is not None

    @pytest.mark.FOCUSED
    def test_verifyOkCancelButtonOnChangeAccount(self):
        log.logger.info(str(TC_Dashboard(98)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().createBaseAcc1()
        with check:
            current_acc = homepage.gotoDashboard().checkForAccount()
            switched_acc = homepage.gotoDashboard().verifyOkOptionOnSwitchToBaseAccount()
            assert current_acc != switched_acc
        with check:
            current_account = homepage.gotoDashboard().checkForAccount()
            switched_account = homepage.gotoDashboard().verifyCancelOptionOnSwitchToBaseAccount()
            assert current_account == switched_account

    @pytest.mark.FOCUSED
    def test_verifyChangeBaseAccount(self):
        log.logger.info(str(TC_Dashboard(96)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().createBaseAcc2()
        with check:
            current_acc = homepage.gotoDashboard().checkForAccount()
            switched_acc = homepage.gotoDashboard().verifySwitchToBaseAccount()
            assert current_acc != switched_acc


    @pytest.mark.FOCUSED
    def test_getStorageDataFromCanvas(self):
        log.logger.info(str(TC_Dashboard(12)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            total_storage = homepage.gotoDashboard().GetTotalStorage()
            total_used_storage = homepage.gotoDashboard().GetTotalUsedStorage()
            bal_storage = int(total_storage) - int(total_used_storage)
            remain_storage = homepage.gotoDashboard().getStorageDataFromCanvas()
            remain_storage_int = int(remain_storage)
            assert abs(bal_storage - remain_storage_int) == 1, f"Test failed: {bal_storage} != {remain_storage_int}"

    @pytest.mark.FOCUSED
    def test_verifySaveCancelOptionOnChangeName(self):
        log.logger.info(str(TC_Dashboard(101)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            userName = homepage.gotoDashboard().getUserName()
            assert userName != homepage.gotoDashboard().verifySaveOptionOnChangeName()
        with check:
            userName = homepage.gotoDashboard().getUserName()
            assert userName == homepage.gotoDashboard().verifyCancelOptionOnChangeName()
        with check:
            isvisible = homepage.gotoDashboard().verifyCancelOption()
            if isvisible == 0:
                assert True
            else:
                assert False

    @pytest.mark.FOCUSED
    def test_verifySaveCancelOptionOnChangePhone(self):
        log.logger.info(str(TC_Dashboard(103)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            original_number = homepage.gotoDashboard().getOriginalNumber()
            assert original_number != homepage.gotoDashboard().verifySaveOptionOnNumberChange()
        with check:
            num = homepage.gotoDashboard().getMobileNumber()
            assert num == homepage.gotoDashboard().verifyCancelOptionOnUpdateMobile()
        homepage.gotoDashboard().updateOriginalNum(original_number)

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyPrivacyPolicy(self):
        log.logger.info(str(TC_Dashboard(114)))
        global privacy_url
        if configReader.getTestData("TestData", "Environment") == "prod":
            privacy_url = configReader.getTestData("TestData", "privacy_policy_prod_url")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            privacy_url = configReader.getTestData("TestData", "privacy_policy_preprod_url")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            privacy_url = configReader.getTestData("TestData", "privacy_policy_sit1_url")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            privacy_url = configReader.getTestData("TestData", "privacy_policy_sit2_url")
        with check:
            homepage = HomePage(self.driver)
            homepage.gotoDashboard().switchToHead()
            assert privacy_url == homepage.gotoDashboard().verifyPrivacyPolicy()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyTermsAndConditions(self):
        log.logger.info(str(TC_Dashboard(115)))
        global tc_url
        if configReader.getTestData("TestData", "Environment") == "prod":
            tc_url = configReader.getTestData("TestData", "tc_prod_url")
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            tc_url = configReader.getTestData("TestData", "tc_preprod_url")
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            tc_url = configReader.getTestData("TestData", "tc_sit1_url")
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            tc_url = configReader.getTestData("TestData", "tc_sit2_url")
        with check:
            homepage = HomePage(self.driver)
            homepage.gotoDashboard().switchToHead()
            assert tc_url == homepage.gotoDashboard().verifyTermsAndConditions()

    @pytest.mark.FOCUSED
    def test_logout(self):
        log.logger.info(str(TC_Dashboard(111)))
        homepage = HomePage(self.driver)
        homepage.gotoDashboard().switchToHead()
        with check:
            if configReader.getTestData("TestData", "Environment") == "prod":
                url = configReader.getTestData("TestData", "prod_sign_in_url")
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                url = configReader.getTestData("TestData", "preprod_sign_in_url")
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                url = configReader.getTestData("TestData", "sit2_sign_in_url")
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                url = configReader.getTestData("TestData", "sit1_sign_in_url")
            assert url == homepage.gotoDashboard().verifyLogout()
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

        homepage.gotoDashboard().switchToHead()

        #######additional Tc ##############

    # @pytest.mark.DEMO
    # @pytest.mark.FOCUSED
    # @pytest.mark.SANITY
    # def test_Displaydisconnected_dashboard(self):
    #     log.logger.info(str(TC_Dashboard(122)))
    #     with check:
    #         homepage = HomePage(self.driver)
    #         ele = homepage.gotoDashboard().gotoDeliveryMgmt().clickOnHDMIOpt()
    #         ele1 = ele.clickondisconnected().getcountdisconnected()
    #         time.sleep(2)
    #         ele2 = homepage.gotoDashboard().getcountdisconnecteddashboard()
    #         time.sleep(2)
    #         if ele1 == ele2:
    #             assert True
    #         else:
    #             assert False

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_verifytagwisecount(self):
        log.logger.info(str(TC_Dashboard(123)))
        with check:
            homepage = HomePage(self.driver)
            homepage.gotoDashboard().switchToHead()
            homepage.goToDash().createDisplay_2().addTagToDisplay()
            ele = homepage.ClickDashboard().gotoDeliveryMgmt().clickOnTagWiseOpt()
            self.driver.refresh()
            ele1 = homepage.ClickDashboard().getcounttagwise()
            if ele == ele1:
                assert True
            else:
                assert False
        homepage.goToDash().delete_display_2()

    @pytest.mark.SMOKE
    @allure.description("Verify display count increase on Dashboard after adding new display from Display page.")
    def test_DisplayCountAfterAdded(self):
        # log.logger.info(str(TC_Dashboard(124)))
        with check:
            homepage = HomePage(self.driver)
            homepage.gotoDashboard().switchToHead()
            BeforeDisplayCount = homepage.gotoDashboard().ReturnDisplayCount()
            homepage.ClickDashboard().CreateDisplay()
            AfterDisplayAddedCount = homepage.ClickDashboard().ReturnDisplayCount()
            assert int(BeforeDisplayCount)+1 == int(AfterDisplayAddedCount), "Display count is not increased in dashboard after Created"

    # @pytest.mark.SANITY
    # def test_raiseTicket(self):
    #     with check:
    #         homepage = HomePage(self.driver)
    #         homepage.gotoDashboard().switchToHead()
    #         db = homepage.gotoDashboard()
    #         db.goToRaiseTicket().fillRaiseTicketInfoAndSubmit()
    #         assert db.verifyTicketIsRaised(), "Not able to raise ticket"
    # added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_informationCards(self):
        with check:
            homepage = HomePage(self.driver)
            homepage.gotoDashboard().switchToHead()
            db = homepage.gotoDashboard()
            assert db.verifyCard_DisplayLicence(), "Display Licence card is not available on dashboard"
        with check:
            assert db.verifyCard_Storage(), "Storage Status card is not available on dashboard"
        with check:
            assert db.verifyCard_DisplayStatus(), "Display Status card is not available on dashboard"
        with check:
            assert db.verifyCard_CableStatus(), "Cable Status card is not available on dashboard"
        with check:
            assert db.verifyCard_MediaUploaded(), "Media Uploaded card is not available on dashboard"
        with check:
            assert db.verifyCard_Layout(), "Layout card is not available on dashboard"
        with check:
            assert db.verifyCard_Playlists(), "Playlists card is not available on dashboard"
        with check:
            assert db.verifyCard_Schedules(), "Schedules card is not available on dashboard"
        with check:
            assert db.verifyCard_DisplayOfflineSince(), "Display offline since card is not available on dashboard"
        with check:
            assert db.verifyCard_TagWiseDisplay(), "Tag wise Display card is not available on dashboard"
        with check:
            assert db.verifyCard_StateWiseDisplay(), "State wise Display card is not available on dashboard"
        with check:
            assert db.verifyCard_CityWiseDisplay(), "City wise Display card is not available on dashboard"
        with check:
            assert db.verifyCard_LocationWiseDisplay(), "Location wise Display card is not available on dashboard"
