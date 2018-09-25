"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
#from selenium import webdriver
from base import capabilities
from appium import webdriver as appiumdriver

class WebDriverFactory():

    def __init__(self, device):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        #self.browser = browser
        self.device = device
        self.capabilities = capabilities.capabilities
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        #baseURL = "https://qa-test.avenuecode.com/"
        if self.device == "ios_mobile":
            self.driver = appiumdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)
            self.driver.implicitly_wait(10)
            #return driver
            #driver.get(baseURL)

        else:
            print("Hello")
        # Setting Driver Implicit Time out for An Element
            self.driver = appiumdriver.Remote('http://localhost:4723/wd/hub', self.capabilities)
            self.driver.implicitly_wait(10)
        return self.driver
        # Maximize the window
        #driver.maximize_window()
        # Loading browser with App URL
        #driver.get(baseURL)
        #return driver