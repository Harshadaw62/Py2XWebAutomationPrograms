import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Selenium 4
#XPATH
# Syntax- //Tagname[@Attributename]

#//input[@id='login-username']
#//input[@name="username"]
# //input[@class="text-input W(100%)"]-Not Recommended
# //input[@type="email"]-Not Recommended
# //input[@data-qa="hocewoqisi"]

# @pytest.mark.smoke
def test_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/")

    make_appointment_btn = driver.find_element(By.XPATH, "//input[@name='username']")
    make_appointment_btn.send_keys("admin")



    time.sleep(5)

    driver.quit()
