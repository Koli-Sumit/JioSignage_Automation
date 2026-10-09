from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage, retry_action
import time

def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


def is_descending(lst):
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            return False
    return True


class UserActivityLogsReport(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyURL(self):
        return self.get_current_url()

    def verifyusernamevisible(self):
        self.wait_for_visible("D_usernme_XPATH")
        return self.is_visible("D_usernme_XPATH")
    def verifyeventvisible(self):
        self.wait_for_visible("D_Event_XPATH")
        return self.is_visible("D_Event_XPATH")
    def verifyitemtypevisible(self):
        self.wait_for_visible("D_Itemtype_XPATH")
        return self.is_visible("D_Itemtype_XPATH")
    def verifyitemnamevisible(self):
        self.wait_for_visible("D_Itemname_XPATH")
        return self.is_visible("D_Itemname_XPATH")
    def verifycreatedatvisible(self):
        self.wait_for_visible("D_CreatedAT_XPATH")
        return self.is_visible("D_CreatedAT_XPATH")

    def verifyuseracttext(self):
        return self.getText("D_UserlogText_XPATH")

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "50")
        time.sleep(2)
        return UserActivityLogsReport(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "100")
        time.sleep(2)
        return UserActivityLogsReport(self.driver)

    def select_200_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "200")
        time.sleep(2)
        return UserActivityLogsReport(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return UserActivityLogsReport(self.driver)

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def clickongenratereport(self):
        self.wait_for_visible("D_genrateuser_report_XPATH")
        self.click("D_genrateuser_report_XPATH")
        return UserActivityLogsReport(self.driver)
    def visibledaily(self):
        self.wait_for_visible("D_Daily_XPATH")
        return self.is_visible("D_Daily_XPATH")
    def visibleweekly(self):
        self.wait_for_visible("D_Weekly_XPATH")
        return self.is_visible("D_Weekly_XPATH")
    def visiblecustom(self):
        self.wait_for_visible("D_Weekly_XPATH")
        return self.is_visible("D_Weekly_XPATH")

    def switchtobaseuser(self):
        ele_XPATH = "//input[@role='searchbox']"
        self.wait_for_visible("D_DropdownselectBaseUser_XPATH")
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        # self.click("D_DropdownselectBaseUser_XPATH")
        self.wait_for_visible("D_selectBase_XPATH")
        self.click("D_selectBase_XPATH")
        self.wait_for_visible("D_clickdropdown_selectbase_XPATH")
        self.click("D_clickdropdown_selectbase_XPATH")
        self.wait_for_visible("D_SearchSchedule_XPATH")
        self.click("D_SearchSchedule_XPATH")
        self.send_keys("D_SearchSchedule_XPATH", "Automation")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        self.wait_for_visible("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return UserActivityLogsReport(self.driver)

    def SwitchtoHeaduser(self):
        self.wait_for_visible("D_DropdownselectBaseUser_XPATH")
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        self.wait_for_visible("D_HeadAcoount_XPATH")
        self.click("D_HeadAcoount_XPATH")
        return UserActivityLogsReport(self.driver)

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")

    def checkForCurrentAccountTypeProd(self):
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

    def verifyInDescendingOrder_Itemname(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_Itemname(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickforsortItemname(self):
        self.wait_for_visible("D_Itemnamecol_XPATH")
        self.click("D_Itemnamecol_XPATH")
        return UserActivityLogsReport(self.driver)


    def verifyInDescendingOrder_CreatedAt(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[5]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_CreatedAt(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[5]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickforsortCreatedAt(self):
        self.wait_for_visible("D_CreatedAtcol_XPATH ")
        self.click("D_CreatedAtcol_XPATH ")
        return UserActivityLogsReport(self.driver)


