#By.CSS_SELECTOR: This is an extremely powerful and versatile locator. It's often faster and more readable than XPath. It can locate elements based on their ID, class, and any other attribute, or by their relationship to other elements. It's a must-know.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from Session1_Testing.Basic_Locators import login_btn

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(2)
driver.get("https://www.saucedemo.com")
time.sleep(2)
#Find the username field using the CSS Selectors --> using .className, We can also use the #idName, tag_name, [attribute='value'], tag_name[attribute='value'].
username = driver.find_element(By.CSS_SELECTOR,".input_error.form_input") #(here 2 css that is why 2 dot)
username.send_keys("visual_user")
time.sleep(3)
#Find the Password field using the Class Selector ( #idName )
password = driver.find_element(By.CSS_SELECTOR,"#password")
password.send_keys("secret_sauce")
time.sleep(3)
# Find the login button using CSS Selector -->  tag_name[attribute='value']
login_btn = driver.find_element(By.CSS_SELECTOR,"input[id='login-button']")
login_btn.click()
time.sleep(5)
driver.quit()


