import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_01_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.get)
        act_title = self.driver.title
        # self.driver.close()

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            assert False
            self.driver.close()

    def test_login(self, setup):
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # or
        self.driver = setup
        self.driver.get(self.baseURL)
        # create an object for POM
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            assert False
            self.driver.close()
