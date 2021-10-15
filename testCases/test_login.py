import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_01_Login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    # step 5
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    # logs
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("********Test_01******")
        self.logger.info("*******Verify Home page Title*********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********Home_page_Title_ pass***********")
        else:
            # step 4
            self.driver.save_screenshot("./Screenshots/" + "test_homePageTitle.png")
            assert False
            self.driver.close()
            self.logger.info("********if it is fail*********")

    def test_login(self, setup):
        self.logger.info("*******Verify Login Test **********")
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

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("./Screenshots/" + "test_login.png")
            assert False
            self.driver.close()
