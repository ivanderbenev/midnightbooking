from webbot import Browser
web = Browser()
web.go_to('https://ncc.leisurecloud.net/Connect/MRMLogin.aspx')
web.type('Ivan.Derbenev@nottingham.ac.uk', into='Email Address', id='ctl00_MainContent_InputLogin')
web.type('', into='Password', id='ctl00_MainContent_InputPassword') # specific selection
web.click('Login', tag='span')  # you are logged in ^_^
