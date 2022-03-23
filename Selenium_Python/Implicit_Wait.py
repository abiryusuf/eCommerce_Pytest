from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(executable_path="/Users/abiryusuf/Documents/eCommerce/Drivers/chromedriver2"))
driver.get("https://admin-demo.nopcommerce.com/")
driver.implicitly_wait(5)  # tell the webdriver wait for each elements
# wait

assert "Your store. Login" in driver.title

ele = driver.find_element(By.XPATH, "//*[text() ='Welcome, please sign in!']")
if ele.is_displayed():
    assert True
else:
    assert False
time.sleep(5)
driver.find_element(By.XPATH, "//*[@type ='submit']").click()
