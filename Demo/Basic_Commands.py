import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(executable_path="/Users/abiryusuf/Documents/eCommerce/Drivers/chromedriver2"))
driver.get("https://www.google.com")
time.sleep(5)
print(driver.title)

driver.get("https://admin-demo.nopcommerce.com/")
print(driver.title)
time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
print(driver.title)
# driver.find_element(By.XPATH, "//*[@type ='submit']").click()

print(driver.current_url)
#driver.quit()