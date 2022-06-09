from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch the Firefox browser')
def browser_open(context):
    context.driver = webdriver.Firefox()


@when('Open OrangeHRM log in page')
def open_login(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Putting the username "{user}"')
def step_impl(context, user):
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)


@when('Putting the password "{pwd}"')
def step_impl(context, pwd):
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)
    context.driver.find_element(By.ID, "btnLogin").click()


@then('Verify the successfull log in attempt')
def log_in_verify(context):

    try:
        text = context.driver.find_element(
            By.XPATH, "//h1[contains(text(),'Dashboard')]").is_displayed()
    except:
        assert False, "Test failed"
    if text == "Dashboard":
        assert True, "Test passed"
        


@when('Close the browser')
def step_impl(context):
    context.driver.close()
