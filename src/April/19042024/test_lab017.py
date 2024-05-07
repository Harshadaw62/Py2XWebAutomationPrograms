import time

import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


@pytest.mark.smoke
@allure.title("Verify That login is working in Cura website")
@allure.description("Simple Login check on CURA Katalon Website")
def test_make_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    #
    # class ="btn btn-dark btn-lg" > Make Appointment < / a >

    make_appointment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    make_appointment_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="Login Screenshot", attachment_type=AttachmentType.PNG)

    print(driver.current_url)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login", "Assertion Fail Message #1-Error matching the URLs"
    time.sleep(3)

    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("John Doe")

    password_element = driver.find_element(By.ID, "txt-password")
    password_element.send_keys("ThisIsNotAPassword")

    login_btn = driver.find_element(By.ID, "btn-login")
    login_btn.click()

    allure.attach(driver.get_screenshot_as_png(), name="Appointment Screenshot", attachment_type=AttachmentType.PNG)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment", "Assertion Fail Message #2-Error Wrong URL(Appointment)"

    verify_apt_txt = driver.find_element(By.CLASS_NAME, "col-sm-12")
    print(verify_apt_txt.text)
    assert verify_apt_txt.text == "Make Appointment"
    driver.quit()
