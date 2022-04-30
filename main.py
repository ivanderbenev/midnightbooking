from selenium.webdriver.support.select import Select
from selenium import webdriver
import os
import time

basedir = os.path.abspath(os.path.dirname(__file__))
chrome_dir = os.path.join(basedir, "chromedriver")
driver = webdriver.Chrome(chrome_dir)
driver.get('https://ncc.leisurecloud.net/Connect/MRMLogin.aspx')
"""Login"""
email_field = driver.find_element_by_id('ctl00_MainContent_InputLogin')
email_field.clear()
email_field.send_keys("Ivan.Derbenev@nottingham.ac.uk")
password_field = self.driver.find_element_by_id('ctl00_MainContent_InputPassword')
password_field.clear()
password_field.send_keys("Param0n0v")
driver.find_element_by_id('ctl00_MainContent_btnLogin').click()
# web.type('Ivan.Derbenev@nottingham.ac.uk', into='Email Address', id='ctl00_MainContent_InputLogin')
# web.type('Param0n0v', into='Password', id='ctl00_MainContent_InputPassword')
# web.click('Login', tag='span')
time.sleep(1)
"""Choose leisure centre"""
# web.click(id='ctl00_MainContent__advanceSearchUserControl_SitesSimple')

