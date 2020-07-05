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
driver =  webdriver.Chrome(r"C:\Python\chromedriver_win32\chromedriver.exe")

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

print('Auto login to facebook has been successfully  # thanks too')

print('opening messenger web app ....')
time.sleep(10)

#press meessenger button to select your friend
messenger_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[2]/span/div')
messenger_button.send_keys(Keys.ENTER)

time.sleep(3)

#go to messenger textarea to search
search_to_message = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div[1]/div/div/div/div[2]/div/div[2]/div/div/span/input')
myfriend = 'ENTER_YOUR_FRIEND_NAME'
search_to_message.send_keys(myfriend)
time.sleep(2)
#press your friend 
results = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/div/div/ul/li')
results.click()
#enter your message in messege_box to send
message = 'ENTER_YOUR_MESSAGE_HERE'
send_message = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div[1]/div/div/div/div[3]/div/div[2]/form/div/div[2]/div[2]/div[1]/div/div/div/div/div/div/div/div/div')
send_message.send_keys(message)
# option to take screenshot 
driver.save_screenshot("screenshot.png")
time.sleep(1)
#click send_button 
send_message.send_keys(Keys.ENTER)

# wait 10 seconds then close chrome
time.sleep(10)
driver.close()

print('Auto message to' +myfriend+ 'has been successfully  # thanks too')
