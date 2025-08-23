
import time
#import webdriver module from selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By

#instantitate webdriver and launch chrome browser
driver = webdriver.Chrome()
#it is use for maximizing the chrome tab
driver.maximize_window()
#Navigate to Google - Open URL
driver.get("https://www.google.com")
time.sleep(2) #wait for 2 sec to let the page load
#Navigate to Saucedemo website - Open URL
driver.get("https://www.saucedemo.com")
time.sleep(2) #wait for 2 sec to let the page load
#Locate Username web element
username = driver.find_element(By.ID,"user-name")
time.sleep(2) #wait for 2 sec to let the page load
#enter username
username.send_keys("standard_user")
#Locate Username web element
password = driver.find_element(By.ID,"password")
time.sleep(2) #wait for 2 sec to let the page load
#enter password
password.send_keys("secret_sauce")
time.sleep(2) #wait for 2 sec
# Locate the login button
login_btn = driver.find_element(By.ID, "login-button")
# Click the login button
login_btn.click()
time.sleep(3) #wait for 2 sec

#browser close
driver.quit()


