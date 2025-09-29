#import webdriver module
from datetime import time

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#instantiate webdiver and launch chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
#Open URL
driver.get("https://dmytro-ch21.github.io/")
time.sleep(2)

#Fetch windows title and Print
print("window title: ", driver.title)
#Fetch url and print
print("url: ", driver.current_url)
time.sleep(7)
driver.quit()