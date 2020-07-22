from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from jproperties import Properties 

mydata = Properties()
with open(r'C:\Users\Owner\Desktop\pythonTest\config.properties', 'rb') as config_file:
	mydata.load(config_file)

username = mydata.get('username').data
password = mydata.get('pass').data

driver =  webdriver.Chrome(r"C:\Python\chromedriver_win32\chromedriver.exe")

driver.maximize_window() 

driver.get('https://facebook.com/')
driver.find_element_by_name('email').send_keys(username)
driver.find_element_by_name('pass').send_keys(password)

# press login button 
driver.find_element_by_id('loginbutton').send_keys(Keys.ENTER)
time.sleep(10)
post_loc = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[3]/div/div/div[1]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]')
post_loc.click()
time.sleep(3)
post_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div')
post_box.send_keys('Hello every one :) ')
submit_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div').click()
time.sleep(20)

driver.close()
