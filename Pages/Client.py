import base64
import glob
import configparser
import os
import time
import subprocess
import logging
import re
from adbutils.errors import AdbError
from uiautomator2.exceptions import AppNotFoundError
from datetime import timedelta, date
from selenium.webdriver.common.by import By
import random
import string
from Pages.BasePage_Client import BasePage
from Utilities.LogUtil import Logger
from selenium.webdriver import ActionChains, Keys
import shutil
import cv2
from Utilities import configReader
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import tempfile
from PIL import Image
import imagehash
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.common.action_chains import ActionChains
import uiautomator2 as u2
log = Logger(__name__, logging.INFO)

class JioSignageClient(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    cwd = os.getcwd()

    SUPPORTED_MEDIA_FORMATS = {
        'jpg': r'\TestData\123.jpg',
        'png': r'\TestData\Tomandjerry.png',
        'gif': r'\TestData\Gifjerry.gif',
        'jfif': r'\TestData\jfifimage.jfif',
        'mp4': r'\TestData\mp4video.mp4',
        'mov': r'\TestData\movvideo.mov',
        'webm': r'\TestData\webmvideo.webm'
    }

#########CORE FUNCTIONS#############START################
    MediaFolderName = "11Automation"
    ContentManager_xpath = (By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[2]")
    ContentManagerMedia_xpath = (By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[2]/ul/li[1]")
    ContentManagerLayout_xpath = (By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[2]/ul/li[2]")
    ContentManagerPlaylist_xpath = (By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[2]/ul/li[3]")
    ContentManagerSchedule_xpath = (By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[2]/ul/li[4]")
    ContentManagerDisplay_xpath = (By.XPATH, "//*[@id='navbarNavDropdown']/ul/li[2]/ul/li[5]")
    MediaPageRootDropdown_xpath = (By.XPATH, "//button[normalize-space()='Root']")
    MediaPageRootDropdownImageSearch_xpath = (By.XPATH, "//input[@id='myInputimage']")
    MediaPageRootDropdownVideoSearch_xpath = (By.XPATH, "//input[@id='myInputvideo']")
    MediaPageRootDropdownSearchResult_xpath = (By.XPATH, f"//a[normalize-space()='{MediaFolderName}']")
    MediaPageNewFolderCreateIcon_xpath = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/a")
    MediaPageNewFolderEnterName_xpath = (By.XPATH, "//input[@name='v2_folder[name]']")
    MediaPageNewFolderCommitOption_xpath = (By.XPATH, "//input[@name='commit']")
    MediaPageFormatDropdownIcon_xpath = (By.XPATH, "//button[normalize-space()='Image']")
    MediaPageFormat_VideoOption_xpath = (By.XPATH, "//a[@href='/v2/materials?type=video']")
    MediaPageAddFolderIcon_xpath = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[2]/a")
    MediaPageText_xpath = (By.XPATH, "//h5[@id='newItemRemoteModalLabel']")
    MediaUploadPlus_xpath = (By.XPATH, "//a[@class='btn btn-add new_button']")
    MediaUploadDropBox_xpath = (By.XPATH, "//input[@aria-label='fui-hidden-input']")
    MediaUploadButton_xpath = (By.XPATH, "//button[@id='uploadBtn']")
    LayoutCreateNewIcon_xpath = (By.XPATH, "//a[@class='btn btn-add new_button']")
    LayoutNameFieldWhileCreating_xpath = (By.XPATH, "//input[@name='v2_content[name]']")
    LayoutBlankTemplate_xpath = (By.XPATH, "//input[@value='1']")
    LayoutCreateButton_xpath = (By.XPATH, "//input[@id='submitButton']")
    LayoutEditMessageClose = (By.XPATH, "//*[@id='dijit_Dialog_16']/div[1]/span[2]")
    LayoutImageIcon_xpath = (By.XPATH, "//span[contains(text(), 'Image (')]/preceding::img[1]")
    LayoutEditPageFolderName_xpath = (By.XPATH, "(//span[@title='11Automation']/preceding::div[2])[1]")
    LayoutEditPageFolderNameVideo_xpath = (By.XPATH, "(//span[@title='11Automation']/preceding::div[2])[2]")
    LayoutEditPageEntireTimeOption_xpath = (By.XPATH, "//button[normalize-space()='Entire screen']")
    LayoutEditPageEntireTimeDurationOption_xpath = (By.XPATH, "//input[@id='slide_duration']")
    LayoutSaveOption_xpath = (By.XPATH, "(//*[normalize-space()='Save'])[1]")
    LayoutCloseOption_xpath = (By.XPATH, "//*[normalize-space()='Close']")
    LayoutTargetElement_xpath = (By.CLASS_NAME, 'dnd_target_element')
    ScheduleCreateIcon_xpath = (By.XPATH, "//a[@class='btn btn-add new_button']")
    ScheduleNameField_xpath = (By.XPATH, "//input[@name='v2_schedule[name]']")
    ScheduleCreateCommit_xpath = (By.XPATH, "//input[@name='commit']")
    ScheduleEditPageLayoutOption_xpath = (By.XPATH, "//h6[normalize-space()='Layout']")
    ScheduleEditPagePlaylistOption_xpath = (By.XPATH, "//h6[normalize-space()='PlayList']")
    ScheduleEditPageSearchIcon_xpath = (By.XPATH, "//input[@id='myInput']")
    PlaylistEditPageSearchIcon_xpath = (By.XPATH, "//input[@id='myPlaylistInput']")
    ScheduleEditPageDropLocationSunday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[2]")
    ScheduleEditPageDropLocationMonday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[3]")
    ScheduleEditPageDropLocationTuesday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[4]")
    ScheduleEditPageDropLocationWednesday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[5]")
    ScheduleEditPageDropLocationThursday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[6]")
    ScheduleEditPageDropLocationFriday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[7]")
    ScheduleEditPageDropLocationSaturday_xpath = (By.XPATH, "//tbody/tr[1]/td/div/div/div/table/tbody/tr/td[8]")
    ScheduleEditPageCloseIcon_xpath = (By.XPATH, "//button[normalize-space()='Close']")
    DisplayCreateIcon_xpath = (By.XPATH, "//a[@class='btn btn-add new_button']")
    DisplayNameFieldWhileCreating_xpath = (By.XPATH, "//input[@name='v2_display[name]']")
    DisplayPasswordFieldWhileCreating_xpath = (By.XPATH, "//input[@id='id_password']")
    DisplayConfirmPasswordFieldWhileCreating_xpath = (By.XPATH, "//input[@name='v2_display[password_confirmation]']")
    DisplayCreateButton_xpath = (By.XPATH, "//input[@name='commit']")
    DisplayPageSearch_xpath = (By.XPATH, "//input[@placeholder='Search...']")
    DisplayFirstCheckbox = (By.XPATH, "//tbody/tr[1]/td[1]//div//input")
    EAFirstCheckbox = (By.XPATH, "//tbody/tr[1]/td[1]//input")
    DisplayAssignScheduleIcon_xpath = (By.XPATH, "//button[@title='Assign Schedule']//img")
    ScheduleColumnInAssignSchedulePopUp_xpath = (By.XPATH, "//*[contains(text(), 'Search Schedule')]")
    SearchbarInAssignSchedulePopUp_xpath = (By.XPATH, "(//input[@class='select2-search__field'])[2]")
    ClickInAssignSchedule_xpath = (By.XPATH, "//input[@name='commit']")
    FirstDisplayId_xpath = (By.XPATH, "//tbody/tr[1]/td[2]")
    # ClientdisplayXpath-----------------------------
    # For resourceId selectors, you can still use resourceId string directly with uiautomator2
    DisplayId_selector = {"resourceId": "com.jio.digitalsignageTv:id/etDeviceId"}
    DisplayPassword_selector = {"resourceId": "com.jio.digitalsignageTv:id/etPassword"}
    LoginButton_selector = {"resourceId": "com.jio.digitalsignageTv:id/btnLogin"}
    WelcomeToJioSignage_selector = {"resourceId": "com.jio.digitalsignageTv:id/tvWelcome"}
    EnvironmentField_selector = {"resourceId": "android:id/text1"}
    rememberMeCheckBox = {"resourceId": "com.android.systemui:id/remember"}

    # For text-based selectors, just use text= argument (instead of UiSelector string)
    PreProdOption_selector = {"text": "PREPROD"}
    Sit2Option_selector = {"text": "SIT2"}
    Sit1Option_selector = {"text": "SIT1"}
    # ------------------------------------------------------------
    searchBar_xpath = (By.XPATH, "//input[@placeholder='Search...']")
    emptyTable_xpath = (By.XPATH, "//td[@class='dataTables_empty']")
    allOption_xpath = (By.XPATH, "//a[@id='toggle-all-rows']")
    moreOption_xpath = (By.XPATH, "//span[@title='Actions']")
    moveToTrash_xpath = (By.XPATH, "//button[@value='Trash']")
    okBtn_Trash_xpath = (By.XPATH, "//button[@value='confirm']")
    trashFolder_xpath = (By.XPATH, "//a[normalize-space()='Trashed']")
    deleteCompletely_xpath = (By.XPATH, "//button[normalize-space()='Delete Completely']")
    LayoutVideoIcon_xpath = (By.XPATH, "//span[contains(text(), 'Video (')]/preceding::img[1]")
    editLayoutBtn_xpath = (By.XPATH, "//span[.='Edit']")
    objectBtn_xpath = (By.XPATH, "//button[normalize-space()='Object']")
    videoObject_xpath = (By.XPATH, "//button[@title='Video']//span")
    fullScreen_xpath = (By.XPATH, "//span[.='Full Screen']")
    LayoutTargetElementForVideo_xpath = (By.XPATH, "(//input[contains(@id,'dijit_form_TextBox')])[2]")
    O_CURRENT_ACCOUNT_TYPE_XPATH = (By.XPATH, "//div[@id='dropdownMenuButton1']//span")
    O_DD_ID =(By.ID, "dropdownMenuButton1")
    O_headSwitch_XPATH =(By.XPATH, "//input[@value='Switch to Head Account']")
#########CORE LOCATORS#############END################
    deliverLater_xpath = (By.XPATH, "//input[@value='deliver_later']")
    deliverTimeTextBox_xpath = (By.XPATH, "//input[@id='deliver_time']")
    timeTB_XPATH = (By.ID, "deliver_time")
    emergencyAlertOptionXPATH = (By.XPATH, "//a[contains(.,'Emergency Alerts')]")
    buildingInMaintenance_XPATH = (By.XPATH, "//p[@title='Building In Maintenance']")
    deliverBtn_XPATH = (By.XPATH, "//button[normalize-space()='Deliver']")
    playlistTB_XPATH = (By.XPATH, "//input[@name='v2_playlist[name]']")
    savePlaylist_XPATH = (By.XPATH, "//button[normalize-space()='Save']")
    savePlaylist_Yes_XPATH= (By.XPATH, "//button[normalize-space()='Yes']")
    displayStatus_XPATH = (By.XPATH, "//a[contains(.,'Display Status')]")
    searchScheduleDisplayStatus_XPATH = (By.XPATH, "//input[@class='select2-search__field']")
    deliverBtn = (By.XPATH, "//input[@value='Deliver']")
    rebootDisplay_XPATH = (By.XPATH, "//button[@title='Reboot']//img")
    syncDisplay_XPATH = (By.XPATH, "//button[@title='Sync']//img")
    okBtn = (By.XPATH, "//button[normalize-space()='OK']")

    ###sanity#####
    smartPlaylistRadio = (By.XPATH, "//label[normalize-space()='Smart Playlist']//preceding-sibling::div//input")
    createdScheduleXpath = (By.XPATH, "//div[@class='fc-event-title-container']")
    triggerBtnXpath = (By.XPATH, "//span[normalize-space()='Trigger']")
    addTriggerBtnXpath = (By.XPATH, "//span[@title='Add Time Trigger']")
    triggerNameXpath = (By.XPATH, "//input[@id='trigger_name']")
    selectLayoutOrPlaylistXpath = (By.XPATH, "//select[@id='trigger_select_content_or_playlist']")
    dailyRadioXpath = (By.XPATH, "//input[@id='trigger_trigger_type_daily']")
    triggerStartDateID = (By.ID, "trigger_start_date")
    triggerEndDateID = (By.ID, "trigger_end_date")
    repeatYesID = (By.ID, "trigger_repeat_true")
    repeatHrsID = (By.XPATH, "//input[@id='hours']")
    repeatMinID = (By.XPATH, "//input[@id='minutes']")
    addTriggerBtnXPATH = (By.CSS_SELECTOR, "input[value='Add']")
    selectLayoutTBXPATH = (By.XPATH, "//span[contains(text(),'Select Layout')]")
    LayoutNameTBXPATH = (By.XPATH, "//span[@class='select2-search select2-search--dropdown']//input[@role='searchbox']")
    deliveryInstantlyXPATH = (By.XPATH, "//button[@title='Deliver Instantly']//img")
    liveMonitoringImageXPATH = (By.XPATH, "//div[@id='remote_modal_body']//img[contains(@class, 'screen_preview')]")
    liveMonitoringXPATH = (By.XPATH, "//a[contains(.,'Live Monitoring')]")
    searchBar_LM_XPATH = (By.XPATH, "//input[@id='search_id']")
    image_LM_XPATH = (By.XPATH, "//img[@class='online_thumb_preview text-center']")
    deleteSchedule = (By.XPATH, "//a[@title='Delete Schedule']")

#########CORE FUNCTIONS#############START################

    def capture_app_version(self):
        val_type = configReader.getTestData("TestData", "validation_type")
        if val_type in ["client_only", "portal_client"]:
            package_name = "com.jio.digitalsignageTv"
            try:
                result = subprocess.check_output(
                    f'adb shell dumpsys package {package_name} --user 0 | findstr versionName',
                    shell=True, text=True
                )
                app_version = result.strip().split("=")[-1]
                config = configparser.ConfigParser()
                config.read('../ConfigurationData/testData.ini')
                if not config.has_section('TestData'):
                    config.add_section('TestData')
                config.set('TestData', 'app_version', f'{app_version}')
                with open('../ConfigurationData/testData.ini', 'w') as configfile:
                    config.write(configfile)
            except subprocess.CalledProcessError:
                return None
        else:
            config = configparser.ConfigParser()
            config.read('../ConfigurationData/testData.ini')
            if not config.has_section('TestData'):
                config.add_section('TestData')
            config.set('TestData', 'app_version', f'Not Available, Since validated only web portal.')
            with open('../ConfigurationData/testData.ini', 'w') as configfile:
                config.write(configfile)
    def UploadMedia(self, Format: str):
        self.refresh_page()
        cwd = os.getcwd()
        global ImageRandomName
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        self.ImageFormat = Format
        ImageOldName = cwd + self.SUPPORTED_MEDIA_FORMATS[Format]
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.{Format}"
        shutil.copy(ImageOldName, imageNewName)
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerMedia_xpath)
        if self.ImageFormat in ["mp4", "webm", "mov"]:
            self.click(self.MediaPageFormatDropdownIcon_xpath)
            self.click(self.MediaPageFormat_VideoOption_xpath)
        folderoption = len(self.driver.find_elements(*self.MediaPageRootDropdown_xpath))
        if folderoption == 1:
            time.sleep(2)
            self.click(self.MediaPageRootDropdown_xpath)
            if Format in ["mp4", "webm", "mov"]:
                self.send_keys(self.MediaPageRootDropdownVideoSearch_xpath, self.MediaFolderName)
            else:
                self.send_keys(self.MediaPageRootDropdownImageSearch_xpath, self.MediaFolderName)
            SearchResult = len(self.driver.find_elements(*self.MediaPageRootDropdownSearchResult_xpath))
            if SearchResult >= 1:
                self.click(self.MediaPageRootDropdownSearchResult_xpath)
            else:
                self.click(self.MediaPageNewFolderCreateIcon_xpath)
                self.send_keys(self.MediaPageNewFolderEnterName_xpath, self.MediaFolderName)
                self.click(self.MediaPageNewFolderCommitOption_xpath)
        else:
            self.click(self.MediaPageNewFolderCreateIcon_xpath)
            self.send_keys(self.MediaPageNewFolderEnterName_xpath, self.MediaFolderName)
            self.click(self.MediaPageNewFolderCommitOption_xpath)
        time.sleep(2)
        self.click(self.MediaUploadPlus_xpath)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.MediaUploadDropBox_xpath))
        self.driver.find_element(*self.MediaUploadDropBox_xpath).send_keys(imageNewName)
        self.click(self.MediaUploadButton_xpath)
        WebDriverWait(self.driver, 60, poll_frequency=0.5).until(EC.invisibility_of_element(self.MediaPageText_xpath))
        self.refresh_page()
        return self

    def UploadMediaWithExactName(self, filename: str):
        self.refresh_page()
        cwd = os.getcwd()
        global ImageRandomName
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        self.ImageFormat = os.path.splitext(filename)[1][1:]
        ImageOldName = os.path.join(cwd, "TestData", filename)
        imageNewName = os.path.join(cwd, "TestData", "Duplicate", f"{ImageRandomName}.{self.ImageFormat}")
        shutil.copy(ImageOldName, imageNewName)
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerMedia_xpath)
        if self.ImageFormat in ["mp4", "webm", "mov"]:
            self.click(self.MediaPageFormatDropdownIcon_xpath)
            self.click(self.MediaPageFormat_VideoOption_xpath)
        folderoption = len(self.driver.find_elements(*self.MediaPageRootDropdown_xpath))
        if folderoption == 1:
            time.sleep(2)
            self.click(self.MediaPageRootDropdown_xpath)
            if self.ImageFormat in ["mp4", "webm", "mov"]:
                self.send_keys(self.MediaPageRootDropdownVideoSearch_xpath, self.MediaFolderName)
            else:
                self.send_keys(self.MediaPageRootDropdownImageSearch_xpath, self.MediaFolderName)
            SearchResult = len(self.driver.find_elements(*self.MediaPageRootDropdownSearchResult_xpath))
            if SearchResult >= 1:
                self.click(self.MediaPageRootDropdownSearchResult_xpath)
            else:
                self.click(self.MediaPageNewFolderCreateIcon_xpath)
                self.send_keys(self.MediaPageNewFolderEnterName_xpath, self.MediaFolderName)
                self.click(self.MediaPageNewFolderCommitOption_xpath)
        else:
            self.click(self.MediaPageNewFolderCreateIcon_xpath)
            self.send_keys(self.MediaPageNewFolderEnterName_xpath, self.MediaFolderName)
            self.click(self.MediaPageNewFolderCommitOption_xpath)
        time.sleep(2)
        self.click(self.MediaUploadPlus_xpath)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.MediaUploadDropBox_xpath))
        self.driver.find_element(*self.MediaUploadDropBox_xpath).send_keys(imageNewName)
        self.click(self.MediaUploadButton_xpath)
        WebDriverWait(self.driver, 60, poll_frequency=0.5).until(EC.invisibility_of_element(self.MediaPageText_xpath))
        self.refresh_page()
        return self

    def CreateLayoutWithBlankTemplateForImage(self):
        self.refresh_page()
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.click(self.LayoutCreateNewIcon_xpath)
        self.send_keys(self.LayoutNameFieldWhileCreating_xpath, LayoutName)
        self.click(self.LayoutBlankTemplate_xpath)
        self.click(self.LayoutCreateButton_xpath)
        time.sleep(2)
        self.driver.find_element(*self.LayoutImageIcon_xpath).click()
        self.click(self.LayoutEditPageFolderName_xpath)
        time.sleep(3)
        ImageNameUploaded = f'{ImageRandomName}.{self.ImageFormat}'
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{ImageNameUploaded}']")
        SourceElement = self.find_element(UploadedImageElement_xpath)
        TargetElement = self.find_element(self.LayoutTargetElement_xpath)
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
            time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.click(self.LayoutSaveOption_xpath)
        time.sleep(2)
        self.click(self.LayoutCloseOption_xpath)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreateSchedule(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedLayoutInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName)
        time.sleep(3)
        Source = self.find_element(CreatedLayoutInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.ScheduleEditPageCloseIcon_xpath)
        return JioSignageClient(self.driver)

    def CreateScheduleForLayout1(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedLayoutInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName1)
        time.sleep(3)
        Source = self.find_element(CreatedLayoutInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.ScheduleEditPageCloseIcon_xpath)
        return JioSignageClient(self.driver)

    def CreateDisplay(self):
        self.refresh_page()
        global DisplayName
        DisplayName = "11AutomationDisplay" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerDisplay_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        self.send_keys(self.DisplayNameFieldWhileCreating_xpath, DisplayName)
        self.send_keys(self.DisplayPasswordFieldWhileCreating_xpath, "Repeated@596")
        self.send_keys(self.DisplayConfirmPasswordFieldWhileCreating_xpath, "Repeated@596")
        self.scroll_to_element(self.DisplayCreateButton_xpath)
        self.click(self.DisplayCreateButton_xpath)
        time.sleep(3)
        self.refresh_page()
        self.wait_for_page_load()
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(2)
        global DisplayID
        DisplayID = self.get_element_text(self.FirstDisplayId_xpath)
        return JioSignageClient(self.driver)

    def AssignCreatedScheduleToDisplay(self):
        self.refresh_page()
        SelectCreatedScheduleDuringAssignSchedule_xpath = (By.XPATH, f"//li[normalize-space()='{ScheduleName}']")
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerDisplay_xpath)
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.DisplayFirstCheckbox)
        self.click(self.DisplayAssignScheduleIcon_xpath)
        self.click(self.ScheduleColumnInAssignSchedulePopUp_xpath)
        self.click(self.SearchbarInAssignSchedulePopUp_xpath)
        self.send_keys(self.SearchbarInAssignSchedulePopUp_xpath, ScheduleName)
        self.click(SelectCreatedScheduleDuringAssignSchedule_xpath)
        self.click(self.ClickInAssignSchedule_xpath)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def AssignCreatedScheduleToDisplay_FromDisplayStatus(self):
        self.refresh_page()
        SelectCreatedScheduleDuringAssignSchedule_xpath = (By.XPATH, f"//li[normalize-space()='{ScheduleName}']")
        self.click(self.displayStatus_XPATH)
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.DisplayFirstCheckbox)
        self.click(self.DisplayAssignScheduleIcon_xpath)
        self.click(self.ScheduleColumnInAssignSchedulePopUp_xpath)
        self.click(self.searchScheduleDisplayStatus_XPATH)
        self.send_keys(self.searchScheduleDisplayStatus_XPATH, ScheduleName)
        self.click(SelectCreatedScheduleDuringAssignSchedule_xpath)
        self.click(self.deliverBtn)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def AssignCreatedScheduleToDisplay_DeliverLater_2Min(self):
        SelectCreatedScheduleDuringAssignSchedule_xpath = (By.XPATH, f"//li[normalize-space()='{ScheduleName}']")
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerDisplay_xpath)
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.DisplayFirstCheckbox)
        self.click(self.DisplayAssignScheduleIcon_xpath)
        self.click(self.ScheduleColumnInAssignSchedulePopUp_xpath)
        self.click(self.SearchbarInAssignSchedulePopUp_xpath)
        self.send_keys(self.SearchbarInAssignSchedulePopUp_xpath, ScheduleName)
        self.click(SelectCreatedScheduleDuringAssignSchedule_xpath)
        self.click(self.deliverLater_xpath)
        self.click(self.deliverLater_xpath)
        dt = datetime.now() + timedelta(minutes=2)
        new_time = dt.strftime("%Y-%m-%dT%H:%M")
        deliver_input = self.find_element(self.timeTB_XPATH)
        self.driver.execute_script("arguments[0].value = arguments[1]", deliver_input, new_time)
        self.click(self.ClickInAssignSchedule_xpath)
        return JioSignageClient(self.driver)

    #Appium
    # def LoginClient(self):
    #     DeviceName = configReader.getTestData("TestData", "DeviceName")
    #     AppLocation = os.getcwd() + configReader.getTestData("TestData", "Package")
    #     Environment = configReader.getTestData("TestData", "environment")
    #     options = UiAutomator2Options()
    #     options.platform_name = "Android"
    #     options.automation_name = "UiAutomator2"
    #     options.device_name = DeviceName
    #     options.app = AppLocation
    #     options.auto_grant_permissions = True
    #     global AppiumDriver
    #     AppiumDriver = webdriver.Remote("http://localhost:4723", options=options)
    #     AppiumDriver.implicitly_wait(10)
    #     time.sleep(2)
    #     Displayid = AppiumDriver.find_element(*self.DisplayId_xpath)
    #     Displayid.click()
    #     Displayid.send_keys(DisplayID)
    #     Displaypassword = AppiumDriver.find_element(*self.DisplayPassword_xpath)
    #     Displaypassword.click()
    #     Displaypassword.send_keys("111111")
    #     if DeviceName == "JSB3000":
    #         AppiumDriver.press_keycode(111)
    #     time.sleep(2)
    #     if Environment == "pre-prod":
    #         Welcometojiosignage = AppiumDriver.find_element(*self.WelcomeToJioSignage_xpath)
    #         for i in range(10):
    #             Welcometojiosignage.click()
    #         time.sleep(3)
    #         AppiumDriver.find_element(*self.EnvironmentField_xpath).click()
    #         AppiumDriver.find_element(*self.PreProdOption_xpath).click()
    #     if Environment == "sit2":
    #         Welcometojiosignage = AppiumDriver.find_element(*self.WelcomeToJioSignage_xpath)
    #         for i in range(10):
    #             Welcometojiosignage.click()
    #         time.sleep(3)
    #         AppiumDriver.find_element(*self.EnvironmentField_xpath).click()
    #         AppiumDriver.find_element(*self.Sit2Option_xpath).click()
    #     if Environment == "sit1":
    #         Welcometojiosignage = AppiumDriver.find_element(*self.WelcomeToJioSignage_xpath)
    #         for i in range(10):
    #             Welcometojiosignage.click()
    #         time.sleep(3)
    #         AppiumDriver.find_element(*self.EnvironmentField_xpath).click()
    #         AppiumDriver.find_element(*self.Sit1Option_xpath).click()
    #
    #
    #     LoginButton = AppiumDriver.find_element(*self.LoginButton_xpath)
    #     LoginButton.click()
    #     try:
    #         LoginButton.click()
    #     except:
    #         pass
    #     time.sleep(3)
    #     client = JioSignageClient(self.driver)
    #     AppiumDriver.quit()
    #     return client

    def get_apk_version(self, apk_path):
        match = re.search(r'(\d+\.\d+\.\d+\.\d+)', os.path.basename(apk_path))
        return match.group(1) if match else None

    def LoginClient(self):
        DeviceName = configReader.getTestData("TestData", "devicename")
        Environment = configReader.getTestData("TestData", "environment")

        # === Get latest APK from TestData/App ===
        app_folder = os.path.join(os.getcwd(), "TestData", "App")
        apk_files = glob.glob(os.path.join(app_folder, "*.apk"))

        if not apk_files:
            raise FileNotFoundError(f"No APK found in {app_folder}")
        elif len(apk_files) == 1:
            AppLocation = apk_files[0]
        else:
            AppLocation = max(apk_files, key=os.path.getmtime)


        # === Connect to device ===
        packageName = "com.jio.digitalsignageTv"
        d = u2.connect()

        # === Uninstall app if exists ===
        try:
            package_info = d.app_info(packageName)
            if package_info.get("packageName"):
                # Try normal uninstall
                uninstall_result = d.adb_shell(f"pm uninstall {packageName}")

                if "Success" not in uninstall_result:

                    uninstall_result = d.adb_shell(f"pm uninstall --user 0 {packageName}")

                if "Success" in uninstall_result:
                    print("✅ Uninstalled successfully.")
                else:
                    print("⚠ Could not uninstall. Will try installing with -d to allow downgrade.")

        except (AppNotFoundError, AdbError):
            print("❌ App not found — skipping uninstall.")

        # === Install APK (with downgrade allowed) ===
        d.adb_device.install(AppLocation, flags=["-r", "-t", "-d"])

        # === Clear data & start app ===
        d.app_clear(packageName)
        d.app_start(packageName)

        command = [
            "adb", "shell", "pm", "grant",
            packageName,
            "android.permission.SYSTEM_ALERT_WINDOW"
        ]

        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            print("Permission granted successfully!")
            time.sleep(1)
            d.app_start(packageName)
        except subprocess.CalledProcessError as e:
            print("Failed to grant permission.")

        time.sleep(6)

        def allow_permissions():
            keywords = [
                "Allow", "While using the app", "Allow all the time",
                "Allow only while using the app", "Allow once", "Allow every time",
                "Start", "Start Now", "Continue", "Next", "Done", "Got it",
                "OK", "Yes", "Grant", "Install", "Confirm"
            ]

            pattern = "(?i)^(" + "|".join(map(re.escape, keywords)) + ")$"

            for _ in range(5):
                try:
                    el = d(textMatches=pattern)
                    if el.exists(timeout=0.3):
                        text_value = el.get_text().strip()

                        # If it's "Start Now", click "Don't show again" first (if present)
                        if re.match("(?i)^Start Now$", text_value):
                            remember_checkbox = d(resourceId="com.android.systemui:id/remember")
                            if remember_checkbox.exists(timeout=0.5):
                                remember_checkbox.click()
                                time.sleep(1)
                        el.click()
                        time.sleep(0.5)
                    else:
                        break
                except Exception:
                    time.sleep(0.2)

        allow_permissions()
        d.wait_timeout = 10
        time.sleep(2)

        d(**self.DisplayId_selector).click()
        d(**self.DisplayId_selector).set_text(DisplayID)

        d(**self.DisplayPassword_selector).click()
        d(**self.DisplayPassword_selector).set_text("Repeated@596")

        time.sleep(1)
        d.press(61)  # Tab Button
        time.sleep(0.5)
        d.press(61)  # Tab Button

        if Environment in ["pre-prod", "sit1", "sit2"]:
            for _ in range(10):
                if d(**self.WelcomeToJioSignage_selector).exists(timeout=3):
                    d(**self.WelcomeToJioSignage_selector).click()
                else:
                    break
            time.sleep(4)

            if not d(**self.EnvironmentField_selector).exists(timeout=10):
                return
            d(**self.EnvironmentField_selector).click()

            if Environment == "pre-prod" and d(**self.PreProdOption_selector).exists(timeout=10):
                d(**self.PreProdOption_selector).click()
            elif Environment == "sit1" and d(**self.Sit1Option_selector).exists(timeout=10):
                d(**self.Sit1Option_selector).click()
            elif Environment == "sit2" and d(**self.Sit2Option_selector).exists(timeout=10):
                d(**self.Sit2Option_selector).click()

        try:
            d(**self.LoginButton_selector).click()
            d(**self.LoginButton_selector).click()
        except:
            pass

        time.sleep(3)
        return JioSignageClient(self.driver)

    def wakeUpApp(self):
        subprocess.run([
            "adb", "shell", "monkey", "-p", "com.jio.digitalsignageTv",
            "-c", "android.intent.category.LAUNCHER", "1"
        ])
        return JioSignageClient(self.driver)


    def captureStbScreenshot(self):
        time.sleep(35)
        cwd = os.getcwd()
        screenshot_path = cwd + r'\TestData\Screenshot\ScreenshotFromClient.jpg'
        device_screenshot_path = "/sdcard/ScreenshotFromClient.jpg"
        subprocess.run(["adb", "shell", "screencap", "-p", device_screenshot_path])
        subprocess.run(["adb", "pull", device_screenshot_path, screenshot_path])
        return JioSignageClient(self.driver)

    def compareImages(self, threshold=10):
        cwd = os.getcwd()
        img1_path = cwd + self.SUPPORTED_MEDIA_FORMATS[self.ImageFormat]
        img2_path = cwd + r'\TestData\Screenshot\ScreenshotFromClient.jpg'
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)
        hash1 = imagehash.phash(img1)
        hash2 = imagehash.phash(img2)
        diff = abs(hash1 - hash2)
        if diff < threshold:
            return True
        else:
            return False

    def captureStbVideo(self, duration=30):
        time.sleep(35)
        cwd = os.getcwd()
        video_path = cwd + r'\TestData\Screenshot\VideoFromClient.mp4'
        device_video_path = "/sdcard/VideoFromClient.mp4"
        subprocess.run(["adb", "shell", "screenrecord", "--time-limit", str(duration), f"{device_video_path}"])
        subprocess.run(["adb", "pull", device_video_path, video_path])
        return JioSignageClient(self.driver)

    def extract_and_hash_frames(self, video_path, interval_sec=5):
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        if fps == 0:  # Fallback
            fps = 25
        interval = int(fps * interval_sec)
        count = 0
        frames = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if count % interval == 0:
                frames.append(frame.copy())
            count += 1
        cap.release()

        # Parallel hash computation
        def compute_hash(frame):
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).resize((256, 256))
            return imagehash.phash(img)

        with ThreadPoolExecutor() as executor:
            hashes = list(executor.map(compute_hash, frames))

        return hashes

    def compareVideos(self, interval_sec=2, threshold=15, window_size=3, thresholdPercentage=90.00):
        cwd = os.getcwd()
        ref_video = cwd + self.SUPPORTED_MEDIA_FORMATS[self.ImageFormat]
        stb_video = cwd + r'\TestData\Screenshot\VideoFromClient.mp4'

        ref_hashes = self.extract_and_hash_frames(ref_video, interval_sec)
        stb_hashes = self.extract_and_hash_frames(stb_video, interval_sec)

        if not ref_hashes or not stb_hashes:
            print("No frames to compare")
            return False

        max_match_percent = 0

        for i in range(len(ref_hashes) - window_size + 1):
            window_ref = ref_hashes[i:i + window_size]
            for j in range(len(stb_hashes) - window_size + 1):
                window_stb = stb_hashes[j:j + window_size]
                match = sum(1 for h1, h2 in zip(window_ref, window_stb) if abs(h1 - h2) < threshold)
                match_percent = (match / window_size) * 100
                max_match_percent = max(max_match_percent, match_percent)

        print(f"Max Match %: {max_match_percent:.2f}")
        return max_match_percent >= thresholdPercentage

    def CreateLayoutWithBlankTemplateForVideo(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.click(self.LayoutCreateNewIcon_xpath)
        self.send_keys(self.LayoutNameFieldWhileCreating_xpath, LayoutName)
        self.click(self.LayoutBlankTemplate_xpath)
        self.click(self.LayoutCreateButton_xpath)
        time.sleep(2)
        self.driver.find_element(*self.LayoutVideoIcon_xpath).click()
        self.click(self.LayoutEditPageFolderNameVideo_xpath)
        time.sleep(3)
        ImageNameUploaded = f'{ImageRandomName}.{self.ImageFormat}'
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{ImageNameUploaded}']")
        SourceElement = self.find_element(UploadedImageElement_xpath)
        self.click(self.editLayoutBtn_xpath)
        self.click(self.objectBtn_xpath)
        self.click(self.videoObject_xpath)
        self.scroll_to_element(self.fullScreen_xpath)
        self.click(self.fullScreen_xpath)
        TargetElement = self.find_element(self.LayoutTargetElementForVideo_xpath)
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
        time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.click(self.LayoutEditPageEntireTimeOption_xpath)
        durationbox = self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath)
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath).send_keys(Keys.BACKSPACE)
        self.send_keys(self.LayoutEditPageEntireTimeDurationOption_xpath, "35.0")
        time.sleep(3)
        self.click(self.LayoutSaveOption_xpath)
        self.click(self.LayoutSaveOption_xpath)
        time.sleep(2)
        self.click(self.LayoutCloseOption_xpath)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreateLayoutWithBlankTemplateForVideo_3min(self):
        global LayoutName
        LayoutName = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.click(self.LayoutCreateNewIcon_xpath)
        self.send_keys(self.LayoutNameFieldWhileCreating_xpath, LayoutName)
        self.click(self.LayoutBlankTemplate_xpath)
        self.click(self.LayoutCreateButton_xpath)
        time.sleep(2)
        self.driver.find_element(*self.LayoutVideoIcon_xpath).click()
        self.click(self.LayoutEditPageFolderNameVideo_xpath)
        time.sleep(3)
        ImageNameUploaded = f'{ImageRandomName}.{self.ImageFormat}'
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{ImageNameUploaded}']")
        SourceElement = self.find_element(UploadedImageElement_xpath)
        self.click(self.editLayoutBtn_xpath)
        self.click(self.objectBtn_xpath)
        self.click(self.videoObject_xpath)
        TargetElement = self.find_element(self.LayoutTargetElementForVideo_xpath)
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
        time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.scroll_to_element(self.fullScreen_xpath)
        self.click(self.fullScreen_xpath)
        self.click(self.LayoutEditPageEntireTimeOption_xpath)
        durationbox = self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath)
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath).send_keys(Keys.BACKSPACE)
        self.send_keys(self.LayoutEditPageEntireTimeDurationOption_xpath, "175.0")
        time.sleep(3)
        self.click(self.LayoutSaveOption_xpath)
        self.click(self.LayoutSaveOption_xpath)
        time.sleep(2)
        self.click(self.LayoutCloseOption_xpath)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def deleteUploadedMedia_Image(self):
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerMedia_xpath)
        self.send_keys(self.searchBar_xpath, "11Automation")
        time.sleep(2)
        empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)
        while empty == 0:
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.moveToTrash_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.click(self.trashFolder_xpath)
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.deleteCompletely_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.click(self.ContentManager_xpath)
            self.click(self.ContentManagerMedia_xpath)
            self.send_keys(self.searchBar_xpath, "11Automation")
            time.sleep(2)
            empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)

    def deleteUploadedMedia_Video(self):
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerMedia_xpath)
        self.click(self.MediaPageFormatDropdownIcon_xpath)
        self.click(self.MediaPageFormat_VideoOption_xpath)
        time.sleep(2)
        self.send_keys(self.searchBar_xpath, "11Automation")
        time.sleep(2)
        empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)
        while empty == 0:
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.moveToTrash_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(3)
            self.click(self.trashFolder_xpath)
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.deleteCompletely_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(4)
            self.click(self.ContentManager_xpath)
            self.click(self.ContentManagerMedia_xpath)
            self.click(self.MediaPageFormatDropdownIcon_xpath)
            self.click(self.MediaPageFormat_VideoOption_xpath)
            time.sleep(2)
            self.send_keys(self.searchBar_xpath, "11Automation")
            time.sleep(2)
            empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)

    def deleteUploadedLayout(self):
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.send_keys(self.searchBar_xpath, "11Automation")
        time.sleep(2)
        empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)
        while empty == 0:
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.moveToTrash_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.trashFolder_xpath)
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.deleteCompletely_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.ContentManager_xpath)
            self.click(self.ContentManagerLayout_xpath)
            self.send_keys(self.searchBar_xpath, "11Automation")
            time.sleep(2)
            empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)

    def deleteUploadedPlaylist(self):
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.send_keys(self.searchBar_xpath, "11Automation")
        time.sleep(2)
        empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)
        while empty == 0:
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.moveToTrash_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.trashFolder_xpath)
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.deleteCompletely_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.ContentManager_xpath)
            self.click(self.ContentManagerPlaylist_xpath)
            self.send_keys(self.searchBar_xpath, "11Automation")
            time.sleep(2)
            empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)

    def deleteUploadedSchedule(self):
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.send_keys(self.searchBar_xpath, "11Automation")
        time.sleep(2)
        empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)
        while empty == 0:
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.moveToTrash_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.trashFolder_xpath)
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.deleteCompletely_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.ContentManager_xpath)
            self.click(self.ContentManagerSchedule_xpath)
            self.send_keys(self.searchBar_xpath, "11Automation")
            time.sleep(2)
            empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)

    def deleteUploadedDisplay(self):
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerDisplay_xpath)
        self.send_keys(self.searchBar_xpath, "11Automation")
        time.sleep(2)
        empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)
        while empty == 0:
            self.click(self.allOption_xpath)
            self.click(self.moreOption_xpath)
            self.click(self.deleteCompletely_xpath)
            self.click(self.okBtn_Trash_xpath)
            time.sleep(2)
            self.refresh_page()
            self.click(self.ContentManager_xpath)
            self.click(self.ContentManagerDisplay_xpath)
            self.send_keys(self.searchBar_xpath, "11Automation")
            time.sleep(2)
            empty = self.return_elements_count(self.emptyTable_xpath, timeout=0)

    def deleteUploadedData(self):
        self.deleteUploadedDisplay()
        self.deleteUploadedSchedule()
        self.deleteUploadedPlaylist()
        self.deleteUploadedLayout()
        self.deleteUploadedMedia_Image()
        self.deleteUploadedMedia_Video()
        BASE_DIR = os.getcwd()
        allure_report_path = os.path.join(BASE_DIR, "TestData", "Duplicate")
        files = glob.glob(os.path.join(allure_report_path, "*.*"))
        for file_path in files:
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        allure_report_path = os.path.join(BASE_DIR, "TestData", "FailedScreenshot")
        files = glob.glob(os.path.join(allure_report_path, "*.*"))
        for file_path in files:
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        return JioSignageClient(self.driver)

    def deleteUploadedData_InBetween(self):
        self.deleteUploadedSchedule()
        self.deleteUploadedPlaylist()
        self.deleteUploadedLayout()
        self.deleteUploadedMedia_Image()
        self.deleteUploadedMedia_Video()
        return JioSignageClient(self.driver)

    def extract_video_frames(self, video_path, output_folder, interval_sec=5):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        cap = cv2.VideoCapture(video_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        interval = int(fps * interval_sec)
        count, saved_frames = 0, []
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            if count % interval == 0:
                frame_path = os.path.join(output_folder, f"frame_{count}.png")
                cv2.imwrite(frame_path, frame)
                saved_frames.append(frame_path)
            count += 1
        cap.release()
        return saved_frames

    def extract_gif_frames(self, gif_path, output_folder, interval_frame=1):
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        gif = Image.open(gif_path)
        saved_frames = []
        frame_idx = 0
        try:
            while True:
                gif.seek(frame_idx)
                if frame_idx % interval_frame == 0:
                    frame_path = os.path.join(output_folder, f"frame_{frame_idx}.png")
                    gif.convert("RGB").save(frame_path)
                    saved_frames.append(frame_path)
                frame_idx += 1
        except EOFError:
            pass  # End of GIF
        return saved_frames

    def compareGif(self, interval_sec=2, threshold=15, window_size=3, thresholdPercentage=90.00):
        cwd = os.getcwd()
        ref_gif_path = cwd + self.SUPPORTED_MEDIA_FORMATS[self.ImageFormat]
        stb_video_path = cwd + r'\TestData\Screenshot\VideoFromClient.mp4'

        with tempfile.TemporaryDirectory() as gif_folder, tempfile.TemporaryDirectory() as video_folder:
            gif_frames = self.extract_gif_frames(ref_gif_path, gif_folder, interval_frame=1)
            video_frames = self.extract_video_frames(stb_video_path, video_folder, interval_sec)

            if not gif_frames or not video_frames:
                return False

            max_match_percent = 0
            for i in range(len(gif_frames) - window_size + 1):
                window_gif = gif_frames[i:i + window_size]
                for j in range(len(video_frames) - window_size + 1):
                    window_video = video_frames[j:j + window_size]
                    match = 0
                    for gif_f, video_f in zip(window_gif, window_video):
                        h1 = imagehash.phash(Image.open(gif_f))
                        h2 = imagehash.phash(Image.open(video_f))
                        if abs(h1 - h2) < threshold:
                            match += 1
                    match_percent = (match / window_size) * 100
                    max_match_percent = max(max_match_percent, match_percent)
            return max_match_percent >= thresholdPercentage

    def getCurrentAccount(self):
        time.sleep(1)
        return self.get_element_text(self.O_CURRENT_ACCOUNT_TYPE_XPATH)

    def checkForCurrentAccountTypeProd(self):
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            self.click(self.O_DD_ID)
            time.sleep(1)
            self.click(self.O_headSwitch_XPATH)
        else:
            pass
        self.refresh_page()
        time.sleep(0.5)
        return self.getCurrentAccount()

    def FailedTestcaseCaptureStbScreenshot(self, testCaseName):
        cwd = os.getcwd()
        screenshot_dir = os.path.join(cwd, 'TestData', 'FailedScreenshot')
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, f'FailedSS_{testCaseName}.jpg')
        device_screenshot_path = f"/sdcard/FailedSS_{testCaseName}.jpg"

        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        subprocess.run(["adb", "shell", "screencap", "-p", device_screenshot_path], check=True)
        time.sleep(2)
        subprocess.run(["adb", "pull", device_screenshot_path, screenshot_path], check=True)
        subprocess.run(["adb", "shell", "rm", device_screenshot_path], check=True)

        time.sleep(3)
        return JioSignageClient(self.driver)

    # def FailedTestcaseCaptureStbScreenshot(self, testCaseName):
    #     cwd = os.getcwd()
    #     screenshot_path = os.path.join(cwd, f'TestData\\FailedScreenshot\\FailedSS_{testCaseName}.jpg')
    #     device_screenshot_path = "/sdcard/FailedSS.jpg"
    #     if os.path.exists(screenshot_path):
    #         os.remove(screenshot_path)
    #     subprocess.run(["adb", "shell", "screencap", "-p", device_screenshot_path])
    #     subprocess.run(["adb", "pull", device_screenshot_path, screenshot_path])
    #     time.sleep(2)
    #     return JioSignageClient(self.driver)

    #########CORE FUNCTIONS#############END################

    def compareImagesWithReferenceImage(self, refImage, threshold=10):
        cwd = os.getcwd()
        img1_path = cwd + fr'\TestData\{refImage}'
        img2_path = cwd + r'\TestData\Screenshot\ScreenshotFromClient.jpg'
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)
        hash1 = imagehash.phash(img1)
        hash2 = imagehash.phash(img2)
        diff = abs(hash1 - hash2)
        print(diff)
        if diff < threshold:
            return True
        else:
            return False

    def compareImagesWithReferenceImage_PleaseSchedule(self, refImage, threshold=15):
        cwd = os.getcwd()
        img1_path = cwd + fr'\TestData\{refImage}'
        img2_path = cwd + r'\TestData\Screenshot\ScreenshotFromClient.jpg'
        img1 = Image.open(img1_path)
        img2 = Image.open(img2_path)
        hash1 = imagehash.phash(img1)
        hash2 = imagehash.phash(img2)
        diff = abs(hash1 - hash2)
        print(diff)
        if diff < threshold:
            return True
        else:
            return False

    def deliverEmgAlert_BuildingInMaintenance(self):
        self.click(self.emergencyAlertOptionXPATH)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.EAFirstCheckbox)
        self.scroll_to_element(self.buildingInMaintenance_XPATH)
        self.click(self.buildingInMaintenance_XPATH)
        self.click(self.deliverBtn_XPATH)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreateLayoutWithBlankTemplateForImage1(self):
        self.refresh_page()
        global LayoutName1
        LayoutName1 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.click(self.LayoutCreateNewIcon_xpath)
        self.send_keys(self.LayoutNameFieldWhileCreating_xpath, LayoutName1)
        self.click(self.LayoutBlankTemplate_xpath)
        self.click(self.LayoutCreateButton_xpath)
        time.sleep(2)
        self.driver.find_element(*self.LayoutImageIcon_xpath).click()
        self.click(self.LayoutEditPageFolderName_xpath)
        time.sleep(3)
        ImageNameUploaded = f'{ImageRandomName}.{self.ImageFormat}'
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{ImageNameUploaded}']")
        SourceElement = self.find_element(UploadedImageElement_xpath)
        TargetElement = self.find_element(self.LayoutTargetElement_xpath)
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
            time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.click(self.editLayoutBtn_xpath)
        self.click(self.LayoutEditPageEntireTimeOption_xpath)
        durationbox = self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath)
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath).send_keys(Keys.BACKSPACE)
        self.send_keys(self.LayoutEditPageEntireTimeDurationOption_xpath, "60.0")
        time.sleep(3)
        self.click(self.LayoutSaveOption_xpath)
        self.click(self.LayoutSaveOption_xpath)
        time.sleep(2)
        self.click(self.LayoutCloseOption_xpath)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreateLayoutWithBlankTemplateForImage2(self):
        self.refresh_page()
        global LayoutName2
        LayoutName2 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.click(self.LayoutCreateNewIcon_xpath)
        self.send_keys(self.LayoutNameFieldWhileCreating_xpath, LayoutName2)
        self.click(self.LayoutBlankTemplate_xpath)
        self.click(self.LayoutCreateButton_xpath)
        time.sleep(2)
        self.driver.find_element(*self.LayoutImageIcon_xpath).click()
        self.click(self.LayoutEditPageFolderName_xpath)
        time.sleep(3)
        ImageNameUploaded = f'{ImageRandomName}.{self.ImageFormat}'
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{ImageNameUploaded}']")
        SourceElement = self.find_element(UploadedImageElement_xpath)
        TargetElement = self.find_element(self.LayoutTargetElement_xpath)
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
            time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.click(self.editLayoutBtn_xpath)
        self.click(self.LayoutEditPageEntireTimeOption_xpath)
        durationbox = self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath)
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath).send_keys(Keys.BACKSPACE)
        self.send_keys(self.LayoutEditPageEntireTimeDurationOption_xpath, "60.0")
        time.sleep(3)
        self.click(self.LayoutSaveOption_xpath)
        self.click(self.LayoutSaveOption_xpath)
        time.sleep(2)
        self.click(self.LayoutCloseOption_xpath)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreateLayoutWithBlankTemplateForImage3(self):
        self.refresh_page()
        global LayoutName3
        LayoutName3 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerLayout_xpath)
        self.click(self.LayoutCreateNewIcon_xpath)
        self.send_keys(self.LayoutNameFieldWhileCreating_xpath, LayoutName3)
        self.click(self.LayoutBlankTemplate_xpath)
        self.click(self.LayoutCreateButton_xpath)
        time.sleep(2)
        self.driver.find_element(*self.LayoutImageIcon_xpath).click()
        self.click(self.LayoutEditPageFolderName_xpath)
        time.sleep(3)
        ImageNameUploaded = f'{ImageRandomName}.{self.ImageFormat}'
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{ImageNameUploaded}']")
        SourceElement = self.find_element(UploadedImageElement_xpath)
        TargetElement = self.find_element(self.LayoutTargetElement_xpath)
        # Assume driver and SourceElement, TargetElement are already defined
        source_location = SourceElement.location
        target_location = TargetElement.location
        # Calculate dynamic offset
        x_offset = target_location['x'] - source_location['x']
        y_offset = target_location['y'] - source_location['y']
        actions = ActionChains(self.driver)
        actions.move_to_element(SourceElement).click_and_hold().pause(1)
        # Break the movement into small steps
        steps = 30  # more steps = smoother and slower
        X_Step = x_offset / steps
        Y_Step = y_offset / steps
        delay_per_step = 3 / steps  # total move time: 3 seconds
        for _ in range(steps):
            actions.move_by_offset(X_Step, Y_Step).perform()
            time.sleep(delay_per_step)
        actions.release().perform()
        time.sleep(3)
        self.click(self.editLayoutBtn_xpath)
        self.click(self.LayoutEditPageEntireTimeOption_xpath)
        durationbox = self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath)
        durationbox.click()
        for i in range(1, 5):
            durationbox.send_keys(Keys.BACKSPACE)
        self.driver.find_element(*self.LayoutEditPageEntireTimeDurationOption_xpath).send_keys(Keys.BACKSPACE)
        self.send_keys(self.LayoutEditPageEntireTimeDurationOption_xpath, "60.0")
        time.sleep(3)
        self.click(self.LayoutSaveOption_xpath)
        self.click(self.LayoutSaveOption_xpath)
        time.sleep(2)
        self.click(self.LayoutCloseOption_xpath)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreatePlaylistImage1_2_3(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        global PlaylistName
        PlaylistName = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.playlistTB_XPATH, PlaylistName)
        self.click(self.ScheduleCreateCommit_xpath)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName1)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)

        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.find_element(self.ScheduleEditPageSearchIcon_xpath).clear()
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName2)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName2}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)

        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.find_element(self.ScheduleEditPageSearchIcon_xpath).clear()
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName3)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName3}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_XPATH)
        self.click(self.savePlaylist_Yes_XPATH)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def CreateScheduleForPlaylist(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedPlaylistInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPagePlaylistOption_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#playlistFolderLI")))
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName)
        time.sleep(3)
        Source = self.find_element(CreatedPlaylistInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(3)
        self.wait_for_page_load()
        self.click(self.ScheduleEditPageCloseIcon_xpath)
        return JioSignageClient(self.driver)

    def adb(self, command):
        try:
            result = subprocess.check_output(f"adb {command}", shell=True, stderr=subprocess.STDOUT)
            return result.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            return e.output.decode('utf-8').strip()

    def validate_adb_reboot_uptime(self, timeout=120):
        start_time = time.time()

        while True:
            uptime = self.adb("shell uptime")
            print(uptime)

            if "device offline" in uptime.lower():
                pass
            else:
                match_alt = re.search(r'up\s+(\d+)\s+min', uptime)
                if match_alt:
                    total_minutes = int(match_alt.group(1))
                    return total_minutes <= 2

                match = re.search(r'up\s+(\d+):(\d+)', uptime)
                if match:
                    hours = int(match.group(1))
                    minutes = int(match.group(2))
                    total_minutes = hours * 60 + minutes
                    return total_minutes <= 2

            if time.time() - start_time > timeout:
                return False
            time.sleep(2)
    def RebootDisplay_FromDisplayStatus(self):
        self.refresh_page()
        self.click(self.displayStatus_XPATH)
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.DisplayFirstCheckbox)
        self.click(self.rebootDisplay_XPATH)
        self.click(self.okBtn)
        time.sleep(0.8)
        self.refresh_page()
        return JioSignageClient(self.driver)

    def SyncDisplay_FromDisplayStatus(self):
        self.refresh_page()
        self.click(self.displayStatus_XPATH)
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.DisplayFirstCheckbox)
        self.click(self.syncDisplay_XPATH)
        self.click(self.okBtn)
        time.sleep(0.8)
        self.refresh_page()
        return JioSignageClient(self.driver)

    def CreatePlaylistLayout1(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        global PlaylistName1
        PlaylistName1 = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.playlistTB_XPATH, PlaylistName1)
        self.click(self.ScheduleCreateCommit_xpath)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName1)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_XPATH)
        self.click(self.savePlaylist_Yes_XPATH)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def CreatePlaylistLayout2(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        global PlaylistName2
        PlaylistName2 = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.playlistTB_XPATH, PlaylistName2)
        self.click(self.ScheduleCreateCommit_xpath)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName2)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName2}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_XPATH)
        self.click(self.savePlaylist_Yes_XPATH)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def CreatePlaylistLayout3(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        global PlaylistName3
        PlaylistName3 = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.playlistTB_XPATH, PlaylistName3)
        self.click(self.ScheduleCreateCommit_xpath)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName3)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName3}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_XPATH)
        self.click(self.savePlaylist_Yes_XPATH)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def CreateSmartPlaylistForPlaylist1_2_3(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        global PlaylistName_Smart
        PlaylistName_Smart = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.playlistTB_XPATH, PlaylistName_Smart)
        self.click(self.smartPlaylistRadio)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(3)
        self.click(self.ScheduleEditPagePlaylistOption_xpath)
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName1)
        time.sleep(1)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        CreatedPlaylist1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName1}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedPlaylist1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(3)
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).clear()
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName2)
        time.sleep(1)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        CreatedPlaylist1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName2}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedPlaylist1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(3)
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).clear()
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName3)
        time.sleep(1)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        CreatedPlaylist1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName3}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedPlaylist1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_XPATH)
        self.click(self.savePlaylist_Yes_XPATH)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def CreateScheduleForSmartPlaylist(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedPlaylistInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName_Smart}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPagePlaylistOption_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#playlistFolderLI")))
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName_Smart)
        time.sleep(3)
        Source = self.find_element(CreatedPlaylistInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(3)
        self.wait_for_page_load()
        self.click(self.ScheduleEditPageCloseIcon_xpath)
        return JioSignageClient(self.driver)

    def CreateSubPlaylistForPlaylist1_2_3(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerPlaylist_xpath)
        self.click(self.DisplayCreateIcon_xpath)
        global PlaylistName_Sub
        PlaylistName_Sub = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.playlistTB_XPATH, PlaylistName_Sub)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(3)
        self.click(self.ScheduleEditPagePlaylistOption_xpath)
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName1)
        time.sleep(1)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        CreatedPlaylist1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName1}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedPlaylist1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(3)
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).clear()
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName2)
        time.sleep(1)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        CreatedPlaylist1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName2}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedPlaylist1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)

        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).clear()
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName3)
        time.sleep(1)
        self.find_element(self.PlaylistEditPageSearchIcon_xpath).send_keys(Keys.ENTER)
        time.sleep(2)
        CreatedPlaylist1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName3}']")
        TargetPlaylist = (By.XPATH, "//section[@id='uploadPlaylist']")
        Source = self.find_element(CreatedPlaylist1InScheduleEditPage_xpath)
        Target = self.find_element(TargetPlaylist)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_XPATH)
        self.click(self.savePlaylist_Yes_XPATH)
        time.sleep(1)
        return JioSignageClient(self.driver)

    def CreateScheduleForSubPlaylist(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedPlaylistInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{PlaylistName_Sub}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPagePlaylistOption_xpath)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#playlistFolderLI")))
        self.click(self.PlaylistEditPageSearchIcon_xpath)
        self.send_keys(self.PlaylistEditPageSearchIcon_xpath, PlaylistName_Sub)
        time.sleep(3)
        Source = self.find_element(CreatedPlaylistInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(3)
        self.wait_for_page_load()
        self.click(self.ScheduleEditPageCloseIcon_xpath)
        return JioSignageClient(self.driver)

    def CreateScheduleForParticularTime(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedLayoutInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName)
        time.sleep(3)
        Source = self.find_element(CreatedLayoutInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.createdScheduleXpath)
        time.sleep(2)
        now = datetime.now()
        global start_time
        global end_time
        start_time = datetime.now() + timedelta(minutes=2)
        startTime = (now + timedelta(minutes=2)).strftime("%H:%M")
        end_time = datetime.now() + timedelta(minutes=3)
        endTime = (now + timedelta(minutes=3)).strftime("%H:%M")
        time.sleep(2)
        start_input = self.driver.find_element(By.ID, "startTime")
        end_input = self.driver.find_element(By.ID, "endTime")
        start_input.clear()
        start_input.send_keys(startTime)
        end_input.clear()
        end_input.send_keys(endTime)
        time.sleep(1)
        self.click(self.savePlaylist_XPATH)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def captureStbScreenshot_atStartTime(self):
        # Wait until exact time
        while datetime.now() < start_time:
            time.sleep(1)
        time.sleep(10)
        cwd = os.getcwd()
        screenshot_path = cwd + r'\TestData\Screenshot\ScreenshotFromClient.jpg'
        device_screenshot_path = "/sdcard/ScreenshotFromClient.jpg"
        subprocess.run(["adb", "shell", "screencap", "-p", device_screenshot_path])
        subprocess.run(["adb", "pull", device_screenshot_path, screenshot_path])
        return JioSignageClient(self.driver)

    def captureStbScreenshot_atEndTime(self):
        # Wait until exact time
        while datetime.now() < end_time:
            time.sleep(1)
        time.sleep(15)
        cwd = os.getcwd()
        screenshot_path = cwd + r'\TestData\Screenshot\ScreenshotFromClient.jpg'
        device_screenshot_path = "/sdcard/ScreenshotFromClient.jpg"
        subprocess.run(["adb", "shell", "screencap", "-p", device_screenshot_path])
        subprocess.run(["adb", "pull", device_screenshot_path, screenshot_path])
        return JioSignageClient(self.driver)

    def CreateScheduleForTrigger(self):
        self.refresh_page()
        global ScheduleName
        ScheduleName = "11AutomationSchedule" + "".join(random.choices(string.ascii_letters, k=5))
        CreatedLayoutInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click(self.ScheduleCreateIcon_xpath)
        self.send_keys(self.ScheduleNameField_xpath, ScheduleName)
        self.click(self.ScheduleCreateCommit_xpath)
        time.sleep(5)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName1)
        time.sleep(3)
        Source = self.find_element(CreatedLayoutInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.triggerBtnXpath)
        self.click(self.addTriggerBtnXpath)
        time.sleep(1)
        global triggerName
        triggerName = "11AutomationTrigger" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys(self.triggerNameXpath, triggerName)
        self.select_dropdown_by_value(self.selectLayoutOrPlaylistXpath, "0")
        self.click(self.selectLayoutTBXPATH)
        self.send_keys(self.LayoutNameTBXPATH, LayoutName2)
        time.sleep(0.7)
        self.find_element(self.LayoutNameTBXPATH).send_keys(Keys.ENTER)
        self.click(self.dailyRadioXpath)
        today = date.today().strftime('%d-%m-%Y')
        start_date_input = self.find_element(self.triggerStartDateID)
        start_date_input.clear()
        start_date_input.send_keys(today)
        end_date_input = self.find_element(self.triggerEndDateID)
        end_date_input.clear()
        end_date_input.send_keys(today)

        self.click(self.repeatYesID)
        time.sleep(1)
        now = datetime.now()
        global start_time
        global end_time
        start_time = datetime.now() + timedelta(minutes=2)
        startTime = (now + timedelta(minutes=2)).strftime("%H:%M")
        end_time = datetime.now() + timedelta(minutes=3)
        endTime = (now + timedelta(minutes=3)).strftime("%H:%M")
        time.sleep(2)
        start_input = self.driver.find_element(By.ID, "trigger_start_time_str")
        end_input = self.driver.find_element(By.ID, "trigger_play_until_time")
        start_input.clear()
        start_input.send_keys(startTime)
        end_input.clear()
        end_input.send_keys(endTime)
        time.sleep(1)
        self.send_keys(self.repeatHrsID, "0")
        self.send_keys(self.repeatMinID, "2")
        self.click(self.addTriggerBtnXPATH)
        time.sleep(2)
        return JioSignageClient(self.driver)

    def editScheduleToReplaceLay1WithLay2(self):
        self.refresh_page()
        CreatedLayoutInScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName2}']")
        day_to_xpath = {
            'sunday': self.ScheduleEditPageDropLocationSunday_xpath,
            'monday': self.ScheduleEditPageDropLocationMonday_xpath,
            'tuesday': self.ScheduleEditPageDropLocationTuesday_xpath,
            'wednesday': self.ScheduleEditPageDropLocationWednesday_xpath,
            'thursday': self.ScheduleEditPageDropLocationThursday_xpath,
            'friday': self.ScheduleEditPageDropLocationFriday_xpath,
            'saturday': self.ScheduleEditPageDropLocationSaturday_xpath,
        }
        current_day = datetime.today().strftime('%A').lower()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerSchedule_xpath)
        self.click((By.XPATH, f"//span[@title='{ScheduleName}']"))
        time.sleep(5)
        self.click(self.ScheduleEditPageLayoutOption_xpath)
        self.click(self.ScheduleEditPageSearchIcon_xpath)
        self.send_keys(self.ScheduleEditPageSearchIcon_xpath, LayoutName2)
        time.sleep(3)
        Source = self.find_element(CreatedLayoutInScheduleEditPage_xpath)
        Target = self.find_element(day_to_xpath[current_day])
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)
        self.click(self.savePlaylist_Yes_XPATH)
        self.click(self.ScheduleEditPageCloseIcon_xpath)
        return JioSignageClient(self.driver)

    def deliveryInstantlyForCreatedDisplay(self):
        self.refresh_page()
        time.sleep(1)
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerDisplay_xpath)
        self.refresh_page()
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        self.click(self.DisplayFirstCheckbox)
        self.click(self.deliveryInstantlyXPATH)
        self.click(self.ScheduleCreateCommit_xpath)
        return JioSignageClient(self.driver)

    def getImageFromLiveMonitoring(self):
        self.click(self.liveMonitoringXPATH)
        time.sleep(5)
        self.refresh_page()
        time.sleep(3)
        self.refresh_page()
        self.send_keys(self.searchBar_LM_XPATH, DisplayName)
        time.sleep(2)
        self.click(self.image_LM_XPATH)
        time.sleep(1)
        img_element = self.find_element(self.liveMonitoringImageXPATH)
        src = img_element.get_attribute("src")
        if src and src.startswith("data:image"):
            base64_data = src.split(",")[1]
            output_dir = os.path.join("TestData")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "screen_capture_LiveMonitoring.png")
            with open(output_file, "wb") as f:
                f.write(base64.b64decode(base64_data))
        else:
            raise Exception("No valid base64 image found in src attribute.")
        self.refresh_page()
        return JioSignageClient(self.driver)

    def deleteScheduleForCreatedDisplay(self):
        self.refresh_page()
        self.click(self.ContentManager_xpath)
        self.click(self.ContentManagerDisplay_xpath)
        self.click(self.DisplayPageSearch_xpath)
        self.send_keys(self.DisplayPageSearch_xpath, DisplayName)
        time.sleep(3)
        if self.return_elements_count(self.deleteSchedule) == 1:
            self.click(self.deleteSchedule)
            self.click(self.okBtn)
        return JioSignageClient(self.driver)
