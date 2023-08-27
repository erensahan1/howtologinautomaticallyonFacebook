from selenium.webdriver.common.keys import Keys
from InstagramUserInfo import username, password
from selenium import webdriver
import time

class facebook:
    def __init__(self,username,password):
        self.browser=webdriver.Chrome()
        self.username=username
        self.password=password


    def signin(self):
        self.browser.get("https://tr-tr.facebook.com/")
        time.sleep(2)
        ein=self.browser.find_element("xpath","//*[@id='email']")
        pin=self.browser.find_element("xpath","//*[@id='pass']")
        ein.send_keys(self.username)
        pin.send_keys(self.password)
        pin.send_keys(Keys.ENTER)
        time.sleep(500)

fc=facebook(username,password)
fc.signin()



