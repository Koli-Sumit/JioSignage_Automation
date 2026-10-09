import secrets
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage, retry_action
from datetime import datetime

global startdateplay
startdateplay = datetime.today().strftime('%d-%m-%Y')


class ContentApproval(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verifyContentApprovalURL(self):
        return self.get_current_url()

    def gotoContentContents(self):
        time.sleep(4)
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        return ContentApproval(self.driver)

    def clikonaddContent(self):
        # self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_CONTENTS_XPATH")
        self.wait_for_visible("D_Plus_Add_Content_XPATH")
        self.click("D_Plus_Add_Content_XPATH")
        return ContentApproval(self.driver)

    def EnterContentname(self):
        self.wait_for_visible("D_Contentname_CSS")
        self.click("D_Contentname_CSS")
        global content_name
        content_name = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("D_Contentname_CSS", content_name)
        self.click("D_Blank_XPATH")
        time.sleep(2)
        self.scroll_to_element("D_Add_Content_Submit_XPATH")
        self.click("D_Add_Content_Submit_XPATH")
        return ContentApproval(self.driver)

    def cancelcontentmessage(self):
        time.sleep(2)
        # self.wait_for_visible("D_Cancel_Content_Message_new_XPATH")
        # self.click("D_Cancel_Content_Message_new_XPATH")
        # time.sleep(1)
        self.wait_for_visible("D_Ok_Button_XPATH")
        self.click("D_Ok_Button_XPATH")
        contentApprovalMsgBox = self.find_elements("O_ContentApprovalMsgBox_X_Btn_XPATH")
        c = len(contentApprovalMsgBox)
        if c == 1:
            self.click("O_ContentApprovalMsgBox_X_Btn_XPATH")
        else:
            pass
        return ContentApproval(self.driver)

    def setDateContent(self):
        self.wait_for_visible("D_StartDate_ID")
        self.scroll_to_element("D_StartDate_ID")
        self.send_keys("D_StartDate_ID", "07-04-2024")
        self.scroll_to_element("D_EndDate_ID")
        self.send_keys("D_EndDate_ID", "08-04-2025")
        return ContentApproval(self.driver)

    def clickonRequestApproval(self):
        self.scroll_to_element("D_requestApproval_CSS")
        self.click("D_requestApproval_CSS")
        return ContentApproval(self.driver)

    def clickonSend(self):
        time.sleep(2)
        self.scroll_to_element("D_Sendkey_XPATH")
        # self.click("D_Sendkey_XPATH")
        self.wait_for_visible("D_Sendkey_new_XPATH")
        self.click("D_Sendkey_new_XPATH")
        # ele = self.find_element("D_Sendkey_XPATH")
        # self.driver.execute_script("arguments[0].click();", ele)
        return ContentApproval(self.driver)

    def verifyApprovaltext(self):
        time.sleep(2)
        self.wait_for_visible("D_approvaltext_XPATH")
        a = self.getText("D_approvaltext_XPATH")
        print(a)
        # self.click("D_Cancelpopup_XPATH")
        time.sleep(2)
        self.wait_for_visible("D_Cancel_Content_Message_new_XPATH")
        ele = self.find_element("D_Cancel_Content_Message_new_XPATH")
        self.driver.execute_script("arguments[0].click();", ele)
        # retry_action(self.driver, By.XPATH, "//div[@id='dijit_Dialog_16']//span[2]//span[@title='Cancel']")
        return a

    def clickcancelpopup(self):
        self.wait_for_visible("D_Cancelcross_XPATH")
        self.click("D_Cancelcross_XPATH")
        return ContentApproval(self.driver)

    def gotoPlaylist(self):
        self.hoverAndSelect("MENU_CONTENT_XPATH", "SUBMENU_PLAYLIST_XPATH")
        return ContentApproval(self.driver)

    def EnterPlaylistname(self):
        self.wait_for_visible("D_EnterPlaylistname_CSS")
        global Playlist_name
        Playlist_name = ''.join(
            secrets.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(6))
        self.send_keys("D_EnterPlaylistname_CSS", Playlist_name)
        self.click("D_AddPlaylist_XPATH")
        return ContentApproval(self.driver)

    def ClickRequestForApproval(self):
        self.wait_for_visible("D_requestforApproval_XPATH")
        self.click("D_requestforApproval_XPATH")
        return ContentApproval(self.driver)

    # def startdateforplaylist(self):
    #     global startdateplay
    #     startdateplay = datetime.today().strftime('%d-%m-%Y')
    #     return ContentApproval(self.driver)

    def EnterDetails(self):
        self.wait_for_visible("D_Searchuser_CSS")
        self.selenium_click("D_Searchuser_CSS")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(existusern)
        self.driver.find_element(By.XPATH, "//input[@role='searchbox']").send_keys(Keys.ENTER)
        time.sleep(1)
        self.send_keys("D_Playlist_StartDate_XPATH", startdateplay)
        time.sleep(1)
        self.send_keys("D_PlaylistEndDate_XPATH", "09-08-2025")
        time.sleep(1)
        self.click("D_AddPlaylist_XPATH")
        return ContentApproval(self.driver)

    def searchcreatedPlaylist(self):
        time.sleep(3)
        self.click("D_Search_Content_XPATH")
        self.send_keys("D_Search_Content_XPATH", Playlist_name)
        return ContentApproval(self.driver)

    def gettextsearchedplaylist(self):
        self.wait_for_visible("D_Searched_Content_XPATH")
        srct = self.getText("D_Searched_Content_XPATH")
        print(srct)
        if srct == Playlist_name:
            assert True
        else:
            assert False
        return srct

    def searchcreatedContent(self):
        time.sleep(2)
        self.click("D_Search_Content_XPATH")
        time.sleep(2)
        self.send_keys("D_Search_Content_XPATH", content_name)
        return ContentApproval(self.driver)

    def searchApprovedContent(self):
        return self.getText("D_NoRecords_XPATH")

    def SearchCreatedcontentinApprovedsection(self):
        time.sleep(1)
        a = self.getText("D_Searched_Content_XPATH")
        if content_name == a:
            assert True
        else:
            assert False
        return a

    def ApproveResponse(self):
        return self.is_visible("D_Approvetickmark_Response_XPATH")

    def conapproveresponse(self):
        return self.getText("D_Searched_Content_XPATH")

    def contentcreatedread(self):
        return self.getText("D_type_XPATH")

    def contentApprovalscreen(self):
        ele = self.find_elements("D_Pending_XPATH")
        ele = len(ele)
        return ele

    def readPending(self):
        return self.getText("D_Pending_XPATH")

    def readApproved(self):
        return self.getText("D_Approved_XPATH")

    def readRejected(self):
        return self.getText("D_RejectedIcon_XPATH")

    def searchcreatedcontent(self):
        self.wait_for_visible("D_Search_contentapproval_XPATH")
        self.send_keys("D_Search_contentapproval_XPATH", content_name)
        return ContentApproval(self.driver)

    def gettextofsearchedcontent(self):
        time.sleep(2)
        self.wait_for_visible("D_Searched_Content_XPATH")
        b = self.getText("D_Searched_Content_XPATH")
        if b == content_name:
            assert True
        else:
            assert False

    def gettextofmodifiedatContentsection(self):
        return self.getText("D_modifiedatcol_Content_XPATH")

    def gettextofmodifiedatContentapprovalsection(self):
        return self.getText("D_modifiedat_Contentapproval_XPATH")

    def getaccountname(self):
        return self.getText("D_accountname_XPATH")

    def getcompanynamecontentapproval(self):
        return self.getText("D_CompanynameContentapproval_XPATH")

    def gettextfromrequester(self):
        time.sleep(2)
        return self.getText("D_Requestername_Dropdown_new_XPATH")

    def gettextfromContentApprovalRequester(self):
        return self.getText("D_Requestername_Contentapproval_XPATH")

    def setExpiryDateContent(self):
        self.wait_for_visible("D_StartDate_ID")
        self.scroll_to_element("D_StartDate_ID")
        self.send_keys("D_StartDate_ID", "05-04-2024")
        self.scroll_to_element("D_EndDate_ID")
        self.send_keys("D_EndDate_ID", "08-04-2024")
        return ContentApproval(self.driver)

    def gettextEnddate(self):
        return self.getText("D_EndDate_ID")

    def getcontentapprovalEnddate(self):
        return self.getText("D_EndDate_contentapproval_XPATH")

    def getcontentapprovalstartdate(self):
        return self.getText("D_StartDate_Contentapproval_XPATH")

    def getlengthexpired(self):
        self.wait_for_visible("D_Expired_redysymbol_XPATH")
        a = print(len("D_Expired_redysymbol_XPATH"))
        return a

    def gettexttypecontentapproval(self):
        return self.getText("D_type_XPATH")

    def identifyapprovesymbolvisible(self):
        return self.is_visible("D_Approve_Symbol_XPATH")

    def identifyrejectsymbolvisible(self):
        return self.is_visible("D_Cancel_Symbol_XPATH")

    def identifypreviewsymbolvisible(self):
        return self.is_visible("D_PreviewSymbol_XPATH")

    def identifyExpiredcontent(self):
        ele = self.find_elements("D_Red_XPATH")
        ele1 = len(ele)
        return ele1

    def identifyGreencontent(self):
        ele = self.find_elements("D_Green_XPATH")
        ele1 = len(ele)
        return ele1

    def approvepopup(self):
        self.click("D_Approve_Symbol_XPATH")
        self.wait_for_visible("D_AddPlaylist_XPATH")
        self.click("D_AddPlaylist_XPATH")
        return ContentApproval(self.driver)

    def verifyapprovepopuptext(self):
        return self.getText("D_Approvepopup_XPATH")

    def verifyrejectpopup(self):
        self.click("D_Cancel_Symbol_XPATH")
        self.wait_for_visible("D_ReasonForReject_CSS")
        self.send_keys("D_ReasonForReject_CSS", "error")
        self.click("D_AddPlaylist_XPATH")
        return self.getText("D_Approvepopup_XPATH")

    def verifypreviewtext(self):
        self.click("D_PreviewSymbol_XPATH")
        self.wait_for_visible("D_Preview_text_XPATH")
        # previ=self.find_element("D_Preview_text_XPATH").get_attribute('value')
        time.sleep(2)
        pr = print(self.getText("D_Preview_text_XPATH"))
        return self.getText("D_Preview_text_XPATH")

    def gotoApprovedSection(self):
        self.wait_for_visible("D_Approvedsection_XPATH")
        self.click("D_Approvedsection_XPATH")
        return ContentApproval(self.driver)

    def gotoRejectedsection(self):
        self.wait_for_visible("D_Rejectsection_XPATH")
        self.click("D_Rejectsection_XPATH")
        return ContentApproval(self.driver)

    def readreasonOfrejected(self):
        self.wait_for_visible("D_modifiedatcol_Content_XPATH")
        a = self.getText("D_modifiedatcol_Content_XPATH")
        if a == 'error':
            assert True
        else:
            assert False
        return a

    def deletecreatedcontent(self):
        self.wait_for_visible("D_Searched_Content_XPATH")
        self.click("D_Searched_Content_XPATH")
        self.click("D_threedots_content_XPATH")
        self.wait_for_visible("D_Movetotrash_XPATH")
        self.click("D_Movetotrash_XPATH")
        time.sleep(1)
        self.wait_for_visible("D_Ok_Content_XPATH")
        self.click("D_Ok_Content_XPATH")
        return ContentApproval(self.driver)

    def deleteAllContents(self):
        self.wait_for_visible("D_SelectAll_Contents_XPATH")
        more_options1 = self.find_element("D_SelectAll_Contents_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options1)
        self.click("D_SelectAll_Contents_XPATH")
        time.sleep(2)
        self.wait_for_visible("D_threedots_content_XPATH")
        more_options = self.find_element("D_threedots_content_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible("D_Movetotrash_XPATH")
        self.click("D_Movetotrash_XPATH")
        self.wait_for_visible("D_Ok_Content_XPATH")
        self.click("D_Ok_Content_XPATH")
        return ContentApproval(self.driver)

    def select_200_entries(self):
        time.sleep(1)
        self.select_option_by_text_from_dropdown("D_entries_XPATH", "200")
        time.sleep(2)
        return ContentApproval(self.driver)

    def gototrash(self):
        self.wait_for_visible("D_SelectTrash_XPATH")
        self.click("D_SelectTrash_XPATH")
        return ContentApproval(self.driver)

    def cleartrash(self):
        time.sleep(1)
        self.scroll_to_element("D_Search_Content_XPATH")
        time.sleep(1)
        self.scroll_to_element("D_Search_Content_XPATH")
        self.wait_for_visible("D_SelectAll_Contents_XPATH")
        more_options = self.find_element("D_SelectAll_Contents_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        # self.click("D_SelectAll_Contents_XPATH")
        time.sleep(2)
        self.wait_for_visible("D_threedots_content_XPATH")
        more_options = self.find_element("D_threedots_content_XPATH")
        self.driver.execute_script("arguments[0].click();", more_options)
        self.wait_for_visible("D_DeleteCompletelytrash_XPATH")
        self.click("D_DeleteCompletelytrash_XPATH")
        self.click("D_Ok_Content_XPATH")
        return ContentApproval(self.driver)

    def readprofileusername(self):
        time.sleep(2)
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_VIEW_PROFILE_XPATH")
        time.sleep(2)
        edit = self.find_element("O_EDIT_UNAME_BTN_XPATH")
        self.driver.execute_script("arguments[0].click();", edit)
        self.wait_for_visible("O_USER_NAME_TEXTBOX_XPATH")
        global existusern
        existusern = self.find_element("O_USER_NAME_TEXTBOX_XPATH").get_attribute('value')
        return ContentApproval(self.driver)

    def selectuserforapproval(self):
        time.sleep(3)
        self.wait_for_visible("D_Usernamebox_CA_XPATH")
        self.click("D_Usernamebox_CA_XPATH")
        self.send_keys("D_Usernamebox_CA_XPATH", existusern)
        # self.driver.find_element(By.XPATH,"//input[@id='user_list']").send_keys(Keys.ENTER)
        return ContentApproval(self.driver)

    def getprofileusernameusername(self):
        time.sleep(2)
        self.click("O_PROFILE_ICON_XPATH")
        self.click("O_VIEW_PROFILE_XPATH")
        time.sleep(2)
        edit = self.find_element("O_EDIT_UNAME_BTN_XPATH")
        self.driver.execute_script("arguments[0].click();", edit)
        self.wait_for_visible("O_USER_NAME_TEXTBOX_XPATH")
        global existusernforrd
        existusernforrd = self.find_element("O_USER_NAME_TEXTBOX_XPATH").get_attribute('value')
        return existusernforrd

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
