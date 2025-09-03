#Task ------------------> ( Open SauceDemo login page )
#1. Find all input fields ( Username and Password ) using find_elements()
#2. Check if they exist.
#3. Enter login details.
#4. Click the Login Button.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(2)
driver.get("https://www.saucedemo.com")
time.sleep(2)

# Find all input fields ( Username and Password ) using find_elements()
input_fields = driver.find_elements(By.TAG_NAME,"input")
#print(len(input_fields)) # how many elements you have found ; len = length will count those.
#Find index of username and password
print(input_fields[0].get_attribute('id'))
print(input_fields[1].get_attribute('id'))
print(input_fields[2].get_attribute('id'))


time.sleep(1) #wait for 2 sec
driver.quit()
