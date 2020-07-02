# Social-Media-Bots
Social media bots is a collection of python tutorials that enable you to control automatically of any website Especial social media websites like (facebook , messenger , whatsapp , instagram , etc...) using selenium webDriver tools and python programming language.
## Setup tools 
Before we will create web bots we should install [Selenium web driver](https://www.selenium.dev/) in python from cmd using pip tool
```
python -m pip install -U Selenium  
```
if you want to make your login data in external properties file, you can use [jproperties](https://pypi.org/project/jproperties/) lib in your project by using pip 
```
python -m pip install jproperties 
```
Example for properties file :-
```
username=YOUR_USERNAME
pass=YOUR_PASSWORD

```
Reading data from properties file in python
```python
   from jproperties import Properties 
   
   #preparing properties object to read data 
   configs = Properties()
   
   #load properties file
with open(r'C:\Users\Owner\Desktop\pythonTest\config.properties', 'rb') as config_file:
	configs.load(config_file)
  
  # get data from file as username and password using keys  
   username = configs.get('username').data   #YOUR_USERNAME
   password = configs.get('pass').data       #YOUR_PASSWORD

```
