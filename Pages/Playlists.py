import os
import random
import re
import secrets
import shutil
import string
import time
import logging

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Utilities import configReader
from Utilities.LogUtil import Logger

from Pages.BasePage import BasePage, retry_action, generate_unique_string, getTextAfterRetry
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

log = Logger(__name__, logging.INFO)
base_account = "base_" + generate_unique_string(3)
playlist1 = generate_unique_string(5)
playlist2 = generate_unique_string(26)
playlist3 = generate_unique_string(5)
playlist4 = generate_unique_string(5)
playlist5 = generate_unique_string(5)
playlist6 = generate_unique_string(5)
playlist7 = generate_unique_string(5)
playlist8 = generate_unique_string(5)
playlist9 = generate_unique_string(5)
playlist10 = generate_unique_string(5)
playlist11 = generate_unique_string(5)
playlist12 = generate_unique_string(4)
playlist13 = generate_unique_string(5)
playlist14 = generate_unique_string(5)
playlist15 = generate_unique_string(5)
playlist16 = generate_unique_string(5)
playlist17 = generate_unique_string(5)


playlist20 = generate_unique_string(5)
playlist21 = generate_unique_string(5)
playlist22 = generate_unique_string(5)
playlist23 = generate_unique_string(5)
playlist24 = "$%$@^$!@#"
playlist25 = generate_unique_string(5)
playlist26 = generate_unique_string(5)
playlist27 = generate_unique_string(5)
playlist28 = generate_unique_string(5)
playlist29 = generate_unique_string(5)
playlist30 = generate_unique_string(5)
playlist31 = generate_unique_string(5)

playlist33 = generate_unique_string(5)
playlist34 = generate_unique_string(5)
playlist35 = generate_unique_string(5)
playlist36 = generate_unique_string(5)
playlist37 = generate_unique_string(5)
playlist38 = generate_unique_string(26)
playlist39 = generate_unique_string(6)
playlist40 = "!@#$%^&*()"
playlist41 = generate_unique_string(6)
playlist42 = generate_unique_string(6)
playlist43 = generate_unique_string(6)
playlist44 = generate_unique_string(6)
playlist45 = generate_unique_string(6)
playlist46 = generate_unique_string(6)
playlist47 = generate_unique_string(26)
playlist48 = generate_unique_string(6)
playlist49 = generate_unique_string(6)
playlist50 = generate_unique_string(6)
playlist51 = generate_unique_string(6)
playlist52 = generate_unique_string(6)
playlist53 = generate_unique_string(6)
playlist54 = generate_unique_string(6)

playlist56 = generate_unique_string(6)
playlist57 = generate_unique_string(6)
playlist58 = generate_unique_string(6)
playlist59 = generate_unique_string(6)
playlist60 = generate_unique_string(6)
playlist61 = generate_unique_string(6)
playlist037 = generate_unique_string(6)
playlist038 = generate_unique_string(6)

folder_name1 = generate_unique_string(26)
folder_name2 = generate_unique_string(5)
folder_name3 = generate_unique_string(5)
folder_name4 = generate_unique_string(5)
folder_name5 = generate_unique_string(5)
folder_name6 = generate_unique_string(5)
folder_name7 = generate_unique_string(5)
folder_name8 = generate_unique_string(5)
folder_name9 = generate_unique_string(5)
folder_name10 = generate_unique_string(5)
folder_name11 = generate_unique_string(5)
folder_name12 = generate_unique_string(5)
folder_name13 = generate_unique_string(5)
folder_name14 = generate_unique_string(5)
folder_name15 = generate_unique_string(5)
folder_name16 = generate_unique_string(5)
folder_name17 = generate_unique_string(5)




def lastWord(string):
    lis = list(string.split(" "))
    length = len(lis)
    return lis[length - 1]


class Playlists(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def switchToHead(self):
        time.sleep(2)
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Base User":
            retry_action(self.driver, By.ID, "dropdownMenuButton1")
            time.sleep(1)
            switch_to_head = self.driver.find_element(By.XPATH, "//input[@value='Switch to Head Account']")
            self.driver.execute_script("arguments[0].click();", switch_to_head)
            # retry_action(self.driver, By.XPATH, "//input[@value='Switch to Head Account']")
            time.sleep(1)
            # self.click("S_HEAD_ID")
            # self.click("S_SWITCH_TO_HEAD_XPATH")
        else:
            pass
        self.refresh()

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def createBaseAccount(self):
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Head User":
            self.click("S_UA_XPATH")
            self.click("S_BM_XPATH")
            self.click("S_NB_ACC_XPATH")
            self.send_keys("S_BASE_ACC_NAME_XPATH", base_account)
            self.click("S_SAVE_BTN_XPATH")
            time.sleep(2)
        else:
            pass
        return Playlists(self.driver)

    def switchToNewBase(self):
        log.logger.info("switchToBase")
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Head User":
            time.sleep(1)
            retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
            time.sleep(1)
            self.click("S_SWITCH_BASE_ID")
            time.sleep(1)
            self.click("S_BASE_DROPDOWN_XPATH")
            time.sleep(1)
            log.logger.info(base_account)
            self.send_keys("S_INPUT_BASE_XPATH", base_account)
            time.sleep(1)
            base = f"//li[.='{base_account}']"
            self.driver.find_element(By.XPATH, base).click()
            self.click("S_ADD_BUTTON_NAME")
        else:
            pass
        self.refresh()
        return Playlists(self.driver)

    def switchToBase(self):
        log.logger.info("switchToBase")
        current_user = self.getCurrentAccount()
        log.logger.info("current_user : " + current_user)
        if current_user == "Head User":
            time.sleep(1)
            retry_action(self.driver, By.CSS_SELECTOR, "#dropdownMenuButton1")
            time.sleep(1)
            self.click("S_SWITCH_BASE_ID")
            time.sleep(1)
            self.click("S_BASE_DROPDOWN_XPATH")
            time.sleep(1)
            log.logger.info(base_account)
            self.send_keys("S_INPUT_BASE_XPATH", base_account)
            time.sleep(1)
            base = f"//li[.='{base_account}']"
            self.driver.find_element(By.XPATH, base).click()
            self.click("S_ADD_BUTTON_NAME")
        else:
            pass
        self.refresh()
        return self.getText("S_ACCOUNT_XPATH")

    def navToPlaylistURL(self):
        time.sleep(2)
        log.logger.info("navToPlaylistURL")
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "playlist_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "playlist_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "playlist_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "playlist_sit2_url"))
        self.refresh()
        time.sleep(2)
        return Playlists(self.driver)

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

    def createPlaylist(self, playlist_name):
        self.navToPlaylistURL()
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist_name)
        self.click("S_SAVE_BTN_XPATH")
        time.sleep(4)
        self.navToPlaylistURL()
        log.logger.info("playlist_name is : " + playlist_name)
        return Playlists(self.driver)

    def createPlay(self, playlist_name):
        time.sleep(3)
        self.wait_for_visible_all_elements("S_CREATE_PLAY_XPATH")
        self.selenium_click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist_name)
        self.click("S_SAVE_BTN_XPATH")
        log.logger.info("playlist_name is : " + playlist_name)

    def verifyCreatePlaylist(self):
        countBeforeAdd = self.getText("S_TOTAL_COUNT_XPATH")
        self.createPlaylist(playlist1)
        countAfterAdd = self.getText("S_TOTAL_COUNT_XPATH")
        assert countBeforeAdd != countAfterAdd

    def verifyCreatePlaylistWitMaxChar(self):
        countBeforeAdd = self.getText("S_TOTAL_COUNT_XPATH")
        self.createPlaylist(playlist2)
        countAfterAdd = self.getText("S_TOTAL_COUNT_XPATH")
        assert countBeforeAdd != countAfterAdd

    def verifyCreatePlaylistWitSpecChar(self):
        countBeforeAdd = self.getText("S_TOTAL_COUNT_XPATH")
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", "@!#$%^&*()")
        self.click("S_SAVE_BTN_XPATH")
        return self.getText("O_INVALID_SCHEDULE_NAME_XPATH")

    def verifyAddOptionOnCreatePlaylist(self):
        countBeforeAdd = self.getText("S_TOTAL_COUNT_XPATH")
        self.createPlaylist(playlist3)
        self.navToPlaylistURL()
        countAfterAdd = self.getText("S_TOTAL_COUNT_XPATH")
        assert countBeforeAdd != countAfterAdd

    def verifyCancelOptionOnCreatePlaylist(self):
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist3)
        self.click("S_CANCEL_BUTTON_XPATH")
        ele = self.find_elements("S_MODAL_XPATH")
        return str(len(ele))

    def verifyCloseOptionOnCreatePlaylist(self):
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist3)
        self.click("S_CLOSE_BUTTON_XPATH")
        ele = self.find_elements("S_MODAL_XPATH")
        return str(len(ele))

    def verifyCreatedPlaylistDetail_Name(self):
        self.createPlaylist(playlist4)
        xpath = f"//span[@title='{playlist4}']"
        title = self.driver.find_element(By.XPATH, xpath).get_attribute('title')
        assert playlist4 == title

    def verifyCreatedPlaylistDetail_Folder(self):
        path = f"//td//span[@title='{playlist4}']/following::td[1]"
        return self.driver.find_element(By.XPATH, path).text

    def verifyCreatedPlaylistDetail_Preview(self):
        path = f"(//td//span[@title='{playlist4}']/following::td[2]//*[local-name()='svg'])[1]"
        self.driver.find_element(By.XPATH, path).click()
        previewText = self.driver.find_element(By.XPATH, "//h5").text
        self.click("S_CLOSE_BUTTON_XPATH")
        return previewText

    def verifyCreatedPlaylistDetail_Count(self):
        path = f"//td//span[@title='{playlist4}']/following::td[3]"
        return self.driver.find_element(By.XPATH, path).text

    def verifyCreatedPlaylistDetail_Detail(self):
        path = f"//td//span[@title='{playlist4}']/following::td[4]"
        return self.driver.find_element(By.XPATH, path).text

    def verifyCreatedPlaylistDetail_ModifiedAt(self):
        path = f"//td//span[@title='{playlist4}']/following::td[5]"
        return self.driver.find_element(By.XPATH, path).text

    def verifyCreatedPlaylistDetail_ModifiedBy(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "user_detail_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "user_detail_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "user_detail_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "user_detail_sit2_url"))
        self.refresh()
        user = self.driver.find_element(By.ID, "firstName").get_attribute('value')
        self.navToPlaylistURL()
        path = f"//td//span[@title='{playlist4}']/following::td[5]"
        userName = self.driver.find_element(By.XPATH, path).text
        assert user == userName

    def verifyCreatedPlaylistDetail_Rename(self):
        p4_xpath = f"//span[@title='{playlist4}']"
        play4_title = self.driver.find_element(By.XPATH, p4_xpath).get_attribute('title')
        path = f"(//td//span[@title='{playlist4}']/following::td[2]//*[local-name()='svg'])[3]"
        self.driver.find_element(By.XPATH, path).click()
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist5)
        self.click("S_SAVE_BTN_XPATH")
        p5_xpath = f"//span[@title='{playlist5}']"
        play5_title = self.driver.find_element(By.XPATH, p5_xpath).get_attribute('title')
        assert play4_title != play5_title

    def verifyRenamePlaylist(self):
        self.createPlaylist(playlist6)
        p6_xpath = f"//span[@title='{playlist6}']"
        play6_title = self.driver.find_element(By.XPATH, p6_xpath).get_attribute('title')
        p6_edit_path = f"(//td//span[@title='{playlist6}']/following::td[2]//*[local-name()='svg'])[3]"
        self.driver.find_element(By.XPATH, p6_edit_path).click()
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist7)
        self.click("S_SAVE_BTN_XPATH")
        p7_xpath = f"//span[@title='{playlist7}']"
        play7_title = self.driver.find_element(By.XPATH, p7_xpath).get_attribute('title')
        assert play6_title != play7_title

    def verifyUpdatePlaylistName(self):
        self.createPlaylist(playlist8)
        p8_xpath = f"//span[@title='{playlist8}']"
        play8_title = self.driver.find_element(By.XPATH, p8_xpath).get_attribute('title')
        log.logger.info("play8_title : " + play8_title)
        retry_action(self.driver, By.XPATH, p8_xpath)
        self.click("S_EDIT_NAME_XPATH")
        self.clear("S_EDIT_SCHEDULE_ID")
        self.clear("S_EDIT_SCHEDULE_ID")
        self.send_keys("S_EDIT_SCHEDULE_ID", playlist9)
        self.click("S_UPDATE_ICON_XPATH")
        time.sleep(5)
        self.navToPlaylistURL()
        p9_xpath = f"//span[@title='{playlist9}']"
        #p9_xpath = f"//a//span[@title='{playlist9}']"
        play9_title = self.driver.find_element(By.XPATH, p9_xpath).get_attribute('title')
        log.logger.info("play9_title : " + play9_title)
        assert play8_title != play9_title

    def createContentInBase(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.click("S_CREATE_CONTENT_XPATH")
        self.send_keys("S_CONTENT_NAME_XPATH", "base_WRv")
        self.click("S_BLANK_TMP_XPATH")
        self.click("S_SUBMIT_BUTTON_ID")
        time.sleep(12)
        self.navToPlaylistURL()

    def verifyCloseButtonOnEditPlaylist(self):
        self.createPlaylist(playlist10)
        p10_xpath = f"//span[@title='{playlist10}']"
        retry_action(self.driver, By.XPATH, p10_xpath)
        url_before = self.get_current_url()
        time.sleep(1)
        self.click("S_CLOSE_ICON_XPATH")
        url_after = self.get_current_url()
        print(url_before)
        print(url_after)
        assert url_before != url_after

    def verifyHeadFolder(self):
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        url_trashed = self.get_current_url()
        base = self.driver.find_element(By.XPATH, "//a[.='Head Folder']")
        self.driver.execute_script("arguments[0].click();", base)
        time.sleep(10)
        url_base = self.get_current_url()
        assert url_trashed != url_base

    def verifyFolderPath(self):
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(4)
        folder_trash = self.getText("S_SUB_FOLDER_XPATH")
        retry_action(self.driver, By.XPATH, "//a[.='Head Folder']")
        time.sleep(10)
        folder_base = self.getText("S_SUB_FOLDER_XPATH")
        print(folder_trash)
        print(folder_base)
        assert folder_trash != folder_base

    def verifyTrashedPlaylist(self):
        self.createPlaylist(playlist11)
        path = f"//span[@title='{playlist11}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        ele_xpath = f"//span[@title='{playlist11}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyCountTrashedPlaylist(self):
        self.createPlaylist(playlist12)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        totalEntries = self.getText("S_TOTAL_COUNT_XPATH")
        self.navToPlaylistURL()
        path = f"//span[@title='{playlist12}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        time.sleep(1)
        totalEntriesAfter = self.getText("S_TOTAL_COUNT_XPATH")
        assert totalEntries != totalEntriesAfter

    def verifySearchAfterTrash(self):
        self.createPlaylist(playlist13)
        path = f"//span[@title='{playlist13}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        self.send_keys("S_SEARCH_LIST_XPATH", playlist13)
        time.sleep(1)
        ele_xpath = f"//span[@title='{playlist13}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyCheckboxInTrashed(self):
        self.createPlaylist(playlist14)
        time.sleep(5)
        path = f"//span[@title='{playlist14}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        more_status = self.find_element("S_MORE_OPTION_XPATH").get_attribute('disabled')
        log.logger.info(str(more_status))
        x_path = f"//span[@title='{playlist14}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        option_status = self.find_element("S_MORE_OPTION_XPATH").get_attribute('disabled')
        log.logger.info(str(option_status))
        assert more_status != option_status

    def verifyMoreOptionsInTrashed(self):
        self.createPlaylist(playlist15)
        path = f"//span[@title='{playlist15}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        x_path = f"//span[@title='{playlist15}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.click("S_MORE_OPTION_XPATH")
        restore_ele = f"//button[@data-confirm-title-value='Restore']"
        delete_ele = f"//button[@data-confirm-title-value='Delete Completely']"
        restore_ele_count = len(self.driver.find_elements(By.XPATH, restore_ele))
        delete_ele_count = len(self.driver.find_elements(By.XPATH, delete_ele))
        log.logger.info(str(restore_ele_count) + str(delete_ele_count))
        return restore_ele_count + delete_ele_count

    def verifyRestorePlaylist(self):
        self.createPlaylist(playlist16)
        path = f"//span[@title='{playlist16}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(4)
        element = f"//span[@title='{playlist16}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist16}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.selenium_click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.selenium_click("S_RESTORE_XPATH")
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        self.refresh()
        time.sleep(1)
        element_count = f"//span[@title='{playlist16}']"
        ele_length = str(len(self.driver.find_elements(By.XPATH, element_count)))
        assert ele_length != ele_len

    def verifyOkButtonRestorePlaylist(self):
        self.createPlaylist(playlist17)
        path = f"//span[@title='{playlist17}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(5)
        self.refresh()
        name_element = f"//span[@title='{playlist17}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        self.wait_for_visible_all_elements("S_TRASHED_XPATH")
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(5)
        element = f"//span[@title='{playlist17}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist17}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.click("S_RESTORE_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(5)
        self.navToPlaylistURL()
        new_element = f"//span[@title='{playlist17}']"
        self.refresh()
        time.sleep(2)
        countAfterRestore = str(len(self.driver.find_elements(By.XPATH, new_element)))
        print(countAfterRestore)
        print(countAfterDelete)
        log.logger.info("countAfterDelete : " + countAfterRestore)
        assert countAfterDelete != countAfterRestore

    def verifyCancelButtonRestorePlaylist(self):
        global playlist18
        playlist18 = generate_unique_string(5)
        self.createPlaylist(playlist18)
        path = f"//span[@title='{playlist18}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(5)
        name_element = f"//span[@title='{playlist18}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        element = f"//span[@title='{playlist18}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist18}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.click("S_RESTORE_XPATH")
        self.click("S_CANCEL_XPATH")
        time.sleep(2)
        self.navToPlaylistURL()
        time.sleep(2)
        new_element = f"//span[@title='{playlist18}']"
        countAfterRestore = str(len(self.driver.find_elements(By.XPATH, new_element)))
        log.logger.info("countAfterDelete : " + countAfterRestore)
        print(countAfterRestore)
        print(countAfterDelete)
        assert countAfterDelete == countAfterRestore

    def verifyCloseButtonRestorePlaylist(self):
        global playlist19
        playlist19 = generate_unique_string(5)
        self.createPlaylist(playlist19)
        path = f"//span[@title='{playlist19}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        self.navToPlaylistURL()  # refresh playlist page
        time.sleep(2)
        name_element = f"//span[@title='{playlist19}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(4)
        element = f"//span[@title='{playlist19}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist19}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1.5)
        self.selenium_click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.selenium_click("S_RESTORE_XPATH")
        time.sleep(1)
        self.selenium_click("S_CLOSE_X_BUTTON_XPATH")
        time.sleep(2)
        self.navToPlaylistURL()
        time.sleep(2)
        new_element = f"//span[@title='{playlist19}']"
        countAfterRestore = str(len(self.driver.find_elements(By.XPATH, new_element)))
        log.logger.info("countAfterDelete : " + countAfterRestore)
        assert countAfterDelete == countAfterRestore

    def verifyCompleteDeletePlaylist(self):
        self.createPlaylist(playlist20)
        path = f"//span[@title='{playlist20}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        name_element = f"//span[@title='{playlist20}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        self.wait_for_visible_all_elements("S_TRASHED_XPATH")
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(4)
        element = f"//span[@title='{playlist20}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist20}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(2)
        self.selenium_click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.selenium_click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", playlist20)
        time.sleep(2)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        log.logger.info(str(count))
        return str(count)

    def verifyOkButtonCompleteDeletePlaylist(self):
        self.createPlaylist(playlist21)
        path = f"//span[@title='{playlist21}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(5)
        name_element = f"//span[@title='{playlist21}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(5)
        element = f"//span[@title='{playlist21}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist21}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.selenium_click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.selenium_click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", playlist21)
        time.sleep(4)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        log.logger.info(str(count))
        return str(count)

    def verifyCancelButtonCompleteDeletePlaylist(self):
        self.createPlaylist(playlist21)
        path = f"//span[@title='{playlist21}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(3)
        name_element = f"//span[@title='{playlist21}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(4)
        element = f"//span[@title='{playlist21}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist21}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.selenium_click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.selenium_click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.selenium_click("S_CANCEL_XPATH")
        time.sleep(1)
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", playlist21)
        time.sleep(2)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        log.logger.info(str(count))
        return str(count)

    def verifyCloseButtonCompleteDeletePlaylist(self):
        self.createPlaylist(playlist22)
        path = f"//span[@title='{playlist22}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        name_element = f"//span[@title='{playlist22}']"
        countAfterDelete = str(len(self.driver.find_elements(By.XPATH, name_element)))
        log.logger.info("countAfterDelete : " + countAfterDelete)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        element = f"//span[@title='{playlist22}']"
        ele_len = str(len(self.driver.find_elements(By.XPATH, element)))
        x_path = f"//span[@title='{playlist22}']/preceding::input[@type='checkbox'][1]"
        s_checkbox = self.driver.find_element(By.XPATH, x_path)
        self.driver.execute_script("arguments[0].click();", s_checkbox)
        time.sleep(1)
        self.click("S_MORE_OPTION_XPATH")
        time.sleep(1)
        self.click("S_DELETE_COMPLETE_XPATH")
        time.sleep(1)
        self.click("S_CLOSE_X_BUTTON_XPATH")
        time.sleep(1)
        self.refresh()
        self.send_keys("S_SEARCH_XPATH", playlist22)
        time.sleep(2)
        cnt = self.getText("S_ENTRIES_COUNT_XPATH")
        parts = cnt.split("entries (filtered", 1)
        var = parts[0] if len(parts) > 1 else cnt
        count = re.findall(r'\d+', var)[-1]
        log.logger.info(str(count))
        return str(count)

    def clickOnTrashed(self):
        time.sleep(2)
        self.wait_for_visible_all_elements("S_TRASHED_PLAY_XPATH")
        self.click("S_TRASHED_PLAY_XPATH")
        time.sleep(3)
        return Playlists(self.driver)

    def get20Entries(self):
        self.select_option_by_value_from_dropdown("S_TRASHED_ENT_XPATH", "20")
        time.sleep(3)
        log.logger.info("get20Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get50Entries(self):
        self.select_option_by_value_from_dropdown("S_TRASHED_ENT_XPATH", "50")
        time.sleep(3)
        log.logger.info("get50Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get100Entries(self):
        self.select_option_by_value_from_dropdown("S_TRASHED_ENT_XPATH", "100")
        time.sleep(3)
        log.logger.info("get100Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get200Entries(self):
        self.select_option_by_value_from_dropdown("S_TRASHED_ENT_XPATH", "200")
        time.sleep(1)
        log.logger.info("get200Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get500Entries(self):
        self.select_option_by_value_from_dropdown("S_TRASHED_ENT_XPATH", "500")
        time.sleep(1)
        log.logger.info("get500Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def verifyFolderOfPlaylistInTrashed(self):
        global folder_name17
        folder_name17 = generate_unique_string(5)
        global playlist55
        playlist55 = generate_unique_string(6)
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name17)
        self.selenium_click("S_ADD_BUTTON_NAME")
        time.sleep(8)
        self.refresh()
        self.selenium_click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist55)
        self.selenium_click("S_SAVE_BTN_XPATH")
        time.sleep(4)
        self.navToPlaylistURL()
        path = f"//span[@title='{playlist55}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(6)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        folder_name = f"//span[@title='{playlist55}']/following::td[1]"
        time.sleep(7)
        folder_text = self.driver.find_element(By.XPATH, folder_name).text
        log.logger.info("folder_text : " + folder_text)
        return folder_text


    def verifyModifyByAtTrashed(self):
        self.createPlaylist(playlist56)
        rename_path = f"//td//span[@title='{playlist56}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist57)
        self.click("S_SAVE_BTN_XPATH")
        self.navToPlaylistURL()
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//a[@href='/v2/profile/user_details']")
        name = self.find_element("S_USER_NAME_ID").get_attribute('value')
        log.logger.info("name : " + name)
        self.navToPlaylistURL()
        path = f"//span[@title='{playlist57}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(5)
        modify_xpath = f"//span[@title='{playlist57}']/following::td[4]"
        modify_by = self.driver.find_element(By.XPATH, modify_xpath).text
        log.logger.info("modify_by : " + modify_by)
        assert name == modify_by

    def verifyModifyBy(self):
        self.createPlaylist(playlist60)
        rename_path = f"//td//span[@title='{playlist60}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist61)
        self.click("S_SAVE_BTN_XPATH")
        self.navToPlaylistURL()
        retry_action(self.driver, By.ID, "myDropdown")
        retry_action(self.driver, By.XPATH, "//a[@href='/v2/profile/user_details']")
        name = self.find_element("S_USER_NAME_ID").get_attribute('value')
        log.logger.info("name : " + name)
        self.navToPlaylistURL()
        modify_xpath = f"//span[@title='{playlist61}']/following::td[5]"
        modify_by = self.driver.find_element(By.XPATH, modify_xpath).text
        log.logger.info("modify_by : " + modify_by)
        assert name == modify_by

    def verifyTrashedPlaylistName(self):
        self.createPlaylist(playlist23)
        path = f"//span[@title='{playlist23}']/preceding::input[@type='checkbox'][1]"
        checkbox = self.driver.find_element(By.XPATH, path)
        self.driver.execute_script("arguments[0].click();", checkbox)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(1)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(3)
        ele_xpath = f"//span[@title='{playlist23}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyCreateFolderOSDForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        time.sleep(1)
        ele = self.find_elements("S_PLAY_FOLDER_NAME_XPATH")
        return str(len(ele))

    def verifyCreateFolderForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name1)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(5)
        # log.logger.info(lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH")))
        # assert folder_name1 == lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH"))
        ele_XPATH = f"//a//span[@class='{folder_name1}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        ele = len(ele)
        return ele


    def verifyPlayFolderWithSC(self):
        self.navToPlaylistURL()
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist24)
        self.click("S_SAVE_BTN_XPATH")
        return self.getText("S_INVALID_MSG_XPATH")

    def verifyOKOptionCreateFolderForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name2)
        self.click("S_ADD_BUTTON_NAME")
        self.wait_for_visible_all_elements("S_SUB_FOLDER_LOC_XPATH")
        time.sleep(4)
        log.logger.info("folder_name2 : " + folder_name2)
        log.logger.info("XXXXXX : " + lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH")))
        assert folder_name2 == lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH"))

    def verifyCancelOptionOnCreateFolderForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name3)
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(2)
        assert "Root" == lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH"))

    def verifyCloseOptionOnCreateFolderForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name4)
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(2)
        assert "Root" == lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH"))

    def CreateFolderForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name5)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(2)
        log.logger.info(lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH")))
        return Playlists(self.driver)

    def verifyFolderInDropDownPlay(self):
        self.navToPlaylistURL()
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", folder_name5)
        option = f"//a[@class='dropdown-item '][contains(.,'{folder_name5}')]"
        folder_detail = self.driver.find_elements(By.XPATH, option)
        return str(len(folder_detail))

    def FolderForPlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name6)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(2)
        log.logger.info(lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH")))
        return Playlists(self.driver)

    def verifySearchFolderInDropDownPlay(self):
        self.navToPlaylistURL()
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", folder_name6)
        option = f"//a[@class='dropdown-item '][contains(.,'{folder_name6}')]"
        folder_detail = self.driver.find_elements(By.XPATH, option)
        return str(len(folder_detail))

    def new_folder(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name7)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(2)
        log.logger.info(lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH")))
        time.sleep(1)
        return lastWord(self.getText("S_SUB_FOLDER_LOC_XPATH"))

    def selectFolderFromDropdownAndOpen(self):
        self.navToPlaylistURL()
        self.wait_for_visible_all_elements("S_FOLDER_DROPDOWN_XPATH")
        self.click("S_FOLDER_DROPDOWN_XPATH")
        self.send_keys("S_INPUT_NAME_XPATH", folder_name7)
        option = f"//a[@class='dropdown-item '][contains(.,'{folder_name7}')]"
        self.driver.find_element(By.XPATH, option).click()
        time.sleep(3)
        folder_path = self.getText("S_FOLDER_NAME_DROP_XPATH")
        return folder_path

    def verifyPlaylistSearch(self):
        self.createPlaylist(playlist25)
        self.navToPlaylistURL()
        self.send_keys("S_SEARCH_PLAYLIST_XPATH", playlist25)
        time.sleep(3)
        nameOf_playlist_xpath = f"//span[@title='{playlist25}']"
        nameOf_playlist = self.driver.find_element(By.XPATH, nameOf_playlist_xpath).text
        assert playlist25 == nameOf_playlist

    def verifyFilterSearchForPlaylist(self):
        self.createPlaylist(playlist26)
        self.navToPlaylistURL()
        self.click("S_FILTER_XPATH")
        time.sleep(1)
        self.wait_for_visible_all_elements("S_COLUMN_INPUT_XPATH")
        element_size = len(self.find_elements("S_COLUMN_INPUT_XPATH"))
        return element_size

    def verifyCheckOptionOnPlaylist(self):
        self.createPlaylist(playlist27)
        self.navToPlaylistURL()
        playlist_xpath = f"//span[@title='{playlist27}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        ele_visible = len(self.find_elements("S_MORE_OPTION_XPATH"))
        return ele_visible

    def verifyMoreOptionsOnPlaylist(self):
        self.createPlaylist(playlist28)
        self.navToPlaylistURL()
        playlist_xpath = f"//span[@title='{playlist28}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        self.wait_for_visible_all_elements("S_MOVE_PLAY_XPATH")
        log.logger.info(str(len(self.find_elements("S_MOVE_TO_TRASH_XPATH"))))
        log.logger.info(str(len(self.find_elements("S_MOVE_PLAY_XPATH"))))
        return len(self.find_elements("S_MOVE_TO_TRASH_XPATH")) + len(self.find_elements("S_MOVE_PLAY_XPATH"))

    def verifyMovePlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name8)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(3)
        self.createPlaylist(playlist29)
        folder = f"//span[@title='{playlist29}']/following::td[1]"
        before_folder = self.driver.find_element(By.XPATH, folder).text
        log.logger.info("Before folder : " + self.driver.find_element(By.XPATH, folder).text)
        playlist_xpath = f"//span[@title='{playlist29}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_PLAY_XPATH")
        move_play = self.find_element("S_MOVE_PLAY_XPATH")
        self.driver.execute_script("arguments[0].click();", move_play)
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        self.send_keys("S_AUTO_XPATH", folder_name8)
        option = f"//li[.='{folder_name8}']"
        time.sleep(3)
        self.driver.find_element(By.XPATH, option).click()

        # option = f"//li[contains(text(),'{folder_name8}')]"
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.XPATH, option))).click()
        self.selenium_click("S_MOVE_XPATH")
        time.sleep(1)
        self.navToPlaylistURL()
        after_folder = self.driver.find_element(By.XPATH, folder).text
        log.logger.info("After folder : " + self.driver.find_element(By.XPATH, folder).text)
        assert before_folder != after_folder

    def verifyFolderOptionOnMovePlaylist(self):
        folder_list = []
        new_folder_list = []
        self.click("S_FOLDER_OPTIONS_XPATH")
        folders = self.find_elements("S_FOLDERS_XPATH")
        for i in folders:
            folder_list.append(i.text)
        time.sleep(1)
        log.logger.info(folder_list)
        self.refresh()
        self.createPlaylist(playlist58)
        playlist_xpath = f"//span[@title='{playlist58}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_PLAY_XPATH")
        move_play = self.find_element("S_MOVE_PLAY_XPATH")
        self.driver.execute_script("arguments[0].click();", move_play)
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        fold = self.find_elements("S_FOLDER_PLAY_XPATH")
        for j in fold:
            new_folder_list.append(j.text)
        time.sleep(2)
        log.logger.info(new_folder_list)
        assert folder_list == new_folder_list


    def verifyCloseOptionOnMovePlaylist(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name9)
        self.click("S_ADD_BUTTON_NAME")
        self.createPlaylist(playlist30)
        folder = f"//span[@title='{playlist30}']/following::td[1]"
        before_folder = self.driver.find_element(By.XPATH, folder).text
        log.logger.info("Before folder : " + self.driver.find_element(By.XPATH, folder).text)
        playlist_xpath = f"//span[@title='{playlist30}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_PLAY_XPATH")
        move_play = self.find_element("S_MOVE_PLAY_XPATH")
        self.driver.execute_script("arguments[0].click();", move_play)
        self.click("S_CLOSE_PLAY_ICON_XPATH")
        time.sleep(1)
        self.navToPlaylistURL()
        after_folder = self.driver.find_element(By.XPATH, folder).text
        log.logger.info("After folder : " + self.driver.find_element(By.XPATH, folder).text)
        assert before_folder == after_folder

    def verifyMovePlaylistToFolder(self):
        self.click("S_PLAY_FOLDER_CREATE_XPATH")
        self.send_keys("S_PLAY_FOLDER_NAME_XPATH", folder_name10)
        self.click("S_ADD_BUTTON_NAME")
        time.sleep(4)
        self.createPlaylist(playlist31)
        folder = f"//span[@title='{playlist31}']/following::td[1]"
        before_folder = self.driver.find_element(By.XPATH, folder).text
        log.logger.info("Before folder : " + self.driver.find_element(By.XPATH, folder).text)
        playlist_xpath = f"//span[@title='{playlist31}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_PLAY_XPATH")
        move_play = self.find_element("S_MOVE_PLAY_XPATH")
        self.driver.execute_script("arguments[0].click();", move_play)
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        self.send_keys("S_AUTO_XPATH", folder_name10)
        option = f"//li[.='{folder_name10}']"
        # option = f"span[title='{folder_name10}']"
        #self.refresh()
        time.sleep(5)
        self.driver.find_element(By.XPATH, option).click()
        self.click("S_MOVE_XPATH")
        time.sleep(1)
        self.navToPlaylistURL()
        after_folder = self.driver.find_element(By.XPATH, folder).text
        log.logger.info("After folder : " + self.driver.find_element(By.XPATH, folder).text)
        assert before_folder != after_folder

    def verifyTrashOSDForPlaylist(self):
        global playlist32
        playlist32 = generate_unique_string(5)
        self.createPlaylist(playlist32)
        playlist_xpath = f"//span[@title='{playlist32}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        message = self.getText("S_TRASH_MSG_XPATH")
        self.refresh()
        return message

    def verifyOkButtonOnTrashOSDForPlaylist(self):
        self.createPlaylist(playlist33)
        playlist_xpath = f"//span[@title='{playlist33}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_TRASH_MSG_XPATH")
        self.click("S_CONFIRM_BTN_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(2)
        self.send_keys("S_SEARCH_LIST_XPATH", playlist33)
        time.sleep(1)
        ele_xpath = f"//span[@title='{playlist33}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyCancelButtonOnTrashOSDForPlaylist(self):
        global playlist33
        playlist33 = generate_unique_string(5)
        self.createPlaylist(playlist33)
        self.navToPlaylistURL()
        playlist_xpath = f"//span[@title='{playlist33}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_TRASH_MSG_XPATH")
        self.click("S_CANCEL_XPATH")
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(4)
        self.send_keys("S_SEARCH_LIST_XPATH", playlist33)
        time.sleep(2)
        return self.getText("S_NO_DATA_XPATH")

    def verifyCloseButtonOnTrashOSDForPlaylist(self):
        self.createPlaylist(playlist34)
        playlist_xpath = f"//span[@title='{playlist34}']/preceding::input[@type='checkbox'][1]"
        retry_action(self.driver, By.XPATH, playlist_xpath)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        self.wait_for_visible_all_elements("S_TRASH_MSG_XPATH")
        self.click("S_CLOSE_X_BUTTON_XPATH")
        time.sleep(1)
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(5)
        getTextAfterRetry(self.driver, By.XPATH, "//input[@class='form-control form-control-sm']")
        self.send_keys("S_SEARCH_LIST_XPATH", playlist34)
        time.sleep(3)
        return self.getText("S_NO_DATA_XPATH")

    def createFolder(self, folder_name):
        self.click("S_NEW_FOLDER_PLAY_XPATH")
        self.send_keys("S_FOLDER_NAME_XPATH", folder_name)
        self.click("S_ADD_BUTTON_NAME")
        log.logger.info(folder_name)
        return Playlists(self.driver)

    def CreatePlaylistInsideFolder(self, playlist_name):
        time.sleep(4)
        # retry_action(self.driver, By.XPATH, "//img[@src='/packs/media/images/plus-f52f2f30a07d6b041ced0381242a9973"
        #                                     ".png']")
        self.driver.find_element(By.XPATH, "//img[@src='/packs/media/images/plus-f52f2f30a07d6b041ced0381242a9973.png']").click()
        self.send_keys("S_PLAY_NAME_XPATH", playlist_name)
        self.selenium_click("S_SAVE_BTN_XPATH")
        time.sleep(1)
        self.selenium_click("S_CLOSE_ICON_XPATH")
        return Playlists(self.driver)

    def copyPlaylistInsideFolder(self, playlist_name, new_playlist_name):
        time.sleep(2)
        copy_path = f"//td//span[@title='{playlist_name}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, copy_path)
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", new_playlist_name)
        self.selenium_click("S_MOVE_XPATH")
        time.sleep(1)

    def CancelCopyPlaylistInsideFolder(self, playlist_name):
        time.sleep(2)
        copy_path = f"//td//span[@title='{playlist_name}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, copy_path)
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.click("S_CLOSE_BUTTON_XPATH")
        time.sleep(1)

    def CloseCopyPlaylistInsideFolder(self, playlist_name):
        time.sleep(2)
        copy_path = f"//td//span[@title='{playlist_name}']/following::td[2]//a[2]"
        retry_action(self.driver, By.XPATH, copy_path)
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.click("S_CANCEL_BUTTON_XPATH")
        time.sleep(1)

    def verifyCopyOptionOnPlaylist(self):
        self.createFolder(folder_name11)
        self.CreatePlaylistInsideFolder(playlist35)
        self.copyPlaylistInsideFolder(playlist35, playlist37)
        self.refresh()
        time.sleep(2)
        folder = f"//td[contains(.,'{folder_name11}')]"
        folder_count = self.driver.find_elements(By.XPATH, folder)
        log.logger.info("folder_count : " + str(len(folder_count)))
        return str(len(folder_count))

    def verifyAllCharInCopyOptionOnPlaylist(self):
        self.createFolder(folder_name12)
        self.CreatePlaylistInsideFolder(playlist037)
        self.copyPlaylistInsideFolder(playlist037, playlist038)
        self.refresh()
        folder = f"//td[contains(.,'{folder_name12}')]"
        folder_count = self.driver.find_elements(By.XPATH, folder)
        log.logger.info("folder_count : " + str(len(folder_count)))
        return str(len(folder_count))

    def verifyAllSPCharInCopyOptionOnPlaylist(self):
        self.createFolder(folder_name13)
        self.CreatePlaylistInsideFolder(playlist39)
        self.copyPlaylistInsideFolder(playlist39, playlist40)
        return self.getText("S_INVALID_SCHEDULE_NAME_XPATH")

    def verifySaveOptionOnCopyPlaylist(self):
        self.createFolder(folder_name14)
        self.CreatePlaylistInsideFolder(playlist41)
        self.copyPlaylistInsideFolder(playlist41, playlist42)
        self.refresh()
        folder = f"//td[contains(.,'{folder_name14}')]"
        folder_count = self.driver.find_elements(By.XPATH, folder)
        log.logger.info("folder_count : " + str(len(folder_count)))
        return str(len(folder_count))

    def verifyCancelOptionOnCopyPlaylist(self):
        self.createFolder(folder_name15)
        self.CreatePlaylistInsideFolder(playlist43)
        self.CancelCopyPlaylistInsideFolder(playlist43)
        time.sleep(1)
        folder = f"//td[contains(.,'{folder_name15}')]"
        folder_count = self.driver.find_elements(By.XPATH, folder)
        log.logger.info("folder_count : " + str(len(folder_count)))
        return str(len(folder_count))

    def verifyCloseOptionOnCopyPlaylist(self):
        self.createFolder(folder_name16)
        self.CreatePlaylistInsideFolder(playlist44)
        self.CancelCopyPlaylistInsideFolder(playlist44)
        time.sleep(2)
        folder = f"//td[contains(.,'{folder_name16}')]"
        folder_count = self.driver.find_elements(By.XPATH, folder)
        log.logger.info("folder_count : " + str(len(folder_count)))
        return str(len(folder_count))

    def verifyOpenPlaylist(self):
        self.createPlaylist(playlist45)
        play_name = f"//span[@title='{playlist45}']"
        retry_action(self.driver, By.XPATH, play_name)
        edit_path = f"//input[@id='nameEdit']"
        value = self.driver.find_element(By.XPATH, edit_path).get_attribute('value')
        log.logger.info("value : " + value)
        assert playlist45 == value

    def verifyEditPlaylistDetail(self):
        self.createPlaylist(playlist59)
        play_url = self.get_current_url()
        play_name = f"//span[@title='{playlist59}']"
        retry_action(self.driver, By.XPATH, play_name)
        time.sleep(1)
        play_edit_url = self.get_current_url()
        assert play_url != play_edit_url

    def verifyEnterAllCharInRename(self):
        self.createPlaylist(playlist46)
        rename_path = f"//td//span[@title='{playlist46}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist47)
        self.click("S_SAVE_BTN_XPATH")
        self.navToPlaylistURL()
        ele_xpath = f"//span[@title='{playlist47}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyEnterSPAllCharInRename(self):
        self.createPlaylist(playlist48)
        rename_path = f"//td//span[@title='{playlist48}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist24)
        self.click("S_SAVE_BTN_XPATH")
        return self.getText("S_INVALID_MSG_XPATH")

    def verifySaveOptionRename(self):
        self.createPlaylist(playlist49)
        rename_path = f"//td//span[@title='{playlist49}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist50)
        self.click("S_SAVE_BTN_XPATH")
        self.navToPlaylistURL()
        ele_xpath = f"//span[@title='{playlist50}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyCancelOptionRename(self):
        self.createPlaylist(playlist51)
        rename_path = f"//td//span[@title='{playlist51}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist52)
        self.click("S_CANCEL_BUTTON_XPATH")
        ele_xpath = f"//span[@title='{playlist52}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def verifyCloseOptionRename(self):
        self.createPlaylist(playlist53)
        rename_path = f"//td//span[@title='{playlist53}']/following::td[2]//a[3]"
        self.driver.find_element(By.XPATH, rename_path).click()
        self.wait_for_visible_all_elements("S_PLAY_NAME_XPATH")
        self.clear("S_PLAY_NAME_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", playlist54)
        self.click("S_CLOSE_BUTTON_XPATH")
        ele_xpath = f"//span[@title='{playlist54}']"
        return str(len(self.driver.find_elements(By.XPATH, ele_xpath)))

    def get20PlaylistEntries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "20")
        time.sleep(3)
        log.logger.info("get20Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get50PlaylistEntries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "50")
        time.sleep(3)
        log.logger.info("get50Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get100PlaylistEntries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(3)
        log.logger.info("get100Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get200PlaylistEntries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "200")
        time.sleep(1)
        log.logger.info("get200Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def get500PlaylistEntries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "500")
        time.sleep(1)
        log.logger.info("get500Entries : " + str(len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))))
        return len(self.find_elements("S_PLAYLIST_COUNT_XPATH"))

    def select_10_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "10")
        time.sleep(10)
        return Playlists(self.driver)

    def verifyNextOptionOnPlaylist(self):
        self.select_10_entries()
        playlist_names = []
        new_playlist_names = []
        path = f"//td[2]"
        playlist_name = self.driver.find_elements(By.XPATH, path)
        for i in playlist_name:
            playlist_names.append(i.text)
        log.logger.info(playlist_names)
        time.sleep(1)
        xpath = f"//a[@data-dt-idx='1']"
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(7)
        n_path = f"//td[2]"
        new_playlist_name = self.driver.find_elements(By.XPATH, n_path)
        for i in new_playlist_name:
            new_playlist_names.append(i.text)
        log.logger.info(new_playlist_names)
        print(new_playlist_names)
        print(playlist_names)

        assert new_playlist_names != playlist_names

    def verifyPreviousOptionOnPlaylist(self):
        play_name = []
        previous_play = []
        xpath = f"//a[@data-dt-idx='1']"
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
        xpath = f"//a[@data-dt-idx='1']"
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(4)
        path = f"//td[2]"
        playlist_name = self.driver.find_elements(By.XPATH, path)
        for i in playlist_name:
            play_name.append(i.text)
        print(play_name)
        log.logger.info(play_name)
        xpath = f"//a[@data-dt-idx='0']"
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(7)
        path = f"//td[2]"
        n_playlist_name = self.driver.find_elements(By.XPATH, path)
        for i in n_playlist_name:
            previous_play.append(i.text)
        print(previous_play)
        log.logger.info(previous_play)
        assert play_name != previous_play

    def createMultiplePlaylists(self):
        self.navToPlaylistURL()
        for i in range(1, 3):
            time.sleep(2)
            self.createPlay(generate_unique_string(3))
            time.sleep(3)
            self.navToPlaylistURL()
            time.sleep(2)
        return Playlists(self.driver)

    def deletePlaylists(self):
        time.sleep(5)
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "50")
        time.sleep(3)
        self.wait_for_visible_all_elements("S_SELECT_ALL_XPATH")
        more_options = self.find_element("S_SELECT_ALL_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(2)
        self.wait_for_visible_all_elements("S_MORE_OPTION_XPATH")
        more_options = self.find_element("S_MORE_OPTION_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_MOVE_TO_TRASH_XPATH")
        moveTrash = self.find_element("S_MOVE_TO_TRASH_XPATH")
        self.driver.execute_script("arguments[0].click();", moveTrash)
        time.sleep(1)
        self.wait_for_visible_all_elements("S_CONFIRM_BUTTON_XPATH")
        self.selenium_click("S_CONFIRM_BUTTON_XPATH")
        time.sleep(9)

    def verifyNextOptionInTrashedPlaylist(self):
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(7)
        trash_page1_playlist_names = []
        trash_page2_playlist_names = []
        path = f"//td[2]"
        playlist_name = self.driver.find_elements(By.XPATH, path)
        for i in playlist_name:
            trash_page1_playlist_names.append(i.text)
        log.logger.info(trash_page1_playlist_names)
        time.sleep(1)
        xpath = f"//a[@data-dt-idx='1']"
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(7)
        n_path = f"//td[2]"
        new_playlist_name = self.driver.find_elements(By.XPATH, n_path)
        for i in new_playlist_name:
            trash_page2_playlist_names.append(i.text)
        log.logger.info(trash_page2_playlist_names)
        assert trash_page1_playlist_names != trash_page2_playlist_names

    def verifyPreviousOptionInTrashedPlaylist(self):
        trash_page2_playlist_names = []
        trash_page1_playlist_names = []
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(7)
        xpath = f"//a[@data-dt-idx='1']"
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(4)
        next_button = self.driver.find_element(By.XPATH, xpath)
        self.driver.execute_script("arguments[0].click();", next_button)
        time.sleep(7)
        n_path = f"//td[2]"
        playlist_name = self.driver.find_elements(By.XPATH, n_path)
        for i in playlist_name:
            trash_page2_playlist_names.append(i.text)
        log.logger.info(trash_page2_playlist_names)
        prev = f"//li[@id='DataTables_Table_1_previous']"
        prev_button = self.driver.find_element(By.XPATH, prev)
        self.driver.execute_script("arguments[0].click();", prev_button)
        time.sleep(7)
        n_path = f"//td[2]"
        s_playlist_name = self.driver.find_elements(By.XPATH, n_path)
        for i in s_playlist_name:
            trash_page1_playlist_names.append(i.text)
        log.logger.info(trash_page1_playlist_names)
        assert trash_page2_playlist_names != trash_page1_playlist_names

    def verifyScrollInPlaylistPage(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "100")
        time.sleep(1)
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

    def verifyScrollInTrashedPlaylistPage(self):
        retry_action(self.driver, By.XPATH, "//a[.='Trashed']")
        time.sleep(2)
        self.select_option_by_value_from_dropdown("S_TRASHED_ENT_XPATH", "100")
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

 ##########additional#########

    def sendspecialchar(self):
        self.send_keys("O_CONTENT_ContentNameTextbox_XPATH", "!@#$%^&*()_+-=[]\{}|;':/.,<>?")
        return Playlists(self.driver)

    def clikonaddContent(self):
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.wait_for_visible("D_Plus_Add_Content_XPATH")
        self.click("D_Plus_Add_Content_XPATH")
        return Playlists(self.driver)

    def EnterPlaylistnamewithspecialchar(self):
        self.wait_for_visible("D_EnterPlaylistname_CSS")
        # global Playlist_name
        # Playlist_name = ''.join(
        #     secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        # self.send_keys("D_EnterPlaylistname_CSS", Playlist_name)
        self.send_keys("D_EnterPlaylistname_CSS", "!@#$%^&*()_+-=[]\{}|;':/.,<>?")
        self.click("D_AddPlaylist_XPATH")
        return Playlists(self.driver)

    def clickonSave(self):
        self.wait_for_visible("D_Playlist_Save_XPATH")
        self.click("D_Playlist_Save_XPATH")
        return Playlists(self.driver)

    def getinvalidtext(self):
        time.sleep(3)
        self.wait_for_visible("O_INVALID_SCHEDULE_NAME_XPATH")
        c= self.getText("O_INVALID_SCHEDULE_NAME_XPATH")
        if "Only letters, numbers, spaces and _ are allowed." in c:
            return True
        else:
            return False

    def Enterplaylistname(self):
        self.wait_for_visible("D_EnterPlaylistname_CSS")
        global Playlist_name
        Playlist_name = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("D_EnterPlaylistname_CSS", Playlist_name)
        self.click("D_AddPlaylist_XPATH")
        return Playlists(self.driver)

    def searchcreatedPlaylist(self):
        self.click("D_Search_Content_XPATH")
        time.sleep(2)
        self.send_keys("D_Search_Content_XPATH", Playlist_name)
        time.sleep(1)
        return Playlists(self.driver)

    def gettextsearchedplaylist(self):
        self.wait_for_visible("D_Searched_Playlist_XPATH")
        time.sleep(2)
        srct = self.getText("D_Searched_Playlist_XPATH")
        time.sleep(2)
        print(srct)
        if srct == Playlist_name:
            assert True
        else:
            assert False
        return srct

#A
    def clickonpreview(self):
        time.sleep(2)
        self.wait_for_visible("D_Preview_Playlist_XPATH")
        self.click("D_Preview_Playlist_XPATH")
        return Playlists(self.driver)

    def cliockonclosepreview(self):
        self.wait_for_visible("O_EDIT_UNAME_CANCEL_BTN_XPATH")
        self.click("O_EDIT_UNAME_CANCEL_BTN_XPATH")
        return Playlists(self.driver)

    def clickonfilter(self):
        time.sleep(2)
        self.wait_for_visible("D_Playlistfilgtericon_XPATH")
        self.click("D_Playlistfilgtericon_XPATH")
        return Playlists(self.driver)

    def filteronname(self):
        time.sleep(2)
        self.wait_for_visible("D_filteronname_XPATH")
        ele = self.find_elements("D_filteronname_XPATH")
        ele1 = len(ele)
        # print(ele1)
        # print(type(ele1))
        return ele1

    def checkboxclikable(self):
        self.wait_for_visible("D_checkboxfirst_XPATH")
        self.click("D_checkboxfirst_XPATH")
        return Playlists(self.driver)

    def verifymoreenabled(self):
        self.wait_for_visible("D_more_playlistthreedot_XPATH")
        c = self.is_disable("D_more_playlistthreedot_XPATH")
        # print(c)
        return c


####sanity####
    def createsmartplaylist(self):
        global smart_playlist
        smart_playlist = generate_unique_string(8)
        self.navToPlaylistURL()
        self.click("S_CREATE_PLAY_XPATH")
        self.send_keys("S_PLAY_NAME_XPATH", smart_playlist)
        self.click("D_Smartplaylist_option_XPATH")
        self.click("S_SAVE_BTN_XPATH")
        self.navToPlaylistURL()
        return Playlists(self.driver)

    def searchcreatedsmartPlaylist(self):
        time.sleep(2)
        self.click("D_Search_Content_XPATH")
        time.sleep(2)
        self.send_keys("D_Search_Content_XPATH", smart_playlist)
        time.sleep(1)
        return Playlists(self.driver)

    def clickonpreview(self):
        self.wait_for_visible("D_Preview_PlaylistS_XPATH")
        time.sleep(1)
        self.click("D_Preview_PlaylistS_XPATH")
        ele = self.find_elements("D_Previewheading_XPATH")
        ele = len(ele)
        return ele

    def returntypeofplaylist(self):
        time.sleep(3)
        return self.getText("D_readtype_playlist_XPATH")

    def Uploadmedia1(self):
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\123.jpg"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.jpg"
        shutil.copy(ImageOldName, imageNewName)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(11)
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Imagename1
        Imagename1= ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename1)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename1:
            return True
        else:
            return False

    def Uploadmedia2(self):
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\123.jpg"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.jpg"
        shutil.copy(ImageOldName, imageNewName)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(11)
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Imagename2
        Imagename2 = ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename2)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename2:
            return True
        else:
            return False

    def Uploadmedia3(self):
        cwd = os.getcwd()
        ImageRandomName = "11AutomationMedia" + "".join(random.choices(string.ascii_letters, k=5))
        ImageOldName = cwd + r"\TestData\123.jpg"
        imageNewName = cwd + f"\TestData\Duplicate\{ImageRandomName}.jpg"
        shutil.copy(ImageOldName, imageNewName)
        self.selenium_click("N_AddNewMediaPlusIcon_XPATH")
        self.send_keys("N_MediaUploadDrop_XPATH", imageNewName)
        self.selenium_click("N_UploadButton_XPATH")
        time.sleep(12)
        self.refresh()
        self.selenium_click("N_MediaSearchBar_XPATH")
        os.remove(imageNewName)
        global Imagename3
        Imagename3 = ImageRandomName+".jpg"
        self.send_keys("N_MediaSearchBar_XPATH", Imagename3)
        time.sleep(3)
        uplodedsamplename = self.getText("N_NameFieldInTable_XPATH")
        if uplodedsamplename == Imagename3:
            return True
        else:
            return False

    def gotoContentPlaylists_Page(self):
        self.wait_for_visible_all_elements("S_CONTENT_HEAD_XPATH")
        time.sleep(3)
        self.selenium_click("S_CONTENT_HEAD_XPATH")
        self.wait_for_visible_all_elements("SUBMENU_PLAYLIST_XPATH")
        self.selenium_click("SUBMENU_PLAYLIST_XPATH")
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
        return Playlists(self.driver)

    def CreatePlaylistImage1(self):
        self.refresh()
        self.hoverAndSelect("O_ContentManager_XPATH", "O_ContentManagerPlaylist_XPATH")
        self.click("O_DisplayCreateIcon_XPATH")
        global PlaylistName
        PlaylistName = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys("playlistTB_XPATH", PlaylistName)
        self.click("O_ScheduleCreateCommit_XPATH")
        self.click("ScheduleEditPageLayoutOption_XPATH")
        self.click("ScheduleEditPageSearchIcon_XPATH")
        #self.send_keys("ScheduleEditPageSearchIcon_XPATH", LayoutName1)
        search = self.find_element("ScheduleEditPageSearchIcon_XPATH")
        search.clear()
        search.send_keys(LayoutName1)

        # time.sleep(3)
        # CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
        # Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        # Target = self.find_element("targetElement_XPATH")
        # actions = ActionChains(self.driver)
        # actions.drag_and_drop(Source, Target).perform()
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")

        Source = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CreatedLayout1InScheduleEditPage_xpath)
        )
        Target = self.find_element("targetElement_XPATH")
        actions = ActionChains(self.driver)
        actions.click_and_hold(Source).move_to_element(Target).release().perform()
        #time.sleep(2)
        self.click("savePlaylist_XPATH")
        self.click("savePlaylist_Yes_XPATH")
        return Playlists(self.driver)

    def CreatePlaylistImage1and2(self):
        self.refresh()
        self.hoverAndSelect("O_ContentManager_XPATH", "O_ContentManagerPlaylist_XPATH")
        self.click("O_DisplayCreateIcon_XPATH")
        global PlaylistName
        PlaylistName = "11AutomationPlaylist" + "".join(random.choices(string.ascii_letters, k=5))
        self.send_keys("playlistTB_XPATH", PlaylistName)
        self.click("O_ScheduleCreateCommit_XPATH")
        self.click("ScheduleEditPageLayoutOption_XPATH")
        self.click("ScheduleEditPageSearchIcon_XPATH")
        self.send_keys("ScheduleEditPageSearchIcon_XPATH", LayoutName1)
        time.sleep(3)
        CreatedLayout1InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName1}']")
        Source = self.find_element(CreatedLayout1InScheduleEditPage_xpath)
        Target = self.find_element("targetElement_XPATH")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source, Target).perform()
        time.sleep(2)

        self.click("ScheduleEditPageSearchIcon_XPATH")
        self.find_element("ScheduleEditPageSearchIcon_XPATH").clear()
        time.sleep(0.8)
        self.send_keys("ScheduleEditPageSearchIcon_XPATH", LayoutName2)
        time.sleep(3)
        CreatedLayout2InScheduleEditPage_xpath = (By.XPATH, f"//li[@title='{LayoutName2}']")
        Source1 = self.find_element(CreatedLayout2InScheduleEditPage_xpath)
        Target1 = self.find_element("targetElement_XPATH")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(Source1, Target1).perform()
        time.sleep(2)
        self.click("savePlaylist_XPATH")
        self.click("savePlaylist_Yes_XPATH")
        time.sleep(2)
        return Playlists(self.driver)


    def CreateLayoutWithBlankTemplateForImage1(self):
        global LayoutName1
        LayoutName1 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName1)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(1)
        self.contentPopupRemoval()
        self.click("LayoutImageIcon_XPATH")
        time.sleep(2)
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{Imagename1}']")
        SourceElement = self.driver.find_element(By.XPATH, f"//span[@title='{Imagename1}']")
        TargetElement = self.find_element("LayoutTargetElement_CLASSNAME")
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
        time.sleep(1)
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(1)
        self.gotoContentContents_PlayPage()
        return Playlists(self.driver)

    def CreateLayoutWithBlankTemplateForImage2(self):
        global LayoutName2
        LayoutName2 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName2)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(1)
        self.contentPopupRemoval()
        self.click("LayoutImageIcon_XPATH")
        time.sleep(1)
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{Imagename2}']")
        SourceElement = self.driver.find_element(By.XPATH, f"//span[@title='{Imagename2}']")
        TargetElement = self.find_element("LayoutTargetElement_CLASSNAME")
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
        time.sleep(2)
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(1)
        self.gotoContentContents_PlayPage()
        return Playlists(self.driver)

    def CreateLayoutWithBlankTemplateForImage3(self):
        global LayoutName3
        LayoutName3 = "11AutomationLayout" + "".join(random.choices(string.ascii_letters, k=5))
        self.click("ContentManager_XPATH")
        self.click("ContentManagerLayout_XPATH")
        self.click("LayoutCreateNewIcon_XPATH")
        self.send_keys("LayoutNameFieldWhileCreating_XPATH", LayoutName3)
        self.click("LayoutBlankTemplate_XPATH")
        self.click("LayoutCreateButton_XPATH")
        time.sleep(1)
        self.contentPopupRemoval()
        self.click("LayoutImageIcon_XPATH")
        time.sleep(1)
        UploadedImageElement_xpath = (By.XPATH, f"//span[@title='{Imagename3}']")
        SourceElement = self.driver.find_element(By.XPATH, f"//span[@title='{Imagename3}']")
        TargetElement = self.find_element("LayoutTargetElement_CLASSNAME")
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
        time.sleep(1)
        self.click("LayoutSaveOption_XPATH")
        self.click("LayoutSaveOption_XPATH")
        time.sleep(1)
        return Playlists(self.driver)
    def contentPopupRemoval(self):
        time.sleep(3)
        self.wait_for_visible_all_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        # element = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, "//span[.='Message']//following-sibling::span//span")))
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return Playlists(self.driver)

    def gotoContentContents_PlayPage(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Playlists(self.driver)

    def select_ImageFolderType(self):
        self.click("O_folderType_XPATH")
        time.sleep(1)
        self.click("O_folderType_IMAGE_XPATH")
        time.sleep(2)
        return Playlists(self.driver)

    def deleteUploadedMedia_Image(self):
        self.click("ContentManager_XPATH")
        self.click("O_ContentManagerMedia_XPATH")
        self.send_keys("O_SEARCHBAR_XPATH", "11Automation")
        time.sleep(2)
        empty = len(self.find_elements("EMPTY_DATA_XPATH"))
        while empty == 0:
            time.sleep(1)
            self.select_ImageFolderType()
            self.selenium_click("allOption_XPATH")
            time.sleep(1)
            self.selenium_click("moreOption_XPATH")
            time.sleep(0.5)
            self.selenium_click("moveToTrash_XPATH")
            self.selenium_click("okBtn_Trash_XPATH")
            time.sleep(2)
            self.selenium_click("trashFolder_XPATH")
            self.selenium_click("allOption_XPATH")
            self.selenium_click("moreOption_XPATH")
            self.selenium_click("deleteCompletely_XPATH")
            self.selenium_click("okBtn_Trash_XPATH")
            time.sleep(4)
            self.hoverAndSelect("ContentManager_XPATH", "O_ContentManagerMedia_XPATH")
            self.send_keys("O_SEARCHBAR_XPATH", "11Automation")
            time.sleep(2)
            empty = len(self.find_elements("EMPTY_DATA_XPATH"))
        return Playlists(self.driver)

    def verifyMultiSlide(self):
        ele1 = len(self.driver.find_elements(By.XPATH, f"//td[contains(.,'{LayoutName1}')]"))
        print(ele1)
        if ele1 == 1:
            return True
        else:
            return False

    def verifyPreview(self):
        ele1 = len(self.find_elements("previewBtn_XPATH"))
        print(ele1)
        if ele1 == 1:
            return True
        else:
            return False

    def verifyContentDeletedFromPlaylistPage(self):
        time.sleep(3)
        ele1 = len(self.driver.find_elements(By.XPATH, f"//td[contains(.,'{LayoutName1}')]"))
        print(ele1)
        if ele1 == 0:
            return True
        else:
            return False

    def deleteCreatedPlaylistContent(self):
        time.sleep(1)
        #self.click("deleteContentFromPlaylistPage_XPATH")
        self.click("A_deleteContentFromPlaylistPage_XPATH")
        return Playlists(self.driver)


