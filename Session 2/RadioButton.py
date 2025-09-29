#import webdriver module
from datetime import time
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

#instantiate webdiver and launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
#Open URL
driver.get("https://dmytro-ch21.github.io/")
time.sleep(2)
DropdownButton= driver.find_element(By.XPATH, "//a[normalize-space()='Go to Dropdowns']")
DropdownButton.click()
time.sleep(2)

# Find the radio buttons and select those
bmw_radio = driver.find_element(By.XPATH, "//input[@id='radio2']")
tesla_radio = driver.find_element(By.XPATH, "//input[@id='radio4']")

# Click those finded radio button
bmw_radio.click()
print("BMW Selected:", bmw_radio.is_selected ())
time.sleep(2)
tesla_radio.click()
print("Tesla Selected:", tesla_radio.is_selected())
time.sleep(2)

#Browser Close
driver.quit()