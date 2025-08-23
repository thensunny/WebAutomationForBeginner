#1. How to navigate Browser
# a) Opening a Browser: We already did this in the last example.
# b) Navigating URLs:

#--------------> Our Navigation Scenario <-----------------#
# Step1: Open Chrome Browser.
# Step2: Navigate to Google.
# Step3: Navigate to Youtube.
# Step4: Go back to Google.
# Step5: Go forward to Youtube.
# Step6: Refresh the current page. (Youtube)
# Step7: Close the Browser.

import time
#import webdriver module from selenium package
from selenium import webdriver
#instantitate webdriver and launch chrome browser
driver = webdriver.Chrome()
#it is use for maximizing the chrome tab
driver.maximize_window()
#Navigate to Google - Open URL
driver.get("https://www.google.com")
time.sleep(2) #wait for 2 sec to let the page load
#Navigate to YouTube - Open URL
driver.get("https://www.youtube.com")
time.sleep(2) #wait for 2 sec to let the page load
#go back to Google
driver.back()
time.sleep(2) #wait for 2 sec to let the page load
#go forward to Youtube
driver.forward()
time.sleep(2) #wait for 2 sec to let the page load
#Refresh the current page
driver.refresh()
time.sleep(2) #wait for 2 sec to let the page load
# How long time the window stay open
time.sleep(10)
#close the browser window
driver.quit()
