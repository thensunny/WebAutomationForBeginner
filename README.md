# WebAutomationForBeginner
A beginner-friendly project to learn web automation with Python and Selenium. Each script has line-by-line comments, and examples are organized by tasks (navigation, locators, waits, forms, etc.). The README explains setup, how to run, and common pitfalls in detail.

## **File Overview: `Verify_Setup.py`**

This file is a straightforward **Selenium** script designed to confirm that your development environment is correctly configured. It acts as a "hello world" program for web automation, ensuring that your Python, Selenium library, and Chrome driver are all installed and working together.

This script is an excellent tool to use when starting a new project or after making any changes to your system.

### **Key Functions of the Script**

1.  **Browser Launch**: The script uses `webdriver.Chrome()` to launch a new Chrome browser window. This confirms that Python, Selenium, and the Chrome driver can communicate successfully.

2.  **Window Maximization**: The `driver.maximize_window()` command expands the browser window to fill the entire screen.

3.  **Website Navigation**: It uses the `driver.get()` method to navigate to the `https://www.w3schools.com` website, verifying that Selenium can successfully open a specific URL.

4.  **Element Interaction**: The script then uses `By.XPATH` to find and click the "PYTHON" link. The `normalize-space()` function is a key part of this, as it handles any extra spaces or line breaks in the text, making the locator more robust. This step confirms that Selenium can not only navigate to a page but also locate and interact with a specific element on it.

5.  **Browser Close**: Finally, the `driver.quit()` command is used to close the browser window. This is a crucial step for ending the automation session and freeing up system resources.

This file provides a simple and effective way to confirm that your web automation setup is ready to go.
(From Selenium 4.6+, ChromeDriver is auto-managed by Selenium Manager.)

## **File Overview: `Basic.py`**

This file is a simple yet fundamental **Selenium** script designed to demonstrate basic browser navigation commands. It simulates a user's journey through a web browser, showing how to move between different web pages, go back and forth in the browser history, and refresh the current page.

This script is an excellent starting point for understanding how to control a browser programmatically.

---

### **Key Functions of the Script**

1.  **Browser Initialization**: The script begins by importing the necessary `webdriver` from Selenium and initializing a Chrome browser instance. It then maximizes the browser window for a full-screen view.

2.  **URL Navigation (`driver.get()`)**: The script navigates to two different URLs in sequence: Google and YouTube. This demonstrates the core function of the `driver.get()` command, which loads a new web page in the current browser window.

3.  **Browser History (`driver.back()` and `driver.forward()`)**: The script simulates a user's experience by using the `driver.back()` command to return to the previous page (Google). It then uses `driver.forward()` to move forward in the browser's history to return to YouTube. This showcases how to control the browser's navigation history.

4.  **Page Refresh (`driver.refresh()`)**: The `driver.refresh()` command is used to reload the current page (YouTube). This is a common and useful function in automation for handling dynamic content or ensuring the page is in its latest state.

5.  **Cleanup**: The script includes a `time.sleep()` command to keep the browser open for a few seconds so you can see the actions, before finally using `driver.quit()` to close the browser and end the session. This is an essential step to ensure system resources are properly released.

This file provides a clear, step-by-step example of how to handle basic browser navigation using Selenium, which is a core skill for any web automation project.


---------------------------------------->

### **Project Overview: Web Automation with Selenium**
## ***File Overview: Basic_Locators.py***

This project uses **Selenium**, a powerful tool for web automation, to perform a series of actions on two websites: Google and Sauce Demo. The script is written in Python and uses the `webdriver` to control a Chrome browser, simulating a user's interactions like navigating to a URL, logging in, adding items to a cart, and clicking buttons.

This script serves as a practical example for anyone new to web automation. It demonstrates fundamental concepts such as:

* **Browser Management**: Opening, maximizing, and closing the browser.
* **Navigation**: Visiting different web pages.
* **Element Interaction**: Finding web elements and performing actions like typing text or clicking buttons.
* **Locator Strategies**: Using different methods (`ID`, `XPath`, `contains()`, `text()`) to locate elements on a page.

---

### **Prerequisites**

Before running this code, you'll need the following installed on your machine:

* **Python 3**: The programming language used for the script.
* **Selenium Library**: The automation framework. You can install it using `pip`:
    ```bash
    pip install selenium
    ```
* **Chrome Driver**: A special driver that allows Selenium to control the Chrome browser. Make sure its version is compatible with your Chrome browser version.

---

### **Code Walkthrough**

The script is a step-by-step automation flow. Below is a breakdown of what each part of the code does:

#### **1. Setup and Navigation**
The script starts by initializing the Chrome browser and maximizing the window. It then navigates to `google.com` and `saucedemo.com`. The `time.sleep()` commands are used to pause the script, giving the pages time to load before the next action.

#### **2. Login**
The script finds the username and password fields using their unique `ID` attributes. It then uses the `send_keys()` method to enter the login credentials (`"visual_user"` and `"secret_sauce"`). Finally, it locates the login button using an **XPath** and clicks it to log in.

* **XPath**: This is a powerful locator that finds elements by navigating the structure of the HTML page. We use it here to locate the login button. The syntax `//input[@id='login-button']` means: "Find an `<input>` tag that has an `id` attribute with the value `login-button`."

#### **3. Adding Items to Cart with `contains()`**
After logging in, the script locates and clicks the "add to cart" button for a t-shirt. It uses the `contains()` method in the XPath to find the button.

* **`contains()` Method**: This is extremely useful when an element's attribute value is too long or contains a dynamic part that changes. Instead of copying the entire attribute value, we can use `contains()` to match just a **partial string**. For example, `//button[contains(@id,'sauce-labs-bolt-t-shirt')]` finds a button with an `id` that includes the text "sauce-labs-bolt-t-shirt", making the locator more flexible.

#### **4. Navigating with `text()`**
The script then clicks on the shopping cart icon and proceeds to the cart page. From there, it needs to find the "Continue Shopping" button. It does this using the `text()` method.

* **`text()` Method**: This method is used when you need to find an element based on its **exact text content**. This is ideal for static, unchanging text on buttons or labels. The XPath `//button[text()= 'Continue Shopping']` will only find a button with the precise text "Continue Shopping".

#### **5. Second Item & Cleanup**
Finally, the script adds a second item to the cart using the `contains()` method again. After all the actions are completed, `driver.quit()` is called to close the browser and end the session.

This script provides a strong foundation for understanding how to interact with web elements using different locator strategies, which is a key skill for any web automation project.

## Best Practice for Beginners 
1. Prefer Relatuve Xpath(//tagname[@attribute='value']) over Absoulte Xpath(/html/body/div/...)
2. Use contains() and text() for dynamic elements.
3. Avoid long, complex Xpath expression.
4. Use and/or for multiple condition.
5. Test Xpath in Chrome DevTool in inspect- ctrl+f ( There is a Chrome extension also "SelectorsHub")


## **File Overview: `Xpath_Condition.py`**

This file is a comprehensive Selenium script designed to teach fundamental and advanced element location strategies. It demonstrates how to find and interact with web elements using a variety of powerful techniques, making it an excellent resource for beginners learning web automation. The script navigates to the Sauce Demo website and performs a series of actions, including logging in, adding items to a cart, and navigating product pages.

This file provides practical examples of:

* **Compound Locators:** Using `AND` and `OR` conditions to create precise and flexible locators.
* **Indexing:** Locating an element based on its position in a list of similar elements.
* **Text-Based Locators:** Finding hyperlinks using `By.LINK_TEXT` and `By.PARTIAL_LINK_TEXT`.

***

### **Key Functions of the Script**

1.  **Login with `AND` and `OR` Conditions**: The script first logs into the Sauce Demo website. It uses an **`AND`** condition to find the username input field, combining its `type` and `id` attributes for a unique match. It then uses an **`OR`** condition to locate the password field, providing a robust locator that works for one of two possible attribute values.

2.  **Add to Cart by Index**: To demonstrate a different method, the script finds and clicks an "Add to Cart" button by its position using an XPath index `[5]`. This method is useful when an element has no unique attributes, but it's important to note that this is a **fragile** locator that can break if the page structure changes.

3.  **Navigate with `By.LINK_TEXT`**: The script navigates to a specific product page ("Sauce Labs Fleece Jacket") using the `By.LINK_TEXT` locator. This is a reliable method for finding links with static, exact text.

4.  **Navigate with `By.PARTIAL_LINK_TEXT`**: The script then uses `By.PARTIAL_LINK_TEXT` to go to another product page by searching for a partial string in the link text ("Backpack"). This shows how to handle long or dynamic link names.

5.  **Cleanup**: Finally, the script performs a series of `driver.back()` and `driver.quit()` commands to properly close the browser and end the automation session.


## **File Overview: `Css_Selector.py`**

This file is a straightforward Selenium script that demonstrates how to use **CSS Selectors** to find and interact with web elements. It performs a simple login action on the Sauce Demo website, showcasing CSS selectors as a reliable and powerful alternative to XPath.

The script highlights key CSS selector syntax, including:

* **By Class Name**: Using the dot (`.`) syntax.
* **By ID**: Using the hash (`#`) syntax.
* **By Attribute**: Using square brackets (`[]`).

---

### **Key Functions of the Script**

1.  **Login with CSS Selectors**: The script navigates to the Sauce Demo login page and uses three different CSS selector methods to complete the login process.

    * **Username Field (`.input_error.form_input`)**: This demonstrates selecting an element that has **multiple classes**. By chaining the class names with a dot (`.`) and no spaces, the selector precisely targets the username input field.

    * **Password Field (`#password`)**: This shows the preferred method for locating elements with a unique `id`. The hash (`#`) symbol provides a quick and reliable way to find the password field.

    * **Login Button (`input[id='login-button']`)**: This combines a tag name (`input`) with an attribute selector (`[id='login-button']`) to uniquely identify the login button. This method is highly specific and robust.

2.  **Browser Cleanup**: After performing the login, the script waits for 5 seconds to allow you to see the result, then closes the browser with `driver.quit()`.

This file is an excellent resource for understanding how to write clear, efficient, and robust locators using CSS selectors, which are an essential tool in any web automation project.


