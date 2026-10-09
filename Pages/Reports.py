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

log = Logger(__name__, logging.INFO)

class Reports(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def createNewDisplay(self):
        self.clickOnAddNewDisplay()
        self.enterDisplayName()
        self.enterDisplayPassword()
        self.enterDisplayPassword_Conf()
        self.clickOnPopupAddBtn()
        time.sleep(2)
        self.refresh()
        return Reports(self.driver)

    def clickOnAddNewDisplay(self):
        self.click("O_ADD_NEW_DISPLAY_BTN_XPATH")
        time.sleep(2)
        return Reports(self.driver)

    def enterDisplayName(self):
        global r_Displayname
        r_Displayname = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DISPLAY_NAME_XPATH", r_Displayname)
        return Reports(self.driver)

    def enterDisplayPassword(self):
        global r_pass
        r_pass = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        self.send_keys("O_DISPLAY_PASSWORD_XPATH", r_pass)
        return Reports(self.driver)

    def enterDisplayPassword_Conf(self):
        self.send_keys("O_DISPLAY_CONF_PASSWORD_XPATH", r_pass)
        return Reports(self.driver)

    def clickOnPopupAddBtn(self):
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return Reports(self.driver)

    def getUserName(self):
        global userName
        self.click("O_PROFILE_ICON_XPATH")
        userName = self.getText("userName_XPATH")
        return Reports(self.driver)

    def verifyActivityLog_DisplayCreated(self):
        self.send_keys("SearchBar_D_XPATH", r_Displayname)
        time.sleep(2)
        ele = self.driver.find_elements(By.XPATH, f"//span[contains(.,'{r_Displayname}')]//parent::td//following-sibling::td[contains(.,'Display created')]")
        if len(ele) ==1:
            return True
        else:
            return False

    def gotoDisplayPage(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return Reports(self.driver)

    def deleteCreatedDisplay(self):
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", r_Displayname)
        time.sleep(3)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(3)
        return Reports(self.driver)