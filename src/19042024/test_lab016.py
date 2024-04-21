import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4


# @pytest.mark.smoke
def test_make_appointmet():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # id -> name -> className -> tagName -> LinkText, PartialText -> css Selector -> Xpath

    # By LINK_TEXT
    # make_appointment_btn = driver.find_element(By.LINK_TEXT, "Make Appointment")
    # make_appointment_btn.click()

    # By PARTIAL_LINK_TEXT
    # make_appointment_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Make")
    # make_appointment_btn.click()

    # By Tag_name
    list_of_tags = driver.find_elements(By.TAG_NAME, "a")
    make_appointment_btn = list_of_tags[5]
    make_appointment_btn.click()

    time.sleep(5)

    driver.quit()
