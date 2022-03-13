from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(executable_path="/Users/abiryusuf/Documents/eCommerce/Drivers/chromedriver2"))
driver.get("https://admin-demo.nopcommerce.com/")
print(driver.title)
driver.find_element(By.XPATH, "//*[@type ='submit']").click()


