import pytest
import allure
import time

from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.positive
@allure.title("Verify and search product on ebay website")
@allure.description("Search for product and get list of product on ebay website")
def test_ebay_login():
    driver = webdriver.Chrome()

    driver.get("https://www.ebay.com/")
    driver.maximize_window()

    search_input = driver.find_element(By.XPATH, "//input[@id='gh-ac']")
    search_input.send_keys("16gb")

    search_btn = driver.find_element(By.XPATH, "//input[@id='gh-btn']")
    search_btn.click()
    time.sleep(5)


    product_list = driver.find_elements(By.XPATH, "//span[@role='heading']")
    for item in product_list:
        product_name = item.text
        print(product_name)

    product_price_list = driver.find_elements(By.XPATH, "//span[@class='s-item__price']")
    price_list = []
    for price in product_price_list:
        product_price = price.text
        print(product_price)
        x = product_price.replace("$", "").strip()
        price_list.append(x)

    price_list.sort()
    min_price = price_list[1]
    print("Cheapest Price is: " + min_price)
    allure.attach(driver.get_screenshot_as_png(), name='Home_Page_Screenshot', attachment_type=AttachmentType.PNG)
    driver.quit()
