import keyword

from selenium import webdriver
import math
import time
try:
    browser = webdriver.Chrome()
    browser.get("https://netpeak.ua/")
    time.sleep(2)
    AboutUsBtn = browser.find_element_by_css_selector('[data-content="58"]').click()
    time.sleep(2)
    TeamBtn = browser.find_element_by_link_text("Команда").click()
    time.sleep(2)
    PartOfTeamBtn = browser.find_element_by_link_text("Стать частью команды").click()
    browser.switch_to_window(browser.window_handles[+1])
    browser.window_handles
    time.sleep(5)
    WantWorkBtn = browser.find_element_by_css_selector('.btn.green-btn').click()
    browser.close()
    browser.switch_to_window(browser.window_handles[0])
    browser.window_handles
    OfficeBtn = browser.find_element_by_link_text("Личный кабинет").click()
    browser.switch_to_window(browser.window_handles[+1])
    browser.window_handles
    LoginField = browser.find_element_by_id('login').send_keys("Qwerty")
    PasswordField = browser.find_element_by_id('password').send_keys("QwertyIsLegendPassword")
    AuthoChkBox = browser.find_element_by_css_selector('.gdpr.ng-pristine.ng-untouched.ng-valid.ng-empty').click()
    time.sleep(3)
    EnterBtn = browser.find_element_by_css_selector('.enter.md-button.md-ink-ripple').click()
finally:
    time.sleep(10)
    browser.quit()



