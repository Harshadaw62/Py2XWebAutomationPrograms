import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from selenium.webdriver.support.relative_locator import locate_with

@pytest.mark.smoke
@allure.title("Verify that codepen registered page is opened ")
@allure.description("TC#1 - Below element - error message assert that error message.")
def test_MiniProject7():
    driver = webdriver.Chrome()
    driver.get("https://codepen.io/AbdullahSajjad/full/LYGVRgK")
    driver.maximize_window()

    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.ID, "result"))

    button_element = driver.find_element(By.XPATH, "//button[text()='Submit']")
    button_element.click()
    time.sleep(3)

    user_name = driver.find_element(By.XPATH, "//input[@id='username']")
    error_msg = driver.find_element(locate_with(By.TAG_NAME, "small").below(user_name)).text
    assert error_msg == "Username must be at least 3 characters"
    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(5)
    driver.quit()
