import pytest
import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify login functionality of iDrive Website")
@allure.description("Simple login check of idrive360 with valid credentials and redirect on my account page")
def test_idrive_login():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")
    email_element = driver.find_element(By.XPATH, "//input[@id='username']")
    email_element.send_keys("augtest_040823@idrive.com")

    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys("123456")

    login_btn = driver.find_element(By.XPATH, "//button[@id='frm-btn']")
    login_btn.click()

    time.sleep(10)
    print(driver.current_url)
    time.sleep(10)

    trial_message = driver.find_element(By.XPATH, "//h5[@class='id-card-title']")
    print(trial_message.text)
    assert trial_message.text == "Your free trial has expired", "Error - Invalid message"
    assert driver.current_url == "https://www.idrive360.com/enterprise/account?upgradenow=true", "Error - Invalid URL"
    allure.attach(driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()
