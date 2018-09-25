"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from appium import webdriver as appiumdriver

class WebDriverFactory():

    def __init__(self):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        #self.browser = browser
        #self.device = device
        pass
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
        capabilities = {

            "platformName": "iOS",
            "platformVersion": "11.4",
            "deviceName": "iPhone 8",
            "automationName": "XCUITest",
            "app": "/Users/marcocelone/Library/Developer/Xcode/DerivedData/MyChariot-fckamflarvkbhqflgkkpyovwukaz/Build/Products/Debug-iphonesimulator/MyChariot.app"
        }
        driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
        driver.implicitly_wait(10)

        driver.find_element_by_accessibility_id("Switch to Sign In").click()
        driver.find_element_by_xpath("//*[@value='you@you.com']").send_keys("rider@rider.com")
        driver.find_element_by_xpath("//*[@value='password']").send_keys("111111")
        driver.find_element_by_accessibility_id("Log In").click()
        driver.find_element_by_xpath("//*[@name='Logout']")
        #driver.quit()
        #driver.get(baseURL)
        #driver.implicitly_wait(3)
        # Maximize the window
        #driver.maximize_window()
        # Loading browser with App URL
        #driver.get(baseURL)
        return driver

x = WebDriverFactory()
x.getWebDriverInstance()