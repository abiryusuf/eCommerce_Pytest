
class LoginPage:
    text_username_id = "Email"
    text_password_id = "Password"
    button_login = "//*[@class='button-1 login-button']"
    link_logout_linkText = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.text_username_id).clear()
        self.driver.find_element_by_id(self.text_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.text_password_id).clear()
        self.driver.find_element_by_id(self.text_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linkText).click()