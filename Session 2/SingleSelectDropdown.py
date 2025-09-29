#import webdriver module
from datetime import time
from selenium import webdriver # To interact with the browser
import time #This module called for add delays ( Demonstration purposes)
from selenium.webdriver.common.by import By # To locate elements on the webpage
from selenium.webdriver.support.select import Select # To handle the drop-down menu.

#instantiate webdiver and launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()
#Open URL
driver.get("https://dmytro-ch21.github.io/")
time.sleep(2)
DropdownButton= driver.find_element(By.XPATH, "//a[normalize-space()='Go to Dropdowns']")
DropdownButton.click()
time.sleep(2)

# Locate the Single-Select-Dropdown
dropdownMenu = Select (driver.find_element(By.ID, "carBrands"))
time.sleep(2)
#Select options by visible text, value, and index.
dropdownMenu.select_by_visible_text("Mercedes")
print("Selected Option:", dropdownMenu.first_selected_option.text)
time.sleep(2)

dropdownMenu.select_by_value("audi")
print("Selected Option:", dropdownMenu.first_selected_option.text)
time.sleep(2)

dropdownMenu.select_by_index(1)  #Index Starts at 0
print("Selected Option:", dropdownMenu.first_selected_option.text)
time.sleep(2)

driver.quit()
