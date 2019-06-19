# -*- coding: utf-8 -*-

# @Author: Stormix - Anas Mazouni
# @Date:   2017-06-19 07:26
# @Email:  anas.mazouni@stormix.co
# @Project: 1337
# @Website: https://stormix.co

# Import Some Python Modules

import inspect, sys
import os
import time
from sys import platform
import re

# Import Browser modules

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Auth:
    # Pronote Class Attributes
    delay = 5
    url = None
    user_input = "user_email"
    password_input = "user_password"
    connect_button = "commit"
    browser = None
    thankyou = """
          -----------------------------------------------------
          All Done ! Thanks for using PronoteDownloader !
          -----------------------------------------------------
          By Anas Mazouni -  Stormix (https://stormix.co)
          """

    def __init__(self, url, email, password):
        self.url = url
        self.username = email
        self.password = password

    def launchBrowser(self):
        assert not self.browser, "Browser already set !"
        # Initiate the Browser webdriver
        currentfolder = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        # Check which operating system is being used !
        if platform == "linux" or platform == "linux2":
            # linux
            chrome_driver = currentfolder+"/Drivers/chromedriver"
        elif platform == "win32":
            # Windows
            chrome_driver = "Drivers/chromedriver.exe"
        print("Chrome Driver Location : "+chrome_driver)
        self.browser = webdriver.Chrome(chrome_driver)
        Browser = self.browser
        Website = self.url
        # Open Pronote
        Browser.get(Website)
        print("Browser Initiated !")
        print("Loading .. " + Website, end=' ')
        time.sleep(self.delay)
        print('[DONE]')

    def login(self):
        """A procedure used to login into Pronote using the students credentials
        """
        Browser = self.browser
        Username = self.username
        Password = self.password
        # Fill in the login form
        username_log = Browser.find_element_by_id(self.user_input)
        password_log = Browser.find_element_by_id(self.password_input)
        username_log.send_keys(Username)
        password_log.send_keys(Password)
        # Click the connect buttun
        print("Logging in ...", end=" ")
        Browser.find_element_by_name(self.connect_button).click()
        time.sleep(self.delay)
        print('[DONE]')
    def check(self):
        """ Check if checkin is available """
        text = self.browser.find_element_by_css_selector("#subs-content > div.row > div > p").text
        print(text)
        return text[:45] != "De nouveaux creneaux ouvriront prochainement."
    
    def refresh(self):
        self.browser.refresh()

    def disconnected(self):
        self.browser.get(self.url)
        try:
            self.browser.find_element_by_id(self.user_input)
        except NoSuchElementException:
            return False
        print("Got disconnect..")
        return True
