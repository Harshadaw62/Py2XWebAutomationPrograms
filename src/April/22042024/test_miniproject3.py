import pytest
import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify error message for username field")
@allure.description("Simple login check with error message for username field ")
def test_codepen_login():
    driver = webdriver.Chrome()

    driver.get("https://cdpn.io/AbdullahSajjad/fullpage/LYGVRgK?anon=true&view=fullpage")
    driver.maximize_window()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))

    email_element = driver.find_element(By.XPATH, "//input[@id='email']")
    email_element.send_keys("harsh@gmail.com")

    password_element = driver.find_element(By.XPATH, "//input[@id='password']")
    password_element.send_keys("123456")

    password_element2 = driver.find_element(By.XPATH, "//input[@id='password2']")
    password_element2.send_keys("123456")

    btn_element = driver.find_element(By.XPATH, "//button[text()='Submit']")
    btn_element.click()

    time.sleep(5)

    allure.attach(driver.get_screenshot_as_png(), name="Login-Screenshot", attachment_type=AttachmentType.PNG)

    assert (driver.find_element(By.XPATH, "//input[@id='username']/following::small").text
            == "Username must be at least 3 characters")
    driver.quit()
