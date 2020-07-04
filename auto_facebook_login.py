from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# download this library using pip with code 'python -m pip install jproperties'
from jproperties import Properties 

print('let us login to facebook automatically')

#preparing properties object to read data 
configs = Properties()

#load properties file
with open(r'C:\Users\Owner\Desktop\pythonTest\config.properties', 'rb') as config_file:
	configs.load(config_file)

# get data from file as username and password using keys  
username = configs.get('username').data
password = configs.get('pass').data

#preparing chrome browser to test 
driver =  webdriver.Chrome(r"C:\Python\chromedriver_win32\chromedriver.exe") #enter your path

#maximize_ chrome_window
driver.maximize_window() 

# go to facebook.com
driver.get('https://www.facebook.com/')

# point mouse over username and password textbox then put (user and pass)
driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(password)

# sleep 2 seconds 
time.sleep(2)

# press login button 
driver.find_element_by_id('loginbutton').send_keys(Keys.ENTER)
time.sleep(20)
#close browser
driver.close()
