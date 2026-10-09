import secrets
import time

from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class BaseManagement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyBaseMgmtURL(self):
        return self.get_current_url()

    def isVisibleSearchBar(self):
        return self.is_visible("O_BASE_MGT_SEARCHBAR_XPATH")

    def isVisibleTrashBtn(self):
        return self.is_visible("O_BASE_MGT_TRASH_BTN_XPATH")

    def isVisibleAddNewBaseBtn(self):
        return self.is_visible("O_BASE_MGT_ADD_NEW_BASE_XPATH")

    def isVisibleAddNewBaseBtn_PlusIcon(self):
        return self.is_visible("O_BASE_MGT_ADD_NEW_BASE_PLUS_ICON_XPATH")

    def clickOnAddNewBaseBtn(self):
        self.click("O_BASE_MGT_ADD_NEW_BASE_XPATH")
        return BaseManagement(self.driver)

    def enterBaseName(self):
        global r_BaseName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        r_BaseName = f"Test_Base_Auto {r_text}"
        self.send_keys("O_BASE_MGT_Base_Name_textbox_XPATH", r_BaseName)
        return BaseManagement(self.driver)

    def clickOnAddNewBase_AddBTN(self):
        self.click("O_BASE_MGT_POP_UP_ADD_BTN_XPATH")
        return BaseManagement(self.driver)

    def clickOnAddNewBase_CancelBTN(self):
        self.click("O_BASE_MGT_POP_UP_Cancel_BTN_XPATH")
        return BaseManagement(self.driver)

    def getBaseAccountsCount(self):
        accounts = self.find_elements("O_BASE_MGT_USER_COUNT_XPATH")
        accounts = len(accounts)
        return accounts

    def verifyDeletedAccountOnBaseMgtPage(self):
        time.sleep(1)
        self.refresh()
        accounts = self.find_elements("O_BASE_MGT_USER_COUNT_XPATH")
        for account in accounts:
            account_name = account.text
            if account_name == r_BaseName:
                return False
            else:
                return True

    def verifyDeletedAccountOnTrashPage(self):
        time.sleep(2)
        self.refresh()
        accounts = self.find_elements("O_BASE_MGT_USER_COUNT_XPATH")
        for account in accounts:
            account_name = account.text
            if account_name == r_BaseName:
                return True
            else:
                return False

    def addNewBaseAccount(self):
        self.clickOnAddNewBaseBtn()
        self.enterBaseName()
        self.clickOnAddNewBase_AddBTN()
        time.sleep(2)
        self.refresh()
        self.refresh()
        return BaseManagement(self.driver)

    def addNewBaseAccount_CancelBtn(self):
        self.clickOnAddNewBaseBtn()
        self.clickOnAddNewBase_CancelBTN()
        time.sleep(2)
        self.refresh()
        self.refresh()
        return BaseManagement(self.driver)

    def isVisible_baseAccountName(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]"
        return self.driver.find_element(By.XPATH, ele_XPATH).is_displayed()

    def accountID_text_colour(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//following::span[1]"
        ele = self.driver.find_element(By.XPATH, ele_XPATH)
        color = ele.value_of_css_property("color")
        return color

    def schedule_text_colour(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//following::span[2]"
        ele = self.driver.find_element(By.XPATH, ele_XPATH)
        color = ele.value_of_css_property("color")
        return color

    def deleteCreatedBaseAccount(self):
        self.refresh()
        ele1_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//parent::div//preceding-sibling::div//div//img"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        self.click("O_BASE_MGT_delete_XPATH")
        self.click("O_BASE_MGT_delete_OK_XPATH")
        return BaseManagement(self.driver)

    def enterBaseName_edit(self):
        self.clear("O_BASE_MGT_Base_Name_textbox_XPATH")
        global r_BaseName_edit
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        r_BaseName_edit = f"Test_Base_Auto {r_text}"
        self.send_keys("O_BASE_MGT_Base_Name_textbox_XPATH", r_BaseName_edit)
        return BaseManagement(self.driver)

    def editCreatedBaseAccount(self):
        self.refresh()
        ele1_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//parent::div//preceding-sibling::div//div//img"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        self.click("O_BASE_MGT_EDIT_BTN_XPATH")
        self.enterBaseName_edit()
        self.clickOnAddNewBase_AddBTN()
        time.sleep(2)
        self.refresh()
        self.refresh()
        return BaseManagement(self.driver)

    def deleteCreatedBaseAccount_edited(self):
        self.refresh()
        ele1_XPATH = f"//div//h6[contains(.,'{r_BaseName_edit}')]//parent::div//preceding-sibling::div//div//img"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        self.click("O_BASE_MGT_delete_XPATH")
        self.click("O_BASE_MGT_delete_OK_XPATH")
        return BaseManagement(self.driver)

    def clickOn_FIRST_ACC_THREE_DOT(self):
        self.click("O_BASE_MGT_FIRST_ACC_THREE_DOT_XPATH")
        return BaseManagement(self.driver)

    def isVisibleEditBTN(self):
        return self.is_visible("O_BASE_MGT_EDIT_BTN_XPATH")

    def isVisibleDeleteBTN(self):
        return self.is_visible("O_BASE_MGT_delete_XPATH")

    def get_accountID_ofCreatedBaseAccount(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//following::span[1]"
        ele = self.driver.find_element(By.XPATH, ele_XPATH)
        ACC_ID = ele.text
        return ACC_ID

    def get_schedule_status_ofCreatedBaseAccount(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//following::span[2]"
        ele = self.driver.find_element(By.XPATH, ele_XPATH)
        sch_status = ele.text
        return sch_status

    def isVisible_baseAccountName_edited(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName_edit}')]"
        return self.driver.find_element(By.XPATH, ele_XPATH).is_displayed()

    def get_accountID_ofCreatedBaseAccount_afterEdit(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName_edit}')]//following::span[1]"
        ele = self.driver.find_element(By.XPATH, ele_XPATH)
        ACC_ID = ele.text
        return ACC_ID

    def get_schedule_status_ofCreatedBaseAccount_afterEdit(self):
        ele_XPATH = f"//div//h6[contains(.,'{r_BaseName_edit}')]//following::span[2]"
        ele = self.driver.find_element(By.XPATH, ele_XPATH)
        sch_status = ele.text
        return sch_status

    def clickOnTrashBtn(self):
        self.click("O_BASE_MGT_TRASH_BTN_XPATH")
        time.sleep(2)
        return BaseManagement(self.driver)

    def clickOnRestoreBtn(self):
        self.click("O_BASE_MGT_TRASH_PAGE_RESTORE_BTN_XPATH")
        return BaseManagement(self.driver)

    def restoreDeletedBaseAccount(self):
        time.sleep(2)
        self.refresh()
        ele1_XPATH = f"//div//h6[contains(.,'{r_BaseName}')]//parent::div//preceding-sibling::div//div//img"
        self.driver.find_element(By.XPATH, ele1_XPATH).click()
        self.click("O_BASE_MGT_TRASH_PAGE_RESTORE_BTN_XPATH")
        self.click("O_BASE_MGT_delete_OK_XPATH")
        return BaseManagement(self.driver)

    def gotoUABaseMgmt_page(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return BaseManagement(self.driver)

    def clickOnBackToBaseMgtBtn(self):
        self.click("O_BASE_MGT_TRASH_PAGE_BACK_TO_MGT_BTN_XPATH")
        return BaseManagement(self.driver)

    def verifyRestoredAccountOnTrashPage(self):
        time.sleep(2)
        self.refresh()
        accounts = self.find_elements("O_BASE_MGT_USER_COUNT_XPATH")
        for account in accounts:
            account_name = account.text
            if account_name == r_BaseName:
                return False
            else:
                return True

    def verifyRestoredAccountOnBaseMgtPage(self):
        time.sleep(3)
        self.refresh()
        accounts = self.find_elements("O_BASE_MGT_USER_COUNT_XPATH")
        for account in accounts:
            account_name = account.text
            if account_name == r_BaseName:
                return True
            else:
                return False

####

    def verifyBaseSearchBar(self):
        time.sleep(1)
        self.send_keys("O_BASE_MGT_SEARCHBAR_XPATH",f"{r_BaseName}")
        time.sleep(3)
        ele = self.find_elements("O_BM_USER_COUNT_XPATH")
        ele = len(ele)
        return ele

