from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
from base.webdriverfactory import WebDriverFactory
from appium import webdriver as appiumdriver
from base import capabilities


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        self.capabilities = capabilities.capabilities
        self.ios_driver = appiumdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)


    def sendKeysIosXp(self, data, locator):
        try:
            element = self.ios_driver.find_element_by_xpath(locator)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator)
            print_stack()

    def elementClickIos(self, data):
        try:
            element = self.ios_driver.find_element_by_accessibility_id(data)
            element.click()
            self.log.info("Sent data on element with Data: " + data)
        except:
            self.log.info("Cannot send data: " + data )
            print_stack()

    def isElementPresentIosId(self, locator):
        try:
            element = self.ios_driver.find_element_by_accessibility_id(locator)
            if element is not None:
                self.log.info("Element Found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False