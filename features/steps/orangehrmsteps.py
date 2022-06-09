from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch Firefox browser')
def launch_browser(context):
    context.driver = webdriver.Firefox()


@when('Open Orange hrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@then('Verify that the logo exists on the page')
def verify_logo(context):
    logo = context.driver.find_element(
        By.XPATH, "//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert logo is True


@then('close the browser')
def close_browser(context):
    context.driver.close()
