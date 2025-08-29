#Finding elements using Multiple Condition (AND , OR)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com")
time.sleep(2)
driver.get("https://www.saucedemo.com")
time.sleep(2)
# AND Condition ------------------>
#Use the AND operator when you need to find an element that matches all the conditions you provide. This is especially useful for uniquely identifying an element when a single attribute or text is not enough.
#The syntax is: //tagname[@attribute1='value1' and @attribute2='value2']
Username = driver.find_element(By.XPATH,"//input[@type='text' and @id='user-name' ]")
time.sleep(2)
Username.send_keys("standard_user")
time.sleep(2)
#OR condition ---------------------->
#The OR operator is used to find an element that satisfies at least one of the specified conditions. This makes your locators flexible, allowing them to match an element that might have one of several possible attributes or text values.
#//tagname[@attribute1='value1' or @attribute2='value2']
#//button[text()='Log In' or text()='Sign In'] (This example will clear the concept more easily.
Password = driver.find_element(By.XPATH,"//input[@type='password' or @type='passkey']")
Password.send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(8)
driver.quit()


#Finding elements by Index