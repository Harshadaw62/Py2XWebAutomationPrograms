import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_make_appointment():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # < a
    # id = "btn-make-appointment"
    # href = "./profile.php#login"
    #
    # class ="btn btn-dark btn-lg" > Make Appointment < / a >

    element = driver.find_element(By.ID, "btn-make-appointment")
    element.click()

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)

    email_element = driver.find_element(By.NAME, "username")
    email_element.send_keys("John Doe")

    password_element = driver.find_element(By.ID, "txt-password")
    password_element.send_keys("ThisIsNotAPassword")

    login_btn = driver.find_element(By.ID,"btn-login")
    login_btn.click()

    time.sleep(5)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    verify_apt_txt = driver.find_element(By.CLASS_NAME, "col-sm-12")
    print(verify_apt_txt.text)
    assert verify_apt_txt.text == "Make Appointment"
    driver.quit()

