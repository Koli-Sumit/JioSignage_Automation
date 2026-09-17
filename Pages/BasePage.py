import logging
import time
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import random
import string
from Utilities import configReader
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


def retry_action(driver, by, value, max_retries=5):
    for _ in range(max_retries):
        try:
            element = driver.find_element(by, value)
            driver.execute_script("arguments[0].click();", element)
            # element.click()
            return element
        except StaleElementReferenceException:
            time.sleep(2)  # You may adjust the sleep duration
    raise StaleElementReferenceException("Failed after multiple retries")


def getTextAfterRetry(driver, by, value, max_retries=5):
    for _ in range(max_retries):
        try:
            element = driver.find_element(by, value)
            return element.text
        except StaleElementReferenceException:
            time.sleep(2)  # You may adjust the sleep duration
    raise StaleElementReferenceException("Failed after multiple retries")


def generate_random_string(length):
    characters = string.ascii_letters  # includes both uppercase and lowercase letters
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def generate_unique_string(length):
    if length > 26:
        raise ValueError("Length exceeds the number of available characters (26)")
    unique_chars = random.sample('abcdefghijklmnopqrstuvwxyz', length)
    unique_string = ''.join(unique_chars)
    return unique_string


def generate_random_number(N):
    minimum = pow(10, N - 1)
    maximum = pow(10, N) - 1
    return random.randint(minimum, maximum)


def image_to_pdf(image_path, pdf_path):
    image = Image.open(image_path)
    width, height = image.size
    pdf = canvas.Canvas(pdf_path, pagesize=letter)
    pdf.drawInlineImage(image_path, 0, 0, width=letter[0], height=letter[1])
    pdf.save()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def send_keys(self, locator, value):
        self.wait_for_visible_all_elements(locator)
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).send_keys(value)
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).send_keys(value)
        elif str(locator).endswith("_LINKTEXT"):
            self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator)).send_keys(
                value)
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                     configReader.getLocator("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CLASSNAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.getLocator("locators", locator)).send_keys(value)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.getLocator("locators", locator)).send_keys(value)
        log.logger.info("Typed in to an Element : " + str(locator) + " Value : " + value)

    def clear(self, locator):
        self.wait_for_visible_all_elements(locator)
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator)).clear()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).clear()
        elif str(locator).endswith("_NAME"):
            self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).clear()
        elif str(locator).endswith("_LINKTEXT"):
            self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator)).clear()
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                     configReader.getLocator("locators", locator)).clear()
        elif str(locator).endswith("_CLASSNAME"):
            self.driver.find_element(By.CLASS_NAME, configReader.getLocator("locators", locator)).clear()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, configReader.getLocator("locators", locator)).clear()
        log.logger.info("Clear data from locator : " + locator)

    def find_elements(self, locator):
        elements = []
        if str(locator).endswith("_XPATH"):
            elements = self.driver.find_elements(By.XPATH, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_ID"):
            elements = self.driver.find_elements(By.ID, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_NAME"):
            elements = self.driver.find_elements(By.NAME, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_LINKTEXT"):
            elements = self.driver.find_elements(By.LINK_TEXT, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_CLASSNAME"):
            elements = self.driver.find_elements(By.CLASS_NAME, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_CSS"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, configReader.getLocator("locators", locator))
        return elements

    def find_element(self, locator):
        element = None
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_NAME"):
            element = self.driver.find_element(By.NAME, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_LINKTEXT"):
            element = self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_CLASSNAME"):
            element = self.driver.find_element(By.CLASS_NAME, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, configReader.getLocator("locators", locator))
        return element

    def getText(self, locator):
        self.wait_for_visible(locator)
        eleText = None
        if str(locator).endswith("_XPATH"):
            eleText = self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator)).text
        elif str(locator).endswith("_ID"):
            eleText = self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).text
        elif str(locator).endswith("_NAME"):
            eleText = self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).text
        elif str(locator).endswith("_LINKTEXT"):
            eleText = self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator)).text
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            eleText = self.driver.find_element(By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator)).text
        elif str(locator).endswith("_CLASSNAME"):
            eleText = self.driver.find_element(By.CLASS_NAME, configReader.getLocator("locators", locator)).text
        elif str(locator).endswith("_CSS"):
            eleText = self.driver.find_element(By.CSS_SELECTOR, configReader.getLocator("locators", locator)).text
        log.logger.info("Text of Element " + str(locator) + " is " + str(eleText))
        return eleText

    # def selenium_click(self, locator):
    #     self.wait_for_element_clickable(locator)
    #     if str(locator).endswith("_XPATH"):
    #         self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator)).click()
    #     elif str(locator).endswith("_ID"):
    #         self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).click()
    #     elif str(locator).endswith("_NAME"):
    #         self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).click()
    #     elif str(locator).endswith("_LINKTEXT"):
    #         self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator)).click()
    #     elif str(locator).endswith("_PARTIALLINKTEXT"):
    #         self.driver.find_element(By.PARTIAL_LINK_TEXT,
    #                                  configReader.getLocator("locators", locator)).click()
    #     elif str(locator).endswith("_CLASSNAME"):
    #         self.driver.find_element(By.CLASS_NAME,
    #                                  configReader.getLocator("locators", locator)).click()
    #     elif str(locator).endswith("_CSS"):
    #         self.driver.find_element(By.CSS_SELECTOR,
    #                                  configReader.getLocator("locators", locator)).click()
    #     log.logger.info("Clicking on Element " + str(locator))

    def selenium_click(self, locator):
        attempts = 0
        while attempts < 3:
            try:
                self.wait_for_element_clickable(locator)
                if str(locator).endswith("_XPATH"):
                    self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator)).click()
                elif str(locator).endswith("_ID"):
                    self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).click()
                elif str(locator).endswith("_NAME"):
                    self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).click()
                elif str(locator).endswith("_LINKTEXT"):
                    self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator)).click()
                elif str(locator).endswith("_PARTIALLINKTEXT"):
                    self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                             configReader.getLocator("locators", locator)).click()
                elif str(locator).endswith("_CLASSNAME"):
                    self.driver.find_element(By.CLASS_NAME,
                                             configReader.getLocator("locators", locator)).click()
                elif str(locator).endswith("_CSS"):
                    self.driver.find_element(By.CSS_SELECTOR,
                                             configReader.getLocator("locators", locator)).click()
                log.logger.info("Clicking on Element " + str(locator))
                return
            except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                log.logger.warning(f"Attempt {attempts + 1}: Exception occurred while clicking - {e}. Retrying...")
                time.sleep(3)
                attempts += 1

        log.logger.error(f"Element not clickable after {attempts} attempts: {locator}")
        raise Exception(f"Element not clickable after retries: {locator}")

    def click(self, locator):
        attempts = 0
        while attempts < 5:
            try:
                self.wait_for_element_clickable(locator)

                if str(locator).endswith("_XPATH"):
                    element = self.driver.find_element(By.XPATH, configReader.getLocator("locators", locator))
                elif str(locator).endswith("_ID"):
                    element = self.driver.find_element(By.ID, configReader.getLocator("locators", locator))
                elif str(locator).endswith("_NAME"):
                    element = self.driver.find_element(By.NAME, configReader.getLocator("locators", locator))
                elif str(locator).endswith("_LINKTEXT"):
                    element = self.driver.find_element(By.LINK_TEXT, configReader.getLocator("locators", locator))
                elif str(locator).endswith("_PARTIALLINKTEXT"):
                    element = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                                       configReader.getLocator("locators", locator))
                elif str(locator).endswith("_CLASSNAME"):
                    element = self.driver.find_element(By.CLASS_NAME, configReader.getLocator("locators", locator))
                elif str(locator).endswith("_CSS"):
                    element = self.driver.find_element(By.CSS_SELECTOR, configReader.getLocator("locators", locator))
                else:
                    raise Exception("Invalid locator type: " + str(locator))

                self.driver.execute_script("arguments[0].click();", element)
                log.logger.info("Clicked on Element " + str(locator))
                return
            except (StaleElementReferenceException, ElementClickInterceptedException) as e:
                log.logger.warning(f"Attempt {attempts + 1}: Exception occurred while clicking - {e}. Retrying...")
                time.sleep(3)
                attempts += 1

        log.logger.error(f"Element not clickable after {attempts} attempts: {locator}")
        raise Exception(f"Element not clickable after retries: {locator}")

    def is_visible(self, locator):
        self.wait_for_visible(locator)
        isDisplayed = None
        if str(locator).endswith("_XPATH"):
            isDisplayed = self.driver.find_element(By.XPATH,
                                                   configReader.getLocator("locators", locator)).is_displayed()
        elif str(locator).endswith("_ID"):
            isDisplayed = self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).is_displayed()
        elif str(locator).endswith("_NAME"):
            isDisplayed = self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).is_displayed()
        elif str(locator).endswith("_LINKTEXT"):
            isDisplayed = self.driver.find_element(By.LINK_TEXT,
                                                   configReader.getLocator("locators", locator)).is_displayed()
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            isDisplayed = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                                   configReader.getLocator("locators", locator)).is_displayed()
        elif str(locator).endswith("_CLASSNAME"):
            isDisplayed = self.driver.find_element(By.CLASS_NAME,
                                                   configReader.getLocator("locators", locator)).is_displayed()
        elif str(locator).endswith("_CSS"):
            isDisplayed = self.driver.find_element(By.CSS_SELECTOR,
                                                   configReader.getLocator("locators", locator)).is_displayed()
        log.logger.info(locator + " is Displayed : " + str(isDisplayed))
        return str(isDisplayed)

    def is_disable(self, locator):
        is_disable = None
        if str(locator).endswith("_XPATH"):
            is_disable = self.driver.find_element(By.XPATH,
                                                  configReader.getLocator("locators", locator)).get_property('disabled')
        elif str(locator).endswith("_ID"):
            is_disable = self.driver.find_element(By.ID, configReader.getLocator("locators", locator)).get_property(
                'disabled')
        elif str(locator).endswith("_NAME"):
            is_disable = self.driver.find_element(By.NAME, configReader.getLocator("locators", locator)).get_property(
                'disabled')
        elif str(locator).endswith("_LINKTEXT"):
            is_disable = self.driver.find_element(By.LINK_TEXT,
                                                  configReader.getLocator("locators", locator)).get_property('disabled')
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            is_disable = self.driver.find_element(By.PARTIAL_LINK_TEXT,
                                                  configReader.getLocator("locators", locator)).get_property('disabled')
        elif str(locator).endswith("_CLASSNAME"):
            is_disable = self.driver.find_element(By.CLASS_NAME,
                                                  configReader.getLocator("locators", locator)).get_property('disabled')
        elif str(locator).endswith("_CSS"):
            is_disable = self.driver.find_element(By.CSS_SELECTOR,
                                                  configReader.getLocator("locators", locator)).get_property('disabled')
        log.logger.info(locator + " is Disabled : " + str(is_disable))
        return str(is_disable)

    def getElementCount(self, locator):
        count = 0
        if str(locator).endswith("_XPATH"):
            count = self.driver.find_elements(By.XPATH,
                                              configReader.getLocator("locators", locator))
        elif str(locator).endswith("_ID"):
            count = self.driver.find_elements(By.ID, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_NAME"):
            count = self.driver.find_elements(By.NAME, configReader.getLocator("locators", locator))
        elif str(locator).endswith("_LINKTEXT"):
            count = self.driver.find_elements(By.LINK_TEXT,
                                              configReader.getLocator("locators", locator))
        elif str(locator).endswith("_PARTIALLINKTEXT"):
            count = self.driver.find_elements(By.PARTIAL_LINK_TEXT,
                                              configReader.getLocator("locators", locator))
        elif str(locator).endswith("_CLASSNAME"):
            count = self.driver.find_elements(By.CLASS_NAME,
                                              configReader.getLocator("locators", locator))
        elif str(locator).endswith("_CSS"):
            count = self.driver.find_elements(By.CSS_SELECTOR,
                                              configReader.getLocator("locators", locator))
        return len(count)

    """
    Drop Down functions
    """

    def get_selected_value_from_dropdown(self, locator):
        element = self.find_element(locator)
        value = Select(element).first_selected_option.get_attribute('value')
        return value

    def get_selected_text_from_dropdown(self, locator):
        element = self.find_element(locator)
        text = Select(element).first_selected_option.text
        return text

    def select_option_by_value_from_dropdown(self, locator, value):
        element = self.find_element(locator)
        select = Select(element)
        log.logger.info("Selecting by value " + value + " of " + str(locator))
        select.select_by_value(value)

    def select_option_by_index_from_dropdown(self, locator, index):
        element = self.find_element(locator)
        select = Select(element)
        log.logger.info("Selecting by index " + index + " of " + str(locator))
        select.select_by_index(index)


    def select_option_by_text_from_dropdown(self, locator, text):
        element = self.find_element(locator)
        select = Select(element)
        log.logger.info("Selecting by index " + text + " of " + str(locator))
        select.select_by_visible_text(text)

    """
    Waits
    """

    def wait_for_visible(self, locator):
        try:
            if str(locator).endswith("_CLASSNAME"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_XPATH"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_ID"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_PARTIALLINKTEXT"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_NAME"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_CSS"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_LINKTEXT"):
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.LINK_TEXT, configReader.getLocator("locators", locator))))
            log.logger.info("Element " + str(locator) + " is visible")
        except TimeoutException:
            log.logger.info("ELEMENT NOT FOUND WITHIN GIVEN TIME!")

    def wait_for_invisible(self, locator):
        try:
            if str(locator).endswith("_CLASSNAME"):
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CLASS_NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_XPATH"):
                WebDriverWait(self.driver, 10, poll_frequency=0.5).until(
                    EC.invisibility_of_element_located((By.XPATH, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_ID"):
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.ID, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_PARTIALLINKTEXT"):
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located(
                        (By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_NAME"):
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_CSS"):
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_LINKTEXT"):
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.LINK_TEXT, configReader.getLocator("locators", locator))))
            log.logger.info("Element " + locator + " is in visible")
        except TimeoutException:
            log.logger.info("ELEMENT FOUND !")

    def wait_for_visible_all_elements(self, locator):
        try:
            if str(locator).endswith("_CLASSNAME"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located(
                        (By.CLASS_NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_XPATH"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located((By.XPATH, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_ID"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located((By.ID, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_PARTIALLINKTEXT"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located(
                        (By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_NAME"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located((By.NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_CSS"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, configReader.getLocator("locators", locator)
                                                           )))
            elif str(locator).endswith("_LINKTEXT"):
                WebDriverWait(self.driver, 20).until(
                    EC.visibility_of_all_elements_located((By.LINK_TEXT, configReader.getLocator("locators", locator))))
            log.logger.info("Element " + locator + " is visible")
        except TimeoutException:
            log.logger.info("ELEMENT NOT FOUND WITHIN GIVEN TIME!")

    def wait_for_element_clickable(self, locator):
        try:
            if str(locator).endswith("_CLASSNAME"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.CLASS_NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_XPATH"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_ID"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.ID, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_PARTIALLINKTEXT"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.PARTIAL_LINK_TEXT, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_NAME"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.NAME, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_CSS"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, configReader.getLocator("locators", locator)
                                                )))
            elif str(locator).endswith("_LINKTEXT"):
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, configReader.getLocator("locators", locator))))
            log.logger.info("Element " + locator + " is clickable")
        except TimeoutException:
            log.logger.info("ELEMENT NOT FOUND WITHIN GIVEN TIME OR NOT CLICKABLE!")

    """
    Driver functions
    """

    def refresh(self):
        log.logger.info("Browser Refreshed")
        self.driver.refresh()

    def quit(self):
        log.logger.info("Browser closed")
        self.driver.quit()

    def close(self):
        log.logger.info("close the browser window")
        self.driver.close()

    def back(self):
        log.logger.info("Navigate back")
        self.driver.back()

    def get_current_url(self):
        time.sleep(3)
        log.logger.info("Current URL is : " + self.driver.current_url)
        return self.driver.current_url

    def get_location(self, locator):
        location = self.find_element(locator).location
        return int(location['x']), int(location['y'])

    """
    Frames / windows 
    """

    def switch_to_frame(self, element):
        element = self.find_element(element)
        log.logger.info("Switching to frame" + str(element))
        self.driver.switch_to.frame(element)

    def switch_to_new_window(self, function, *args):
        pass

    def switch_to_default_content(self):
        log.logger.info("Switching to default content")
        self.driver.switch_to.default_content()

    def close_current_window_and_focus_to_previous_one(self):
        handles = self.driver.window_handles
        self.close()
        self.driver.switch_to.window(handles[-2])

    """
    Mouse click / Hover
    """

    def right_click(self, locator):
        actionChains = ActionChains(self.driver)
        actionChains.context_click(locator).perform()

    def hover(self, locator):
        element = self.find_element(locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def hoverAndSelect(self, HoverLocator, clickLocator):
        ele1 = self.find_element(HoverLocator)
        ele2 = self.find_element(clickLocator)
        Hover = ActionChains(self.driver).move_to_element(ele1).move_to_element(ele2)
        time.sleep(5)
        Hover.click().perform()
        log.logger.info("Hover on element " + HoverLocator + " and click on element " + clickLocator)

    def dragAndDrop(self, source_locator, target_locator):
        # action = ActionChains(self.driver)
        drag = self.find_element(source_locator)
        drop = self.find_element(target_locator)
        # action.click_and_hold(drag).move_by_offset(150, 100).pause(2).move_by_offset(-10, -10).release().perform()
        # action.click_and_hold(drag).move_to_element(drop).pause(2).move_by_offset(20, 20).release().perform()
        # drag_and_drop(self.driver, drag, drop)
        ActionChains(self.driver).drag_and_drop(drag, drop).perform()
        # ActionChains(self.driver).click_and_hold(drag).move_to_element(drop).release().perform()

    def scroll_to_element(self, locator):
        ele = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    def safest_click(self, locator):
        global element
        try:
            element = None
            if str(locator).endswith("_XPATH"):
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_ID"):
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, configReader.getLocator("locators", locator))))
            elif str(locator).endswith("_NAME"):
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, configReader.getLocator("locators", locator))))
        #     element.click()
        #     log.logger.info("selenium clicked on element")
        # except StaleElementReferenceException:
            # log.logger.info("TimeoutException: The element was not found within the given time.")
            tries = 3
            while tries > 0:
                try:
                    # element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
                    element.click()
                    print("try")
                    log.logger.info("selenium clicked on element")
                    break
                except StaleElementReferenceException:
                    tries -= 1
                    print("stale")
                    log.logger.info("Stale Element Exception occurred, retrying...")
                    self.wait_till_progressBar_Disappear()
                except ElementClickInterceptedException:
                    tries -= 1
                    print("ElementClickInterceptedException")
                    log.logger.info("Element Click Intercepted Exception occurred, retrying...")
                    self.wait_till_progressBar_Disappear()
        except TimeoutException:
            log.logger.info("TimeoutException: The element was not found within the given time.")


    def wait_till_progressBar_Disappear(self):
        ele = self.driver.find_elements(By.XPATH, "//div[@class='turbo-progress-bar']")
        c = len(ele)
        if c == 0:
            pass
        else:
            print("waittttttt")
            WebDriverWait(self.driver, 500).until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='turbo-progress-bar']")))
