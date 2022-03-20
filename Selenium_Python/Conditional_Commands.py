# is_Displayed
# is_enabled
# is_selected

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=Service(executable_path="/Users/abiryusuf/Documents/eCommerce/Drivers/chromedriver2"))
driver.get("https://admin-demo.nopcommerce.com/")
ele = driver.find_element(By.XPATH, "//*[text() ='Welcome, please sign in!']")
print(ele.is_displayed())
print(ele.is_enabled())
time.sleep(5)
driver.find_element(By.XPATH, "//*[@type ='submit']").click()

