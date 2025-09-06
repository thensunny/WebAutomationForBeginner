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
# print(input_fields[0].get_attribute('id'))
# print(input_fields[1].get_attribute('id'))
# print(input_fields[2].get_attribute('id'))

          # You can print this with For Loop

# index =0
# for field in input_fields:
#     print(f"Index {index} : {field.get_attribute('id')}")
#     index += 1

#Enter username
input_fields[0].send_keys("standard_user")
time.sleep(2)
#Enter Password
input_fields[1].send_keys("secret_sauce")
time.sleep(2)
# Click on submit button
input_fields[2].click()

#List all the Products
products = driver.find_elements(By.XPATH,"//div[@class='inventory_item_name ']")
print("Products List")
for item  in products:
    print(item .text)  #Text methode to extract visible text

time.sleep(8) #wait for 8 sec
driver.quit()
