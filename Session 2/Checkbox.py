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
#find check box
ford_checkbox = driver.find_element(By.ID,"option1")
if not ford_checkbox.is_selected():
    ford_checkbox.click()  #select ford checkbox
time.sleep(2)
bmw_checkbox = driver.find_element(By.ID,"option2")
if not bmw_checkbox.is_selected():
    bmw_checkbox.click()
time.sleep(2)
tesla_checkbox = driver.find_element(By.ID,"option4")
if not tesla_checkbox.is_selected():
    tesla_checkbox.click()
time.sleep(2)
#Verify selection
print("Is ford selected: ", ford_checkbox.is_selected())
print("Is BMW selected: ", bmw_checkbox.is_selected())
print("is Tesla selected: ", tesla_checkbox.is_selected())
time.sleep(8)
driver.quit()



