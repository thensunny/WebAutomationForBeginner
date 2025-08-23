#import webdriver module from selenium package
import time
from selenium import webdriver
#In Selenium 4+, you must import it before using By.XPATH (or By.NAME, etc.).Without it, Python doesn’t know what By means, so you get NameError.
from selenium.webdriver.common.by import By

#instantitate webdriver and launch chrome browser
driver = webdriver.Chrome()
#it is use for maximizing the chrome tab
driver.maximize_window()
#open googl.com web browser
driver.get("https://www.w3schools.com/default.asp")
driver.find_element(By.XPATH, "//a[normalize-space()='PYTHON']").click()

time.sleep(10)
#close the browser window
driver.quit()
