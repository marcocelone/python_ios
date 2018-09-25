import pytest
from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("\nRunning method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--device")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--device")
