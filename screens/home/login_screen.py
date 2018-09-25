from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginScreen(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field = "//*[@value='you@you.com']"
    _password_field = "//*[@value='password']"
    _switch_to_login = "Switch to Sign In"
    _login = "Log In"
    _logout = "//*[@name='Logout']"
    _call = "Call"
    _navigation = "//*[@type='XCUIElementTypeNavigationBar']"

    def switch_to_login(self):
        self.elementClickIos(self._switch_to_login)

    def enterEmail(self, email):
        self.sendKeysIosXp(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeysIosXp(password, self._password_field)

    def login_app(self):
        self.elementClickIos(self._login)



    def login(self, email, password):
        self.switch_to_login()
        self.enterEmail(email)
        self.enterPassword(password)
        self.login_app()

    def verifyLoginSuccessful(self):
        result = self.isElementPresentIosId(self._call)
        return result

