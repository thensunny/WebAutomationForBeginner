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

#Select multiple checkboxes using find_elements method
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
for checkbox in checkboxes:
  #if not checkbox.is_selected():  # This line we should use that time when I want to ignore default selected option. It will help us if checkbox is selected then it won't click on that Becasue if it will click again then it will be unselected.
    checkbox.click()
time.sleep(8)
driver.quit()