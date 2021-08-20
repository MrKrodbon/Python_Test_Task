from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
try:

    browser.get("https://reports.netpeak.net/login")
    LoginField = browser.find_element_by_id('login').send_keys("Qwerty")
    PasswordField = browser.find_element_by_id('password').send_keys("QwertyIsLegendPassword")
    AuthoChkBox = browser.find_element_by_css_selector('.gdpr.ng-pristine.ng-untouched.ng-valid.ng-empty').click()
    time.sleep(1)
    EnterBtn = browser.find_element_by_css_selector('.enter.md-button.md-ink-ripple').click()
finally:
    time.sleep(15)
