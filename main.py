from webbot import Browser
import time

web = Browser()
web.go_to('https://ncc.leisurecloud.net/Connect/MRMLogin.aspx')
"""Login"""
web.type('Ivan.Derbenev@nottingham.ac.uk', into='Email Address', id='ctl00_MainContent_InputLogin')
web.type('***', into='Password', id='ctl00_MainContent_InputPassword')
web.click('Login', tag='span')
time.sleep(1)
"""Choose leisure centre"""
# web.click(id='ctl00_MainContent__advanceSearchUserControl_SitesSimple')
web.click(tag='option', text='Djanogly Leisure Centre')
"""Click the button '7 days'"""
web.click(id='ctl00_MainContent__advanceSearchUserControl__lnkBtnSevenDaysTime')
time.sleep(3)
"""Choose a class"""
web.click(id='ctl00_MainContent__advanceSearchResultsUserControl_Classes_ctrl7_lnkActivitySelect_lg')
time.sleep(1)
"""Click 'Book'"""
web.click(id='ctl00_MainContent_ClassStatus_ctrl0_btnBook')
time.sleep(1)
"""Click 'Book & Checkout'"""
web.click(id='ctl00_MainContent_btnBasket')
time.sleep(1)
"""Click 'Pay with Card'"""
web.click(id='ctl00_MainContent_btnPay2')
time.sleep(2)
"""Click 'pay now'"""
web.click(text='Pay Now', tag='a')
