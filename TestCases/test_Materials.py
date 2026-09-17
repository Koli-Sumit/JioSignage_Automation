import time
import logging

import allure
import pytest
from selenium.webdriver.common.by import By
from Pages.BasePage import retry_action
from pytest_check import check
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities import configReader
from Utilities.LogUtil import Logger
from utils.TC_Material import TC_Material

log = Logger(__name__, logging.INFO)

MATERIAL_COUNT_ZERO_TEXT = configReader.getTestData("TestData", "O_MATERIAL_COUNT_ZERO")
MAX_100_FILE_LIMIT_TEXT = configReader.getTestData("TestData", "O_MAX_100_FILE_LIMIT_TEXT")
WARN_MSG_Only_lettersNumbers = configReader.getTestData("TestData", "O_WARN_MSG_Only_lettersNumbers")

MATERIAL_PAGE_URL = configReader.getTestData("TestData", "O_MATERIAL_URL")
MATERIAL_PAGE_URL_PREPROD = configReader.getTestData("TestData", "O_MATERIAL_URL_PREPROD")
MATERIAL_PAGE_URL_SIT1 = configReader.getTestData("TestData", "image_content_sit1_url")
MATERIAL_PAGE_URL_SIT2 = configReader.getTestData("TestData", "image_content_sit2_url")

MATERIAL_PAGE_SHARED_URL = configReader.getTestData("TestData", "O_MATERIAL_SHARED_URL")
MATERIAL_PAGE_SHARED_URL_PREPROD = configReader.getTestData("TestData", "O_MATERIAL_SHARED_URL_PREPROD")
MATERIAL_PAGE_SHARED_URL_SIT1 = configReader.getTestData("TestData", "N_MATERIAL_SHARED_URL_SIT1")
MATERIAL_PAGE_SHARED_URL_SIT2 = configReader.getTestData("TestData", "N_MATERIAL_SHARED_URL_SIT2")

MATERIAL_PAGE_TRASHED_URL = configReader.getTestData("TestData", "O_MATERIAL_TRASHED_URL")
MATERIAL_PAGE_TRASHED_URL_PREPROD = configReader.getTestData("TestData", "O_MATERIAL_TRASHED_URL_PREPROD")
MATERIAL_PAGE_TRASHED_URL_SIT1 = configReader.getTestData("TestData", "N_MATERIAL_TRASHED_URL_SIT1")
MATERIAL_PAGE_TRASHED_URL_SIT2 = configReader.getTestData("TestData", "N_MATERIAL_TRASHED_URL_SIT2")


class TestMaterials(BaseTest):

    @pytest.fixture(autouse=True)
    def test_refreshBrowser(self):
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_materialPage_noDataUploaded(self):
        log.logger.info("TC" + str(TC_Material(1)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().createBaseAccount_SwitchToBaseUser().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            count_text = ele.getDataCountOfMaterialPage()
            assert count_text == MATERIAL_COUNT_ZERO_TEXT
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_addNewMaterial_OSD(self):
        log.logger.info("TC" + str(TC_Material(2)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().clickOnAddMaterialBtn()
            time.sleep(2)
            heading = ele.isVisibleUploadMaterialsHeading()
            if heading == "True":
                assert True
            else:
                assert False
        with check:
            maxSize = ele.isVisibleFileMaxSize()
            if maxSize == "True":
                assert True
            else:
                assert False
        with check:
            maxFiles = ele.isVisibleMaxFiles()
            if maxFiles == "True":
                assert True
            else:
                assert False
        with check:
            X_btn = ele.isVisibleUploadMaterials_X_BTN()
            if X_btn == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_addNewMaterial_clickOnBrowse(self):
        log.logger.info("TC" + str(TC_Material(4)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().uploadMaterial()
            c = ele.numberOfUploadedFiles()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_addNewMaterial_JPEG(self):
        log.logger.info("TC" + str(TC_Material(5)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_ImageFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_PNG(self):
        log.logger.info("TC" + str(TC_Material(6)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_PNG().clickOnUpload()
            self.driver.refresh()
            time.sleep(2)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_ImageFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_GIF(self):
        log.logger.info("TC" + str(TC_Material(7)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            # .createBaseAccount_SwitchToBaseUser().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_GIF().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_ImageFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_JFIF(self):
        log.logger.info("TC" + str(TC_Material(8)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JFIF().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_ImageFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_addNewMaterial_MP4(self):
        log.logger.info("TC" + str(TC_Material(9)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToVideo()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_MP4().clickOnUpload_forMP4()
            time.sleep(5)
            ele.changeTypeImageToVideo()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_VideoFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        print(before_count)
        print(after_count)
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_MOV(self):
        log.logger.info("TC" + str(TC_Material(10)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToVideo()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_MOV().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_VideoFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_Webm(self):
        log.logger.info("TC" + str(TC_Material(11)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToVideo()
            self.driver.refresh()
            time.sleep(3)# 1 to 3
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_WEBM().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(3) #1 to 3
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_VideoFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_MP3(self):
        log.logger.info("TC" + str(TC_Material(12)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToAudio()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_MP3().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_AudioFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_OGG(self):
        log.logger.info("TC" + str(TC_Material(13)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToAudio()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_OGG().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_AudioFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_WAV(self):
        log.logger.info("TC" + str(TC_Material(14)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToAudio()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_WAV().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_AudioFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    @pytest.mark.SANITY
    def test_addNewMaterial_PDF(self):
        log.logger.info("TC" + str(TC_Material(15)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToDocument()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_PDF().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_DOCFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_PPT(self):
        log.logger.info("TC" + str(TC_Material(16)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToDocument()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_PPT().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_DOCFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_PPTX(self):
        log.logger.info("TC" + str(TC_Material(17)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToDocument()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_PPTX().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_DOCFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_DOCX(self):
        log.logger.info("TC" + str(TC_Material(18)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele.changeTypeImageToDocument()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_DOCX().clickOnUpload_forMP4()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_DOCFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_OSD_X_BTN(self):
        log.logger.info("TC" + str(TC_Material(19)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().clickOnAddMaterialBtn()
            ele1 = ele.verify_addNewMaterial_OSD_X_BTN()
            if ele1 == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_SUPPORTED_FILES_text(self):
        log.logger.info("TC" + str(TC_Material(20)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().clickOnAddMaterialBtn()
            ele1 = ele.isVisibleUploadMaterialsSUPPORTED_FILES()
            if ele1 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_xxaddNewMaterial_deselectFile(self):
        with check:
            log.logger.info("TC" + str(TC_Material(24)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().uploadMaterial().clickOn_X_BTN_DESELECT_FILES()
            c = ele.numberOfUploadedFiles()
            if c == 0:
                assert True
            else:
                assert False
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_xaddNewMaterial_detailsOfSelectedFile(self):
        with check:
            log.logger.info("TC" + str(TC_Material(25)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().uploadMaterial().clickOn_I_BTN_SELECTED_FILE()
            nameOfFile = ele.getNameOfSelectedFile()
            sizeOfFile = ele.getSizeOfSelectedFile()
            typeOfFile = ele.getTypeOfSelectedFile()
            assert nameOfFile == "car.jpg"
        with check:
            assert sizeOfFile == "2.82 MB"
        with check:
            assert typeOfFile == "image/jpeg"
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_addNewMaterial_isValid(self):
        with check:
            log.logger.info("TC" + str(TC_Material(26)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().uploadMaterial()
            isValid = ele.isValid()
            assert isValid == "Valid"
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_yaddNewMaterial_deselectFile_moreThanOneFile(self):
        with check:
            log.logger.info("TC" + str(TC_Material(27)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage().uploadMaterial_10Files().clickOn_X_BTN_DESELECT_ALL_FILES()
            c = ele.numberOfUploadedFiles()
            if c == 0:
                assert True
            else:
                assert False
            self.driver.refresh()
            self.driver.refresh()

    # def test_addNewMaterial_1_99GB_FileSize(self):
    #     with check:
    # log.logger.info("TC" + str(TC_Material(28)))
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentMaterials()
    #         ele.changeTypeImageToDocument()
    #         self.driver.refresh()
    #         time.sleep(1)
    #         before_count = ele.getDataCountOfMaterialPage()
    #         before_count = before_count.split()[-2]
    #         before_count = int(before_count)
    #         ele2 = ele.uploadMaterial_1_99GB_SIZE().clickOnUpload_forMP4()
    #         time.sleep(5)
    #         self.driver.refresh()
    #         time.sleep(1)
    #         after_count = ele2.getDataCountOfMaterialPage()
    #         after_count = after_count.split()[-2]
    #         after_count = int(after_count)
    #         if after_count == before_count + 1:
    #             ele2.createdContentMoveToTrash()
    #             assert True
    #         else:
    #             assert False
    #     self.driver.refresh()
    #     self.driver.refresh()
    #
    # def test_addNewMaterial_2GB_FileSize(self):
    #     with check:
    #         log.logger.info("TC" + str(TC_Material(29)))
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentMaterials().uploadMaterial_2GB_SIZE()
    #         c = ele.numberOfUploadedFiles()
    #         if c == 1:
    #             assert True
    #         else:
    #             assert False
    #         self.driver.refresh()
    #         self.driver.refresh()
    #
    # def test_addNewMaterial_2_1GB_FileSize(self):
    #     with check:
    #         log.logger.info("TC" + str(TC_Material(30)))
    #         Home = HomePage(self.driver)
    #         ele = Home.gotoContentMaterials().uploadMaterial_2_1GB_SIZE()
    #         c = ele.numberOfUploadedFiles()
    #         if c == 1:
    #             assert True
    #         else:
    #             assert False
    #         self.driver.refresh()
    #         self.driver.refresh()
    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_addNewMaterial_isVisibleProgressBar(self):
        with check:
            log.logger.info("TC" + str(TC_Material(31)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG51().clickOnUpload_ForProgressBar()
            c = ele2.isVisibleProgressBar()
            if c == 1:
                assert True
            else:
                assert False
        with check:
            time.sleep(7)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                ele2.select_ImageFolderType().createdContentMoveToTrash()
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_MoveToTrashOSD(self):
        with check:
            log.logger.info("TC" + str(TC_Material(32)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG52().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.select_ImageFolderType().createdContentMoveToTrash_OSDisVisible()
                if result == 1:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.select_ImageFolderType().createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    @pytest.mark.SANITY
    def test_addNewMaterial_MoveToTrash_Functionality(self):
        with check:
            log.logger.info("TC" + str(TC_Material(33)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            ele2 = ele.uploadMaterial_JPEG53().clickOnUpload()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(2)
            before_count = ele2.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2.select_ImageFolderType().createdContentMoveToTrash_OG()
            time.sleep(2)
            self.driver.refresh()
            time.sleep(2)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            self.driver.refresh()
            time.sleep(2)
            if after_count == before_count - 1:
                assert True
            else:
                assert False
        with check:
            r = ele2.verifyFileInTrashFolder()
            r = str(r)
            if r == "True":
                assert True
            else:
                assert False
        ele2.createdContentMoveToTrash_fromTrashFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_MoveToTrashOSD_CancelBtn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(34)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG54().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.select_ImageFolderType().createdContentMoveToTrash_OSDisVisible_CancelBtn()
                if result == 0:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_MoveToTrashOSD_X_Btn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(35)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG55().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.select_ImageFolderType().createdContentMoveToTrash_OSDisVisible_X_Btn()
                if result == 0:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_MoveMaterial_OSD(self):
        with check:
            log.logger.info("TC" + str(TC_Material(35)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG56().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.select_ImageFolderType().MoveMaterial_OSD_isVisible()
                if result == 1:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_MoveMaterial_OSD_X_Btn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(38)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG57().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.select_ImageFolderType().createdContentMoveMaterial_OSD_isVisible_CancelBtn()
                if result == 0:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_search_byName(self):
        with check:
            log.logger.info("TC" + str(TC_Material(45)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG59().clickOnUpload()
            c = ele2.searchByName()
            if c == 1:
                assert True
            else:
                assert False
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_search_byName_filter(self):
        with check:
            log.logger.info("TC" + str(TC_Material(46)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG60().clickOnUpload()
            c = ele2.searchByName_filter()
            if c == 1:
                assert True
            else:
                assert False
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_createNewFolder_OSD(self):
        with check:
            log.logger.info("TC" + str(TC_Material(48)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.select_ImageFolderType().clickOnCreateFolderIcon()
            c = ele2.isVisibleCreateFolder_OSD()
            if c == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_Material_createNewFolder_enterAllCharacters(self):
        with check:
            log.logger.info("TC" + str(TC_Material(49)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.select_ImageFolderType().clickOnCreateFolderIcon().enterFolderName().clickOnAddBtn()
            r1 = ele2.verifyFolderIsCreated()
            if r1 == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_Material_CreateFolder_WarnMsg_SpecialCharacter(self):
        with check:
            log.logger.info("TC" + str(TC_Material(50)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.select_ImageFolderType().createNewFolder_SplChar()
            warnMsg = ele2.getTextFromWarningMsg()
            assert warnMsg == WARN_MSG_Only_lettersNumbers
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_createNewFolder(self):
        with check:
            log.logger.info("TC" + str(TC_Material(51)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.select_ImageFolderType().clickOnCreateFolderIcon().enterFolderName().clickOnAddBtn()
            r1 = ele2.verifyFolderIsCreated()
            if r1 == 1:
                assert True
            else:
                assert False
        with check:
            r2 = ele2.verifyFolderNameInDropdown()
            if r2 == 1:
                assert True
            else:
                assert False
        #ele.deleteCreatedFolder()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_CreateFolder_OSD_CancelBtn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(52)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.select_ImageFolderType().goToCreateFolderPage()
            result = ele2.isVisibleCreateFolderPopup()
            self.driver.refresh()
            if result == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_CreateFolder_OSD_X_Btn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(53)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.select_ImageFolderType().goToCreateFolderPage_X_BTN()
            result = ele2.isVisibleCreateFolderPopup()
            self.driver.refresh()
            if result == 0:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_HeadFolder(self):
        with check:
            log.logger.info("TC" + str(TC_Material(54)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.goToHeadFolder()
            time.sleep(2)
            url = ele2.get_current_url()
            if url == MATERIAL_PAGE_URL:
                assert url in MATERIAL_PAGE_URL
            elif url == MATERIAL_PAGE_URL_PREPROD:
                assert url in MATERIAL_PAGE_URL_PREPROD
            elif url == MATERIAL_PAGE_URL_SIT1:
                assert url in MATERIAL_PAGE_URL_SIT1
            elif url == MATERIAL_PAGE_URL_SIT2:
                assert url in MATERIAL_PAGE_URL_SIT2
            else:
                assert False
        with check:
            r = ele2.isVisibleTableHeadings()
            if r == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_SharedFolder(self):
        log.logger.info("TC" + str(TC_Material(55)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.goToSharedFolder()
            time.sleep(2)
            url = ele2.get_current_url()
            if url == MATERIAL_PAGE_SHARED_URL:
                assert url in MATERIAL_PAGE_SHARED_URL
            elif url == MATERIAL_PAGE_SHARED_URL_PREPROD:
                assert url in MATERIAL_PAGE_SHARED_URL_PREPROD
            elif url == MATERIAL_PAGE_SHARED_URL_SIT1:
                assert url in MATERIAL_PAGE_SHARED_URL_SIT1
            elif url == MATERIAL_PAGE_SHARED_URL_SIT2:
                assert url in MATERIAL_PAGE_SHARED_URL_SIT2
            else:
                assert False
        with check:
            r = ele2.isVisibleTableHeadings()
            if r == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_TrashedFolder(self):
        log.logger.info("TC" + str(TC_Material(56)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.goToTrashedFolder()
            time.sleep(2)
            url = ele2.get_current_url()
            if url == MATERIAL_PAGE_TRASHED_URL:
                assert url in MATERIAL_PAGE_TRASHED_URL
            elif url == MATERIAL_PAGE_TRASHED_URL_PREPROD:
                assert url in MATERIAL_PAGE_TRASHED_URL_PREPROD
            elif url == MATERIAL_PAGE_TRASHED_URL_SIT1:
                assert url in MATERIAL_PAGE_TRASHED_URL_SIT1
            elif url == MATERIAL_PAGE_TRASHED_URL_SIT2:
                assert url in MATERIAL_PAGE_TRASHED_URL_SIT2
            else:
                assert False
        with check:
            r = ele2.isVisibleTableHeadings()
            if r == 1:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()
        # ele.deleteCreatedBaseAccount_SwitchToHeadUser()

    @pytest.mark.FOCUSED
    @pytest.mark.SMOKE
    def test_Material_filter_image_video_audio_doc(self):
        log.logger.info("TC" + str(TC_Material(57)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            ele2 = ele.uploadMaterial_JPEG101().clickOnUpload()
            r1 = ele2.verifyImage101()
            if r1 == 1:
                assert True
            else:
                assert False
            ele2.select_ImageFolderType().createdContentMoveToTrash()
            time.sleep(5)
        with check:
            ele2.changeTypeImageToVideo()
            ele3 = ele2.uploadMaterial_MP4101().clickOnUpload_forMP4()
            r2 = ele3.verifyVideo101()
            if r2 == 1:
                assert True
            else:
                assert False
            ele3.select_VideoFolderType().createdContentMoveToTrash()
            time.sleep(5)
        with check:
            ele3.changeTypeImageToAudio()
            ele4 = ele3.uploadMaterial_MP3101().clickOnUpload_forMP4()
            r3 = ele4.verifyAudio101()
            if r3 == 1:
                assert True
            else:
                assert False
            ele4.select_AudioFolderType().createdContentMoveToTrash()
            time.sleep(5)
        with check:
            ele4.changeTypeImageToDocument()
            ele5 = ele4.uploadMaterial_PDF101().clickOnUpload_forMP4()
            r4 = ele5.verifyDoc101()
            if r4 == 1:
                assert True
            else:
                assert False
            ele5.select_DOCFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_Material_selectFolderFromDropdown(self):
        log.logger.info("TC" + str(TC_Material(58)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType().selectFirstFolderFromDropdown()
            time.sleep(2)
            result = ele.verifyFolderIsSelected()
            if result == 1:
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_preview(self):
        log.logger.info("TC" + str(TC_Material(59)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG_preview().clickOnUpload()
            self.driver.refresh()
            time.sleep(2)
            r = ele2.verify_Preview()
            if r == 1:
                assert True
            else:
                assert False
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_editMaterialName(self):
        log.logger.info("TC" + str(TC_Material(60)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG_editName().clickOnUpload()
            self.driver.refresh()
            time.sleep(2)
            r1 = ele2.verifyNameAlreadyExistToastMsg()
            r1 = str(r1)
            if r1 == "True":
                assert True
            else:
                assert False
        self.driver.refresh()
        with check:
            r2 = ele2.verifyEditedMaterialName()
            if r2 == 1:
                assert True
            else:
                assert False
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_preview_X_Btn(self):
        log.logger.info("TC" + str(TC_Material(61)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG_preview_X_Btn().clickOnUpload()
            self.driver.refresh()
            time.sleep(2)
            r = ele2.verify_PreviewPage_X_Btn()
            if r == 0:
                assert True
            else:
                assert False
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_thumbnail(self):
        log.logger.info("TC" + str(TC_Material(62)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            ele2 = ele.uploadMaterial_JPEG_thumbnail().clickOnUpload()
            self.driver.refresh()
            time.sleep(2)
            r = ele2.verify_thumbnail()
            if r == 1:
                assert True
            else:
                assert False
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_navigateToParticularFolder(self):
        log.logger.info("TC" + str(TC_Material(63)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            time.sleep(2)
            ele2 = ele.uploadMaterial_JPEG_folder().clickOnUpload().select_ImageFolderType().clickOnCreateFolderIcon().enterFolderName().clickOnAddBtn()
            time.sleep(3)
            ele2 = ele2.gotoContentMaterials_MaterialPage()
            result = ele2.select_ImageFolderType().verifyFolderMaterial()
            if result == 1:
                assert True
            else:
                assert False
        ele2.deleteCreatedFolder()
        ele2.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_editFolderName(self):
        log.logger.info("TC" + str(TC_Material(64)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType().selectFirstFolderFromDropdown()
            time.sleep(2)
            result = ele.editFolderName()
            if result == 1:
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_editFolderName_Cancel_Btn(self):
        log.logger.info("TC" + str(TC_Material(65)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType().selectFirstFolderFromDropdown()
            time.sleep(2)
            result = ele.editFolderName_CancelBtn()
            if result == 0:
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_FolderMoveToTrash_Close_Btn(self):
        log.logger.info("TC" + str(TC_Material(67)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType().selectFirstFolderFromDropdown()
            time.sleep(2)
            result = ele.folderMoveToTrash_CloseBtn()
            if result == 0:
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_selectFolderFromDropdown_BySearchBar(self):
        log.logger.info("TC" + str(TC_Material(68)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType().createNewFolder()
            self.driver.refresh()
            time.sleep(1)
            self.driver.refresh()
            self.driver.refresh()
            ele.selectFirstFolderFromDropdown_SearchBar()
            time.sleep(2)
            result = ele.verifyFolderIsSelected()
            if result == 1:
                assert True
            else:
                assert False
        ele.deleteCreatedFolder()
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_clickOnFolderNameFromDropdown(self):
        log.logger.info("TC" + str(TC_Material(69)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType().selectFirstFolderFromDropdown()
            time.sleep(2)
            result = ele.verifyFolderIsSelected()
            if result == 1:
                assert True
            else:
                assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_tableHeadings(self):
        log.logger.info("TC" + str(TC_Material(71)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            result = ele.verifyHeadings()
            print(result)
            if result == 9:
                assert True
            else:
                assert False
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_ALL_Option(self):
        log.logger.info("TC" + str(TC_Material(72)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            ele.uploadMaterial_10Files().clickOnUpload_for10files()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            count = count.split()[-4]
            before_count = int(before_count)
            count = int(count)
            ele2 = ele.select_ImageFolderType().verify_All_Option()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count - count:
                assert True
            else:
                assert False
            ele2.select_ImageFolderType().createdContentMoveToTrash_fromTrashFolder()
            ele2.switchToBaseUser_Previous()
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_verifyScroll_MaterialPage(self):
        log.logger.info("TC" + str(TC_Material(74)))
        homepage = HomePage(self.driver)
        ele = homepage.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
        ele.scroll()
        ele.switchToBaseUser_Previous()

    @pytest.mark.FOCUSED
    def test_MaterialPage_Checkbox_one_and_Multiple(self):
        log.logger.info("TC" + str(TC_Material(75)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            ele.uploadMaterial_10Files().clickOnUpload_for10files().select_ImageFolderType()
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.verify_1_Checkbox()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count - 1:
                assert True
            else:
                assert False
            self.driver.refresh()
        with check:
            time.sleep(1)
            self.driver.refresh()
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.verify_2_Checkboxes()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count - 2:
                assert True
            else:
                assert False
            self.driver.refresh()
            ele2.select_ImageFolderType().createdContentMoveToTrash_fromTrashFolder()
            ele2.switchToBaseUser_Previous()
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_SharedFolderPage_Checkbox_one_and_Multiple(self):
        log.logger.info("TC" + str(TC_Material(76)))
        with (check):
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            ele.uploadMaterial_10Files().clickOnUpload_for10files().select_ImageFolderType()
            ele.clickOnSharedFolderBtn()
            before_count = ele.getDataCountOfSharedPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.clickOnHEAD_OR_BASEBtn().verify_1_Checkbox_sharedFolder().clickOnSharedFolderBtn()
            time.sleep(1)
            after_count = ele2.getDataCountOfSharedPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                assert True
            else:
                assert False
        with check:
            before_count = ele.getDataCountOfSharedPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.clickOnHEAD_OR_BASEBtn().verify_2_Checkboxes_sharedFolder().clickOnSharedFolderBtn()
            time.sleep(1)
            after_count = ele2.getDataCountOfSharedPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 2:
                assert True
            else:
                assert False
            self.driver.refresh()
            ele2.restoreDeletedFilesForSharedFolder()
            ele2.select_ImageFolderType().createdContentMoveToTrash()
            ele2.switchToBaseUser_Previous()
            self.driver.refresh()
            self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_TrashPage_Checkbox_one_and_Multiple(self):
        log.logger.info("TC" + str(TC_Material(77)))
        with (check):
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            ele.uploadMaterial_10Files().clickOnUpload_for10files().select_ImageFolderType()
            ele.clickOnTrashBtn()
            before_count = ele.getDataCountOfTrashPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.clickOnHEAD_OR_BASEBtn().verify_1_Checkbox().clickOnTrashBtn()
            time.sleep(1)
            after_count = ele2.getDataCountOfTrashPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                assert True
            else:
                assert False
        with check:
            before_count = ele.getDataCountOfTrashPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.clickOnHEAD_OR_BASEBtn().verify_2_Checkboxes().clickOnTrashBtn()
            time.sleep(1)
            after_count = ele2.getDataCountOfTrashPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 2:
                assert True
            else:
                assert False
        self.driver.refresh()
        ele2.clickOnHEAD_OR_BASEBtn().restoreDeletedAllFiles()
        ele2.select_ImageFolderType().createdContentMoveToTrash()
        time.sleep(10)
        self.driver.refresh()
        ele2.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_Material_20_50_100_200_500_entries(self):
        log.logger.info("TC" + str(TC_Material(78)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            user20 = ele.UserCount()
            if user20 <= 20:
                assert True
            else:
                assert False
        with check:
            user50 = ele.select_50_entries().UserCount()
            if user50 <= 50:
                assert True
            else:
                assert False
        with check:
            user100 = ele.select_100_entries().UserCount()
            if user100 <= 100:
                assert True
            else:
                assert False
        with check:
            user10 = ele.select_10_entries().UserCount()
            if user10 <= 10:
                assert True
            else:
                assert False
        # with check:
        #     user500 = ele.select_500_entries().UserCount()
        #     if user500 <= 500:
        #         assert True
        #     else:
        #         assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_Material_show_entries(self):
        log.logger.info("TC" + str(TC_Material(79)))
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage()
            count = ele.getDataCountOfSharedPage()
            count = count.split()[-4]
            count = int(count)
            if count <= 20:
                assert True
            else:
                assert False
        with check:
            user50 = ele.select_50_entries()
            count = ele.getDataCountOfSharedPage()
            count = count.split()[-4]
            count = int(count)
            if count <= 50:
                assert True
            else:
                assert False
        with check:
            user100 = ele.select_100_entries()
            count = ele.getDataCountOfSharedPage()
            count = count.split()[-4]
            count = int(count)
            if count <= 100:
                assert True
            else:
                assert False
        with check:
            user10 = ele.select_10_entries()
            count = ele.getDataCountOfSharedPage()
            count = count.split()[-4]
            count = int(count)
            if count <= 10:
                assert True
            else:
                assert False
        # with check:
        #     user500 = ele.select_500_entries()
        #     count = ele.getDataCountOfSharedPage()
        #     count = count.split()[-4]
        #     count = int(count)
        #     if count <= 500:
        #         assert True
        #     else:
        #         assert False
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_verifyNextOptionOnMaterial(self):
        log.logger.info("TC" + str(TC_Material(80)))
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType()
            ele.uploadMaterial_10Files().clickOnUpload_for10files()
            ele.uploadMaterial_10Files_20().clickOnUpload_for10files()
            ele.uploadMaterial_10Files_30().clickOnUpload_for10files()
            sch_count = ele.select_10_entries().getScheduleCount()
            sch_cnt_next = ele.verifyNextOption()
            assert sch_count != sch_cnt_next
        ele.select_ImageFolderType().createdContentMoveToTrash()
        time.sleep(10)
        ele.select_ImageFolderType().createdContentMoveToTrash()
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()


    @pytest.mark.FOCUSED
    def test_verifyPreviousOptionOnMaterial(self):
        log.logger.info("TC" + str(TC_Material(81)))
        with check:
            homepage = HomePage(self.driver)
            ele = homepage.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType()
            ele.uploadMaterial_10Files().clickOnUpload_for10files()
            ele.uploadMaterial_10Files_20().clickOnUpload_for10files()
            ele.uploadMaterial_10Files_30().clickOnUpload_for10files()
            sch_count = ele.select_10_entries().moreSchedules()
            sch_cnt_back = ele.verifyPreviousOptionOnSchedule()
            assert sch_count != sch_cnt_back
        ele.createdContentMoveToTrash()
        time.sleep(10)
        ele.createdContentMoveToTrash()
        ele.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_xxCopyToShared_OSD(self):
        with check:
            log.logger.info("TC" + str(TC_Material(39)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG58().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.CopyToShared_OSD_isVisible()
                if result == 1:
                    self.driver.refresh()
                    time.sleep(5)# 2 to 5
                    ele2.select_ImageFolderType().createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
            ele2.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_CopyToShared_OSD_Cancel_Btn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(41)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG61().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.createdContentCopyToShared_OSD_isVisible_CancelBtn()
                if result == 0:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.select_ImageFolderType().createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
            ele2.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_CopyToShared_OSD_X_Btn(self):
        with check:
            log.logger.info("TC" + str(TC_Material(42)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_JPEG62().clickOnUpload()
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 1:
                result = ele2.createdContentCopyToShared_OSD_isVisible_X_Btn()
                if result == 0:
                    self.driver.refresh()
                    time.sleep(2)
                    ele2.select_ImageFolderType().createdContentMoveToTrash()
                    assert True
                else:
                    assert False
            else:
                assert False
            ele2.switchToBaseUser_Previous()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_99Files(self):
        Home = HomePage(self.driver)
        with check:
            log.logger.info("TC" + str(TC_Material(21)))
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(3)# 1 to 3
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_99Files().clickOnUpload_for100files()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 99:
                assert True
            else:
                assert False
        ele.select_ImageFolderType().AllContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.FOCUSED
    def test_addNewMaterial_100Files(self):
        with check:
            log.logger.info("TC" + str(TC_Material(22)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(1)
            before_count = ele.getDataCountOfMaterialPage()
            before_count = before_count.split()[-2]
            before_count = int(before_count)
            ele2 = ele.uploadMaterial_100Files().clickOnUpload_for100files()
            time.sleep(5)
            self.driver.refresh()
            time.sleep(1)
            after_count = ele2.getDataCountOfMaterialPage()
            after_count = after_count.split()[-2]
            after_count = int(after_count)
            if after_count == before_count + 100:
                assert True
            else:
                assert False
        ele.select_ImageFolderType().AllContentMoveToTrash()
        self.driver.refresh()
        self.driver.refresh()

    @pytest.mark.DEMO
    @pytest.mark.FOCUSED
    def test_addNewMaterial_101Files(self):
        with check:
            log.logger.info("TC" + str(TC_Material(23)))
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials().stayOnBaseAccount().gotoContentMaterials_MaterialPage()
            self.driver.refresh()
            time.sleep(5) #1 is replace to 5
            ele2 = ele.uploadMaterial_101Files()
            c1, c1text = ele2.length_getTextFromWarnPopup()
            if c1 == 1:
                # warn_msg = ele2.getTextFromWarnPopup()
                assert c1text == MAX_100_FILE_LIMIT_TEXT, f"error Pop up is mismatching"
            else:
                assert False, f"Maximum 100 file pop up is Missing or Not appearing"
        with check:
            self.driver.refresh()
            time.sleep(3)
            ele3 = ele2.uploadMaterial_100Files().uploadMaterial_1MoreFile()
            c2, c2text = ele3.length_getTextFromWarnPopup()
            if c2 == 1:
                # warn_msg = ele2.getTextFromWarnPopup()
                assert c2text == MAX_100_FILE_LIMIT_TEXT , f"error Pop up is mismatching"
            else:
                assert False, f"Maximum 100 file pop up is Missing or Not appearing"
        self.driver.refresh()
        self.driver.refresh()

    @allure.description("Verify able to upload media")
    @pytest.mark.SMOKE
    def test_UploadMedia(self):
        with check:
            Home = HomePage(self.driver)
            assert Home.gotoContentMaterials().Uploadmedia(), "Unable to upload media"

    @allure.description("Verify Delete > Restore and then permanent delete material")
    @pytest.mark.SMOKE
    def test_Trash_Restore_PermanentlyDel(self):
        Home = HomePage(self.driver)
        Home.gotoContentMaterials().Uploadmedia()
        with check:
            assert Home.gotoContentMaterials().DeleteMedia().VerifyMedia(), "Media not moved to trash page"
        with check:
            assert Home.gotoContentMaterials().RestoreMedia().VerifyMedia(), "Media not Restored"
        with check:
            assert Home.gotoContentMaterials().DeletePermanentlyMedia().VerifyMedia(), "Media not deleted permanently"

    @allure.description("Verify Create folder and upload material @ material module")
    @pytest.mark.SMOKE
    def test_CreateFolderAndUploadMedia(self):
        with check:
            Home = HomePage(self.driver)
            assert Home.gotoContentMaterials().CreateFolder(), "Folder Not Created or Folder Name is mismatched"
        with check:
            Home.gotoContentMaterials().UploadMediaInsideFolder(), "Unable to upload inside Folder"


    @allure.description("Verify material logs @ material module")
    @pytest.mark.SMOKE
    def test_VerifyMedialogs(self):
        Home = HomePage(self.driver)
        Home.gotoContentMaterials().Uploadmedia()
        Result = Home.gotoContentMaterials().MediaLogsOptions()
        assert Result == True, "Some element or options are mismatching in medialogs page"

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @allure.description("Verify user is able to move media file")
    @pytest.mark.SANITY
    def test_MoveMedia(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials()
            ele.Uploadmedia()
            ele.select_ImageFolderType().createNewFolder()
            Home.gotoContentMaterials().select_ImageFolderType().moveMedia()
            assert ele.verifyMoveMedia(), "Not able to move media"
        ele.select_ImageFolderType().createdContentMoveToTrashForCreatedMedia()

    @allure.description("Verify user is able to media to shared folder")
    @pytest.mark.SANITY
    @pytest.mark.FOCUSED
    def test_CopySharedFolder(self):
        with check:
            Home = HomePage(self.driver)
            time.sleep(1) # new changed
            ele = Home.gotoContentMaterials().SwitchToHeadUser().gotoContentMaterials_MaterialPage().select_ImageFolderType()
            ele.Uploadmedia()
            Home.gotoContentMaterials().select_ImageFolderType().copyToShared()
            assert ele.verifyCopiedMediaInSharedMedia(), "Not able to copy to shared folder"
        Home.gotoContentMaterials()
        ele.select_ImageFolderType().createdContentMoveToTrashForCreatedMedia()

    #added_to_detaled_tc_13_11_25
    @pytest.mark.FOCUSED
    @allure.description("Verify Create Playlist feature from Material section")
    @pytest.mark.SANITY
    def test_CreatePlaylistFromMediaPage(self):
        with check:
            Home = HomePage(self.driver)
            ele = Home.gotoContentMaterials()
            ele.Uploadmedia()
            Home.gotoContentMaterials().select_ImageFolderType().createPlaylistFromMedia()
            assert ele.verifyCreatePlaylist(), "Not able to create playlist from media page"
        Home.gotoContentMaterials()
        ele.select_ImageFolderType().createdContentMoveToTrashForCreatedMedia()