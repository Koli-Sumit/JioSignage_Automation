import secrets
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


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


class RoleManagement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyRoleMgmtURL(self):
        return self.get_current_url()

    def getSubTitleOfRoleMgtPage(self):
        return self.getText("O_ROLE_MGT_AddDeleteModify_TEXT_XPATH")

    def isVisibleSearchBar(self):
        return self.is_visible("O_SEARCH_BAR_XPATH")

    def isVisibleAddNewRoleBtn(self):
        return self.is_visible("O_ROLE_MGT_ADD_ROLE_BTN_XPATH")

    def isVisibleNameClm(self):
        return self.is_visible("O_ROLE_MGT_NAME_COLUMN_XPATH")

    def isVisiblePermissionsClm(self):
        return self.is_visible("O_ROLE_MGT_PERMISSIONS_COLUMN_XPATH")

    def isVisibleUsersClm(self):
        return self.is_visible("O_ROLE_MGT_USERS_COLUMN_XPATH")

    def isVisibleActionClm(self):
        return self.is_visible("O_ROLE_MGT_ACTION_COLUMN_XPATH")

    def clickOnAddNewRoleBtn(self):
        self.click("O_ROLE_MGT_ADD_ROLE_BTN_XPATH")
        return RoleManagement(self.driver)

    def clickOnPopup_AddBtn(self):
        self.click("O_ROLE_MGT_POP_UP_ADD_BTN_XPATH")
        return RoleManagement(self.driver)

    def getPOPUP(self):
        time.sleep(2)
        ele = self.find_element("O_ROLE_MGT_Name_Textbox_XPATH")
        msg = ele.get_attribute("title")
        print(msg)

    def enterRoleName(self):
        global r_RoleName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4))
        r_RoleName = f"TR {r_text}"
        #edited_by_dixit
        self.send_keys("O_ROLE_MGT_Name_Textbox_XPATH", r_RoleName)
        return RoleManagement(self.driver)

    def editRoleName(self):
        self.clear("O_ROLE_MGT_Name_Textbox_XPATH")
        global r_RoleName_edit
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        r_RoleName_edit = f"Test Role {r_text}"
        self.send_keys("O_ROLE_MGT_Name_Textbox_XPATH", r_RoleName_edit)
        return RoleManagement(self.driver)

    def getTextFromWarnMsg(self):
        return self.getText("O_ROLE_MGT_ADD_ROLE_PAGE_WARN_MSG_XPATH")

    def addNewRole(self):
        self.clickOnAddNewRoleBtn()
        self.enterRoleName()
        self.clickOn_UserCheckbox()
        self.clickOnPopup_AddBtn()
        time.sleep(1)
        self.refresh()
        return RoleManagement(self.driver)

    def editRole(self):
        self.searchCreatedRole_byName()
        self.clickOnEditRole()
        self.editRoleName()
        self.clickOnPopup_AddBtn()
        time.sleep(1)
        self.refresh()
        return RoleManagement(self.driver)

    def getPermissions_CreatedRole(self):
        self.driver.refresh()
        self.driver.refresh()
        global role_permissions
        time.sleep(0.5)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_RoleName}")
        time.sleep(0.7)
        delete_BTN_XPATH = f"//tr//td[contains(.,'{r_RoleName}')]/following-sibling::td[1]"
        role_permissions = self.driver.find_element(By.XPATH, delete_BTN_XPATH).text
        return role_permissions

    def gotoUAUserMgmt_O(self):
        time.sleep(2)
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_UM_XPATH")
        time.sleep(1)
        return RoleManagement(self.driver)

    def gotoUARoleMgmt_O(self):
        time.sleep(5)
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_RM_XPATH")
        time.sleep(1)
        return RoleManagement(self.driver)

    def addNewUser_customUser(self):
        self.clickOnAddUser()
        self.enterUserName()
        self.enterEmailAddress()
        self.enterConfEmailAddress()
        self.enterPhoneNumber()
        self.selectCustomUser()
        self.selectLatestRole()
        self.clickOnPopup_AddBtn()
        time.sleep(2)
        return RoleManagement(self.driver)

    def clickOnAddUser(self):
        self.click("O_USER_MGT_ADD_USER_BTN_XPATH")
        return RoleManagement(self.driver)

    def enterUserName(self):
        global r_UserName
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(7))
        r_UserName = f"Test Account {r_text}"
        self.send_keys("O_USER_MGT_USER_NAME_TEXTBOX_XPATH", r_UserName)
        return RoleManagement(self.driver)

    def enterEmailAddress(self):
        global r_gmail
        r_text = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))
        r_gmail = f"{r_text}@auto.com"
        self.send_keys("O_USER_MGT_EMAIL_TEXTBOX_XPATH", r_gmail)
        return RoleManagement(self.driver)

    def enterConfEmailAddress(self):
        self.send_keys("O_USER_MGT_EMAIL_Conf_TEXTBOX_XPATH", r_gmail)
        return RoleManagement(self.driver)

    def enterPhoneNumber(self):
        time.sleep(1)
        global r_phoneNum
        r_phoneNum = ''.join(
            secrets.choice('1234567890') for _ in range(10))
        self.send_keys("O_PHONE_NUM_TEXTBOX_XPATH", r_phoneNum)
        return RoleManagement(self.driver)

    def selectCustomUser(self):
        self.click("O_USER_MGT_Custom_USER_XPATH")
        return RoleManagement(self.driver)

    def selectLatestRole(self):
        self.select_option_by_text_from_dropdown("O_ROLE_MGY_SELECT_ROLE_DROPDOWN_XPATH", f"{r_RoleName}")
        return RoleManagement(self.driver)

    def getPermissions_CreatedUsers_custom(self):
        global user_permissions
        time.sleep(3)
        delete_BTN_XPATH = f"//tr[1]//td[2]"
        user_permissions = self.driver.find_element(By.XPATH, delete_BTN_XPATH).text
        return user_permissions

    def clickOnPermissions_link(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(0.5)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_gmail}")
        time.sleep(1)
        delete_BTN_XPATH = f"//tr//td[normalize-space()='{r_gmail}']//following-sibling::td[2]//a"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        return RoleManagement(self.driver)

    def deleteCreatedUser(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(0.5)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_gmail}")
        time.sleep(1)
        delete_BTN_XPATH = f"//tr//td[normalize-space()='{r_gmail}']//following-sibling::td[4]//a[2]"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        self.click("O_USER_MGT_DELETE_POP_UP_OK_BTN_XPATH")
        time.sleep(3)
        return RoleManagement(self.driver)

    def deleteCreatedRole(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(0.5)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_RoleName}")
        time.sleep(1)
        delete_BTN_XPATH = f"//tr//td[contains(.,'{r_RoleName}')]/following-sibling::td[3]//div//a[2]"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        time.sleep(1)
        self.click("O_USER_MGT_DELETE_POP_UP_OK_BTN_XPATH")
        return RoleManagement(self.driver)

    def clickOnEditRole(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(2)
        self.searchCreatedRole_byName()
        delete_BTN_XPATH = f"//tr//td[contains(.,'{r_RoleName}')]/following-sibling::td[3]//div//a[1]"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        return RoleManagement(self.driver)

    def verifyEditedName(self):
        sam = ""
        ele_XPATH = f"//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        for name in names:
            name = name.text
            if name == r_RoleName_edit:
                sam = "True"
                break
            else:
                sam = "False"
        return sam

    def deleteEditedRole(self):
        self.driver.refresh()
        self.driver.refresh()
        time.sleep(0.5)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_RoleName_edit}")
        time.sleep(1)
        delete_BTN_XPATH = f"//tr//td[contains(.,'{r_RoleName_edit}')]/following-sibling::td[3]//div//a[2]"
        self.driver.find_element(By.XPATH, delete_BTN_XPATH).click()
        self.click("O_USER_MGT_DELETE_POP_UP_OK_BTN_XPATH")
        return RoleManagement(self.driver)

    def editPermission(self):
        self.clickOnEditRole()
        self.clickOn_UserCheckbox()
        self.clickOn_MaterialCheckbox()
        self.clickOnPopup_AddBtn()
        time.sleep(1)
        self.refresh()
        return RoleManagement(self.driver)

    def searchCreatedRole_byName(self):
        self.select_100_entries()
        time.sleep(2)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_RoleName}")
        time.sleep(2)
        return RoleManagement(self.driver)

    def searchCreatedRole_byPermission(self):
        self.send_keys("O_SEARCH_BAR_XPATH",
                       "View User, Create/Edit User, Edit/Update User, Delete User, Enable/Disable "
                       "User")
        time.sleep(2)
        return RoleManagement(self.driver)

    def getRowCount(self):
        ele_XPATH = "//tbody//tr"
        c = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(c)
        return c

    def verifyFirstRow_Name(self):
        ele_XPATH = "//tbody//tr[1]//td[1]"
        name = self.driver.find_element(By.XPATH, ele_XPATH).text
        if name == r_RoleName:
            return True
        else:
            return False

    def getCount_customPermission(self):
        self.select_100_entries()
        time.sleep(2)
        ele_XPATH = ("//td[contains(text(),'View User, Create/Edit User, Edit/Update User, Delete User, Enable/Disable "
                     "User')]")
        c = self.driver.find_elements(By.XPATH, ele_XPATH)
        c = len(c)
        return c

    def verify_searchByUser1(self):
        sam = ""
        r = ""
        self.select_100_entries()
        ele_XPATH = "//td[3]//a"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        for name in names:
            name = name.text
            if name == "1":
                sam = "True"
                break
            else:
                sam = "False"
        time.sleep(2)
        self.send_keys("O_SEARCH_BAR_XPATH", "1")
        time.sleep(3)
        if sam == "True":
            names = self.driver.find_elements(By.XPATH, ele_XPATH)
            for name in names:
                name = name.text
                if name == "1":
                    r = "True"
                    break
                else:
                    r = "False"
        else:
            time.sleep(1)
            if len(self.driver.find_elements(By.XPATH, "//td[@class='dataTables_empty']")) == 1:
                return "True"
            else:
                return "False"
        return r

    def verifyInDescendingOrder_name(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            # userName = userName.replace(" ", "")
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_name(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[1]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            # userName = userName.replace(" ", "")
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_permission(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            # userName = userName.replace(" ", "")
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_permission(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[2]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            # userName = userName.replace(" ", "")
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def verifyInDescendingOrder_user(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            # userName = userName.replace(" ", "")
            userNames.append(userName)
        result = is_descending(userNames)
        return result

    def verifyInAscendingOrder_user(self):
        time.sleep(2)
        userNames = []
        ele_XPATH = "//tr//td[3]"
        names = self.driver.find_elements(By.XPATH, ele_XPATH)
        Count = len(names)
        for name in names:
            userName = name.text
            # userName = userName.replace(" ", "")
            userNames.append(userName)
        result = is_ascending(userNames)
        return result

    def clickOnNameClm(self):
        self.click("O_USER_MGT_NAME_COLUMN_XPATH")
        return RoleManagement(self.driver)

    def clickOnPermissionClm(self):
        self.click("O_ROLE_MGT_PERMISSIONS_COLUMN_XPATH")
        return RoleManagement(self.driver)

    def clickOnUserClm(self):
        self.click("O_ROLE_MGT_USERS_COLUMN_XPATH")
        return RoleManagement(self.driver)

    def getRoleAccountsCount(self):
        accounts = self.find_elements("O_2ROLE_MGT_Role_entries_Count_XPATH")
        accounts = len(accounts)
        return accounts

    def select_50_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "50")
        time.sleep(2)
        return RoleManagement(self.driver)

    def select_100_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "100")
        time.sleep(2)
        return RoleManagement(self.driver)

    def select_200_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "200")
        time.sleep(2)
        return RoleManagement(self.driver)

    def select_500_entries(self):
        self.select_option_by_text_from_dropdown("O_ENTRIES_DROPDOWN_XPATH", "500")
        time.sleep(2)
        return RoleManagement(self.driver)

    def clickOn_UserCheckbox(self):
        self.click("O_ROLE_MGT_USER_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUserCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_USER_CHECKBOX_XPATH")
        return ele

    def clickOn_UserSub1_Checkbox(self):
        self.click("O_2ROLE_MGT_USER_ViewUser_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUser_Sub1_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_USER_ViewUser_CHECKBOX_XPATH")
        return ele

    def clickOn_UserSub2_Checkbox(self):
        self.click("O_2ROLE_MGT_USER_Create_EditUser_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUser_Sub2_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_USER_Create_EditUser_CHECKBOX_XPATH")
        return ele

    def clickOn_UserSub3_Checkbox(self):
        self.click("O_2ROLE_MGT_USER_Edit_UpdateUser_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUser_Sub3_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_USER_Edit_UpdateUser_CHECKBOX_XPATH")
        return ele

    def clickOn_UserSub4_Checkbox(self):
        self.click("O_2ROLE_MGT_USER_DeleteUser_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUser_Sub4_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_USER_DeleteUser_CHECKBOX_XPATH")
        return ele

    def clickOn_UserSub5_Checkbox(self):
        self.click("O_2ROLE_MGT_USER_Enable_Disable_User_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUser_Sub5_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_USER_Enable_Disable_User_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialCheckbox(self):
        self.click("O_ROLE_MGT_Material_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterialCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_Material_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialOpt1_Checkbox(self):
        self.click("O_2ROLE_MGT_Material_VM_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterial_Opt1_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Material_VM_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialOpt2_Checkbox(self):
        self.click("O_2ROLE_MGT_Material_UCE_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterial_Opt2_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Material_UCE_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialOpt3_Checkbox(self):
        self.click("O_2ROLE_MGT_Material_MC_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterial_Opt3_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Material_MC_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialOpt4_Checkbox(self):
        self.click("O_2ROLE_MGT_Material_MTT_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterial_Opt4_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Material_MTT_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialOpt5_Checkbox(self):
        self.click("O_2ROLE_MGT_Material_RM_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterial_Opt5_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Material_RM_CHECKBOX_XPATH")
        return ele

    def clickOn_MaterialOpt6_Checkbox(self):
        self.click("O_2ROLE_MGT_Material_DC_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfMaterial_Opt6_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Material_DC_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentCheckbox(self):
        self.click("O_ROLE_MGT_Content_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContentCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_Content_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt1_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt1_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt1_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt2_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt2_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt2_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt2_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt3_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt3_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt3_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt3_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt4_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt4_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt4_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt4_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt5_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt5_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt5_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt5_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt6_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt6_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt6_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt6_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt7_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt7_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt7_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt7_CHECKBOX_XPATH")
        return ele

    def clickOn_ContentOpt8_Checkbox(self):
        self.click("O_2ROLE_MGT_Content_Opt8_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfContent_Opt8_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Content_Opt8_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistCheckbox(self):
        self.click("O_ROLE_MGT_Playlist_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylistCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_Playlist_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistOpt1_Checkbox(self):
        self.click("O_2ROLE_MGT_Playlist_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylist_Opt1_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Playlist_Opt1_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistOpt2_Checkbox(self):
        self.click("O_2ROLE_MGT_Playlist_Opt2_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylist_Opt2_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Playlist_Opt2_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistOpt3_Checkbox(self):
        self.click("O_2ROLE_MGT_Playlist_Opt3_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylist_Opt3_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Playlist_Opt3_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistOpt4_Checkbox(self):
        self.click("O_2ROLE_MGT_Playlist_Opt4_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylist_Opt4_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Playlist_Opt4_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistOpt5_Checkbox(self):
        self.click("O_2ROLE_MGT_Playlist_Opt5_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylist_Opt5_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Playlist_Opt5_CHECKBOX_XPATH")
        return ele

    def clickOn_PlaylistOpt6_Checkbox(self):
        self.click("O_2ROLE_MGT_Playlist_Opt6_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlaylist_Opt6_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Playlist_Opt6_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleCheckbox(self):
        self.click("O_ROLE_MGT_Schedule_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfScheduleCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_Schedule_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleOpt1_Checkbox(self):
        self.click("O_2ROLE_MGT_Schedule_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfSchedule_Opt1_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Schedule_Opt1_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleOpt2_Checkbox(self):
        self.click("O_2ROLE_MGT_Schedule_Opt2_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfSchedule_Opt2_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Schedule_Opt2_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleOpt3_Checkbox(self):
        self.click("O_2ROLE_MGT_Schedule_Opt3_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfSchedule_Opt3_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Schedule_Opt3_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleOpt4_Checkbox(self):
        self.click("O_2ROLE_MGT_Schedule_Opt4_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfSchedule_Opt4_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Schedule_Opt4_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleOpt5_Checkbox(self):
        self.click("O_2ROLE_MGT_Schedule_Opt5_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfSchedule_Opt5_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Schedule_Opt5_CHECKBOX_XPATH")
        return ele

    def clickOn_ScheduleOpt6_Checkbox(self):
        self.click("O_2ROLE_MGT_Schedule_Opt6_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfSchedule_Opt6_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_Schedule_Opt6_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryCheckbox(self):
        self.click("O_ROLE_MGT_DisplayAndDelivery_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDeliveryCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_DisplayAndDelivery_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt1_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt1_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt1_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt2_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt2_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt2_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt2_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt3_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt3_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt3_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt3_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt4_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt4_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt4_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt4_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt5_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt5_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt5_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt5_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt6_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt6_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt6_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt6_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt7_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt7_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt7_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt7_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt8_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt8_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt8_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt8_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt9_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt9_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt9_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt9_CHECKBOX_XPATH")
        return ele

    def clickOn_DisplayAndDeliveryOpt10_Checkbox(self):
        self.click("O_2ROLE_MGT_DisplayAndDelivery_Opt10_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfDisplayAndDelivery_Opt10_Checkbox(self):
        ele = self.find_element("O_2ROLE_MGT_DisplayAndDelivery_Opt10_CHECKBOX_XPATH")
        return ele

    def clickOn_PlayLogCheckbox(self):
        self.click("O_ROLE_MGT_Play_log_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlayLogCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_Play_log_CHECKBOX_XPATH")
        return ele

    def clickOn_PlayLogOpt1_Checkbox(self):
        self.click("O_ROLE_MGT_Play_log_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfPlayLog_Opt1_Checkbox(self):
        ele = self.find_element("O_ROLE_MGT_Play_log_Opt1_CHECKBOX_XPATH")
        return ele

    def clickOn_UserActivityLogCheckbox(self):
        self.click("O_ROLE_MGT_UserActivityLog_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUserActivityLogCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_UserActivityLog_CHECKBOX_XPATH")
        return ele

    def clickOn_UserActivityLogOpt1_Checkbox(self):
        self.click("O_ROLE_MGT_UserActivityLog_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfUserActivityLog_Opt1_Checkbox(self):
        ele = self.find_element("O_ROLE_MGT_UserActivityLog_Opt1_CHECKBOX_XPATH")
        return ele

    def clickOn_EmergencyAlertLogCheckbox(self):
        self.click("O_ROLE_MGT_EmergencyAlert_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfEmergencyAlertLogCheckbox(self):
        ele = self.find_element("O_ROLE_MGT_EmergencyAlert_CHECKBOX_XPATH")
        return ele

    def clickOn_EmergencyAlertLogOpt1_Checkbox(self):
        self.click("O_ROLE_MGT_EmergencyAlert_Opt1_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def elementOfEmergencyAlertLog_Opt1_Checkbox(self):
        ele = self.find_element("O_ROLE_MGT_EmergencyAlert_Opt1_CHECKBOX_XPATH")
        return ele

####Sanity
    def clickOn_UserOptions(self):
        self.click("O_ROLE_MGT_USER_CHECKBOX_XPATH")
        return RoleManagement(self.driver)

    def verifyAddedRole(self):
        time.sleep(2)
        self.refresh()
        time.sleep(0.5)
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_RoleName}")
        time.sleep(1)
        addedRole_XPATH = f"//td//a[normalize-space()='{r_RoleName}']"
        ele = self.driver.find_elements(By.XPATH, addedRole_XPATH)
        ele = len(ele)
        return ele

    def verifyUserCountAssociatedWithRole(self):
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_RoleName}")
        user_XPATH = f"//tr//td[contains(.,'{r_RoleName}')]/following-sibling::td[2]//a"
        ele = self.driver.find_element(By.XPATH, user_XPATH).text
        return ele

    def clickOnPopup_AddBtn_O(self):
        self.click("O_ROLE_MGT_POP_UP_ADD_BTN_XPATH")

    def verifyRoleDeleted(self):
        if len(self.driver.find_elements(By.XPATH, f"//span[@title='{r_RoleName}']"))==0:
            return True
        else:
            return False

    def verifyCustomUser(self):
        self.send_keys("O_SEARCH_BAR_XPATH", f"{r_UserName}")
        time.sleep(1)
        if len(self.driver.find_elements(By.XPATH, f"//td[.='{r_UserName}']//following-sibling::td//a[.='Permissions']"))==1:
            return True
        else:
            return False
