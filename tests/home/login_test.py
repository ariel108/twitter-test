from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from pages.home.home_page import HomePage
from pages.home.login_after_logout import LogAgain

import pytest
import unittest

class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseUrl = "https://twitter.com/login"
        driver = webdriver.Chrome("/usr/local/bin/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)


        lp = LoginPage(driver)
        lp.login("variial@gmail.com", "108stoosiem108")

        signupLink = driver.find_element(By.XPATH, "//*[@id='user-dropdown-toggle']")

        if signupLink is not None:
            print("Login Good")
        else:
            print("Login Bad")


        hp = HomePage(driver)
        hp.clicking()


        ap = LogAgain(driver)
        ap.againLogin("variial@gmail.com", "dupa8")