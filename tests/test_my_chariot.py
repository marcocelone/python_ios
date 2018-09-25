from screens.home.login_screen import LoginScreen
import unittest
import pytest
import string
import time
from random import *

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    # Setup
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp, setUp):
        self.lp = LoginScreen(self.driver)

    # Login to application and verify Success
    @pytest.mark.run(order=1)
    def test_a_validLogin(self):
        self.lp.login("rider@rider.com", "111111")
        time.sleep(3)
        result = self.lp.verifyLoginSuccessful()
        assert result == True
