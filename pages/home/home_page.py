from selenium.webdriver.common.by import By



class HomePage():

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _user_dropdown = "//*[@id='user-dropdown-toggle']"
    _log_out = "// *[ @ id = 'signout-button'] / button"
    def findUserDropdown(self):
        return self.driver.find_element(By.XPATH, self._user_dropdown)

    def findLogOut(self):
        return self.driver.find_element(By.XPATH, self._log_out)


    def clickUserDropdown(self):
        self.findUserDropdown().click()

    def clickLogOut(self):
        self.findLogOut().click()

    def clicking(self):
        self.clickUserDropdown()
        self.clickLogOut()

