
import time
#import webdriver module from selenium package
from selenium import webdriver
from selenium.webdriver.common.by import By

#instantitate webdriver and launch chrome browser
driver = webdriver.Chrome()
#it is use for maximizing the chrome tab
driver.maximize_window()
#Navigate to Google - Open URL
driver.get("https://www.google.com")
time.sleep(2) #wait for 2 sec to let the page load
#Navigate to Saucedemo website - Open URL
driver.get("https://www.saucedemo.com")
time.sleep(1) #wait for 2 sec to let the page load
#Locate Username web element
username = driver.find_element(By.ID,"user-name")
time.sleep(1) #wait for 2 sec to let the page load
#enter username
username.send_keys("visual_user")
#Locate Username web element
password = driver.find_element(By.ID,"password")
time.sleep(1) #wait for 2 sec to let the page load
#enter password
password.send_keys("secret_sauce")
time.sleep(1) #wait for 2 sec
# Locate the login button ; Here we are used the "Relative Xpath" --> //tagname[@attribute='value'] <--- Here tagnam is input; attribute is id; value is login-button. In Chrome Browser there is extension which name is "SelectorsHub", You can also use this to get the Xpath or others things.
login_btn = driver.find_element(By.XPATH, "//input[@id='login-button']")
# Click the login button
login_btn.click()
time.sleep(2) #wait for 2 sec
#locate add to cart
addToCart = driver.find_element(By.XPATH,"//button[contains(@id,'sauce-labs-bolt-t-shirt')]")
addToCart.click()
time.sleep(2) #wait for 2 sec
#Locate the my shopping cart
ShoppingCart= driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']")
ShoppingCart.click()
time.sleep(2)

#Now we will see, how the TEXT METHODS works.  Syntax: //tagname[text() = 'Exact Text Here']
# When to use it: Use text() when the text of the element is static and won't change. For example, to find a button with the text "Log In" exactly as it appears. Ekhane text ta exact same copy kora lagbe.

#text() ---> Locate the Continue Shopping button with the TEXT methode and Click on this.
ContinueButton= driver.find_element(By.XPATH,"//button[text()= 'Continue Shopping']")
ContinueButton.click()
time.sleep(2)

#contains() ---> you can ignore the dynamic part and just focus on what's always the same; Syntax: //tagname[contains(@attribute, 'value')]; When attributes value will be so long or it is dynamically changing then we use the contains methode and copy some partial match value not the full value.
#Locate the addToCart using the contains methode
addToCart2=driver.find_element(By.XPATH,"//button[contains(@id,'sauce-labs-bike-ligh')]")
addToCart2.click()

time.sleep(8) #wait for 5 sec
#browser close
driver.quit()


