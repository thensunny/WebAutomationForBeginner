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
Password = driver.find_element(By.XPATH,"//input[@type='password' or @type='passkeys']")
Password.send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
time.sleep(5)

#Finding elements by Index
#Finding elements by index in XPath is a method for selecting a specific element from a group of similar elements based on its position. It works by appending a number inside square brackets [] to the XPath expression. The index starts at 1, not 0, which is a common point of confusion for those familiar with array indexing in programming languages.
# Syntax --> (//tagname)[index] , (//tagname[@attribute='value'])[index]
addToCart5 = driver.find_element(By.XPATH,"(//button)[5]")
addToCart5.click()
time.sleep(2)

#Finding the product link for Sauce Labs Fleece Jacket By.Link_TEXT
#By.LINK_TEXT is a locator strategy in Selenium that finds an element (specifically an <a> tag) based on its exact, visible text. It is used for finding hyperlinked text on a webpage, such as a "Home" or "Contact Us" link.
#Syntax : driver.find_element(By.LINK_TEXT, "Exact Link Text Here")
productLink = driver.find_element(By.LINK_TEXT,"Sauce Labs Fleece Jacket")
productLink.click()
time.sleep(2)

getBack= driver.find_element(By.XPATH,"//button[@id='back-to-products']")
getBack.click()
time.sleep(2)

#Finding the product link for Sauce Labs Fleece Jacket By.PARTIAL_Link_TEXT
productLink1 = driver.find_element(By.PARTIAL_LINK_TEXT,"Backpack")
productLink1.click()
time.sleep(8) #WAIT FOR 5 SECONDS
driver.quit()

