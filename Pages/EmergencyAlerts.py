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


class EmergencyAlerts(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def verifyURL(self):
        return self.get_current_url()

    def clicktimedropdown(self):
        self.wait_for_visible("D_time_Dropdown_XPATH")
        self.selenium_click("D_time_Dropdown_XPATH")
        return EmergencyAlerts(self.driver)

    def visibleonehour(self):
        return self.is_visible("D_Onehour_XPATH")

    def visiblesixhour(self):
        return self.is_visible("D_Sixhour_XPATH")

    def visibletwentyfourhour(self):
        return self.is_visible("D_Twentyfourhour_XPATH")

    def selecttimedurationonehour(self):
        self.selenium_click("D_Onehour_XPATH")
        return EmergencyAlerts(self.driver)

    def selecttimedurationsixhour(self):
        self.click("D_Sixhour_XPATH")

    def selecttwentyfourhour(self):
        self.click("D_Twentyfourhour_XPATH")
    def gettextfromdropdownbeforechange(self):
        return self.get_selected_value_from_dropdown("D_time_Dropdown_XPATH")

    def gettextdropdown(self):
        return self.get_selected_value_from_dropdown("D_time_Dropdown_XPATH")
        #return self.getText("D_time_Dropdown_XPATH")

    def clickonFilter(self):
        self.wait_for_visible("D_Filtersearch_XPATH")
        self.click("D_Filtersearch_XPATH")
        return EmergencyAlerts(self.driver)

    def FindlenghthDisplayIDcol(self):
        ele = self.find_elements("D_DisplayID_filtered_XPATH")
        ele = len(ele)
        print(ele)
        return EmergencyAlerts(self.driver)

    def FindlengthAfterFilterAppliedDisplayIDcol(self):
        ele = self.find_elements("D_DisplayID_filtered_XPATH")
        ele = len(ele)
        print(ele)
        return EmergencyAlerts(self.driver)

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
        return EmergencyAlerts(self.driver)

    def clickonDisplayIDsorting(self):
        time.sleep(2)
        self.wait_for_visible("D_DisplayID_Column_XPATH")
        self.selenium_click("D_DisplayID_Column_XPATH")
        return EmergencyAlerts(self.driver)
    def clickonDisplayIDsortingDSC(self):
        self.wait_for_visible("D_Display_ID_dsc_col_XPATH")
        self.click("D_Display_ID_dsc_col_XPATH")
        return EmergencyAlerts(self.driver)

    def clickonDisplaynameSorting(self):
        self.wait_for_visible("D_Displaynamee_Col_XPATH")
        self.click("D_Displaynamee_Col_XPATH")
        return EmergencyAlerts(self.driver)
    def clickondispnamedscsort(self):
        self.wait_for_visible("D_Displaynamee_col_dsc_XPATH")
        self.click("D_Displaynamee_col_dsc_XPATH")
        return EmergencyAlerts(self.driver)

    def clickonDisplayStatesorting(self):
        time.sleep(2)
        self.wait_for_visible("D_Displaystate_XPATH")
        self.click("D_Displaystate_XPATH")
        return EmergencyAlerts(self.driver)
    def clickonDisplaystatedscsorting(self):
        self.wait_for_visible("D_Displaystatedscsort_XPATH")
        self.click("D_Displaystatedscsort_XPATH")
        return EmergencyAlerts(self.driver)

    def clickonDisplaycitySorting(self):
        self.wait_for_visible("D_Displaycity_XPATH")
        self.click("D_Displaycity_XPATH")
        return EmergencyAlerts(self.driver)
    def clickonDisplaycitysortingdesc(self):
        self.wait_for_visible("D_Displaycity_desc_XPATH")
        self.click("D_Displaycity_desc_XPATH")
        return EmergencyAlerts(self.driver)


    def verifyInDescendingOrder_name(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_namee(self):
        time.sleep(5)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_Dispname(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_Dispnamee(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_DispState(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_DispState(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_DispCity(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[5]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_DispCity(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[5]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

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

    def clickonFirstdisplay(self):
        self.wait_for_visible("D_Display_EMAlt_XPATH")
        time.sleep(3)
        self.selenium_click("D_Display_EMAlt_XPATH")
        time.sleep(1)
        return EmergencyAlerts(self.driver)

    def clickonbuildingmaintenance(self):
        # self.wait_for_visible("D_Building_maintenance_XPATH")
        # time.sleep(2)
        # self.click("D_Building_maintenance_XPATH")
        self.wait_for_visible("D_BldgMaintenance_SIT_XPATH")
        time.sleep(2)
        self.click("D_BldgMaintenance_SIT_XPATH")
        return EmergencyAlerts(self.driver)

    def checkDeliverButton(self):
        return self.is_disable("D_Deliver_Button_XPATH")

    def gotoEmergencyAlerts_EA(self):
        self.click("MENU_EA_XPATH")
        time.sleep(1)
        return EmergencyAlerts(self.driver)

    def getDisplayIDs_fromDisplayPage(self):
        global displayID_displayPage
        displayID_displayPage = []
        elements = self.find_elements("D_Displays_Did_XPATH")
        for element in elements:
            ele = element.text
            displayID_displayPage.append(ele)
        return EmergencyAlerts(self.driver)

    def getDisplayIDs_fromEmergencyAlertPage(self):
        global displayID_EmergencyAlertPage
        displayID_EmergencyAlertPage = []
        elements = self.find_elements("D_Displays_Did_XPATH")
        for element in elements:
            ele = element.text
            displayID_EmergencyAlertPage.append(ele)
        return EmergencyAlerts(self.driver)

    def verifyDisplayIDs(self):
        self.refresh()
        if displayID_displayPage == displayID_EmergencyAlertPage:
            return True
        else:
            return False

    ####verify displayname###

    def getDisplayNames_fromDisplayPage(self):
        global displayName_displayPage
        displayName_displayPage = []
        elements = self.find_elements("D_Displays_Name_XPATH")
        for element in elements:
            ele = element.text
            displayName_displayPage.append(ele)
        return EmergencyAlerts(self.driver)

    def getDisplayNames_fromEmergencyAlertPage(self):
        global displayName_EmergencyAlertPage
        displayName_EmergencyAlertPage = []
        elements = self.find_elements("D_Displays_Name_XPATH")
        for element in elements:
            ele = element.text
            displayName_EmergencyAlertPage.append(ele)
        return EmergencyAlerts(self.driver)

    def verifyDisplayNames(self):
        self.refresh()
        if displayName_displayPage == displayName_EmergencyAlertPage:
            return True
        else:
            return False

    def clickonEditBuildingMaintenance(self):
        # self.wait_for_visible("D_Edit_BldgMaintenance_XPATH")
        # self.click("D_Edit_BldgMaintenance_XPATH")
        self.wait_for_visible("D_Editicon_BLDGMaintenance_SIT_XPATH")
        self.click("D_Editicon_BLDGMaintenance_SIT_XPATH")
        return EmergencyAlerts(self.driver)

    def verifyeditbldgmaintenanceokbtn(self):
        self.wait_for_visible("O_ContentApprovalMsgBox_X_Btn_XPATH")
        ele = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        ele = len(ele)
        return ele
        # self.wait_for_visible("D_Edit_OkButton_XPATH")
        # return self.getText("D_Edit_OkButton_XPATH")


    def verifyeditpagemaintenancedragtext(self):
        self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        self.wait_for_visible("BldgMain_SIT_XPATH")
        return self.getText("BldgMain_SIT_XPATH")
        # self.wait_for_visible("D_Dragdrop_edit_XPATH")
        # return self.getText("D_Dragdrop_edit_XPATH")


    def clickonfirealert(self):
        # self.wait_for_visible("D_Firealert_XPATH")
        # time.sleep(2)
        # self.scroll_to_element("D_Firealert_XPATH")
        # time.sleep(2)
        # self.click("D_Firealert_XPATH")
        self.wait_for_visible("D_Firealert_SIT_XPATH")
        time.sleep(2)
        self.click("D_Firealert_SIT_XPATH")
        return EmergencyAlerts(self.driver)

    def clickoneditfirealert(self):
        # self.wait_for_visible("D_Edit_Firealert_XPATH")
        # self.click("D_Edit_Firealert_XPATH")
        self.wait_for_visible("D_Firealert_edit_SIT_XPATH")
        self.click("D_Firealert_edit_SIT_XPATH")
        return EmergencyAlerts(self.driver)

    def clickonHeavyrain(self):
        # self.wait_for_visible("D_Heavyrain_XPATH")
        # time.sleep(2)
        # self.scroll_to_element("D_Heavyrain_XPATH")
        # time.sleep(2)
        # self.click("D_Heavyrain_XPATH")
        self.wait_for_visible("D_HeavyRain_SIT_XPATH")
        time.sleep(1)
        self.click("D_HeavyRain_SIT_XPATH")
        return EmergencyAlerts(self.driver)

    def clickoneditheavyrain(self):
        # self.wait_for_visible("D_editicon_heavyrain_XPATH")
        # self.click("D_editicon_heavyrain_XPATH")
        self.wait_for_visible("D_Editicon_Heavrrain_SIT_XPATH")
        self.click("D_Editicon_Heavrrain_SIT_XPATH")
        return EmergencyAlerts(self.driver)

    def clickodisplayneditbutton(self):
        self.wait_for_visible("D_EditDisplay_XPATH")
        self.click("D_EditDisplay_XPATH")
        return EmergencyAlerts(self.driver)
    def geteditdisplayname(self):
        global dispnm
        dispnm = self.find_element("D_getDisplay_name_XPATH").get_attribute('value')
        return dispnm

    def getvaluestate(self):
        return self.get_selected_value_from_dropdown("D_StateValue_XPATH")
    def searchinEA(self):
        self.wait_for_visible("D_Search_Content_XPATH")
        self.send_keys("D_Search_Content_XPATH", dispnm)
        return EmergencyAlerts(self.driver)

    def getvalueCity(self):
        return self.get_selected_value_from_dropdown("D_CityValue_XPATH")
    def clickoncancel(self):
        self.click("O_EDIT_UNAME_CANCEL_BTN_XPATH")
        return EmergencyAlerts(self.driver)
    def getemgstatedisplay(self):
        return self.getText("D_DisplayState_emg_XPATH")

    def getemgcitydisplay(self):
        return self.getText("D_DisplayCity_emg_XPATH")

    def gotodisplays(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return EmergencyAlerts(self.driver)
    def clickOnSideBarHideBtn(self):
        self.refresh()
        self.click("D_SIDEBAR_HIDE_BTN_XPATH")
        return EmergencyAlerts(self.driver)
    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount
    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "50")
        time.sleep(2)
        return EmergencyAlerts(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "100")
        time.sleep(2)
        return EmergencyAlerts(self.driver)

    def select_200_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "200")
        time.sleep(2)
        return EmergencyAlerts(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "500")
        time.sleep(2)
        return EmergencyAlerts(self.driver)


    ###########sanity###############
    def clickondeliverbutton(self):
        time.sleep(2)
        self.click("D_Deliver_Button_XPATH")
        return EmergencyAlerts(self.driver)

    def readpopup(self):
        self.wait_for_visible("D_Approvepopup_XPATH")
        return self.getText("D_Approvepopup_XPATH")


