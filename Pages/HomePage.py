import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BaseManagement import BaseManagement
from Pages.BasePage import BasePage, retry_action
from Pages.Content import Content
from Pages.ContentApproval import ContentApproval
from Pages.Dashboard import Dashboard
from Pages.DeliveryManagement import DeliveryManagement
from Pages.Displays import Displays
from Pages.EmergencyAlerts import EmergencyAlerts
from Pages.LoginProfile import LoginProfile
from Pages.Materials import Materials
from Pages.Playlists import Playlists
from Pages.PlaylogsReport import PlayLogsReport
from Pages.Reports import Reports
from Pages.RoleManagement import RoleManagement
from Pages.Schedules import Schedules
from Pages.UserActivitylogsReport import UserActivityLogsReport
from Pages.UserManagement import UserManagement
from Utilities import configReader
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    # Click on JioSignage Home icon
    def clickOnSignageHome(self):
        retry_action(self.driver, By.XPATH, "//img[@class='logo-icon']")
        # self.click("SIGNAGE_HOME_LOGO_XPATH")
        return HomePage(self.driver)

    # code change by shivaji

    def goToDash(self):
        return Dashboard(self.driver)

    # Code for navigate to Dashboard module
    ###change in code
    ###change in code 18 april
    def gotoDashboard(self):
        # retry_action(self.driver, By.XPATH, "//a[contains(.,'Dashboard')]")
        # time.sleep(3)
        # self.selenium_click("DASHBOARD_XPATH")
        # time.sleep(2)
        # return Dashboard(self.driver)

        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/dashboard")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/dashboard")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/dashboard")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/dashboard")
        return Dashboard(self.driver)

    def ClickDashboard(self):
        time.sleep(2)
        retry_action(self.driver, By.XPATH, "//a[contains(.,'Dashboard')]")
        # time.sleep(2)
        # self.selenium_click("DASHBOARD_XPATH")
        time.sleep(2)
        return Dashboard(self.driver)

    # Code for navigate to Content module
    def gotoContentMaterials(self):
        self.refresh()
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        return Materials(self.driver)

    def gotoContentMaterialsForContents(self):
        self.refresh()
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        return Content(self.driver)

    def gotoContentMaterialsForPlaylist(self):
        self.refresh()
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_MATERIALS_XPATH")
        return Playlists(self.driver)


    def gotoContentContents(self):
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/contents")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/contents")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/contents")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/contents")
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Content(self.driver)

    def gotoReports_UserActivityLogs(self):
        env = configReader.getTestData("TestData", "Environment")
        if env == "prod":
            self.driver.get("https://digitalsignage.jio.com/v2/activity_logs")
        elif env == "pre-prod":
            self.driver.get("https://preprod-jiosignage.jio.com/v2/activity_logs")
        elif env == "sit1":
            self.driver.get("https://sit1.jiosignage.jio.com/v2/activity_logs")
        elif env == "sit2":
            self.driver.get("https://sit2.jiosignage.jio.com/v2/activity_logs")
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Reports(self.driver)

    def gotocs(self):
        self.refresh()
        return Schedules(self.driver)

    def gotoContentSchedules(self):
        time.sleep(3)
        self.wait_for_visible_all_elements("MENU_CONTENT_XPATH")
        time.sleep(2)
        self.selenium_click("MENU_CONTENT_XPATH")
        self.wait_for_visible_all_elements("SUBMENU_SCHEDULE_XPATH")
        time.sleep(1)
        self.selenium_click("SUBMENU_SCHEDULE_XPATH")
        time.sleep(1)
        # if configReader.getTestData("TestData", "Environment") == "prod":
        #     self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        # elif configReader.getTestData("TestData", "Environment") == "pre-prod":
        #     self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        return Schedules(self.driver)

    def gotoContentDisplays(self):
        time.sleep(3)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        time.sleep(2)
        return Displays(self.driver)

    def gotoContentApproval(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENT_APPROVAL_XPATH")
        time.sleep(1)
        return ContentApproval(self.driver)

    def goToPlaylist(self):
        return Playlists(self.driver)

    def openSchedulePage(self):
        if configReader.getTestData("TestData", "Environment") == "prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_prod_url"))
        elif configReader.getTestData("TestData", "Environment") == "pre-prod":
            self.driver.get(configReader.getTestData("TestData", "total_schedules_preprod_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit1":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit1_url"))
        elif configReader.getTestData("TestData", "Environment") == "sit2":
            self.driver.get(configReader.getTestData("TestData", "all_content_sit2_url"))
        return Schedules(self.driver)


    def gotoContentPlaylists(self):
        self.wait_for_visible_all_elements("S_CONTENT_HEAD_XPATH")
        time.sleep(3)
        self.selenium_click("S_CONTENT_HEAD_XPATH")
        self.wait_for_visible_all_elements("SUBMENU_PLAYLIST_XPATH")
        self.selenium_click("SUBMENU_PLAYLIST_XPATH")
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
        return Playlists(self.driver)

    # Code for navigate to User access module
    def gotoUAUserMgmt(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_UM_XPATH")
        time.sleep(1)
        return UserManagement(self.driver)

    def gotoUABaseMgmt(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_BM_XPATH")
        time.sleep(1)
        return BaseManagement(self.driver)

    def gotoUARoleMgmt(self):
        self.hoverAndSelect("MENU_UA_XPATH", "SUBMENU_RM_XPATH")
        time.sleep(1)
        return RoleManagement(self.driver)

    # Code for navigate to Delivery management module
    def gotoDeliveryMgmt(self):
        time.sleep(5)
        self.click("MENU_DELIVERY_MGMT_XPATH")
        time.sleep(1)
        return DeliveryManagement(self.driver)
        # wait = WebDriverWait(self.driver, 10)
        #
        # wait.until(
        #     lambda driver: self.find_element("MENU_DELIVERY_MGMT_XPATH").is_displayed()
        # )
        # self.click("MENU_DELIVERY_MGMT_XPATH")
        # return DeliveryManagement(self.driver)

    # Code for navigate to Reports module
    def gotoReportsPlaylogs(self):
        self.hoverAndSelect("MENU_REPORTS_XPATH", "SUBMENU_PLAYLOGS_XPATH")
        self.wait_for_visible_all_elements("GENERATE_REPORT_XPATH")
        return PlayLogsReport(self.driver)

    def gotoReportsUserActivityLogs(self):
        self.hoverAndSelect("MENU_REPORTS_XPATH", "SUBMENU_USER_ACTIVITY_XPATH")
        self.wait_for_visible_all_elements("GENERATE_REPORT_XPATH")
        return UserActivityLogsReport(self.driver)

    # Code for navigate to Emergency alert module
    def gotoEmergencyAlerts(self):
        self.click("MENU_EA_XPATH")
        time.sleep(1)
        return EmergencyAlerts(self.driver)

    def verifySignageHome(self):
        self.click("SIGNAGE_HOME_LOGO_XPATH")
        return self.is_visible("SIGNAGE_HOME_LOGO_XPATH")

    def verifyWelcomeMsg(self):
        self.refresh()
        heading = self.getText("S_HEADING_XPATH")
        subheading = self.getText("S_SUBHEADING_XPATH")
        return heading + subheading

    def gotoSchedules(self):
        return Schedules(self.driver)

    # START############################OMKAR##############################################
    def goToSignInPage(self):
        self.driver.delete_all_cookies()
        self.driver.refresh()
        self.driver.refresh()
        return LoginProfile(self.driver)

    def O_clickOnViewProfile(self):
        time.sleep(2)
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_VIEW_PROFILE_XPATH")
        return LoginProfile(self.driver)

    def O_clickOnViewServicePlan(self):
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_VIEW_SERVICE_PLAN_XPATH")
        time.sleep(2)
        return LoginProfile(self.driver)

    def O_clickOnHelp(self):
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_HELP_XPATH")
        time.sleep(2)
        return LoginProfile(self.driver)

    def O_ClickOnLogout(self):
        self.driver.delete_all_cookies()
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_LOGOUT_XPATH")
        self.click("O_LOGOUT_OK_BTN_XPATH")
        self.refresh()
        time.sleep(2)
        return LoginProfile(self.driver)

    # END############################OMKAR##############################################

    ####Devanshu#########
    ####devanshu display#####
    def gotodisplays(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_DISPLAY_XPATH")
        return DeliveryManagement(self.driver)

    def gotoshedules_D(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_SCHEDULE_XPATH")
        return DeliveryManagement(self.driver)

    ###end###

    ###added##
    def gotoContentContents_S(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return Schedules(self.driver)

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

    def getCurrentAccount(self):
        time.sleep(1)
        return self.getText("S_CURRENT_ACCOUNT_TYPE_XPATH")
