from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service(executable_path="./Drivers/chromedriver2"))
driver.get("https://www.google.com/")