from selenium import webdriver
from selenium.webdriver.common.by import By
from Base.InitiateDriver import driver
from Library.ConfigReader import readElementLocators

class RegistrationClass:
    
    def __init__(self, driver):
        self.driver = driver
    
    def enterUsername(self, username):
        name_el = self.driver.find_element(By.NAME, readElementLocators("Registration", "Username_name"))
        name_el.send_keys(username)
    
    def enterEmail(self, email):
        email_el = self.driver.find_element(By.NAME, readElementLocators("Registration", "Email_name"))
        email_el.send_keys(email)
