import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage, retry_action


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


class PlayLogsReport(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyURL(self):
        return self.get_current_url()

    def verifyReportHeadingMessage(self):
        return self.getText("D_MessageText_report_XPATH")

    def clickfilterIcon(self):
        self.wait_for_visible("D_refreshicon_XPATH")
        self.click("D_refreshicon_XPATH")
        return PlayLogsReport(self.driver)

    def verifyDisplayvisible(self):
        d = self.find_elements("D_DisplayName_Column_XPATH")
        count = len(d)
        print(str(count))
        return str(count)

    def clickonrefresh(self):
        self.click("D_refreshicon_XPATH")
        time.sleep(2)
        return PlayLogsReport(self.driver)

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "50")
        time.sleep(2)
        return PlayLogsReport(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "100")
        time.sleep(2)
        return PlayLogsReport(self.driver)

    def select_200_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "200")
        time.sleep(2)
        return PlayLogsReport(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return PlayLogsReport(self.driver)

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount

    def clickongenrateReport(self):
        self.click("D_genratereport_XPATH")
        return PlayLogsReport(self.driver)

    def contentoptionvisible(self):
        return self.is_visible("D_Content_Option_XPATH")

    def Displayoptionvisible(self):
        return self.is_visible("D_Displayoption_XPATH")

    def clickoncontentreportoption(self):
        self.wait_for_visible("D_Content_Option_XPATH")
        self.click("D_Content_Option_XPATH")
        return PlayLogsReport(self.driver)

    def verifycustomreportvisible(self):
        return self.is_visible("D_Customreport_XPATH")

    def verifyContentreportvisible(self):
        return self.is_visible("D_Contentreport_XPATH")

    def verifyContentTagwisevisible(self):
        return self.is_visible("D_ContentTagwise_XPATH")

    def clickondisplayreport(self):
        self.wait_for_visible("D_Displayoption_XPATH")
        self.click("D_Displayoption_XPATH")
        return PlayLogsReport(self.driver)

    def verifydisplayreportvisible(self):
        return self.is_visible("D_DisplayReport_XPATH")

    def verifydisplaytagwisevisible(self):
        return self.is_visible("D_DisplayTagwisereport_XPATH")

    def verifydatewisevisible(self):
        return self.is_visible("D_datewisereport_XPATH")

    def visibledisplayid(self):
        self.wait_for_visible("D_DisplayID_XPATH")
        return self.is_visible("D_DisplayID_XPATH")

    def visibledisplayname(self):
        self.wait_for_visible("D_DisplayName_XPATH")
        return self.is_visible("D_DisplayName_XPATH")

    def visibleitemname(self):
        self.wait_for_visible("D_ItemNameplay_XPATH")
        return self.is_visible("D_ItemNameplay_XPATH")

    def visibleplaystart(self):
        self.wait_for_visible("D_PlayStart_XPATH")
        return self.is_visible("D_PlayStart_XPATH")

    def visibleplaytime(self):
        self.wait_for_visible("D_Playtime_XPATH")
        return self.is_visible("D_Playtime_XPATH")

    def visiblehdmistatus(self):
        self.wait_for_visible("D_HDMIStatus_XPATH")
        return self.is_visible("D_HDMIStatus_XPATH")

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
        return PlayLogsReport(self.driver)

    def SwitchtoHeaduser(self):
        self.wait_for_visible("D_DropdownselectBaseUser_XPATH")
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        self.wait_for_visible("D_HeadAcoount_XPATH")
        self.click("D_HeadAcoount_XPATH")
        return PlayLogsReport(self.driver)

    def clickonclose(self):
        self.wait_for_visible("S_CLOSE_BUTTON_XPATH")
        self.click("S_CLOSE_BUTTON_XPATH")

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

    def clikforsortdisplay(self):
        self.wait_for_visible("D_DISPLAY_CLM_XPATH")
        self.click("D_DISPLAY_CLM_XPATH")
        return PlayLogsReport(self.driver)

    def verifyInDescendingOrder_DisplayID(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_DisplayID(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_DisplayName(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_DisplayName(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clikforsortdisplayName(self):
        self.wait_for_visible("D_DisplayName_CLM_XPATH")
        self.click("D_DisplayName_CLM_XPATH")
        return PlayLogsReport(self.driver)

    def verifyInDescendingOrder_ItemName(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_ItemName(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clikforsortItemname(self):
        self.wait_for_visible("D_ItemNamePL__XPATH")
        self.click("D_ItemNamePL__XPATH")
        return PlayLogsReport(self.driver)

    def verifyInDescendingOrder_Playtime(self):
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

    def verifyInAscendingOrder_Playtime(self):
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

    def clickforsortPlaytime(self):
        self.wait_for_visible("D_PlaytimePL_XPATH")
        self.click("D_PlaytimePL_XPATH")
        return PlayLogsReport(self.driver)

    def verifyInDescendingOrder_Playtimeseconds(self):
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

    def verifyInAscendingOrder_Playtimeseconds(self):
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

    def clickforsortPlaytimeseconds(self):
        self.wait_for_visible("D_Playtimesec_XPATH")
        self.click("D_Playtimesec_XPATH")
        return PlayLogsReport(self.driver)

    def verifyInDescendingOrder_Cablestatus(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[6]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_Cablestatus(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr/td[6]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickforsortcablestatus(self):
        self.wait_for_visible("D_Cablestatus_XPATH")
        self.click("D_Cablestatus_XPATH")
        return PlayLogsReport(self.driver)
