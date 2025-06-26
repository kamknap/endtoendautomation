from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.InitiateDriver import driver
from Library.ConfigReader import readElementLocators
import pytest

def test_validate_invalid_data(driver):
    name_el = driver.find_element(By.NAME, readElementLocators("Registration", "Username_name"))
    name_el.send_keys("12341234")
    