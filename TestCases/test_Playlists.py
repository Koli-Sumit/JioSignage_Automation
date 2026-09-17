import time

import pytest
from pytest_check import check

from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
import logging
from Utilities.LogUtil import Logger
from utils.TC_Playlist import TC_Playlist

log = Logger(__name__, logging.INFO)
msg = "Are you sure you want to move the selected media to trash?" or "Are you sure want to move the selected playlist to trash?"


class TestPlaylists(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        home = HomePage(self.driver)
        home.goToPlaylist().switchToHead()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_verifyCreateNewPlaylist(self):
        log.logger.info(str(TC_Playlist(1)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCreatePlaylist()
        time.sleep(3)

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SANITY
    def test_verifyPlaylistWithAllChar(self):
        log.logger.info(str(TC_Playlist(2)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCreatePlaylistWitMaxChar()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifySpecCharInPlayName(self):
        log.logger.info(str(TC_Playlist(3)))
        home = HomePage(self.driver)
        msg = home.gotoContentPlaylists().verifyCreatePlaylistWitSpecChar()
        assert "Only letters, numbers, spaces and _ are allowed." in msg

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SANITY
    def test_verifyAddOptionOnCreatePlaylist(self):
        log.logger.info(str(TC_Playlist(4)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyAddOptionOnCreatePlaylist()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifyCancelOptionOnCreatePlaylist(self):
        log.logger.info(str(TC_Playlist(5)))
        home = HomePage(self.driver)
        assert "0" == home.gotoContentPlaylists().verifyCancelOptionOnCreatePlaylist()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifyCloseOptionOnCreatePlaylist(self):
        log.logger.info(str(TC_Playlist(6)))
        home = HomePage(self.driver)
        assert "0" == home.gotoContentPlaylists().verifyCloseOptionOnCreatePlaylist()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifyCreatedPlaylistDetail(self):
        log.logger.info(str(TC_Playlist(7)))
        home = HomePage(self.driver)
        with check:
            home.gotoContentPlaylists().verifyCreatedPlaylistDetail_Name()
        with check:
            assert "Root Folder" == home.goToPlaylist().verifyCreatedPlaylistDetail_Folder()
        with check:
            assert home.goToPlaylist().verifyCreatedPlaylistDetail_Detail() is not None
        with check:
            assert home.goToPlaylist().verifyCreatedPlaylistDetail_Preview() is not None
        with check:
            assert "0" == home.goToPlaylist().verifyCreatedPlaylistDetail_Count()
        with check:
            home.goToPlaylist().verifyCreatedPlaylistDetail_ModifiedBy()
        with check:
            assert home.goToPlaylist().verifyCreatedPlaylistDetail_ModifiedAt() is not None
        with check:
            home.goToPlaylist().verifyCreatedPlaylistDetail_Rename()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SMOKE
    def test_verifyRenamePlaylist(self):
        log.logger.info(str(TC_Playlist(8)))
        home = HomePage(self.driver)
        home.goToPlaylist().verifyRenamePlaylist()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SANITY
    def test_verifyUpdatePlaylistName(self):
        log.logger.info(str(TC_Playlist(9)))
        home = HomePage(self.driver)
        home.goToPlaylist().verifyUpdatePlaylistName()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifyCloseButtonOnEditPlaylist(self):
        log.logger.info(str(TC_Playlist(26)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCloseButtonOnEditPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyHeadFolder(self):
        log.logger.info(str(TC_Playlist(28)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyHeadFolder()
        home.gotoContentPlaylists().verifyFolderPath()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    @pytest.mark.SANITY
    def test_verifyTrashedPlaylist(self):
        log.logger.info(str(TC_Playlist(29)))
        home = HomePage(self.driver)
        with check:
            assert "1" == home.gotoContentPlaylists().verifyTrashedPlaylist()
        with check:
            home.gotoContentPlaylists().verifyCountTrashedPlaylist()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifySearchAfterTrash(self):
        log.logger.info(str(TC_Playlist(30)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().verifySearchAfterTrash()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifyCheckboxInTrashed(self):
        log.logger.info(str(TC_Playlist(31)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCheckboxInTrashed()

    @pytest.mark.FOCUSED
    def test_verifyMoreOptionsInTrashed(self):
        log.logger.info(str(TC_Playlist(32)))
        home = HomePage(self.driver)
        assert 2 == home.gotoContentPlaylists().verifyMoreOptionsInTrashed()

    @pytest.mark.FOCUSED
    def test_verifyRestorePlaylist(self):
        log.logger.info(str(TC_Playlist(33)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyRestorePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyOkButtonRestorePlaylist(self):
        log.logger.info(str(TC_Playlist(34)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyOkButtonRestorePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCancelButtonRestorePlaylist(self):
        log.logger.info(str(TC_Playlist(35)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCancelButtonRestorePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCloseButtonRestorePlaylist(self):
        log.logger.info(str(TC_Playlist(36)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCloseButtonRestorePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCompleteDeletePlaylist(self):
        log.logger.info(str(TC_Playlist(37)))
        home = HomePage(self.driver)
        assert "0" == home.gotoContentPlaylists().verifyCompleteDeletePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyOkButtonCompleteDeletePlaylist(self):
        log.logger.info(str(TC_Playlist(38)))
        home = HomePage(self.driver)
        assert "0" == home.gotoContentPlaylists().verifyOkButtonCompleteDeletePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCancelButtonCompleteDeletePlaylist(self):
        log.logger.info(str(TC_Playlist(39)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().verifyCancelButtonCompleteDeletePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCloseButtonCompleteDeletePlaylist(self):
        log.logger.info(str(TC_Playlist(40)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().verifyCloseButtonCompleteDeletePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyScrollInTrashedPlaylistPage(self):
        log.logger.info(str(TC_Playlist(42)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyScrollInTrashedPlaylistPage()

    @pytest.mark.FOCUSED
    def test_verifyTrashedPlaylistName(self):
        log.logger.info(str(TC_Playlist(47)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().verifyTrashedPlaylistName()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.DEMO
    def test_verifyFolderOfPlaylistInTrashed(self):
        log.logger.info(str(TC_Playlist(48)))
        home = HomePage(self.driver)
        r = home.gotoContentPlaylists().verifyFolderOfPlaylistInTrashed()
        if r == "Root Folder":
            assert True
        else:
            assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyModifyByAtTrashed(self):
        log.logger.info(str(TC_Playlist(50)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyModifyByAtTrashed()

    @pytest.mark.FOCUSED
    def test_verifyCreateFolderOSDForPlaylist(self):
        log.logger.info(str(TC_Playlist(52)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().verifyCreateFolderOSDForPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCreateFolderForPlaylist(self):
        log.logger.info(str(TC_Playlist(53)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCreateFolderForPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyPlayFolderWithSC(self):
        log.logger.info(str(TC_Playlist(54)))
        home = HomePage(self.driver)
        message = home.gotoContentPlaylists().verifyPlayFolderWithSC()
        assert "Only letters, numbers, spaces and _ are allowed." in message

    @pytest.mark.FOCUSED
    def test_verifyOkOptionOnCreateFolderForPlaylist(self):
        log.logger.info(str(TC_Playlist(55)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyOKOptionCreateFolderForPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCancelOptionOnCreateFolderForPlaylist(self):
        log.logger.info(str(TC_Playlist(56)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCancelOptionOnCreateFolderForPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnCreateFolderForPlaylist(self):
        log.logger.info(str(TC_Playlist(57)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyCloseOptionOnCreateFolderForPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyFolderInDropDownPlay(self):
        log.logger.info(str(TC_Playlist(58)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().CreateFolderForPlaylist().verifyFolderInDropDownPlay()

    @pytest.mark.FOCUSED
    def test_verifySearchFolderInDropDownPlay(self):
        log.logger.info(str(TC_Playlist(59)))
        home = HomePage(self.driver)
        assert "1" == home.gotoContentPlaylists().FolderForPlaylist().verifySearchFolderInDropDownPlay()

    @pytest.mark.FOCUSED
    def test_selectPlaylistFolderFromDropdownAndOpen(self):
        log.logger.info(str(TC_Playlist(60)))
        homepage = HomePage(self.driver)
        folder_names = homepage.gotoContentPlaylists().new_folder()
        se_fName = homepage.gotoContentPlaylists().selectFolderFromDropdownAndOpen()
        assert folder_names == se_fName

    @pytest.mark.FOCUSED
    def test_verifyPlaylistSearch(self):
        log.logger.info(str(TC_Playlist(61)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyPlaylistSearch()

    @pytest.mark.FOCUSED
    def test_verifyFilterSearchForPlaylist(self):
        log.logger.info(str(TC_Playlist(62)))
        homepage = HomePage(self.driver)
        assert 1 == homepage.gotoContentPlaylists().verifyFilterSearchForPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCheckOptionOnPlaylist(self):
        log.logger.info(str(TC_Playlist(63)))
        homepage = HomePage(self.driver)
        assert 1 == homepage.gotoContentPlaylists().verifyCheckOptionOnPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyMoreOptionsOnPlaylist(self):
        log.logger.info(str(TC_Playlist(64)))
        homepage = HomePage(self.driver)
        assert 2 == homepage.gotoContentPlaylists().verifyMoreOptionsOnPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyMovePlaylist(self):
        log.logger.info(str(TC_Playlist(65)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyMovePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyFolderOptionOnMovePlaylist(self):
        log.logger.info(str(TC_Playlist(66)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyFolderOptionOnMovePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnMovePlaylist(self):
        log.logger.info(str(TC_Playlist(67)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyCloseOptionOnMovePlaylist()

    @pytest.mark.FOCUSED
    def test_verifyMovePlaylistToFolder(self):
        log.logger.info(str(TC_Playlist(68)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyMovePlaylistToFolder()

    @pytest.mark.FOCUSED
    def test_verifyTrashOSDForPlaylist(self):
        log.logger.info(str(TC_Playlist(69)))
        homepage = HomePage(self.driver)
        assert homepage.gotoContentPlaylists().verifyTrashOSDForPlaylist() == "Are you sure you want to move the selected media to trash?" or "Are you sure want to move the selected playlist to trash?"
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyOkButtonOnTrashOSDForPlaylist(self):
        log.logger.info(str(TC_Playlist(70)))
        homepage = HomePage(self.driver)
        assert "1" == homepage.gotoContentPlaylists().verifyOkButtonOnTrashOSDForPlaylist()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyCancelButtonOnTrashOSDForPlaylist(self):
        log.logger.info(str(TC_Playlist(71)))
        homepage = HomePage(self.driver)
        # assert "No matching records found" == homepage.gotoContentPlaylists().verifyCancelButtonOnTrashOSDForPlaylist()
        # self.driver.refresh()
        # self.driver.refresh()
        #Change by Akash due to prod and preprod different data new code
        actual_text = homepage.gotoContentPlaylists().verifyCancelButtonOnTrashOSDForPlaylist()
        expected_messages = [
            "No matching records found",
            "No data available in table"
        ]
        assert actual_text in expected_messages
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_verifyCloseButtonOnTrashOSDForPlaylist(self):
        log.logger.info(str(TC_Playlist(72)))
        homepage = HomePage(self.driver)
        #assert "No matching records found" == homepage.gotoContentPlaylists().verifyCloseButtonOnTrashOSDForPlaylist()
        actual_text = homepage.gotoContentPlaylists().verifyCloseButtonOnTrashOSDForPlaylist()
        expected_messages = [
            "No matching records found",
            "No data available in table"
        ]
        assert actual_text in expected_messages

    @pytest.mark.FOCUSED
    def test_verifyCopyOptionOnPlaylist(self):
        log.logger.info(str(TC_Playlist(74)))
        homepage = HomePage(self.driver)
        copied_play = homepage.gotoContentPlaylists().verifyCopyOptionOnPlaylist()
        assert "2" == copied_play

    @pytest.mark.FOCUSED
    def test_verifyAllCharInCopyOptionOnPlaylist(self):
        log.logger.info(str(TC_Playlist(75)))
        homepage = HomePage(self.driver)
        copied_play = homepage.gotoContentPlaylists().verifyAllCharInCopyOptionOnPlaylist()
        assert "2" == copied_play

    @pytest.mark.FOCUSED
    def test_verifyAllSPCharInCopyOptionOnPlaylist(self):
        log.logger.info(str(TC_Playlist(76)))
        homepage = HomePage(self.driver)
        msg = homepage.gotoContentPlaylists().verifyAllSPCharInCopyOptionOnPlaylist()
        assert "Only letters, numbers, spaces and _ are allowed." in msg

    @pytest.mark.FOCUSED
    def test_verifySaveOptionOnCopyPlaylist(self):
        log.logger.info(str(TC_Playlist(77)))
        homepage = HomePage(self.driver)
        copied_play = homepage.gotoContentPlaylists().verifySaveOptionOnCopyPlaylist()
        assert "2" == copied_play

    @pytest.mark.FOCUSED
    def test_verifyCancelOptionOnCopyPlaylist(self):
        log.logger.info(str(TC_Playlist(78)))
        homepage = HomePage(self.driver)
        copied_play = homepage.gotoContentPlaylists().verifyCancelOptionOnCopyPlaylist()
        assert "1" == copied_play

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionOnCopyPlaylist(self):
        log.logger.info(str(TC_Playlist(79)))
        homepage = HomePage(self.driver)
        copied_play = homepage.gotoContentPlaylists().verifyCloseOptionOnCopyPlaylist()
        assert "1" == copied_play

    @pytest.mark.FOCUSED
    def test_verifyOpenPlaylist(self):
        log.logger.info(str(TC_Playlist(80)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyOpenPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyEditPlaylistDetail(self):
        log.logger.info(str(TC_Playlist(81)))
        homepage = HomePage(self.driver)
        homepage.gotoContentPlaylists().verifyEditPlaylistDetail()

    @pytest.mark.FOCUSED
    def test_verifyEnterAllCharInRename(self):
        log.logger.info(str(TC_Playlist(82)))
        homepage = HomePage(self.driver)
        assert "1" == homepage.gotoContentPlaylists().verifyEnterAllCharInRename()

    @pytest.mark.FOCUSED
    def test_verifyEnterSPAllCharInRename(self):
        log.logger.info(str(TC_Playlist(83)))
        homepage = HomePage(self.driver)
        message = homepage.gotoContentPlaylists().verifyEnterSPAllCharInRename()
        assert "Only letters, numbers, spaces and _ are allowed." in message

    @pytest.mark.FOCUSED
    def test_verifySaveOptionRename(self):
        log.logger.info(str(TC_Playlist(84)))
        homepage = HomePage(self.driver)
        assert "1" == homepage.gotoContentPlaylists().verifySaveOptionRename()

    @pytest.mark.FOCUSED
    def test_verifyCancelOptionRename(self):
        log.logger.info(str(TC_Playlist(85)))
        homepage = HomePage(self.driver)
        assert "0" == homepage.gotoContentPlaylists().verifyCancelOptionRename()

    @pytest.mark.FOCUSED
    def test_verifyCloseOptionRename(self):
        log.logger.info(str(TC_Playlist(86)))
        homepage = HomePage(self.driver)
        assert "0" == homepage.gotoContentPlaylists().verifyCloseOptionRename()

    @pytest.mark.FOCUSED
    def test_verifyModifyBy(self):
        log.logger.info(str(TC_Playlist(89)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyModifyBy()

    @pytest.mark.FOCUSED
    def test_verifyNextOptionOnPlaylist(self):
        log.logger.info(str(TC_Playlist(93)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyNextOptionOnPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyNumOfEntriesInTrashed(self):
        log.logger.info(str(TC_Playlist(43)))
        home = HomePage(self.driver)
        with check:
            assert home.gotoContentPlaylists().clickOnTrashed().get20Entries() <= 20
        with check:
            assert home.goToPlaylist().get50Entries() <= 50
        with check:
            assert home.goToPlaylist().get100Entries() <= 100
        # with check:
        #     assert home.goToPlaylist().get200Entries() <= 200
        # with check:
        #     assert home.goToPlaylist().get500Entries() <= 500

    @pytest.mark.FOCUSED
    def test_verifyScrollInPlaylistPage(self):
        log.logger.info(str(TC_Playlist(91)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().verifyScrollInPlaylistPage()

    @pytest.mark.FOCUSED
    def test_verifyPreviousOptionOnPlaylist(self):
        log.logger.info(str(TC_Playlist(94)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().createMultiplePlaylists().verifyPreviousOptionOnPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyNumOfEntriesInPlaylist(self):
        log.logger.info(str(TC_Playlist(92)))
        home = HomePage(self.driver)
        with check:
            assert home.gotoContentPlaylists().get20PlaylistEntries() <= 20
        with check:
            assert home.goToPlaylist().get50PlaylistEntries() <= 50
        with check:
            assert home.goToPlaylist().get100PlaylistEntries() <= 100
        # with check:
        #     assert home.goToPlaylist().get200PlaylistEntries() <= 200
        # with check:
        #     assert home.goToPlaylist().get500PlaylistEntries() <= 500


 #####additional#####
    @pytest.mark.FOCUSED
    def test_addplaylistwithspecialchar(self):
        log.logger.info(str(TC_Playlist(95)))
        with check:
            home = HomePage(self.driver)
            ele = home.gotoContentPlaylists().clikonaddContent()
            ele1 = ele.EnterPlaylistnamewithspecialchar()
            time.sleep(1)
            ele2 = ele.getinvalidtext()
            assert ele2
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_saveplaylist(self):
        log.logger.info(str(TC_Playlist(96)))
        with check:
            home = HomePage(self.driver)
            ele = home.gotoContentPlaylists().clikonaddContent()
            ele1 = ele.Enterplaylistname()
            time.sleep(3)
            # ele2= ele1.clickonSave()
            home.gotoContentPlaylists()
            ele2 = ele1.searchcreatedPlaylist()
            time.sleep(2)
            ele3 = ele2.gettextsearchedplaylist()

    @pytest.mark.FOCUSED
    def test_FilteronName(self):
        log.logger.info(str(TC_Playlist(97)))
        with check:
            home = HomePage(self.driver)
            ele = home.gotoContentPlaylists().clikonaddContent()
            ele1 = ele.Enterplaylistname()
            time.sleep(3)
            # ele2= ele1.clickonSave()
            home.gotoContentPlaylists()
            ele2 = ele1.clickonfilter().filteronname()
            if ele2 == 1:
                assert True
            else:
                assert False

    @pytest.mark.FOCUSED
    def test_checkboxclikable(self):
        log.logger.info(str(TC_Playlist(98)))
        with check:
            home = HomePage(self.driver)
            ele = home.gotoContentPlaylists().clikonaddContent()
            ele1 = ele.Enterplaylistname()
            time.sleep(3)
            # ele2= ele1.clickonSave()
            home.gotoContentPlaylists()
            ele2 = ele1.checkboxclikable()
            ele3 = ele2.verifymoreenabled()
            if ele3 == 'False':
                assert True
            else:
                assert False

    @pytest.mark.FOCUSED
    def test_verifyNextOptionInTrashedPlaylist(self):
        log.logger.info(str(TC_Playlist(44)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().createMultiplePlaylists().deletePlaylists()
        home.goToPlaylist().verifyNextOptionInTrashedPlaylist()

    @pytest.mark.FOCUSED
    def test_verifyPreviousOptionInTrashedPlaylist(self):
        log.logger.info(str(TC_Playlist(45)))
        home = HomePage(self.driver)
        home.gotoContentPlaylists().createMultiplePlaylists().deletePlaylists()
        self.driver.refresh()
        time.sleep(3)
        home.gotoContentPlaylists().verifyPreviousOptionInTrashedPlaylist()

#######################sanity###############################
    def test_createnormalandsmarplaylistsanity(self):
        self.driver.refresh()
        time.sleep(1)
        self.test_verifyCreateNewPlaylist()
        time.sleep(3)
        home = HomePage(self.driver)
        ele = home.gotoContentPlaylists().createsmartplaylist().searchcreatedsmartPlaylist()
        ele1 = ele.returntypeofplaylist()
        assert ele1 == "Smart Playlist"

    def test_previewPlaylist(self):
        home = HomePage(self.driver)
        ele = home.gotoContentPlaylists().createsmartplaylist().searchcreatedsmartPlaylist()
        ele1 = ele.clickonpreview()
        # print(ele1)
        assert ele1 == 1

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_createPlaylistWithImages(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterialsForPlaylist().deleteUploadedMedia_Image()
            ele.Uploadmedia1()
            ele.gotoContentContents_PlayPage().CreateLayoutWithBlankTemplateForImage1()
            ele.gotoContentPlaylists_Page().CreatePlaylistImage1()
            assert ele.verifyMultiSlide()
        self.driver.refresh()
        self.driver.refresh()
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_previewOfIndividualContentInCreatedPlaylist(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterialsForPlaylist().deleteUploadedMedia_Image()
            ele.Uploadmedia1()
            ele.gotoContentContents_PlayPage().CreateLayoutWithBlankTemplateForImage1()
            ele.gotoContentPlaylists_Page().CreatePlaylistImage1()
            assert ele.verifyPreview()
        self.driver.refresh()
        self.driver.refresh()
    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_deleteOfIndividualContentInCreatedPlaylist(self):
        self.driver.refresh()
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterialsForPlaylist().deleteUploadedMedia_Image()
            ele.Uploadmedia1()
            ele.gotoContentContents_PlayPage().CreateLayoutWithBlankTemplateForImage1()
            ele.gotoContentPlaylists_Page().CreatePlaylistImage1().deleteCreatedPlaylistContent()

            assert ele.verifyContentDeletedFromPlaylistPage()

            #assert ele.verifyContentDeletedFromPlaylistPage()
        self.driver.refresh()
        #self.driver.refresh()