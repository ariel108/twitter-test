from selenium.webdriver.common.by import By



class LogAgain():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _already_log = "//*[@id='signin-link']"
    _email_field = "//*[@id='signin-dropdown']/div[3]/form/div[1]/input"
    _password_field = "//*[@id='signin-dropdown']/div[3]/form/div[2]/input"
    _login_button = "//*[@id='signin-dropdown']/div[3]/form/input[1]"

    def findAlreadyLog(self):
        return self.driver.find_element(By.XPATH, self._already_log)

    def getEmailField(self):
        return self.driver.find_element(By.XPATH, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.XPATH, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def clickAlreadyLog(self):
        self.findAlreadyLog().click()

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, wrongpassword):
        self.getPasswordField().send_keys(wrongpassword)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def againLogin(self, email, wrongpassword):
        self.clickAlreadyLog()
        self.enterEmail(email)
        self.enterPassword(wrongpassword)
        self.clickLoginButton()


