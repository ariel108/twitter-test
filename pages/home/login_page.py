from selenium.webdriver.common.by import By



class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _email_field = "js-username-field"
    _password_field = "js-password-field"
    _login_button = "//*[@id='page-container']/div/div[1]/form/div[2]/button"

    def getEmailField(self):
        return self.driver.find_element(By.CLASS_NAME, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.CLASS_NAME, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def enterEmail(self, email ):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()