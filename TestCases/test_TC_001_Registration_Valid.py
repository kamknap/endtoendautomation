from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.InitiateDriver import driver
from Library.ConfigReader import readElementLocators
from DataGenerator.DataGenerator import dataGenerator
from Pages.RegistrationPage import RegistrationClass
import pytest
import openpyxl

@pytest.mark.parametrize("data", dataGenerator())
def test_ValidateRegistration(driver, data):
    registration = RegistrationClass(driver)    
    registration.enterUsername(data[0])
    registration.enterEmail(data[1])
