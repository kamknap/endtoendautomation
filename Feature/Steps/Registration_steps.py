from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'User is on registration page')
def step_impl(context):
    pass

@when(u'User enters username "User1"')
def step_impl(context):
    username = context.driver.find_element(By.NAME, "fld_username")
    username.send_keys("User1")


@when(u'User enters email "User1@gmail.com"')
def step_impl(context):
    email = context.driver.find_element(By.NAME, "fld_email")
    email.send_keys("User1@gmail.com")


@when(u'User enters password "Password1"')
def step_impl(context):
    password = context.driver.find_element(By.NAME, "fld_password")
    password_r = context.driver.find_element(By.NAME, "fld_cpassword")
    password.send_keys("Password1")
    password_r.send_keys("Password1")


@when(u'User click the signup button')
def step_impl(context):
    signup_btn = context.driver.find_element(By.CSS_SELECTOR, "#tab-content1 > form > div > input[type=submit]:nth-child(3)")
    signup_btn.click()


@then(u'Usser should be registered successfully')
def step_impl(context):
    print("registered")