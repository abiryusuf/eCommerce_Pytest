from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(executable_path="/Users/abiryusuf/Documents/eCommerce/Drivers/chromedriver2"))
driver.get("https://www.google.com/")

links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
for link in links:
    print("Name of the link", link.text)
driver.find_element(By.LINK_TEXT, "Gmail").click()
driver.find_element(By.PARTIAL_LINK_TEXT, "Gma").click()
