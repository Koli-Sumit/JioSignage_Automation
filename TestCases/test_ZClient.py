import time
import pytest
from pytest_check import check
from Pages.Client import JioSignageClient
from TestCases.BaseTest import BaseTest
import inspect
import allure
from allure_commons.types import AttachmentType
from Utilities import configReader

def save_screenshot(driver, test_name, step):
    allure.attach(driver.get_screenshot_as_png(), name=f"{test_name}_step_{step}",
                  attachment_type=AttachmentType.PNG)

repeat_count = configReader.getTestData("TestData", "iteration")


@pytest.mark.repeat(repeat_count)
@pytest.mark.detailed
class Test_JioSignageClient(BaseTest):
    is_data_deleted = False

    def setup_method(self):
        if not Test_JioSignageClient.is_data_deleted:
            HomePage = JioSignageClient(self.driver)
            HomePage.checkForCurrentAccountTypeProd()
            HomePage.deleteUploadedData()
            HomePage.CreateDisplay().LoginClient()
            HomePage.capture_app_version()
            Test_JioSignageClient.is_data_deleted = True

    @pytest.fixture(autouse=True)
    def test_switchToHead(self):
        HomePage = JioSignageClient(self.driver)
        HomePage.checkForCurrentAccountTypeProd()

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @allure.description("Create display in Display module > Login to JioSignage Client with created display ID")
    def test_LoginCreatedDisplay(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage_PleaseSchedule(
                    "pleaseSchedule.jpg"), "Not able to login created display on client "
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Deliver Playlist to Display")
    def test_deliverPlaylistToDisplay(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage1()
                HomePage.UploadMedia("png").CreateLayoutWithBlankTemplateForImage2()
                HomePage.UploadMedia("jfif").CreateLayoutWithBlankTemplateForImage3()
                HomePage.CreatePlaylistImage1_2_3().CreateScheduleForPlaylist()
                HomePage.AssignCreatedScheduleToDisplay().captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "123.jpg"), "Mismatched in Delivered playlist for content1"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise
        with check:
            try:
                time.sleep(15)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "Tomandjerry.png"), "Mismatched in Delivered playlist for content2"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step2")
                raise
        with check:
            try:
                time.sleep(15)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "jfifimage.jfif"), "Mismatched in Delivered playlist for content3"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step3")
                raise


    @pytest.mark.SANITY_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description(
        "Verify Deliver content Instantly Functionality at display > select display > Assign Schedule > deliver now")
    def test_DeliverNow(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia(
                    "jpg").CreateLayoutWithBlankTemplateForImage().CreateSchedule().AssignCreatedScheduleToDisplay()
                HomePage.captureStbScreenshot()
                assert HomePage.compareImages(), "Not able to deliver content with deliver now option"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description(
        "Verify Deliver later content option at display > select display > Assign Schedule > deliver later")
    def test_DeliverLater(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia(
                    "png").CreateLayoutWithBlankTemplateForImage().CreateSchedule().AssignCreatedScheduleToDisplay_DeliverLater_2Min()
                time.sleep(90)  # Since I have kept deliver later as 2 min
                HomePage.captureStbScreenshot()
                assert HomePage.compareImages(), "Not able to deliver content with deliver later option"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Verify deliver content when existing content is playing on display")
    def test_DeliveryOfContentOnExistingContent(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia(
                    "jpg").CreateLayoutWithBlankTemplateForImage().CreateSchedule().AssignCreatedScheduleToDisplay()
                HomePage.captureStbScreenshot()
                assert HomePage.compareImages(), "Not able to deliver existing content"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia(
                    "png").CreateLayoutWithBlankTemplateForImage().CreateSchedule().AssignCreatedScheduleToDisplay()
                HomePage.captureStbScreenshot()
                assert HomePage.compareImages(), "Not able to deliver content on existing content"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step2")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Delivery Management - Deliver (Assign Schedule-Deliver Now)")
    def test_DisplayStatus_Deliver(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia(
                    "jpg").CreateLayoutWithBlankTemplateForImage().CreateSchedule().AssignCreatedScheduleToDisplay_FromDisplayStatus()
                HomePage.captureStbScreenshot()
                assert HomePage.compareImages(), "Not able to deliver content with deliver option through display status"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Delivery Management - Sync")
    def test_SyncDisplay(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMediaWithExactName(
                    "3frames.mp4").CreateLayoutWithBlankTemplateForVideo_3min().CreateSchedule().AssignCreatedScheduleToDisplay()
                time.sleep(80)
                HomePage.SyncDisplay_FromDisplayStatus().captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "frame1.jpg"), "Not able to sync display from display status"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("To verify delivery the Building In Maintenance Template to monitor")
    def test_EA_BuildingInMaintenance(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.deleteUploadedData_InBetween()
                HomePage.deliverEmgAlert_BuildingInMaintenance()
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "buildingInMaintenance.jpg"), "Not able to deliver Building In Maintenance Template to client"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise


    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Create Smart Playlist and deliver to display")
    def test_smartPlaylist(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage1().CreatePlaylistLayout1()
                HomePage.UploadMedia("png").CreateLayoutWithBlankTemplateForImage2().CreatePlaylistLayout2()
                HomePage.UploadMedia("jfif").CreateLayoutWithBlankTemplateForImage3().CreatePlaylistLayout3()
                HomePage.CreateSmartPlaylistForPlaylist1_2_3().CreateScheduleForSmartPlaylist()
                HomePage.AssignCreatedScheduleToDisplay().captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "123.jpg"), "Mismatched in Delivered playlist for content1"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise
        with check:
            try:
                time.sleep(15)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "Tomandjerry.png"), "Mismatched in Delivered playlist for content2"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step2")
                raise
        with check:
            try:
                time.sleep(15)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "jfifimage.jfif"), "Mismatched in Delivered playlist for content3"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step3")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Create sub Playlist and deliver to display")
    def test_subPlaylist(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage1().CreatePlaylistLayout1()
                HomePage.UploadMedia("png").CreateLayoutWithBlankTemplateForImage2().CreatePlaylistLayout2()
                HomePage.UploadMedia("jfif").CreateLayoutWithBlankTemplateForImage3().CreatePlaylistLayout3()
                HomePage.CreateSubPlaylistForPlaylist1_2_3().CreateScheduleForSubPlaylist()
                HomePage.AssignCreatedScheduleToDisplay().captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "123.jpg"), "Mismatched in Delivered playlist for content1"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise
        with check:
            try:
                time.sleep(15)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "Tomandjerry.png"), "Mismatched in Delivered playlist for content2"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step2")
                raise
        with check:
            try:
                time.sleep(15)
                HomePage.captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage(
                    "jfifimage.jfif"), "Mismatched in Delivered playlist for content3"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=3)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step3")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Create a new schedule and deliver to display with start and end time")
    def test_scheduleStartEndTime(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.deleteUploadedData_InBetween()
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage()
                HomePage.CreateScheduleForParticularTime().AssignCreatedScheduleToDisplay().captureStbScreenshot_atStartTime()
                assert HomePage.compareImagesWithReferenceImage("123.jpg"), "Mismatched in Delivered schedule at start time"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise
        with check:
            try:
                HomePage.captureStbScreenshot_atEndTime()
                assert HomePage.compareImagesWithReferenceImage("pleaseSchedule.jpg"), "Mismatched in Delivered schedule at end time"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step2")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Create new Trigger and deliver to display")
    def test_triggerFunction(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with (check):
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage1()
                HomePage.UploadMedia("png").CreateLayoutWithBlankTemplateForImage2()
                HomePage.CreateScheduleForTrigger().AssignCreatedScheduleToDisplay().captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage("123.jpg"), "Mismatched in Delivered schedule"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise
        with check:
            try:
                HomePage.captureStbScreenshot_atStartTime()
                assert HomePage.compareImagesWithReferenceImage( "Tomandjerry.png"), "Mismatched in triggered content"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=2)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step2")
                raise
        with check:
            try:
                HomePage.captureStbScreenshot_atEndTime()
                assert HomePage.compareImagesWithReferenceImage( "123.jpg"), "Mismatched in Delivered schedule after trigger over"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=3)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step3")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Verify Deliver Instantly Functionality")
    def test_DeliverInstantly(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage1()
                HomePage.UploadMedia("png").CreateLayoutWithBlankTemplateForImage2()
                HomePage.CreateScheduleForLayout1().AssignCreatedScheduleToDisplay().editScheduleToReplaceLay1WithLay2()
                HomePage.deliveryInstantlyForCreatedDisplay().captureStbScreenshot()
                assert HomePage.compareImagesWithReferenceImage("Tomandjerry.png"), "Mismatched in Delivered schedule"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Verify Live monitoring feature")
    def test_LiveMonitoring(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                HomePage.UploadMedia("jpg").CreateLayoutWithBlankTemplateForImage()
                HomePage.CreateSchedule().AssignCreatedScheduleToDisplay().captureStbScreenshot().getImageFromLiveMonitoring()
                assert HomePage.compareImagesWithReferenceImage("screen_capture_LiveMonitoring.png"), "Mismatched in livemonitoring image"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise

    @pytest.mark.SANITY_CLIENT
    @pytest.mark.SMOKE_CLIENT
    @pytest.mark.FOCUSED_CLIENT
    @allure.description("Delivery Management - Reboot")
    def test_RebootDisplay(self):
        current_method = inspect.currentframe().f_code.co_name
        self.driver.refresh()
        with check:
            try:
                HomePage = JioSignageClient(self.driver)
                time.sleep(5)
                HomePage.RebootDisplay_FromDisplayStatus()
                time.sleep(25)
                assert HomePage.validate_adb_reboot_uptime(), "Not able to reboot display from display status"
            except AssertionError:
                save_screenshot(self.driver, current_method, step=1)
                HomePage.FailedTestcaseCaptureStbScreenshot(f"{current_method}_step1")
                raise