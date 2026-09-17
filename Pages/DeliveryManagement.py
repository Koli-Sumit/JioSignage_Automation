import secrets
import time
import re
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from Pages.BasePage import BasePage, retry_action, generate_random_string
from pytest_check import check

from Utilities import configReader

env = configReader.getTestData("TestData", "Environment")
##added
global schedule_name
schedule_name = generate_random_string(7)
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


class DeliveryManagement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyDeliveryMgmtURL(self):
        return self.get_current_url()

    def verifycreatedisplay(self):
        self.wait_for_visible("AddButton_Display_D_XPATH")
        self.click("AddButton_Display_D_XPATH")
        self.wait_for_visible("Display_name_D_XPATH")
        self.click("Display_name_D_XPATH")
        global d_displayname
        d_displayname = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(6))
        self.send_keys("Display_name_D_XPATH", d_displayname)
        self.wait_for_visible("EnterPassword_Display_D_XPATH")
        self.click("EnterPassword_Display_D_XPATH")
        global p_pssd
        p_pssd = ''.join(
            secrets.choice('0123456789') for _ in range(9))
        self.send_keys("EnterPassword_Display_D_XPATH", p_pssd)
        self.wait_for_visible("Confirm_Password_Display_D_XPATH")
        self.click("Confirm_Password_Display_D_XPATH")
        self.send_keys("Confirm_Password_Display_D_XPATH", p_pssd)
        self.wait_for_visible_all_elements("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return DeliveryManagement(self.driver)

    def verifySearchFunctionality(self):
        time.sleep(3)
        self.wait_for_visible_all_elements("SearchBar_D_XPATH")
        self.click("SearchBar_D_XPATH")
        self.send_keys("SearchBar_D_XPATH", d_displayname)
        time.sleep(5)
        return DeliveryManagement(self.driver)

    def clickOnSideBarHideBtn(self):
        # self.refresh()
        # self.click("D_SIDEBAR_HIDE_BTN_XPATH")
        self.wait_for_visible("D_SIDEBAR_HIDE_BTN_XPATH")
        more_options = self.find_element("D_SIDEBAR_HIDE_BTN_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def search_192(self):
        time.sleep(2.5)
        self.send_keys("D_SEARCH_BAR_XPATH", f"192")
        time.sleep(4)
        return DeliveryManagement(self.driver)

    def getDisplayID_fromTable(self):
        global ID
        ele_XPATH = "//tr[1]//td[2]"
        ID = self.driver.find_element(By.XPATH, ele_XPATH).text
        return ID

    def getDisplayName_fromTable(self):
        global Name
        ele_XPATH = "//tr[1]//td[3]"
        Name = self.driver.find_element(By.XPATH, ele_XPATH).text
        return Name

    def getDisplaySchedule_fromTable(self):
        global Schedule
        #ele_XPATH = "//tbody//tr//td[7]"
        ele_XPATH = "//tbody//tr//td[6]//a"
        Schedule = self.driver.find_element(By.XPATH, ele_XPATH).text
        print(Schedule)
        return Schedule

    def getCountOfSchedules(self):
        global schedule_count
        #ele_XPATH = f"//tr//td[7]//a[.='{Schedule}']"
        ele_XPATH = f"//tr//td[6]//a[.='{Schedule}']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        schedule_count = len(ele)
        return schedule_count

    def getIPAdd_fromTable(self):
        global IP
        ele_XPATH = "//tr[1]//td[6]"
        IP = self.driver.find_element(By.XPATH, ele_XPATH).text
        return IP

    def searchByDisplayID(self):
        self.clear("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"{ID}")
        return DeliveryManagement(self.driver)

    def searchByDisplayName(self):
        self.clear("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"{Name}")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    def searchByDisplaySchedule(self):
        self.clear("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"{Schedule}")
        time.sleep(5)
        return DeliveryManagement(self.driver)

    def searchByIPAdd(self):
        self.clear("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"{IP} {ID}")
        return DeliveryManagement(self.driver)

    def search_connected(self):
        self.clear("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"Connected")
        return DeliveryManagement(self.driver)

    def Count_forSearch(self):
        time.sleep(5)
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(ele) - 1
        return Count

    def countOfConnectedHDMI(self):
        time.sleep(2)
        ele_XPATH = "//tr//td[.='Connected']"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        connected_count = len(ele)
        return connected_count

    def UserCount(self):
        self.driver.refresh()
        self.driver.refresh()
        ele_XPATH = "//tr"
        ele = self.driver.find_elements(By.XPATH, ele_XPATH)
        uCount = len(ele) - 1
        return uCount
    
    def select_20_entries(self):
        self.select_option_by_value_from_dropdown("S_DROPDOWN_XPATH", "20")
        time.sleep(1)
        return DeliveryManagement(self.driver)

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "50")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "100")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    def select_200_entries(self):
        if env == "prod":
            self.select_option_by_text_from_dropdown("D_entries_XPATH", "100")
            time.sleep(2)
        elif env == "pre-prod":
            self.select_option_by_text_from_dropdown("D_entries_XPATH", "200")
            time.sleep(2)
        else:
            self.select_100_entries()
        return DeliveryManagement(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "500")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    def clickOnOnlineOfflineOpt(self):
        time.sleep(3)
        # self.click("D_Online_Offline_Option_XPATH")
        self.wait_for_visible("D_Online_Offline_Option_XPATH")
        more_options = self.find_element("D_Online_Offline_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def clickOnBaseOpt(self):
        time.sleep(2)
        self.wait_for_visible("D_Base_Option_XPATH")
        # more_options = self.find_element("D_Base_Option_XPATH")
        # self.driver.execute_script("arguments[0].click();", more_options)
        self.selenium_click("D_Base_Option_XPATH")
        # self.click("D_Base_Option_XPATH")
        return DeliveryManagement(self.driver)

    def clickOnStateOpt(self):
        time.sleep(1)
        self.wait_for_visible("D_State_Option_XPATH")
        more_options = self.find_element("D_State_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("D_State_Option_XPATH")
        return DeliveryManagement(self.driver)

    def clickOnCityOpt(self):
        time.sleep(3)
        self.wait_for_visible("D_City_Option_XPATH")
        more_options = self.find_element("D_City_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("D_City_Option_XPATH")
        return DeliveryManagement(self.driver)

    def clickOnDistrictOpt(self):
        time.sleep(2)
        self.wait_for_visible("D_District_Option_XPATH")
        # self.click("D_District_Option_XPATH")
        # self.wait_for_visible("D_City_Option_XPATH")
        more_options = self.find_element("D_District_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def clickOnPincodeOpt(self):
        time.sleep(2)
        # self.click("D_Pincode_Option_XPATH")
        self.wait_for_visible("D_Pincode_Option_XPATH")
        more_options = self.find_element("D_Pincode_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def clickOnOS_TypeOpt(self):
        time.sleep(3)
        # self.click("D_OS_Type_Option_XPATH")
        self.wait_for_visible("D_OS_Type_Option_XPATH")
        more_options = self.find_element("D_OS_Type_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def clickOnScheduleOpt(self):
        time.sleep(3)
        # self.click("D_Schedule_Option_XPATH")
        self.wait_for_visible("D_Schedule_Option_XPATH")
        more_options = self.find_element("D_Schedule_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def clickOnHDMIOpt(self):
        time.sleep(1)
        # self.click("D_CableDMStatus_XPATH")
        self.wait_for_visible("D_CableDMStatus_XPATH")
        more_options = self.find_element("D_CableDMStatus_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def clickOnTagWiseOpt(self):
        time.sleep(1)
        # self.click("D_TagWise_Option_XPATH")
        self.wait_for_visible("D_TagWise_Option_XPATH")
        more_options = self.find_element("D_TagWise_Option_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def nestedActiveListCount(self):
        time.sleep(5)
        eles = self.find_elements("D_current_activeOption_XPATH")
        count = len(eles)
        return count

    def isVisibleWithMinusSign_onlineOffline(self):
        return self.click("D_Online_Offline_Option_withMinusSign_XPATH")

    def verifyInDescendingOrder_name(self):
        time.sleep(4)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_name(self):
        time.sleep(4)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_Displayname(self):
        time.sleep(5)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_Displayname(self):
        time.sleep(5)
        userNames = []
        ele_XPATH = "//tr//td[4]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text.strip()
            userNames.append(userName)
            result = is_ascending(userNames)
            print(result)
        return result

    def verifydeliveryicontentenabled(self):
        time.sleep(5)
        self.wait_for_visible("D_FirstCheckbox_XPATH")
        # self.click("D_FirstCheckbox_XPATH")
        # self.wait_for_visible("D_DisplayNAME_Col_XPATH")
        more_options = self.find_element("D_FirstCheckbox_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible("D_SecondCheckbox_XPATH")
        more_options1 = self.find_element("D_SecondCheckbox_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options1)
        # self.click("D_SecondCheckbox_XPATH")
        # self.click("D_Deliver_icon_XPATH")
        self.wait_for_visible("D_Deliver_icon_XPATH")
        more_options2 = self.find_element("D_Deliver_icon_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options2)
        return DeliveryManagement(self.driver)

    def verifyreaddeliverycontent(self):
        self.wait_for_visible("D_Delivery_Text_XPATH")
        return self.getText("D_Delivery_Text_XPATH")

    def verifySyncbuttonenabled(self):
        time.sleep(4)
        self.wait_for_visible("D_FirstCheckbox_XPATH")
        more_options = self.find_element("D_FirstCheckbox_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible("D_SecondCheckbox_XPATH")
        more_options1 = self.find_element("D_SecondCheckbox_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options1)
        # self.click("D_FirstCheckbox_XPATH")
        # self.wait_for_visible("D_SecondCheckbox_XPATH")
        # self.click("D_SecondCheckbox_XPATH")
        self.wait_for_visible("D_Sync_icon_XPATH")
        more_options2 = self.find_element("D_Sync_icon_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options2)
        # self.click("D_Sync_icon_XPATH")
        return DeliveryManagement(self.driver)

    def readsynccontent(self):
        self.wait_for_visible("D_Sync_Text_CSS")
        return self.getText("D_Sync_Text_CSS")
        # self.wait_for_visible("D_Sync_Text_XPATH")
        # return self.getText("D_Sync_Text_XPATH")

    def verifyrebootbuttonenabled(self):
        time.sleep(4)
        # self.wait_for_visible("D_FirstCheckbox_XPATH")
        # self.click("D_FirstCheckbox_XPATH")
        # self.wait_for_visible("D_SecondCheckbox_XPATH")
        # self.click("D_SecondCheckbox_XPATH")
        self.wait_for_visible("D_FirstCheckbox_XPATH")
        more_options = self.find_element("D_FirstCheckbox_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible("D_SecondCheckbox_XPATH")
        more_options1 = self.find_element("D_SecondCheckbox_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options1)
        self.wait_for_visible("D_Reboot_icon_XPATH")
        more_options2 = self.find_element("D_Reboot_icon_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options2)

        # self.click("D_Reboot_icon_XPATH")
        return DeliveryManagement(self.driver)

    def readrebootcontent(self):
        self.wait_for_visible("D_Reboot_Text_XPATH")
        return self.getText("D_Reboot_Text_XPATH")

    def verifyOkbuttonvisible(self):
        time.sleep(5)
        self.wait_for_visible("D_OkButton_XPATH")
        ele_size = self.find_elements("D_OkButton_XPATH")
        return str(len(ele_size))

    def verifycrossbutonvisible(self):
        self.wait_for_visible("D_X_Icon_XPATH")
        time.sleep(2)
        ele_x_size = self.find_elements("D_X_Icon_XPATH")
        return str(len(ele_x_size))

    def verifycancelbutoonvisible(self):
        self.wait_for_visible("D_Cancel_button_XPATH")
        time.sleep(2)
        ele_c_size = self.find_elements("D_Cancel_button_XPATH")
        return str(len(ele_c_size))

    def clickOnDisplayID_Clm(self):
        self.click("D_DisplayID_Col_XPATH")
        return DeliveryManagement(self.driver)

    def clickOnDisplayNAME_Clm(self):
        time.sleep(4)
        # self.click("D_DisplayNAME_Col_XPATH")
        self.wait_for_visible("D_Displayname_asc_XPATH")
        # more_options = self.find_element("D_Displayname_asc_XPATH")
        # self.driver.execute_script("arguments[0].click();", more_options)
        self.selenium_click("D_Displayname_asc_XPATH")
        return DeliveryManagement(self.driver)

    def clickonDispnameDesc(self):
        self.wait_for_visible("D_Dispname_Desc_XPATH")
        more_options = self.find_element("D_Dispname_Desc_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("D_Dispname_Desc_XPATH")
        return DeliveryManagement(self.driver)
    def createScheduleemtpy(self):
        self.wait_for_visible("D_Plus_Schedule_XPATH")
        self.click("D_Plus_Schedule_XPATH")
        self.wait_for_visible("D_Scheduleentername_XPATH")
        self.click("D_Scheduleentername_XPATH")
        global Schedule_name
        Schedule_name = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(9))
        self.send_keys("D_Scheduleentername_XPATH", Schedule_name)
        self.click("D_AddSchedulebutton_XPATH")
        return DeliveryManagement(self.driver)

    def AssignScheduletodisplay(self):
        time.sleep(2)
        ele_XPATH = "//input[@role='searchbox']"
        self.driver.refresh()
        self.wait_for_visible("D_SEARCH_BAR_XPATH")
        self.click("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"{d_displayname}")
        time.sleep(2)
        self.click("D_FirstCheckbox_XPATH")
        self.click("D_Schedule_icon_XPATH")
        time.sleep(3)
        self.selenium_click("D_SelectScheduledropdown_XPATH")
        self.click("D_SearchSchedule_XPATH")
        self.send_keys("D_SearchSchedule_XPATH", f"{Schedule_name}")
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        time.sleep(3)
        self.click("D_deliverbutton_XPATH")
        time.sleep(1)
        return DeliveryManagement(self.driver)

    def searchdisplaycreated(self):
        self.driver.refresh()
        self.wait_for_visible("D_SEARCH_BAR_XPATH")
        self.click("D_SEARCH_BAR_XPATH")
        self.send_keys("D_SEARCH_BAR_XPATH", f"{d_displayname}")
        return DeliveryManagement(self.driver)

    def ScheduleofCreatedDisplay(self):
        global createdsch
        createdsch = self.getText("D_SearchedDisplay_Schedule_XPATH")
        return DeliveryManagement(self.driver)

    def verifyschedulename(self):
        self.is_visible("D_SearchedDisplay_Schedule_XPATH")
        if createdsch == Schedule_name:
            return True
        else:
            return False

    def clickOnfirstdisplay(self):
        time.sleep(3)
        self.click("D_FirstCheckbox_XPATH")
        return DeliveryManagement(self.driver)

    def verifyDelivericonIsDisable(self):
        ele1 = self.is_disable("D_Deliver_icon_XPATH")
        ele2 = self.is_disable("D_Sync_icon_XPATH")
        ele3 = self.is_disable("D_Reboot_icon_XPATH")
        ele4 = self.is_disable("D_Status_icon_XPATH")
        ele5 = self.is_disable("D_Schedule_icon_XPATH")
        print(ele1)
        print(type(ele1))
        if ele1 == "True" and ele2 == "True" and ele3 == "True" and ele4 == "True" and ele5 == "True":
            return True
        else:
            return False

    def verifyDelivericonIsEnable(self):
        time.sleep(1)
        ele1 = self.is_disable("D_Deliver_icon_XPATH")
        ele2 = self.is_disable("D_Sync_icon_XPATH")
        ele3 = self.is_disable("D_Reboot_icon_XPATH")
        ele4 = self.is_disable("D_Status_icon_XPATH")
        ele5 = self.is_disable("D_Schedule_icon_XPATH")
        if ele1 == "None" and ele2 == "None" and ele3 == "None" and ele4 == "None" and ele5 == "None":
            return True
        else:
            return False

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("D_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    def gotouseraccess(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return DeliveryManagement(self.driver)

    def createbaseuser(self):
        time.sleep(2)
        self.wait_for_visible("D_AddBase_Icon_XPATH")
        self.click("D_AddBase_Icon_XPATH")
        self.wait_for_visible("D_EnterBaseuserName_XPATH")
        self.click("D_EnterBaseuserName_XPATH")
        global D_baseusername
        D_baseusername = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("D_EnterBaseuserName_XPATH", D_baseusername)
        self.click("D_AddSchedulebutton_XPATH")
        return DeliveryManagement(self.driver)

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
        self.send_keys("D_SearchSchedule_XPATH", D_baseusername)
        time.sleep(3)
        self.driver.find_element(By.XPATH, ele_XPATH).send_keys(Keys.ENTER)
        self.wait_for_visible("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        return DeliveryManagement(self.driver)

    def gotodisplaysBase(self):
        time.sleep(2)
        self.wait_for_visible("MENU_CONTENT_XPATH")
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return DeliveryManagement(self.driver)

    def verifycreatedisplayBase(self):
        for i in range(1, 6):
            self.wait_for_visible("AddButton_Display_D_XPATH")
            self.click("AddButton_Display_D_XPATH")
            self.wait_for_visible("Display_name_D_XPATH")
            self.click("Display_name_D_XPATH")
            global d_displaynameb
            d_displaynameb = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
            self.send_keys("Display_name_D_XPATH", d_displaynameb)
            self.wait_for_visible("EnterPassword_Display_D_XPATH")
            self.click("EnterPassword_Display_D_XPATH")
            global p_pssdb
            p_pssdb = ''.join(secrets.choice('0123456789') for _ in range(6))
            self.send_keys("EnterPassword_Display_D_XPATH", p_pssdb)
            self.wait_for_visible("Confirm_Password_Display_D_XPATH")
            self.click("Confirm_Password_Display_D_XPATH")
            self.send_keys("Confirm_Password_Display_D_XPATH", p_pssdb)
            self.wait_for_visible_all_elements("Add_Display_D_XPATH")
            self.click("Add_Display_D_XPATH")
            time.sleep(2)
        return DeliveryManagement(self.driver)

    def DeleteCreatedDisplay(self):
        self.wait_for_visible("D_All_Display_base_XPATH")
        self.click("D_All_Display_base_XPATH")
        self.click("D_Three_Dots_base_XPATH")
        self.wait_for_visible("D_delete_completely_XPATH")
        self.click("D_delete_completely_XPATH")
        self.click("D_OkButton_XPATH")
        return DeliveryManagement(self.driver)

    def SwitchtoHeaduser(self):
        self.wait_for_visible("D_DropdownselectBaseUser_XPATH")
        retry_action(self.driver, By.XPATH, "//div[@class='dropdown text-light fw-bold pt-2']//div["
                                            "@id='dropdownMenuButton1']")
        self.wait_for_visible("D_HeadAcoount_XPATH")
        self.click("D_HeadAcoount_XPATH")
        return DeliveryManagement(self.driver)

    def deletecreatedbaseuser(self):
        self.wait_for_visible("D_Searchbaseuser_XPATH")
        self.click("D_Searchbaseuser_XPATH")
        self.send_keys("D_Searchbaseuser_XPATH", D_baseusername)
        time.sleep(2)
        self.wait_for_visible("D_Baseuser_threedot_XPATH")
        time.sleep(1)
        self.click("D_Baseuser_threedot_XPATH")
        time.sleep(1)
        self.click("D_Baseuser_Delete_XPATH")
        time.sleep(1)
        self.click("D_OkButton_XPATH")
        return DeliveryManagement(self.driver)

    def getCurrentAccount(self):
        time.sleep(3)
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

####added#######
    def clickonIPaddresssortingASC(self):
        self.wait_for_visible("D_SortascIP_XPATH")
        self.click("D_SortascIP_XPATH")
        return DeliveryManagement(self.driver)
    def clickonIPaddresssortingDSC(self):
        self.wait_for_visible("D_SortdscIP_XPATH")
        self.click("D_SortdscIP_XPATH")
        return DeliveryManagement(self.driver)

    def verifyInDescendingOrder_IPaddress(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[6]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        # Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_IPaddress(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[6]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickokdelivery(self):
        time.sleep(2)
        self.wait_for_visible("D_Ok_Content_XPATH")
        more_options = self.find_element("D_Ok_Content_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        return DeliveryManagement(self.driver)

    def gettextofdeliver(self):
        time.sleep(3)
        self.wait_for_visible("D_text_deliveryicon_XPATH")
        txt = self.getText("D_text_deliveryicon_XPATH")
        print(txt)
        if txt == "Schedule delivered successfully":
            assert True
        else:
            assert False
        return DeliveryManagement(self.driver)

    def gettextofsync(self):
        time.sleep(2)
        self.wait_for_visible("D_text_deliveryicon_XPATH")
        txt1 = self.getText("D_text_deliveryicon_XPATH")
        # print(txt)
        if txt1 == "Display Sync successfully":
            assert True
        else:
            assert False
        return DeliveryManagement(self.driver)

    def gettextofreboot(self):
        time.sleep(2)
        self.wait_for_visible("D_text_deliveryicon_XPATH")
        txt2 = self.getText("D_text_deliveryicon_XPATH")
        print(txt2)
        if txt2 == "Display Reboot successfully":
            assert True
        else:
            assert False
        return DeliveryManagement(self.driver)

    def createdisplay(self):
        self.clickOnAddNewDisplay()
        self.enterDisplayName()
        self.enterDisplayPassword()
        self.enterDisplayPassword_Conf()
        self.clickOnPopupAddBtn()
        time.sleep(2)
        self.refresh()
        return DeliveryManagement(self.driver)

    def clickOnAddNewDisplay(self):
        self.click("O_ADD_NEW_DISPLAY_BTN_XPATH")
        time.sleep(3)
        return DeliveryManagement(self.driver)

    def enterDisplayName(self):
        global r_Displayname
        r_Displayname = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(8))
        self.send_keys("O_DISPLAY_NAME_XPATH", r_Displayname)
        return DeliveryManagement(self.driver)

    def enterDisplayPassword(self):
        global r_pass
        r_pass = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8))
        self.send_keys("O_DISPLAY_PASSWORD_XPATH", r_pass)
        return DeliveryManagement(self.driver)

    def enterDisplayPassword_Conf(self):
        self.send_keys("O_DISPLAY_CONF_PASSWORD_XPATH", r_pass)
        return DeliveryManagement(self.driver)

    def clickOnPopupAddBtn(self):
        self.click("O_DISPLAY_POPUP_ADD_BTN_XPATH")
        return DeliveryManagement(self.driver)

    def gotoContentDisplays(self):
        time.sleep(5)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return DeliveryManagement(self.driver)
    def gotoContentContents(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return DeliveryManagement(self.driver)


    def gotoContentSchedules(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        return DeliveryManagement(self.driver)

    def addSchedule(self):
        time.sleep(2)
        self.wait_for_visible("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        more_options = self.find_element("S_ADD_NEW_SCHEDULE_PLUS_ICON_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.send_keys("S_SCHEDULE_NAME_INPUT_XPATH", schedule_name)
        self.click("S_ADD_BUTTON_NAME")
        return DeliveryManagement(self.driver)

    def searchDisplayNamecraetedinDM(self):
        time.sleep(2)
        self.send_keys("O_USER_MGT_SEARCHBAR_XPATH", f"{r_Displayname}")
        time.sleep(4)
        return DeliveryManagement(self.driver)
    
    def clickcreateddisplay(self):
        time.sleep(2)
        self.wait_for_visible("D_Firstdisplay_Checkbox_XPATH")
        self.click("D_Firstdisplay_Checkbox_XPATH")
        return DeliveryManagement(self.driver)

    def clickassignschedule(self):
        time.sleep(2)
        self.wait_for_visible("D_Schedule_icon_XPATH")
        self.click("D_Schedule_icon_XPATH")
        return DeliveryManagement(self.driver)

    def Assignschedule(self):
        time.sleep(2)
        self.wait_for_visible("S_BASE_DROPDOWN_XPATH")
        self.selenium_click("S_BASE_DROPDOWN_XPATH")
        time.sleep(2)
        self.selenium_click("D_Searchboxfield_schedule_Display_XPATH")
        time.sleep(1)
        self.send_keys("D_Searchboxfield_schedule_Display_XPATH", schedule_name)
        self.driver.find_element(By.XPATH,
                                 "//span[@class='select2-search select2-search--dropdown']//input[@role='searchbox']").send_keys(
            Keys.ENTER)
        self.selenium_click("D_Deliverschedulebutton_XPATH")
        return DeliveryManagement(self.driver)

    def readpopup(self):
        self.wait_for_visible("D_Popup_XPATH")
        rdd = self.getText("D_Popup_XPATH")
        time.sleep(2)
        print(rdd)
        if rdd == "Schedule delivered successfully ×":
            assert True
        else:
            assert False
        return DeliveryManagement(self.driver)

    def readschedulenamecolinDM(self):
        time.sleep(2)
        rd_sch = self.getText("D_Schedulesectionofdisplay_XPATH")
        time.sleep(2)
        print(rd_sch)
        print(schedule_name)
        if rd_sch == schedule_name:
            assert True
        else:
            assert False
        return DeliveryManagement(self.driver)

    def deleteCreatedDisplay(self):
        time.sleep(2)
        checkbox_XPATH = f"//td//a//span[contains(text(),'{r_Displayname}')]/preceding::input[@type='checkbox'][1]"
        self.driver.find_element(By.XPATH, checkbox_XPATH).click()
        more_options = self.find_element("O_DISPLAY_THREE_DOT_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.click("O_DELETE_COMPLETELY_XPATH")
        self.click("O_DISPLAY_POPUP_OK_BTN_XPATH")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    #############
    def createindividualdisp(self):
        self.wait_for_visible("AddButton_Display_D_XPATH")
        self.click("AddButton_Display_D_XPATH")
        self.wait_for_visible("Display_name_D_XPATH")
        self.click("Display_name_D_XPATH")
        global d_displaynameforvrify
        d_displaynameforvrify = ''.join(secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(6))
        self.send_keys("Display_name_D_XPATH", d_displaynameforvrify)
        self.wait_for_visible("EnterPassword_Display_D_XPATH")
        self.click("EnterPassword_Display_D_XPATH")
        #p_pssdbb = ''.join(secrets.choice('0123456789') for _ in range(6))
        self.send_keys("EnterPassword_Display_D_XPATH", "Test@357")
        self.wait_for_visible("Confirm_Password_Display_D_XPATH")
        self.click("Confirm_Password_Display_D_XPATH")
        self.send_keys("Confirm_Password_Display_D_XPATH", "Test@357")
        self.wait_for_visible_all_elements("Add_Display_D_XPATH")
        self.click("Add_Display_D_XPATH")
        time.sleep(2)
        return DeliveryManagement(self.driver)

    def textofsearchbar(self):
        time.sleep(2)
        return self.getText("D_SEARCH_BAR_XPATH")
    def searchcreateddisplay(self):
        time.sleep(2)
        self.send_keys("D_SEARCH_BAR_XPATH",d_displaynameforvrify)
        return DeliveryManagement(self.driver)

    def gettextofdisplayid(self):
        time.sleep(3)
        verifydis_id = self.getText("D_type_XPATH")
        return verifydis_id

    def textofdisplaynameinDM(self):
        time.sleep(3)
        tt = self.getText("D_DisplayState_emg_XPATH")
        return tt

    def textofdisplayname(self):
        time.sleep(3)
        tt = self.getText("D_Thirdrow_DisplayName_XPATH")
        return tt

    def CheckOfflineDisplay(self):
        self.wait_for_visible("D_Online_Offline_Option_XPATH")
        self.selenium_click("D_Online_Offline_Option_XPATH")
        self.wait_for_visible("N_OfflineDisplayFilterOption_XPATH")
        self.selenium_click("N_OfflineDisplayFilterOption_XPATH")
        time.sleep(5)
        entries = self.getText("N_TotalEntries_XPATH")
        totalcount = re.findall(r'of\s*(.*?)\s*entries', entries)
        return totalcount[0]

    def verifyDisplaySettings(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//span[@title='{r_Displayname}']").click()
        self.click("displaySettings_XPATH")
        r1 = len(self.find_elements("displaySettings_XPATH"))
        r2 = len(self.find_elements("settings_XPATH"))
        if r1+r2 == 2:
            return True
        else:
            return False

    def verifyRefreshBtn(self):
        time.sleep(2)
        row_count_before = len(self.find_elements("O_ROLE_MGT_Role_entries_Count_XPATH"))
        self.wait_for_visible_all_elements("SearchBar_D_XPATH")
        self.click("SearchBar_D_XPATH")
        self.send_keys("SearchBar_D_XPATH", r_Displayname)
        time.sleep(2)
        r = len(self.find_elements("O_ROLE_MGT_Role_entries_Count_XPATH"))
        if r == 1:
            self.click("refreshBtn_XPATH")
            time.sleep(2)
            row_count_after = len(self.find_elements("O_ROLE_MGT_Role_entries_Count_XPATH"))
            if row_count_before == row_count_after:
                return True
            else:
                return False
        else:
            return False

    def getOfflineDisplayCount(self):
        global offline_display
        offline_display = self.getText("S_OFFLINE_DISPLAY_XPATH")
        return offline_display

    def gotoDashboard_DM(self):
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/dashboard")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/dashboard")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/dashboard")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/dashboard")
        return DeliveryManagement(self.driver)

    def verifyLeftPanelList(self):
        if len(self.find_elements("leftPanelList_XPATH")) == 1:
            return True
        else:
            return False

    def selectAndReturn_OfflineDisplay(self):
        self.click("onlineDisplayOpt_XPATH")
        self.click("offlineDisplayOption_XPATH")
        time.sleep(1)
        return str(len(self.find_elements("O_ROLE_MGT_Role_entries_Count_XPATH")))
