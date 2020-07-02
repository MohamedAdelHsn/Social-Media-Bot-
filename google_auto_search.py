from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
print("sample auto web search test case ...")
# define path of chromeDriver driver executable file
driver =  webdriver.Chrome(r"C:\Python\chromedriver_win32\chromedriver.exe")
driver.maximize_window()  
#define website to test
driver.get("https://www.google.com/")  
#in google we will send value to textbox search

inputElements = driver.find_elements_by_css_selector('input[name=q]')

for inputElement in inputElements:

	   inputElement.send_keys('MohamedAdel Hsn github') 

       # presses button to search .. 
       
inputElement.send_keys(Keys.ENTER)

results = driver.find_elements_by_xpath('//div[@class="r"]/a/h3')  # finds webresults
results[0].click() # clicks the first one

time.sleep(10)
# close chrome browser
driver.close()
print('sample test case successfully completed')   
