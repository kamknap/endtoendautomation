from selenium import webdriver
from Library import ConfigReader
import pytest

@pytest.fixture(scope="function")
def driver():
    browser = ConfigReader.readConfigData("Details", "Browser")
    if(browser.lower() == "chrome"):
        driver = webdriver.Chrome()
    elif(browser.lower() == "firefox"):
        driver = webdriver.Firefox()
    else:
        raise Exception(f"Unsupported browser: {browser}")
    driver.get(ConfigReader.readConfigData("Details", "Application_URL"))
    yield driver
    driver.close()