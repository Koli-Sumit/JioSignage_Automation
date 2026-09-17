import datetime
import re
import secrets
import time
import logging

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from datetime import date, timedelta
from Pages.BasePage import BasePage, generate_random_string, generate_unique_string, retry_action, getTextAfterRetry
from Utilities import configReader
from Utilities.LogUtil import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

log = Logger(__name__, logging.INFO)

new_base_acc_name = generate_unique_string(5)
f_name = generate_unique_string(5)
schedule090 = generate_unique_string(5)
sch_name_new_01 = generate_unique_string(6)
sch_name_new_02 = generate_unique_string(6)

schedule007 = generate_random_string(5)
dra_drop_schedule100 = generate_random_string(5)
dra_drop_schedule1 = generate_random_string(5)
dra_drop_schedule2 = generate_random_string(5)
dra_drop_schedule3 = generate_random_string(5)
dra_drop_schedule4 = generate_random_string(5)
dra_drop_schedule5 = generate_random_string(5)
dra_drop_schedule6 = generate_random_string(5)
dra_drop_schedule7 = generate_random_string(5)
dra_drop_schedule8 = generate_unique_string(6)
dra_drop_schedule10 = generate_unique_string(6)
dra_drop_schedule = "drag_" + generate_random_string(3)
new_content_name_new = "base_" + generate_random_string(3)
base_acc_name = "BASE_" + generate_random_string(3)
test_content_name = "content" + generate_random_string(5)
trigger_name = "trigger_" + generate_random_string(5)
trigger_name2 = "trigger_" + generate_random_string(5)
sc_cont_name = generate_random_string(5)
scheduleName = generate_random_string(5)
scheduleName1 = generate_random_string(5)
scheduleName2 = generate_random_string(5)
scheduleName3 = generate_random_string(5)
scheduleName4 = generate_random_string(5)
scheduleName5 = generate_random_string(5)
scheduleName6 = generate_random_string(5)
sch_name_new = generate_random_string(5)
sch_name_new1 = generate_random_string(5)
folder_name = generate_random_string(5)
folder_name1 = generate_random_string(5)
new_folder_name = generate_random_string(5)
folder_name_new = generate_random_string(5)
fname = "data_" + generate_random_string(3)
new_fname = "fm_" + generate_random_string(4)
fn = "old_" + generate_random_string(4)
scheduleForCount = "Count_" + generate_random_string(2)
new_content_name = generate_random_string(6)
new_content_name2 = generate_random_string(6)
xxx = generate_random_string(3)
sc1 = generate_random_string(5)
schedule21 = generate_random_string(5)
sc_name2 = generate_random_string(5)
schedule30 = generate_random_string(5)
sc_name = generate_random_string(5)
sc_name20 = generate_random_string(5)
sch1 = generate_random_string(5)
sch2 = generate_unique_string(26)
sch3 = generate_random_string(5)
sch4 = generate_random_string(5)
sch5 = generate_random_string(5)
sch6 = generate_random_string(5)
sch7 = generate_random_string(5)
sch8 = generate_random_string(5)
sch9 = generate_random_string(5)
sch10 = generate_random_string(5)
sch_name = generate_random_string(5)
scheduleName_7 = generate_random_string(5)
sch_n = generate_random_string(5)
schedule_nm = generate_random_string(5)
schedule_n = generate_random_string(5)
scheduleName_8 = generate_random_string(5)
schedule_1 = generate_random_string(5)
sc_name1 = generate_random_string(5)
cn_name = generate_random_string(5)
sch_newName = generate_random_string(5)
##additional
trigger_name1 = generate_random_string(5)
Schedulenew_name_trigger2 = generate_random_string(5)
s_Name = generate_random_string(5)
def lastWord(string):
    lis = list(string.split(" "))
    length = len(lis)
    return lis[length - 1]


class Schedules(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def gotoUrl(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        return Schedules(self.driver)

    def deleteSchedule(self, sch_name):
        schedule_title = f"//span[@title='{sch_name}']"
        if len(self.driver.find_elements(By.XPATH, schedule_title)) > 0:
            time.sleep(1)
            ele = f"//span[@title='{sch_name}']/preceding::input[@type='checkbox'][1]"
            checkbox = self.driver.find_element(By.XPATH, ele)
            self.driver.execute_script("arguments[0].click();", checkbox)
            log.logger.info("Schedule checkbox selected ")
            time.sleep(1)
            self.click("S_MORE_OPTION_XPATH")
            log.logger.info("More option selected ")
            time.sleep(1)
            self.click("S_MOVE_TO_TRASH_XPATH")
            log.logger.info("Move to trash selected")
            time.sleep(1)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(4)
            self.click("S_TRASHED_XPATH")
            log.logger.info("clicked on trashed")
            time.sleep(3)
            chk = f"//span[@title='{sch_name}']/preceding::input[@type='checkbox'][1]"
            self.driver.find_element(By.XPATH, chk).click()
            #self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, chk))
            log.logger.info("Select checkbox again")
            time.sleep(2)
            self.click("S_MORE_OPTION_XPATH")
            time.sleep(2)
            log.logger.info("Click on more options")
            self.click("S_DELETE_COMPLETE_XPATH")
            self.click("S_CONFIRM_BTN_XPATH")
            time.sleep(3)
        else:
            pass

    def Complete_deleteSchedule(self, sch_name):
        schedule_title = f"//span[@title='{sch_name}']"
        if len(self.driver.find_elements(By.XPATH, schedule_title)) > 0:
            ele = f"//span[@title='{sch_name}']/preceding::input[@type='checkbox'][1]"
            checkbox = self.driver.find_element(By.XPATH, ele)
            self.driver.execute_script("arguments[0].click();", checkbox)
            log.logger.info("Schedule checkbox selected ")
            self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
            more_options = self.find_element("S_MORE_OPTION_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options)
            log.logger.info("More option selected ")
            self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
            moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
            self.driver.execute_script("arguments[0].click();", moveTrash)
            log.logger.info("Move to trash selected")
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(1)
            mv = self.find_element("S_TRASHED_XPATH")
            self.driver.execute_script("arguments[0].click();", mv)
            log.logger.info("clicked on trashed")
            chk = f"//span[@title='{sch_name}']/preceding::input[@type='checkbox'][1]"
            check = self.driver.find_element(By.XPATH, chk)
            self.driver.execute_script("arguments[0].click();", check)
            log.logger.info("Select checkbox again")
            time.sleep(1)
            more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
            self.driver.execute_script("arguments[0].click();", more_options_trash)
            time.sleep(1)
            log.logger.info("Click on more options")
            delete_complete = self.find_element("S_DELETE_COMPLETE_XPATH")
            self.driver.execute_script("arguments[0].click();", delete_complete)
            self.click("S_CONFIRM_BTN_XPATH")
            time.sleep(1)
        else:
            pass

    def createSchedule(self, schedule):
        time.sleep(2)
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", schedule)
        self.click("S_ADD_BUTTON_NAME")
        # self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        time.sleep(4)

    def addSchedule(self, schedule_name):
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", schedule_name)
        self.click("S_ADD_BUTTON_NAME")
        self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{schedule_name}']"
        log.logger.info("schedule_xpath : " + schedule_xpath)
        schedule_count = self.driver.find_elements(By.XPATH, schedule_xpath)
        log.logger.info("schedule_count : " + str(len(schedule_count)))
        return str(len(schedule_count))

    def addScheduleWith5Char(self):
        schedule_name = self.addSchedule(sch1)
        return schedule_name

    def addSchedulesWithMaxChar(self):
        return self.addSchedule(sch2)

    def addScheduleNameWithSpecialChar(self):
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", "shi@v")
        self.click("S_ADD_BUTTON_NAME")
        return self.getText("S_INVALID_SCHEDULE_NAME_XPATH")

    def scheduleNameOnCustomizePage(self):
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", sch3)
        self.click("S_ADD_BUTTON_NAME")
        self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        return self.find_element("S_EDIT_SCHEDULE_ID").get_attribute('value')

    def getEditScheduleOptions(self):
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", sch4)
        self.click("S_ADD_BUTTON_NAME")
        self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        return self.getText("S_TIME_DURATION_DROPDOWN_XPATH")

    def cancelOptionOnAddSchedule(self):
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        scheduleName_3 = generate_random_string(5)
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", scheduleName_3)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName_3}']"
        schedule_count = self.driver.find_elements(By.XPATH, schedule_xpath)
        log.logger.info("schedule_count : " + str(len(schedule_count)))
        return str(len(schedule_count))

    def closeOptionOnAddSchedule(self):
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        scheduleName_4 = generate_random_string(5)
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", scheduleName_4)
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName_4}']"
        schedule_count = self.driver.find_elements(By.XPATH, schedule_xpath)
        log.logger.info("schedule_count : " + str(len(schedule_count)))
        return str(len(schedule_count))

    def editScheduleNameOnEditPage(self):
        self.createSchedule(sch5)
        old_schedule_name = self.find_element("S_EDIT_SCHEDULE_ID").get_attribute('value')
        log.logger.info("old_schedule_name : " + old_schedule_name)
        self.click("S_EDIT_PEN_XPATH")
        self.clear("S_EDIT_SCHEDULE_ID")
        # n_schedule_Name = generate_random_string(5)
        self.send_keys("S_EDIT_SCHEDULE_ID", sch6)
        self.click("S_UPDATE_BUTTON_XPATH")
        time.sleep(4)
        new_scheduleName = self.find_element("S_EDIT_SCHEDULE_ID").get_attribute('value')
        log.logger.info("new_scheduleName : " + new_scheduleName)
        assert old_schedule_name != sch6

    def UpdateScheduleNameOnEditPage(self):
        self.createSchedule(sch7)
        old_schedule_name = self.find_element("S_EDIT_SCHEDULE_ID").get_attribute('value')
        log.logger.info("old_schedule_name : " + old_schedule_name)
        time.sleep(2)
        self.click("S_EDIT_PEN_XPATH")
        time.sleep(1)
        self.clear("S_EDIT_SCHEDULE_ID")
        time.sleep(1)
        self.send_keys("S_EDIT_SCHEDULE_ID", sch8)
        self.selenium_click("S_UPDATE_BUTTON_XPATH")
        time.sleep(1)
        self.wait_for_visible("O_ALERT_MESSAGE_XPATH")
        time.sleep(1)
        p = self.getText("O_ALERT_MESSAGE_XPATH")
        return p

    def verifyCloseOptionOnEditSchedule(self):
        self.createSchedule(scheduleName_7)
        self.selenium_click("S_CLOSE_BUTTON_ON_XPATH")
        self.selenium_click("S_YES_BUTTON_XPATH")
        time.sleep(1)
        return self.get_current_url()

    def verifyAddTrigger(self):
        self.createSchedule(sch9)
        time.sleep(2)
        self.click("S_ADD_TRIGGER_BTN_XPATH")
        time.sleep(2)
        self.click("S_ADD_TIME_TRIGGER_XPATH")
        time.sleep(5)
        return self.getText("S_ADD_TIME_TRIGGER_BUTTON_XPATH")

    def verifyCancelOptionOnAddTrigger(self):
        self.createSchedule(sch10)
        self.click("S_ADD_TRIGGER_BTN_XPATH")
        self.click("S_ADD_TIME_TRIGGER_XPATH")
        self.click("S_CANCEL_BUTTON_XPATH")
        return self.getText("S_NO_DATA_XPATH")

    def moreOptionTrashed(self):
        self.createSchedule(schedule_n)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        ele = f"//span[@title='{schedule_n}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        time.sleep(2)
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(10)
        log.logger.info("clicked on confirm button")
        time.sleep(3)
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        time.sleep(1)
        chk = f"//span[@title='{schedule_n}']/preceding::input[@type='checkbox'][1]"
        check = self.driver.find_element(By.XPATH, chk)
        self.driver.execute_script("arguments[0].click();", check)
        log.logger.info("Select checkbox again")
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        log.logger.info("Click on more options")
        restore = self.getText("S_RESTORE_XPATH")
        delete = self.getText("S_DELETE_COMPLETELY_XPATH")
        log.logger.info(restore + delete)
        return restore + delete

    def restoreSchedule(self):
        self.createSchedule(scheduleName_8)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(2)
        ele = f"//span[@title='{scheduleName_8}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        time.sleep(2)
        chk = f"//span[@title='{scheduleName_8}']/preceding::input[@type='checkbox'][1]"
        check = self.driver.find_element(By.XPATH, chk)
        self.driver.execute_script("arguments[0].click();", check)
        log.logger.info("Select checkbox again")
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        self.click("S_RESTORE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(4)
        schedules = self.find_elements("S_SCHEDULE_NAMES_XPATH")
        for sch in schedules:
            if sch.text == scheduleName_8:
                assert False
            else:
                assert True

    def schedulePath(self):
        time.sleep(2)
        return self.getText("S_SCHEDULE_PATH_XPATH")

    def subFolderPath(self):
        time.sleep(1)
        return self.getText("S_SUB_FOLDER_XPATH")

    def verifyHeadFolder(self):
        time.sleep(1)
        root = self.schedulePath()
        subFolder = self.subFolderPath()
        log.logger.info(root + subFolder)
        return root + subFolder

    def verifyHeadTrashFolder(self):
        time.sleep(2)
        self.click("S_TRASHED_XPATH")
        time.sleep(5)
        root = self.schedulePath()
        subFolder = self.subFolderPath()
        log.logger.info(root + subFolder)
        return root + subFolder

    def verifyTrashedSchedule(self):
        self.createSchedule(sch_n)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        time.sleep(1)
        ele = f"//span[@title='{sch_n}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        count = self.driver.find_elements(By.XPATH, ele)
        return str(len(count))

    def SearchScheduleInsideTrashed(self):
        self.createSchedule(schedule_nm)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(2)
        ele = f"//span[@title='{schedule_nm}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        time.sleep(1)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        time.sleep(5)
        log.logger.info("clicked on trashed")
        # self.send_keys("S_SEARCH_XPATH", schedule_nm)
        # cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        # parts = cnt.split("entries (filtered", 1)
        # time.sleep(1)
        # var = parts[0] if len(parts) > 1 else cnt
        # count = re.findall(r'\d+', var)[-1]
        # return str(count)
        #Changed Akash
        self.send_keys("S_SEARCH_XPATH", schedule_nm)
        time.sleep(2)

        search_xpath = f"//span[@title='{schedule_nm}']"
        elements = self.driver.find_elements(By.XPATH, search_xpath)

        return len(elements)

    def CancelOnRestoreSchedule(self):
        self.createSchedule(s_Name)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        ele = f"//span[@title='{s_Name}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        time.sleep(3)
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        self.click("S_RESTORE_XPATH")
        time.sleep(1)
        self.click("S_CANCEL_XPATH")
        time.sleep(1)
        element = f"//span[@title='{s_Name}']/preceding::input[@type='checkbox'][1]"
        ele_count = self.driver.find_elements(By.XPATH, element)
        return str(len(ele_count))

    def CloseOnRestoreSchedule(self):
        self.createSchedule(sch_newName)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        ele = f"//span[@title='{sch_newName}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        self.click("S_RESTORE_XPATH")
        time.sleep(1)
        self.click("S_CLOSE_X_BUTTON_XPATH")
        time.sleep(1)
        element = f"//span[@title='{sch_newName}']/preceding::input[@type='checkbox'][1]"
        ele_count = self.driver.find_elements(By.XPATH, element)
        return str(len(ele_count))

    def verifyCompleteDeleteSchedule(self):
        time.sleep(1)
        schedule_1 = generate_random_string(5)
        self.createSchedule(schedule_1)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        time.sleep(2)
        ele = f"//span[@title='{schedule_1}']/preceding::input[@type='checkbox'][1]"
        #ele = f"//tr[.//span[@title='{schedule_1}']]//input[@type='checkbox']"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        time.sleep(2)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        time.sleep(1)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        log.logger.info("clicked on confirm button")
        time.sleep(2)
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        time.sleep(2)
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", schedule_1)
        time.sleep(2)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        return str(count)

    def verifyCancelOnCompleteDeleteSchedule(self):
        schedule_1 = generate_random_string(5)
        self.createSchedule(schedule_1)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        ele = f"//span[@title='{schedule_1}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.click("S_CANCEL_XPATH")
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", schedule_1)
        time.sleep(2)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        return str(count)

    def verifyCloseButtonOnDeleteSchedule(self):
        self.createSchedule(schedule_1)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        ele = f"//span[@title='{schedule_1}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        #Changed Akash
        # wait = WebDriverWait(self.driver, 20, poll_frequency=0.5,
        #                      ignored_exceptions=[StaleElementReferenceException])
        # ele = f"//span[@title='{schedule_1}']/preceding::input[@type='checkbox'][1]"
        # checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, ele)))
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.click("S_CLOSE_X_BUTTON_XPATH")
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", schedule_1)
        time.sleep(2)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        return str(count)

    def verifyFolders(self):
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        folders = self.find_elements("S_FOLDERS_XPATH")
        for i in folders:
            pass
        return str(len(folders))

    def selectFolderFromDropdown(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.wait_for_visible_all_elements("S_INPUT_NAME_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", fname)
        option = f"//a[@class='dropdown-item '][contains(.,'{fname}')]"
        folder_detail = self.driver.find_elements(By.XPATH, option)
        return str(len(folder_detail))

    def selectFolderFromDropdownAndOpen(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        time.sleep(2)
        self.click("S_FOLDER_DROPDOWN_XPATH")
        time.sleep(5)
        self.send_keys("S_INPUT_NAME_XPATH", new_fname)
        time.sleep(2)
        option = f"//a[@class='dropdown-item '][contains(.,'{new_fname}')]"
        time.sleep(3)
        self.driver.find_element(By.XPATH, option).click()
        time.sleep(2)
        #folder_path = self.getText("S_FOLDER_NAME_DROP_XPATH")
        folder_path = self.driver.find_element(By.XPATH,"//button[contains(@class,'folder-btn')]//span").text.strip()

        print(folder_path)
        return folder_path

    def verifyClickOnScheduleName(self):
        schedule2 = generate_random_string(5)
        self.createSchedule(schedule2)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{schedule2}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        return self.find_element("S_EDIT_SCHEDULE_ID").get_attribute('value')

    def AddSchedule1(self):
        self.createSchedule(scheduleName1)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName1}']"
        log.logger.info(self.driver.find_element(By.XPATH, schedule_xpath).text)
        return self.driver.find_element(By.XPATH, schedule_xpath).text

    def AddEditSchedule(self):
        self.createSchedule(scheduleName2)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName2}']"
        log.logger.info(self.driver.find_element(By.XPATH, schedule_xpath).text)
        return self.driver.find_element(By.XPATH, schedule_xpath).text

    def AddEditSchedule3(self):
        self.createSchedule(scheduleName3)
        time.sleep(1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName3}']"
        log.logger.info(self.driver.find_element(By.XPATH, schedule_xpath).text)
        return self.driver.find_element(By.XPATH, schedule_xpath).text

    def AddEditSchedule5(self):
        time.sleep(2)
        self.createSchedule(scheduleName5)
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(2)
        schedule_xpath = f"//span[@title='{scheduleName5}']"
        log.logger.info(self.driver.find_element(By.XPATH, schedule_xpath).text)
        return self.driver.find_element(By.XPATH, schedule_xpath).text

    def rename_schedule_with_all_char(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        edit_xpath = f"//td//span[@title='{scheduleName1}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        new_schedule = generate_unique_string(26)
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", new_schedule)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        path = f"//span[@title='{new_schedule}']"
        log.logger.info(self.driver.find_element(By.XPATH, path).text)
        return self.driver.find_element(By.XPATH, path).text

    def rename_schedule_with_all_char2(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        edit_xpath = f"//td//span[@title='{scheduleName2}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        new_schedule = generate_unique_string(26)
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", new_schedule)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(1)
        self.refresh()
        path = f"//span[@title='{new_schedule}']"
        log.logger.info(self.driver.find_element(By.XPATH, path).text)
        return self.driver.find_element(By.XPATH, path).text

    def rename_schedule_with_sc(self):
        self.createSchedule(scheduleName2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        edit_xpath = f"//td//span[@title='{scheduleName2}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", "@g$%")
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(3)
        return self.getText("S_INVALID_MSG_XPATH")

    def verifySaveButtonOnEditSchName(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        edit_xpath = f"//td//span[@title='{scheduleName}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        new_schedule = generate_unique_string(26)
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", new_schedule)
        self.click("S_SAVE_XPATH")
        time.sleep(1)
        self.refresh()
        path = f"//span[@title='{new_schedule}']"
        log.logger.info(self.driver.find_element(By.XPATH, path).text)
        return self.driver.find_element(By.XPATH, path).text

    def cancel_option_on_edit_scheduleName(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        log.logger.info("scheduleName3 : " + scheduleName3)
        edit_xpath = f"//td//span[@title='{scheduleName3}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName3}']"
        log.logger.info(self.driver.find_element(By.XPATH, schedule_xpath).text)
        return self.driver.find_element(By.XPATH, schedule_xpath).text

    def close_option_on_edit_scheduleName(self):
        time.sleep(2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(2)
        edit_xpath = f"//td//span[@title='{scheduleName5}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        time.sleep(2)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        time.sleep(2)
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(2)
        schedule_xpath = f"//span[@title='{scheduleName5}']"
        log.logger.info(self.driver.find_element(By.XPATH, schedule_xpath).text)
        return self.driver.find_element(By.XPATH, schedule_xpath).text

    def getModifiedDateOfSchedule(self):
        self.createSchedule(scheduleName)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        date = f"//td//span[contains(@title,'{scheduleName}')]/following::td[7]"
        return self.driver.find_element(By.XPATH, date).text

    def getModifiedUpdatedDateOfSchedule(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        schedule_xpath = f"//span[@title='{scheduleName}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.click("S_EDIT_PEN_XPATH")
        self.clear("S_EDIT_SCHEDULE_ID")
        new_name = generate_random_string(5)
        self.send_keys("S_EDIT_SCHEDULE_ID", new_name)
        self.click("S_UPDATE_BUTTON_XPATH")
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        date = f"//td//span[contains(@title,'{new_name}')]/following::td[7]"
        return self.driver.find_element(By.XPATH, date).text

    def createFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", folder_name)
        self.click("S_ADD_BUTTON_NAME")
        log.logger.info(folder_name)
        self.refresh()
        self.refresh()
        return folder_name

    def CreateScheduleInsideFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", folder_name)
        option = f"//a[@class='dropdown-item '][contains(.,'{folder_name}')]"
        self.driver.find_element(By.XPATH, option).click()
        time.sleep(2)
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", scheduleName4)
        self.click("S_ADD_BUTTON_NAME")
        self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        folder_name_xpath = f"//td//span[@title='{scheduleName4}']/following::td[1]"
        log.logger.info(self.driver.find_element(By.XPATH, folder_name_xpath).text)
        time.sleep(2)
        return self.driver.find_element(By.XPATH, folder_name_xpath).text

    def createFolder1(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", folder_name1)
        self.click("S_ADD_BUTTON_NAME")
        log.logger.info(folder_name1)
        return folder_name1

    def CreateScheduleInsideFolder1(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.refresh()
        self.refresh()
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", folder_name1)
        option = f"//a[normalize-space()='{folder_name1}']"
        time.sleep(1)
        self.driver.find_element(By.XPATH, option).click()
        time.sleep(2)
        self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", scheduleName6)
        self.click("S_ADD_BUTTON_NAME")
        self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        folder_name_xpath = f"//td//span[@title='{scheduleName6}']/following::td[1]"
        log.logger.info(self.driver.find_element(By.XPATH, folder_name_xpath).text)
        return self.driver.find_element(By.XPATH, folder_name_xpath).text

    def copyScheduleInsideFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", folder_name1)
        option = f"//a[@class='dropdown-item '][contains(.,'{folder_name1}')]"
        self.driver.find_element(By.XPATH, option).click()
        time.sleep(4)
        copy_xpath = f"//td//span[@title='{scheduleName6}']/following::td[2]//a[1]"
        self.driver.find_element(By.XPATH, copy_xpath).click()
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", generate_random_string(5))
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(3)
        folder = f"//td[contains(.,'{folder_name1}')]"
        folder_count = self.driver.find_elements(By.XPATH, folder)
        print(len(folder_count))
        return str(len(folder_count))

    def getScheduleCount(self):
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def createMultipleSchedule(self, count):
        for i in range(count):
            if configReader.getTestData("TestData", "Environment") == "prod":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
            self.click("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
            self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", generate_random_string(5))
            self.click("S_ADD_BUTTON_NAME")
            self.wait_for_visible_all_elements("S_EDIT_SCHEDULE_ID")
            time.sleep(1)

    def deleteAllSchedules(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_SELECT_ALL_XPATH")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(4)

    def getScheduleTrashedCount(self):
        time.sleep(1)
        self.click("S_TRASHED_XPATH")
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def verifyNextOptionOnTrashed(self):
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def verifyNextOptionOnTrash(self):
        self.click("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def verifyPreviousOptionOnScheduleTrashed(self):
        time.sleep(1)
        previous_button_xpath = f"//a[@data-dt-idx='0']"
        getTextAfterRetry(self.driver, By.XPATH, previous_button_xpath)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_PREVIOUS_BUTTON_XPATH"))
        time.sleep(1)
        getTextAfterRetry(self.driver, By.XPATH, previous_button_xpath)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_PREVIOUS_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def createFolder_new(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", new_folder_name)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        return self.getText("S_SUB_FOLDER_LOC_XPATH")

    def createFolder_new1(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", folder_name_new)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        return self.getText("S_SUB_FOLDER_LOC_XPATH")

    def folder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", fname)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        return self.getText("S_SUB_FOLDER_LOC_XPATH")

    def new_folder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", new_fname)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(4)
       # return lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH"))
        return new_fname

    def verifyCancelButtonOnCreateFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", folder_name_new)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(1)
        self.click("S_CREATE_CONTENT_XPATH")
        self.refresh()
        elements = self.find_elements("S_HEADING_CREATE_FOLDER_XPATH")
        log.logger.info(str(len(elements)))
        return str(len(elements))

    def verifyAllCharInCreateFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", generate_unique_string(26))
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        return self.getText("S_SUB_FOLDER_LOC_XPATH")

    def verifySCInCreateFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", "#@%@")
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        return self.getText("S_INVALID_MSG_XPATH")

    def verifySCDotInCreateFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        name = generate_random_string(3) + ".xx"
        self.send_keys("S_FOLDER_NAME_XPATH", name)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(1)
        ele = self.find_elements("S_INVALID_MSG_XPATH")
        return str(len(ele))
    
    def get10Entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "10")
        time.sleep(1)
        return Schedules(self.driver)

    def get20Entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "20")
        time.sleep(1)
        return Schedules(self.driver)

    def get50Entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "50")
        time.sleep(1)
        return Schedules(self.driver)

    def get100Entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(1)
        return Schedules(self.driver)

    def get200Entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "200")
        time.sleep(1)
        return Schedules(self.driver)

    def get500Entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "500")
        time.sleep(1)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def verifyNextOption(self):
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(2)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def moreSchedules(self):
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_NEXT_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def verifyPreviousOptionOnSchedule(self):
        time.sleep(1)
        previous_button_xpath = f"//a[@data-dt-idx='0']"
        getTextAfterRetry(self.driver, By.XPATH, previous_button_xpath)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_PREVIOUS_BUTTON_XPATH"))
        time.sleep(1)
        getTextAfterRetry(self.driver, By.XPATH, previous_button_xpath)
        self.driver.execute_script("arguments[0].click();", self.find_element("S_PREVIOUS_BUTTON_XPATH"))
        time.sleep(1)
        return self.getText("S_ENTRIES_COUNT_XPATH")

    def getCurrentWeek(self):
        self.createSchedule(sc_name)
        return self.getText("S_CURRENT_WEEK_XPATH")

    def getCurrentWeek_(self):
        self.createSchedule(sc_name20)
        return self.getText("S_CURRENT_WEEK_XPATH")

    def getCurrentWeekDate(self):
        self.createSchedule(sch_name)
        self.click("S_NEXT_WEEK_BUTTON_XPATH")
        self.click("S_NEXT_WEEK_BUTTON_XPATH")
        return self.getText("S_CURRENT_WEEK_XPATH")

    def getPreviousWeek(self):
        self.click("S_PREVIOUS_WEEK_BUTTON_XPATH")
        return self.getText("S_CURRENT_WEEK_XPATH")

    def getNextWeek(self):
        self.click("S_NEXT_WEEK_BUTTON_XPATH")
        return self.getText("S_CURRENT_WEEK_XPATH")

    def clickToday(self):
        self.click("S_TODAY_BTN_XPATH")
        return self.getText("S_CURRENT_WEEK_XPATH")

    def createTrigger(self):
        today = date.today()
        d1 = today.strftime("%d%m%Y")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.createSchedule(sc_cont_name)
        self.click("S_ADD_TRIGGER_BTN_XPATH")
        self.click("S_ADD_TIME_TRIGGER_BUTTON_XPATH")
        self.send_keys("S_TRIGGER_NAME_ID", trigger_name)
        self.click("S_SELECT_PLAY_CONTENT_XPATH")
        self.click("S_CONTENT_XPATH")
        self.click("S_DAILY_TRIGGER_RB_ID")
        self.click("S_TRIGGER_CONTENT_ID")
        ele = f"//select[@id='trigger_content_id']//option[3]"
        self.driver.find_element(By.XPATH, ele).click()
        self.selenium_click("S_DAILY_TRIGGER_RB_ID")
        self.send_keys("S_TRIGGER_START_DATE_ID", d1)
        self.send_keys("S_TRIGGER_END_DATE_ID", d1)
        self.send_keys("S_TRIGGER_START_TIME_ID", "15:01")
        self.click("S_ADD_BUTTON_NAME")
        element_XPATH = f"//span[@title='{trigger_name}']"
        cnt = self.driver.find_elements(By.XPATH, element_XPATH)
        return str(len(cnt))

    def createNewSchedule(self):
        self.createSchedule(sch_name_new_01)

    def DuplicateSchedule(self):
        self.createSchedule(sch_name_new_02)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        edit_xpath = f"//td//span[@title='{sch_name_new_01}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        self.clear("S_SCHEDULE_NAME_INPUT_XPATH")
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", sch_name_new_02)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(1)
        return self.getText("S_INVALID_MSG_XPATH")

    def editSchedule(self):
        self.createSchedule(sch_name_new1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        edit_xpath = f"//td//span[@title='{sch_name_new1}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, edit_xpath)
        name = self.find_elements("S_SCHEDULE_NAME_INPUT_XPATH")
        return str(len(name))

    def scroll(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(1)
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount == lenOfPage:
                match = True

    def scrollTrash(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        self.click("S_TRASHED_XPATH")
        self.wait_for_visible_all_elements("S_DROP_TRASH_XPATH")
        self.select_option_by_value_from_dropdown("S_DROP_TRASH_XPATH", "100")
        time.sleep(2)
        lenOfPage = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match = False
        while (match == False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return "
                "lenOfPage;")
            if lastCount == lenOfPage:
                match = True

    def verifyCloseOptionOnCreateFolder(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_CREATE_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", fn)
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(1)
        return self.get_current_url()

    def trashedSchedule(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "trashed_schedule_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "trashed_schedule_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "trashed_schedule_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "trashed_schedule_sit2_url"))

    def pop_up(self):
        # self.driver.get("https://digitalsignage.jio.com/v2/profile/user_details")
        # self.driver.find_element(By.XPATH, "(//button[@class='btn edit-pen login-pass'])[1]").click()
        # self.driver.find_element(By.XPATH, "//input[@name='v2_user[name]']").clear()
        # # self.driver.find_element(By.XPATH, "//input[@name='v2_user[name]']").send_keys("Shivaji")
        # self.driver.execute_script("document.getElementsByName('v2_user[name]')[0].value='abcde'")
        # self.driver.find_element(By.XPATH, "//input[@class='btn btn-base1']").send_keys(Keys.ENTER)
        # WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@id='alertFlash']")))
        # self.driver.find_element(By.XPATH, "//div[@id='alertFlash']")
        # # self.wait_for_visible_all_elements("S_FLASH_ID")
        # # log.logger.info(self.getText("S_FLASH_ID"))
        # time.sleep(2)
        # print(self.driver.page_source)
        # flash_message_text = self.driver.execute_script("document.getElementById('flash').textContent")
        # print(flash_message_text)
        pass

    def createScheduleForCount(self):
        self.createSchedule(scheduleForCount)

    def verify1hrDuration(self):
        self.refresh()
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_1HR_DURATION_XPATH")
        time.sleep(1)
        element_text = []
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        for i in time_count:
            element_text.append(i.text)
        return element_text

    def verify1hrDurationCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_1HR_DURATION_XPATH")
        empty_time = self.find_elements("S_BLANK_TIME_XPATH")
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        return len(time_count) + len(empty_time)

    def verify30MinDuration(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_30MIN_DURATION_XPATH")
        time.sleep(1)
        element_text = []
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        for i in time_count:
            element_text.append(i.text)
        return element_text

    def verify30MinDurationCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_30MIN_DURATION_XPATH")
        empty_time = self.find_elements("S_BLANK_TIME_XPATH")
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        log.logger.info("time_count : " + str(len(time_count)))
        log.logger.info("empty_time : " + str(len(empty_time)))
        log.logger.info(len(time_count) + len(empty_time))
        return len(time_count) + len(empty_time)

    def verify15MinDuration(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_15MIN_DURATION_XPATH")
        time.sleep(1)
        element_text = []
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        for i in time_count:
            element_text.append(i.text)
        return element_text

    def verify15MinDurationCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_15MIN_DURATION_XPATH")
        empty_time = self.find_elements("S_BLANK_TIME_XPATH")
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        log.logger.info("time_count : " + str(len(time_count)))
        log.logger.info("empty_time : " + str(len(empty_time)))
        log.logger.info(len(time_count) + len(empty_time))
        return len(time_count) + len(empty_time)

    def verify10MinDuration(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_10MIN_DURATION_XPATH")
        time.sleep(1)
        element_text = []
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        for i in time_count:
            element_text.append(i.text)
        return element_text

    def verify10MinDurationCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_10MIN_DURATION_XPATH")
        empty_time = self.find_elements("S_BLANK_TIME_XPATH")
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        log.logger.info("time_count : " + str(len(time_count)))
        log.logger.info("empty_time : " + str(len(empty_time)))
        log.logger.info(len(time_count) + len(empty_time))
        return len(time_count) + len(empty_time)

    def verify05MinDuration(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_05MIN_DURATION_XPATH")
        time.sleep(1)
        element_text = []
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        for i in time_count:
            element_text.append(i.text)
        return element_text

    def verify05MinDurationCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{scheduleForCount}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        self.selenium_click("S_TIME_DROPDOWN_XPATH")
        self.click("S_05MIN_DURATION_XPATH")
        empty_time = self.find_elements("S_BLANK_TIME_XPATH")
        time_count = self.find_elements("S_FILLED_TIME_XPATH")
        log.logger.info("time_count : " + str(len(time_count)))
        log.logger.info("empty_time : " + str(len(empty_time)))
        log.logger.info(len(time_count) + len(empty_time))
        return len(time_count) + len(empty_time)

    def contentPopupRemoval(self):
        time.sleep(3)
        self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return Schedules(self.driver)

    def clickOnOkBtn(self):
        # time.sleep(2)
        # self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        okBtn = self.find_elements("O_CONTENT_OK_BTN_XPATH")
        c = len(okBtn)
        if c == 1:
            self.click("O_CONTENT_OK_BTN_XPATH")
        else:
            pass
        return Schedules(self.driver)

    def createContentForTesting(self, contentName):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        self.send_keys("S_CONTENT_NAME_XPATH", contentName)
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        time.sleep(3)
        self.contentPopupRemoval()
        log.logger.info("Created content : " + contentName )
        return Schedules(self.driver)

    def createContent_c1(self):
        global c1
        c1 = generate_random_string(5)
        self.createContentForTesting(c1)
        return Schedules(self.driver)

    def createContent_c2(self):
        global c2
        c2 = generate_random_string(5)
        self.createContentForTesting(c2)
        return Schedules(self.driver)

    def createContent_c3(self):
        global c3
        c3 = generate_random_string(5)
        self.createContentForTesting(c3)
        return Schedules(self.driver)

    def createContent_c4(self):
        global c4
        c4 = generate_random_string(5)
        self.createContentForTesting(c4)
        return Schedules(self.driver)

    def createContent_c5(self):
        global c5
        c5 = generate_random_string(5)
        self.createContentForTesting(c5)
        return Schedules(self.driver)

    def createContent_c6(self):
        global c6
        c6 = generate_random_string(5)
        self.createContentForTesting(c6)
        return Schedules(self.driver)

    def createContent_c7(self):
        global c7
        c7 = generate_random_string(5)
        self.createContentForTesting(c7)
        return Schedules(self.driver)

    def createContent_c8(self):
        global c8
        c8 = generate_random_string(5)
        self.createContentForTesting(c8)
        return Schedules(self.driver)

    def createContent_c9(self):
        global c9
        c9 = generate_random_string(5)
        self.createContentForTesting(c9)
        return Schedules(self.driver)

    def createContent_c10(self):
        global c10
        c10 = generate_random_string(5)
        self.createContentForTesting(c10)
        return Schedules(self.driver)

    def createContent_c11(self):
        global c11
        c11 = generate_random_string(5)
        self.createContentForTesting(c11)
        return Schedules(self.driver)

    def createContent_c12(self):
        global c12
        c12 = generate_random_string(5)
        self.createContentForTesting(c12)
        return Schedules(self.driver)

    def deleteContent(self, contentName):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        content_title = f"//span[@title='{contentName}']"
        if len(self.driver.find_elements(By.XPATH, content_title)) > 0:
            time.sleep(1)
            ele = f"//span[@title='{contentName}']/preceding::input[@type='checkbox'][1]"
            checkbox = self.driver.find_element(By.XPATH, ele)
            self.driver.execute_script("arguments[0].click();", checkbox)
            log.logger.info("Content checkbox selected ")
            time.sleep(1)
            self.click("X_MORE_OPTIONS_XPATH")
            log.logger.info("More option selected ")
            time.sleep(1)
            self.click("S_MOVE_TO_TRASH_XPATH")
            log.logger.info("Move to trash selected")
            time.sleep(1)
            self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
            self.click("S_CONFIRM_BUTTON_XPATH")
            time.sleep(1)
            self.click("S_TRASHED_XPATH")
            log.logger.info("clicked on trashed")
            time.sleep(2)
            # self.driver.find_element(By.XPATH, chk).click()
            self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, ele))
            log.logger.info("Select checkbox again")
            time.sleep(1)
            self.click("X_MORE_OPTIONS_XPATH")
            time.sleep(1)
            log.logger.info("Click on more options")
            self.click("S_DELETE_C_XPATH")
            self.click("S_CONFIRM_BTN_XPATH")
            time.sleep(1)
        else:
            pass

    def delete_content_c1(self):
        log.logger.info("deleting content : " + c1)
        self.deleteContent(c1)

    def delete_content_c2(self):
        log.logger.info("deleting content : " + c2)
        self.deleteContent(c2)

    def delete_content_c3(self):
        log.logger.info("deleting content : " + c3)
        self.deleteContent(c3)

    def delete_content_c4(self):
        log.logger.info("deleting content : " + c4)
        self.deleteContent(c4)

    def delete_content_c5(self):
        log.logger.info("deleting content : " + c5)
        self.deleteContent(c5)

    def delete_content_c6(self):
        log.logger.info("deleting content : " + c6)
        self.deleteContent(c6)

    def delete_content_c7(self):
        log.logger.info("deleting content : " + c7)
        self.deleteContent(c7)

    def delete_content_c8(self):
        log.logger.info("deleting content : " + c8)
        self.deleteContent(c8)

    def delete_content_c9(self):
        log.logger.info("deleting content : " + c9)
        self.deleteContent(c9)

    def delete_content_c10(self):
        log.logger.info("deleting content : " + c10)
        self.deleteContent(c10)

    def delete_content_c11(self):
        log.logger.info("deleting content : " + c11)
        self.deleteContent(c11)

    def delete_content_c12(self):
        log.logger.info("deleting content : " + c12)
        self.deleteContent(c12)

    def createContent(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        self.send_keys("S_CONTENT_NAME_XPATH", new_content_name)
        self.click("S_BLANK_TMP_XPATH")
        self.click("S_SUBMIT_BUTTON_ID")
        self.wait_for_visible_all_elements("S_POPUP_XPATH")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "dashboard_preprod_url"))
        log.logger.info(self.getText("S_ALL_CONTENT_COUNT_XPATH"))
        return self.getText("S_ALL_CONTENT_COUNT_XPATH")

    def searchForContent(self):
        self.createSchedule(xxx)
        self.click("S_LAYOUT_PLUS_XPATH")
        self.send_keys("S_SEARCH_CONTENT_ID", c1)
        time.sleep(1)
        path = f"//span[contains(text(),'{c1}')]"
        log.logger.info("length is : " + str(len(self.driver.find_elements(By.XPATH, path))))
        return len(self.driver.find_elements(By.XPATH, path))

    def getApprovalStatus(self):
        time.sleep(2)
        self.wait_for_visible_all_elements("S_LAYOUT_PLUS_XPATH")
        self.click("S_LAYOUT_PLUS_XPATH")
        self.send_keys("S_SEARCH_CONTENT_ID", c1)
        time.sleep(1)
        status = f"//span[contains(text(),'{c1}')]//div"
        #edited_by_dixit
        approval_status = self.driver.find_element(By.XPATH, status).text
        log.logger.info("approval_status : " + approval_status)
        return approval_status

    def getDuration(self):
        self.click("S_LAYOUT_PLUS_XPATH")
        self.send_keys("S_SEARCH_CONTENT_ID", c1)
        time.sleep(1)
        duration_xpath = f"//span[contains(.,'{c1}')]//div[@class='sidebar-duration']"
        duration = self.driver.find_element(By.XPATH, duration_xpath).text
        log.logger.info(duration)
        return duration

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def checkForAccount(self):
        current_user = self.getCurrentAccount()
        if current_user != "Head User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(1)
            retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
        else:
            pass
        self.refresh()
        time.sleep(1)
        return self.getCurrentAccount()

    def createBaseAccount(self):
        self.checkForAccount()
        self.click("S_UA_XPATH")
        self.click("S_BM_XPATH")
        self.click("S_NB_ACC_XPATH")
        self.send_keys("S_BASE_ACC_NAME_XPATH", base_acc_name)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)
        return Schedules(self.driver)

    def createNewBaseAccount(self):
        self.checkForAccount()
        self.click("S_UA_XPATH")
        self.click("S_BM_XPATH")
        self.click("S_NB_ACC_XPATH")
        self.send_keys("S_BASE_ACC_NAME_XPATH", new_base_acc_name)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)

    def switchToBase(self):
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Head User":
            retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
            time.sleep(1)
            self.click("S_SWITCH_BASE_ID")
            time.sleep(1)
            self.click("S_BASE_DROPDOWN_XPATH")
            time.sleep(1)
            log.logger.info(base_acc_name)
            self.send_keys("S_INPUT_BASE_XPATH", base_acc_name)
            time.sleep(1)
            base = f"//li[.='{base_acc_name}']"
            self.driver.find_element(By.XPATH, base).click()
            self.click("S_ADD_BUTTON_NAME")
        else:
            pass
        self.refresh()

    def switchToNewBase(self):
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Head User":
            retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
            time.sleep(1)
            self.click("S_SWITCH_BASE_ID")
            time.sleep(1)
            self.click("S_BASE_DROPDOWN_XPATH")
            time.sleep(1)
            log.logger.info(new_base_acc_name)
            self.send_keys("S_INPUT_BASE_XPATH", base_acc_name)
            time.sleep(1)
            base = f"//li[.='{base_acc_name}']"
            self.driver.find_element(By.XPATH, base).click()
            self.click("S_ADD_BUTTON_NAME")
        else:
            pass
        self.refresh()

    def createContentInBase(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "all_content_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        self.get100Entries()
        content_count = self.driver.find_elements(By.XPATH, "//span[@title='base_aaa']")
        if len(content_count) == 0:
            log.logger.info("Creating content with name : base_aaa")
            self.click("S_CREATE_CONTENT_XPATH")
            self.send_keys("S_CONTENT_NAME_XPATH", "base_aaa")
            self.click("S_BLANK_TMP_XPATH")
            self.click("S_SUBMIT_BUTTON_ID")
            time.sleep(12)
            if configReader.getTestData("TestData", "Environment") == "prod":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
            elif configReader.getTestData("TestData", "Environment") == "pre-prod":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit1":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
            elif configReader.getTestData("TestData", "Environment") == "sit2":
                self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        else:
            log.logger.info("Content base_WRv is already present..")
            pass

    def checkItemCountBeforeDrag(self):
        self.createSchedule(dra_drop_schedule)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        path = f"//td[contains(.,'{dra_drop_schedule}')]/following-sibling::td[5]"
        log.logger.info("checkItemCountBeforeDrag :" + self.driver.find_element(By.XPATH, path).text)
        return self.driver.find_element(By.XPATH, path).text

    def before_checkItemCount(self):
        self.createSchedule(dra_drop_schedule100)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        path = f"//td[contains(.,'{dra_drop_schedule100}')]/following-sibling::td[5]"
        return self.driver.find_element(By.XPATH, path).text

    def verifyCountAfterDrag(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule100}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        item_count = self.driver.find_element(By.XPATH, "//td[7]").text
        return item_count

    def verifyDragDrop(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        self.refresh()
        time.sleep(1)
        schedule_xpath = f"//span[@title='{dra_drop_schedule}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        log.logger.info("schedule_xpath : schedule_xpath")
        self.clickonpluscomntent()
        time.sleep(1)
        C2_XPATH = f"//span[contains(.,'{c2}')]"
        Content_C2_Drag = self.driver.find_element(By.XPATH, C2_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        Content_C2_Drop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_C2_Drag, Content_C2_Drop).perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        item_count = self.driver.find_element(By.XPATH, "//td[7]").text
        log.logger.info("verifyDragDrop : " + item_count)
        return item_count

    def verifyEditScheduleOnDragContent(self):
        self.createSchedule(dra_drop_schedule1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule1}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        time.sleep(1)
        C3_XPATH = f"//span[contains(.,'{c3}')]"
        Content_C3_Drag = self.driver.find_element(By.XPATH, C3_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        Content_C3_Drop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_C3_Drag, Content_C3_Drop).perform()
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        text = self.getText("S_MODEL_HEADER_XPATH")
        return text

    def verifyStartTime(self):
        self.createSchedule(dra_drop_schedule2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule2}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        C4_XPATH = f"//span[contains(.,'{c4}')]"
        Content_C4_Drag = self.driver.find_element(By.XPATH, C4_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        Content_C4_Drop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        time.sleep(2)
        ActionChains(self.driver).drag_and_drop(Content_C4_Drag, Content_C4_Drop).perform()
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02am")
        self.send_keys("S_END_TIME_ID", "20:20pm")
        self.click("S_SAVE_B_XPATH")
        time.sleep(2)
        getTime = self.getText("S_EVENT_TIME_XPATH")
        log.logger.info("getTime : " + getTime)
        assert getTime == "2:02am - 8:20pm"

    def verifyStartEndTimeOnSchedule(self):
        global schedule200
        schedule200 = generate_random_string(5)
        self.createSchedule(schedule200)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{schedule200}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02am")
        time.sleep(2)
        self.send_keys("S_END_TIME_ID", "20:20pm")
        time.sleep(3)
        self.selenium_click("S_SAVE_B_XPATH")
        time.sleep(3)
        getTime = self.getText("S_EVENT_TIME_XPATH")
        log.logger.info(getTime)
        assert "2:02am - 8:20pm" == getTime

    def verifyUpdateTime(self):
        self.createSchedule(schedule007)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{schedule007}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02")
        self.send_keys("S_END_TIME_ID", "20:20")
        self.click("S_SAVE_B_XPATH")
        time.sleep(1)
        getTime = self.getText("S_EVENT_TIME_XPATH")
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "03:03")
        self.send_keys("S_END_TIME_ID", "21:20")
        self.click("S_SAVE_B_XPATH")
        time.sleep(1)
        getTime_new = self.getText("S_EVENT_TIME_XPATH")
        assert getTime != getTime_new

    def verifyEndTime(self):
        self.createSchedule(dra_drop_schedule3)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule3}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        C5_XPATH = f"//span[contains(.,'{c5}')]"
        Content_C5_Drag = self.driver.find_element(By.XPATH, C5_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        Content_C5_Drop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_C5_Drag, Content_C5_Drop).perform()
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02am")
        time.sleep(5)
        self.send_keys("S_END_TIME_ID", "20:20pm")
        time.sleep(5)
        self.click("S_SAVE_B_XPATH")
        getTime = self.getText("S_EVENT_TIME_XPATH")
        log.logger.info(getTime)
        assert getTime == "2:02am - 8:20pm"

    def verifyRepeatCheckBox(self):
        self.createSchedule(dra_drop_schedule4)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule4}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        C6_XPATH = f"//span[contains(.,'{c6}')]"
        Content_C6_Drag = self.driver.find_element(By.XPATH, C6_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        Content_C6_Drop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_C6_Drag, Content_C6_Drop).perform()
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.click("S_REPEAT_CHECK_XPATH")
        S_Date = self.getText("S_START_DATE_XPATH")
        E_Date = self.getText("S_END_DATE_XPATH")
        log.logger.info(S_Date + E_Date)
        return S_Date + E_Date

    def verifyStartDate(self):
        today = date.today()
        tomorrow = today + timedelta(days=2)
        today_date = today.strftime('%d-%m-%Y')
        tomorrow_date = tomorrow.strftime('%d-%m-%Y')
        self.createSchedule(dra_drop_schedule5)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule5}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        Content_XPATH = f"//span[contains(.,'{c7}')]"
        Content_Drag = self.driver.find_element(By.XPATH, Content_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        ContentDrop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_Drag, ContentDrop).perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        getDate = f"//td//span[@title='{dra_drop_schedule5}']/following::td[4]"
        data = self.driver.find_element(By.XPATH, getDate).text
        log.logger.info(data)
        schedule_xpath = f"//span[@title='{dra_drop_schedule5}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.click("S_REPEAT_CHECK_XPATH")
        self.send_keys("S_SET_START_DATE_ID", today_date)
        self.send_keys("S_SET_END_DATE_ID", tomorrow_date)
        self.click("S_SAVE_B_XPATH")
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        getUpdatedDate = f"//td//span[@title='{dra_drop_schedule5}']/following::td[4]"
        updated_data = self.driver.find_element(By.XPATH, getUpdatedDate).text
        log.logger.info(updated_data)
        assert data != updated_data

    def getRepeatCount(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule5}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        cnt = len(self.find_elements("S_CONTAINER_XPATH"))
        assert cnt == 3

    def verifyEndDate(self):
        today = date.today()
        tomorrow = today + timedelta(days=2)
        today_date = today.strftime('%d-%m-%Y')
        tomorrow_date = tomorrow.strftime('%d-%m-%Y')
        self.createSchedule(dra_drop_schedule6)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule6}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        Content_XPATH = f"//span[contains(.,'{c8}')]"
        Content_Drag = self.driver.find_element(By.XPATH, Content_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        ContentDrop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_Drag, ContentDrop).perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        getDate = f"//td//span[@title='{dra_drop_schedule6}']/following::td[4]"
        data = self.driver.find_element(By.XPATH, getDate).text
        log.logger.info(data)
        schedule_xpath = f"//span[@title='{dra_drop_schedule6}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.click("S_REPEAT_CHECK_XPATH")
        self.send_keys("S_SET_START_DATE_ID", today_date)
        self.send_keys("S_SET_END_DATE_ID", tomorrow_date)
        self.click("S_SAVE_B_XPATH")
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        getUpdatedDate = f"//td//span[@title='{dra_drop_schedule6}']/following::td[4]"
        updated_data = self.driver.find_element(By.XPATH, getUpdatedDate).text
        log.logger.info(updated_data)
        assert data != updated_data

    def getRepeat(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule6}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        cnt = len(self.find_elements("S_CONTAINER_XPATH"))
        assert cnt == 3

    def verifySaveSchedule(self):
        self.createSchedule(dra_drop_schedule7)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule7}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        Content_XPATH = f"//span[contains(.,'{c9}')]"
        Content_Drag = self.driver.find_element(By.XPATH, Content_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        ContentDrop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_Drag, ContentDrop).perform()
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02am")
        time.sleep(1)
        self.send_keys("S_END_TIME_ID", "20:20pm")
        time.sleep(1)
        self.click("S_SAVE_B_XPATH")
        time.sleep(1)
        getTime = self.getText("S_EVENT_TIME_XPATH")
        log.logger.info(getTime)
        print(getTime)
        assert getTime == "2:02am - 8:20pm"

    def verifyCancelSchedule(self):
        self.createSchedule(dra_drop_schedule8)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule8}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        Content_XPATH = f"//span[contains(.,'{c10}')]"
        Content_Drag = self.driver.find_element(By.XPATH, Content_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        ContentDrop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_Drag, ContentDrop).perform()
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02")
        self.send_keys("S_END_TIME_ID", "20:20")
        self.click("S_CANCEL_OPTION_XPATH")
        count = len(self.find_elements("S_EVENT_TIME_XPATH"))
        assert count == 0

    def verifyDeleteSchedule(self):
        self.createSchedule(dra_drop_schedule10)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{dra_drop_schedule10}']"
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(By.XPATH, schedule_xpath))
        time.sleep(1)
        self.clickonpluscomntent()
        Content_XPATH = f"//span[contains(.,'{c11}')]"
        Content_Drag = self.driver.find_element(By.XPATH, Content_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        ContentDrop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_Drag, ContentDrop).perform()
        time.sleep(1)
        self.selenium_click("S_CLOSE_BUTTON_ON_XPATH")
        time.sleep(1)
        xpath = f"//span[@title='{dra_drop_schedule10}']/following::td[5]"
        item_count = self.driver.find_element(By.XPATH, xpath).text
        schedule_xpath = f"//span[@title='{dra_drop_schedule10}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02")
        time.sleep(1)
        self.send_keys("S_END_TIME_ID", "20:20")
        time.sleep(0.7)
        self.click("S_DELETE_SCHEDULE_XPATH")
        self.wait_for_visible_all_elements("S_YES_BUTTON_XPATH")
        time.sleep(0.5)
        self.click("S_YES_BUTTON_XPATH")
        self.selenium_click("S_CLOSE_BUTTON_ON_XPATH")
        # time.sleep(1)
        # self.click("S_YES_BUTTON_XPATH")
        time.sleep(1)
        n_xpath = f"//span[@title='{dra_drop_schedule10}']/following::td[5]"
        item_count_after = self.driver.find_element(By.XPATH, n_xpath).text
        log.logger.info(" item_count : " + item_count)
        log.logger.info(" item_count_after : " + item_count_after)
        assert item_count != item_count_after

    def verifyCurrentDate(self):
        value = None
        today = date.today()
        day = today.strftime('%a')
        month = int(today.strftime('%m'))
        dates = int(today.strftime('%d'))
        final_date = day + " " + str(month) + "/" + str(dates)
        self.createSchedule(sc1)
        log.logger.info("today_date : " + final_date)
        all_dates = self.driver.find_elements(By.XPATH, "//a[@class='fc-col-header-cell-cushion']")
        log.logger.info(str(len(all_dates)))
        for i in all_dates:
            new_date = i.text
            if new_date in final_date:
                value = "True"
                break
            else:
                value = "False"
        return value

    def createPlaylist(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
        self.driver.find_element(By.XPATH,
                                 "//img[@src='/packs/media/images/plus-f52f2f30a07d6b041ced0381242a9973.png']").click()
        self.driver.find_element(By.XPATH, "//input[@class='form-control add-new-playlist']").send_keys("xxx")
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-base1']").click()
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        ele = self.find_element("O_FIRST_CONTENT_XPATH")
        # self.dragAndDrop("O_FIRST_CONTENT_XPATH", "s_CAN_XPATH")
        # time.sleep(5)
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(ele, 100, 100).perform()
        time.sleep(10)

    def verifyCheckOptionOnSchedule(self):
        self.createSchedule(schedule21)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        schedule_xpath = f"//span[@title='{schedule21}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        ele_visible = len(self.find_elements("S_MORE_OPTION_XPATH"))
        return ele_visible

    def verifySearchSchedule(self):
        self.createSchedule(sc_name1)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.send_keys("S_SEARCH_XPATH", sc_name1)
        time.sleep(3)
        nameOf_schedule_xpath = f"//span[@title='{sc_name1}']"
        nameOf_schedule = self.driver.find_element(By.XPATH, nameOf_schedule_xpath).text
        assert sc_name1 == nameOf_schedule

    def verifyFilterSearch(self):
        self.createSchedule(sc_name2)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_FILTER_XPATH")
        self.wait_for_visible_all_elements("S_COLUMN_INPUT_XPATH")
        element_size = len(self.find_elements("S_COLUMN_INPUT_XPATH"))
        return element_size

    def verifyFilterSearchName(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.click("S_FILTER_XPATH")
        self.wait_for_visible_all_elements("S_COLUMN_INPUT_XPATH")
        self.send_keys("S_COLUMN_INPUT_XPATH", sc_name2)
        time.sleep(3)
        nameOf_schedule_xpath = f"//span[@title='{sc_name2}']"
        nameOf_schedule = self.driver.find_element(By.XPATH, nameOf_schedule_xpath).text
        assert sc_name2 == nameOf_schedule

    def verifyCheckOptionOnScheduleTrashed(self):
        self.createSchedule(schedule30)
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        ele = f"//span[@title='{schedule30}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, ele)
        self.driver.execute_script("arguments[0].click();", checkbox)
        log.logger.info("Schedule checkbox selected ")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        log.logger.info("clicked on confirm button")
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        chk = f"//span[@title='{schedule30}']/preceding::input[@type='checkbox'][1]"
        check = self.driver.find_element(By.XPATH, chk)
        #time.sleep(2)
        self.driver.execute_script("arguments[0].click();", check)
        log.logger.info("Select checkbox again")
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        ele_visible = len(self.find_elements("S_MORE_OPTION_XPATH"))
        return ele_visible

    def EditExistingSchedule(self):
        schedule99 = generate_random_string(5)
        self.createSchedule(schedule99)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        schedule_xpath = f"//span[@title='{schedule99}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_3RD_POS_XPATH")
        time.sleep(2)
        self.selenium_click("S_DROP_3RD_POS_XPATH")
        return self.getText("S_MODEL_HEADER_XPATH")

    def verifyDragDropForExistingSchedule(self):
        schedule999 = generate_random_string(5)
        self.createSchedule(schedule999)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        schedule_xpath = f"//span[@title='{schedule999}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(3)
        self.clickonpluscomntent()
        time.sleep(2)
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_3RD_POS_XPATH")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        item_count = self.driver.find_element(By.XPATH, "//td[7]").text
        return item_count

    def createContentInFolder(self):
        global c12
        c12 = generate_random_string(5)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_FOLDER_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", f_name)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(2)
        self.wait_for_visible_all_elements("S_CREATE_CONTENT_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        self.send_keys("S_CONTENT_NAME_XPATH", c12)
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        self.clickOnOkBtn()
        self.contentPopupRemoval()
        log.logger.info("Created content : " + c12)
        return Schedules(self.driver)

    def verifyDragAndDropFromFolder(self):
        self.createSchedule(schedule090)
        log.logger.info("Schedule created : " + schedule090)
        path = f"//span[contains(.,'{f_name}')]"
        log.logger.info("path : " + path)
        self.clickonpluscomntent()
        self.driver.find_element(By.XPATH, path).click()
        log.logger.info("Clicked on folder + icon")
        # content_path = f"//span[contains(.,'{cn_name}')]"
        # log.logger.info("content_path : " + content_path)
        # drop_loc = f"(//div[@class='fc-daygrid-day-events'])[4]"
        # c_path = self.driver.find_element(By.XPATH, content_path)
        # # self.driver.execute_script("arguments[0].scrollIntoView();", c_path)
        # time.sleep(1)
        # self.clickonpluscomntent()
        # time.sleep(1)
        Content_XPATH = f"//span[contains(.,'{c12}')]"
        Content_Drag = self.driver.find_element(By.XPATH, Content_XPATH)
        drop_location_XPATH = f"(//div[@class='fc-daygrid-day-events'])[4]"
        ContentDrop = self.driver.find_element(By.XPATH, drop_location_XPATH)
        ActionChains(self.driver).drag_and_drop(Content_Drag, ContentDrop).perform()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[.='Close']").click()
        time.sleep(1)
        item_count = self.driver.find_element(By.XPATH, "//td[7]").text
        return item_count

    def createScheduleForTime(self):
        global schedule121
        schedule121 = generate_unique_string(5)
        self.createSchedule(schedule121)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        self.dragAndDrop("O_FIRST_CONTENT_XPATH", "S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.selenium_click("S_DROP_LOCATION_XPATH")
        self.send_keys("S_START_TIME_ID", "05:02am")
        self.send_keys("S_END_TIME_ID", "07:230pm")
        self.selenium_click("S_SAVE_B_XPATH")
        time.sleep(1)
        getTime = self.getText("S_EVENT_TIME_XPATH")
        log.logger.info("Old time : " + getTime)
        return getTime

    def verifyTime(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_sit2_url"))
        schedule_xpath = f"//span[@title='{schedule121}']"
        retry_action(self.driver, By.XPATH, schedule_xpath)
        time.sleep(1)
        self.click("S_EVENT_NAME_TIME_XPATH")
        self.send_keys("S_START_TIME_ID", "02:02am")
        self.send_keys("S_END_TIME_ID", "20:20pm")
        self.selenium_click("S_SAVE_B_XPATH")
        time.sleep(1)
        getTime = self.getText("S_EVENT_TIME_XPATH")
        log.logger.info("new time : " + getTime)
        return getTime

    def switchToHead(self):
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Base User":
            self.click("S_HEAD_ID")
            S_SWITCH_TO_HEAD_XPATH = self.find_elements("S_SWITCH_TO_HEAD_XPATH")
            log.logger.info("Len of element is : " + str(len(S_SWITCH_TO_HEAD_XPATH)))
            self.click("S_SWITCH_TO_HEAD_XPATH")
        else:
            pass
        self.refresh()

    def delete_sch1(self):
        log.logger.info("deleting schedule : " + sch1)
        self.deleteSchedule(sch1)

    def delete_sch2(self):
        log.logger.info("deleting schedule : " + sch2)
        self.deleteSchedule(sch2)

    def delete_sch3(self):
        log.logger.info("deleting schedule : " + sch3)
        self.deleteSchedule(sch3)

    def delete_sch4(self):
        log.logger.info("deleting schedule : " + sch4)
        self.deleteSchedule(sch4)

    def delete_sch6(self):
        log.logger.info("deleting schedule : " + sch6)
        self.deleteSchedule(sch6)

    def delete_sch8(self):
        log.logger.info("deleting schedule : " + sch8)
        self.deleteSchedule(sch8)

    def delete_scheduleForCount(self):
        log.logger.info("deleting schedule : " + scheduleForCount)
        self.deleteSchedule(scheduleForCount)

    def delete_sc_name(self):
        log.logger.info("deleting schedule : " + sc_name)
        self.deleteSchedule(sc_name)

    def delete_sc_name20(self):
        log.logger.info("deleting schedule : " + sc_name20)
        self.deleteSchedule(sc_name20)

    def delete_sch_name(self):
        log.logger.info("deleting schedule : " + sch_name)
        self.deleteSchedule(sch_name)

    def delete_xxx(self):
        log.logger.info("deleting schedule : " + xxx)
        self.deleteSchedule(xxx)

    def delete_dra_drop_schedule(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule)
        self.deleteSchedule(dra_drop_schedule)

    def delete_dra_drop_schedule1(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule1)
        self.deleteSchedule(dra_drop_schedule1)

    def delete_dra_drop_schedule2(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule2)
        self.deleteSchedule(dra_drop_schedule2)

    def delete_dra_drop_schedule3(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule3)
        self.deleteSchedule(dra_drop_schedule3)

    def delete_dra_drop_schedule4(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule4)
        self.deleteSchedule(dra_drop_schedule4)

    def delete_dra_drop_schedule5(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule5)
        self.deleteSchedule(dra_drop_schedule5)

    def delete_dra_drop_schedule6(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule6)
        self.deleteSchedule(dra_drop_schedule6)

    def delete_dra_drop_schedule7(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule7)
        self.deleteSchedule(dra_drop_schedule7)

    def delete_dra_drop_schedule8(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule8)
        self.deleteSchedule(dra_drop_schedule8)

    def delete_dra_drop_schedule10(self):
        log.logger.info("deleting schedule : " + dra_drop_schedule10)
        self.deleteSchedule(dra_drop_schedule10)

    def delete_schedule090(self):
        log.logger.info("deleting schedule : " + schedule090)
        self.deleteSchedule(schedule090)

    def delete_scheduleName_7(self):
        log.logger.info("deleting schedule : " + scheduleName_7)
        self.deleteSchedule(scheduleName_7)

    def delete_sch_9(self):
        self.deleteSchedule(sch9)

    def delete_sch_10(self):
        self.deleteSchedule(sch10)

    def delete_sc_cont_name(self):
        self.deleteSchedule(sc_cont_name)

    def delete_sch_n(self):
        self.deleteSchedule(sch_n)

    def delete_schedule_nm(self):
        self.deleteSchedule(schedule_nm)

    def delete_schedule30(self):
        self.deleteSchedule(schedule30)

    def delete_schedule_n(self):
        self.deleteSchedule(schedule_n)

    def delete_scheduleName_8(self):
        self.deleteSchedule(scheduleName_8)

    def delete_s_Name(self):
        self.deleteSchedule(s_Name)

    def delete_sch_newName(self):
        self.deleteSchedule(sch_newName)

    def delete_schedule_1(self):
        log.logger.info("deleting schedule : " + schedule_1)
        self.deleteSchedule(schedule_1)

    def deleteLast20Entries(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        time.sleep(1)
        self.click("S_SELECT_ALL_XPATH")
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        log.logger.info("More option selected ")
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        log.logger.info("Move to trash selected")
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        log.logger.info("Deleting 20 entries on Schedule main page")
        time.sleep(2)
        mv = self.find_element("S_TRASHED_XPATH")
        self.driver.execute_script("arguments[0].click();", mv)
        log.logger.info("clicked on trashed")
        time.sleep(1)
        # log.logger.info("Selecting 20 entries on trashed page")
        # self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "20")
        # time.sleep(1)
        s_all = self.find_element("S_SELECT_ALL_XPATH")
        self.driver.execute_script("arguments[0].click();", s_all)
        log.logger.info("Selecting all entries inside trashed")
        more_options_trash = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options_trash)
        time.sleep(1)
        log.logger.info("Click on more options inside trashed")
        delete_complete = self.find_element("S_DELETE_C_XPATH")
        self.driver.execute_script("arguments[0].click();", delete_complete)
        self.click("S_CONFIRM_BTN_XPATH")
        log.logger.info("Deleted last 20 entries")
        time.sleep(2)

    def delete_sc_name1(self):
        self.deleteSchedule(sc_name1)

    def delete_sc_name2(self):
        self.deleteSchedule(sc_name2)

    #########Additional TC#########
    def clickonAddtrigger(self):
        time.sleep(1)
        self.wait_for_visible("Add_trigger_XPATH")
        self.click("Add_trigger_XPATH")
        return Schedules(self.driver)

    def clickonAddtimeTrigger(self):
        time.sleep(1)
        self.wait_for_visible("Add_time_trigger_XPATH")
        self.click("Add_time_trigger_XPATH")

    def verifycreateTrigger(self):
        today = date.today()
        d1 = today.strftime("%d%m%Y")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        global Schedulenew_name_trigger
        Schedulenew_name_trigger = generate_random_string(5)
        self.createSchedule(Schedulenew_name_trigger)
        self.click("S_ADD_TRIGGER_BTN_XPATH")
        time.sleep(2)
        self.click("S_ADD_TIME_TRIGGER_BTN_XPATH")
        time.sleep(2)
        self.send_keys("S_TRIGGER_NAME_ID", trigger_name)
        time.sleep(3)
        self.click("O_SELECT_PLAY_CONTENT_XPATH")
        time.sleep(2)
        self.selenium_click("S_CONTENT_XPATH")
        time.sleep(1)
        ele1 = "//select[@id='trigger_content_id']//option[2]"
        self.driver.find_element(By.XPATH, ele1).click()
        # self.find_element("D_Createdcontent_XPATH")
        self.click("S_DAILY_TRIGGER_RB_ID")
        time.sleep(2)
        self.click("S_TRIGGER_CONTENT_ID")
        time.sleep(2)
        # ele = f"//select[@id='trigger_content_id']//option[3]"
        # self.driver.find_element(By.XPATH, ele).click()
        time.sleep(2)
        self.click("S_DAILY_TRIGGER_RB_ID")
        time.sleep(2)
        self.send_keys("S_TRIGGER_START_DATE_ID", d1)
        time.sleep(1)
        self.send_keys("S_TRIGGER_END_DATE_ID", d1)
        time.sleep(2)
        self.send_keys("S_TRIGGER_START_TIME_ID", "15:01")
        time.sleep(2)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(0.7)
        return Schedules(self.driver)

    def verifycreateTrigger_(self):
        today = date.today()
        d1 = today.strftime("%d%m%Y")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.createSchedule(Schedulenew_name_trigger2)
        self.click("S_ADD_TRIGGER_BTN_XPATH")
        time.sleep(2)
        self.click("S_ADD_TIME_TRIGGER_BUTTON_XPATH")
        time.sleep(2)
        self.send_keys("S_TRIGGER_NAME_ID", trigger_name2)
        time.sleep(3)
        self.click("O_SELECT_PLAY_CONTENT_XPATH")
        time.sleep(2)
        self.selenium_click("S_CONTENT_XPATH")
        time.sleep(1)
        ele1 = "//select[@id='trigger_content_id']//option[2]"
        self.driver.find_element(By.XPATH, ele1).click()
        # self.find_element("D_Createdcontent_XPATH")
        self.click("S_DAILY_TRIGGER_RB_ID")
        time.sleep(2)
        self.click("S_TRIGGER_CONTENT_ID")
        time.sleep(2)
        # ele = f"//select[@id='trigger_content_id']//option[3]"
        # self.driver.find_element(By.XPATH, ele).click()
        time.sleep(2)
        self.click("S_DAILY_TRIGGER_RB_ID")
        time.sleep(2)
        self.send_keys("S_TRIGGER_START_DATE_ID", d1)
        time.sleep(1)
        self.send_keys("S_TRIGGER_END_DATE_ID", d1)
        time.sleep(2)
        self.send_keys("S_TRIGGER_START_TIME_ID", "15:01")
        time.sleep(2)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(0.7)
        return Schedules(self.driver)

    def addScheduleWith5Charfortrigger(self):
        self.addSchedule(generate_random_string(5))
        return Schedules(self.driver)

    def createContentfortrigger(self):
        time.sleep(2)
        self.wait_for_visible_all_elements("MENU_CONTENT_XPATH")
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        self.send_keys("S_CONTENT_NAME_XPATH", new_content_name)
        self.click("S_BLANK_TMP_XPATH")
        self.click("S_SUBMIT_BUTTON_ID")
        # self.wait_for_visible("D_Dontshowagain_XPATH")
        return Schedules(self.driver)

    def createContentfortrigger_(self):
        time.sleep(2)
        self.wait_for_visible_all_elements("MENU_CONTENT_XPATH")
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        self.send_keys("S_CONTENT_NAME_XPATH", new_content_name2)
        self.click("S_BLANK_TMP_XPATH")
        self.click("S_SUBMIT_BUTTON_ID")
        # self.wait_for_visible("D_Dontshowagain_XPATH")
        return Schedules(self.driver)

    def cancel(self):
        time.sleep(3)
        # self.click("D_Dontshowagain_XPATH")
        # time.sleep(1)
        # self.wait_for_visible("D_Cancel_Content_Message_new_XPATH")
        # self.click("D_Cancel_Content_Message_new_XPATH")
        self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return Schedules(self.driver)

    def setDateContent(self):
        self.wait_for_visible("D_StartDate_ID")
        self.scroll_to_element("D_StartDate_ID")
        self.send_keys("D_StartDate_ID", "07-04-2024")
        self.scroll_to_element("D_EndDate_ID")
        self.send_keys("D_EndDate_ID", "08-04-2025")
        return Schedules(self.driver)

    def switchToNewBasetrigeer(self):
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Head User":
            retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
            time.sleep(1)
            self.click("S_SWITCH_BASE_ID")
            time.sleep(1)
            self.click("S_BASE_DROPDOWN_XPATH")
            time.sleep(1)
            log.logger.info(new_base_acc_name)
            self.send_keys("S_INPUT_BASE_XPATH", base_acc_name)
            time.sleep(1)
            base = f"//li[.='{base_acc_name}']"
            self.driver.find_element(By.XPATH, base).click()
            self.click("S_ADD_BUTTON_NAME")
        else:
            pass
        return Schedules(self.driver)


    def gotoContentContents_SS(self):
        time.sleep(4)
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Schedules(self.driver)

    def gettextofpopup(self):
        Trigger_XPATH = f"//span[@title='{trigger_name}']"
        # txt = self.getText("D_Approvepopup_XPATH")
        time.sleep(2)
        if len(self.driver.find_elements(By.XPATH, Trigger_XPATH)) == 1:
            assert True
        else:
            assert False

    def gettextofpopup_(self):
        Trigger_XPATH = f"//span[@title='{trigger_name2}']"
        # txt = self.getText("D_Approvepopup_XPATH")
        time.sleep(4)
        if len(self.driver.find_elements(By.XPATH, Trigger_XPATH)) == 1:
            assert True
        else:
            assert False

    def verifycreateRepeatTrigger(self):
        today = date.today()
        d1 = today.strftime("%d%m%Y")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_SIT2_url"))
        self.createSchedule(Schedulenew_name_trigger2)
        self.click("S_ADD_TRIGGER_BTN_XPATH")
        self.click("S_ADD_TIME_TRIGGER_BTN_XPATH")
        self.send_keys("S_TRIGGER_NAME_ID", trigger_name2)
        self.click("O_SELECT_PLAY_CONTENT_XPATH")
        time.sleep(1)
        self.selenium_click("S_CONTENT_XPATH")
        time.sleep(1)
        ele1 = "//select[@id='trigger_content_id']//option[2]"
        self.driver.find_element(By.XPATH, ele1).click()
        # self.find_element("D_Createdcontent_XPATH")
        self.click("S_DAILY_TRIGGER_RB_ID")
        time.sleep(1)
        self.click("S_TRIGGER_CONTENT_ID")
        time.sleep(1)
        # ele = f"//select[@id='trigger_content_id']//option[3]"
        # self.driver.find_element(By.XPATH, ele).click()
        time.sleep(1)
        self.click("S_DAILY_TRIGGER_RB_ID")
        time.sleep(1)
        self.send_keys("S_TRIGGER_START_DATE_ID", d1)
        time.sleep(0.3)
        self.send_keys("S_TRIGGER_END_DATE_ID", d1)
        time.sleep(0.3)
        self.send_keys("S_TRIGGER_START_TIME_ID", "15:01")
        self.click("D_RepeatYes_XPATH")
        time.sleep(0.3)
        self.send_keys("D_Endtime_XPATH", "16:01")
        self.send_keys("O_REPEAT_HOUR_XPATH", "1")
        self.send_keys("O_REPEAT_XPATH", "1")
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(2)
        return Schedules(self.driver)

    def cancelcontentmessage(self):
        # self.wait_for_visible("D_Cancel_Content_Message_new_XPATH")
        # self.click("D_Cancel_Content_Message_new_XPATH")
        self.wait_for_visible("D_Ok_Button_XPATH")
        self.click("D_Ok_Button_XPATH")
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return Schedules(self.driver)

    def clickonpluscomntent(self):
        time.sleep(2)
        log.logger.info("D_CLickonpluscontent_XPATH : D_CLickonpluscontent_XPATH")
        self.wait_for_visible("D_CLickonpluscontent_XPATH")
        self.click("D_CLickonpluscontent_XPATH")
        return Schedules(self.driver)

    def createScheduleForReplaceOption(self):
        global schedule1200
        schedule1200 = generate_unique_string(5)
        self.createSchedule(schedule1200)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.send_keys("N_SearchBoxInsidePlaylistEdit_XPATH", r_ContentName1)
        time.sleep(1)
        source_locator = f"//span[contains(.,'{r_ContentName1}')]"
        target_locator = "(//div[@class='fc-daygrid-day-events'])[4]"
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        drag = self.driver.find_element(By.XPATH, source_locator)
        drop = self.driver.find_element(By.XPATH, target_locator)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        time.sleep(3)
        return Schedules(self.driver)

    def createScheduleForPreviewOption(self):
        global schedule1201
        schedule1201 = generate_unique_string(5)
        self.createSchedule(schedule1201)
        time.sleep(2)
        self.clickonpluscomntent()
        time.sleep(2)
        self.send_keys("N_SearchBoxInsidePlaylistEdit_XPATH", r_ContentName1)
        time.sleep(1)
        source_locator = f"//span[contains(.,'{r_ContentName1}')]"
        target_locator = "(//div[@class='fc-daygrid-day-events'])[4]"
        self.wait_for_visible_all_elements("O_FIRST_CONTENT_XPATH")
        self.wait_for_visible_all_elements("S_DROP_LOCATION_XPATH")
        drag = self.driver.find_element(By.XPATH, source_locator)
        drop = self.driver.find_element(By.XPATH, target_locator)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        time.sleep(3)
        return Schedules(self.driver)

    def addNewContent1(self):
        self.gotoContentContents_Replace()
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName1()
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        return Schedules(self.driver)

    def enterContentName1(self):
        global r_ContentName1
        r_ContentName1 = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_CONTENT_ContentNameTextbox_XPATH", r_ContentName1)
        return Schedules(self.driver)

    def enterContentName2(self):
        global r_ContentName2
        r_ContentName2 = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_CONTENT_ContentNameTextbox_XPATH", r_ContentName2)
        return Schedules(self.driver)

    def addNewContent2(self):
        self.gotoContentContents_Replace()
        self.click("O_CONTENT_AddNewContent_BTN_XPATH")
        self.enterContentName2()
        self.click("O_CONTENT_BLANK_XPATH")
        self.click("O_CONTENT_ADD_BTN_XPATH")
        self.contentPopupRemoval()
        return Schedules(self.driver)

    def gotoContentContents_Replace(self):
        #self.refresh()
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Schedules(self.driver)

    def verifyReplaceOption(self):
        self.selenium_click("S_DROP_LOCATION_XPATH")
        time.sleep(2)
        self.click("replaceDD_XPATH")
        time.sleep(1)
        self.send_keys("replaceTB_XPATH", r_ContentName2)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@class=' css-hlgwow']//div//input").send_keys(Keys.ENTER)
        self.click("D_Playlist_Save_XPATH")
        time.sleep(1)
        if len(self.driver.find_elements(By.XPATH, f"//div[contains(text(),'{r_ContentName2}')]")) == 1:
            return True
        else:
            return False


    def verifyPreviewOption(self):
        self.selenium_click("S_DROP_LOCATION_XPATH")
        if len(self.find_elements("previewOption_XPATH")) == 1:
            self.click("previewOption_XPATH")
            if len(self.find_elements("previewTitle_XPATH")) == 1:
                self.refresh()
                return True
            else:
                self.refresh()
                return False
        else:
            self.refresh()
            return False
