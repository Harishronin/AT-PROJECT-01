"""
Test case ID:TC_login_01

Test objective:
  Successful employee login to OrangeHRM Portal
Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
 1.In the login panel,enter the user name(Test data: “Admin”)
2.Enter the password for ESS User account in the password field (Test data:”admin123”)
3.Click”login”button

 Expected result:
The user is logged successfully
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# test case ID and objective
test_case_id = "TC_login_01"
test_objective = "Successful employee login to OrangeHRM Portal"

# Initialize the WebDriver
driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.

try:
    # Launch the OrangeHRM site
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")

    # login elements
    wait = WebDriverWait(driver, 10)
    
    # Step 1: Enter the username
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")  

    # Step 2: Enter the password
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys("admin123")  

    # Step 3: Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Expected result: Check if login was successful
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # If the Dashboard is visible, the login is successful
    print(f"{test_case_id}: {test_objective} - Passed")
    
except Exception as e:
    print(f"{test_case_id}: {test_objective} - Failed. Error: {str(e)}")
finally:
    # Close the browser
    driver.quit()


"""
Test case ID:TC_login_02

Test objective:
Invalid employee login to orangeHRM portal

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
 1.In the login panel,enter the user name(Test data: “Admin”)
2.Enter the password for ESS User account in the password field (Test data:”admin123”)
3.Click”login”button

 Expected result:
A valid error message displayed for invalid credentials is displayed.

TestCases dealing with the PIM:
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define test case ID and objective
test_case_id = "TC_login_02"
test_objective = "Invalid employee login to OrangeHRM portal"

# Initialize the WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in your PATH

try:
    # Launch the OrangeHRM site and maximize the window
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Initialize explicit wait
    wait = WebDriverWait(driver, 10)

    # Step 1: Enter the username
    username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")  

    # Step 2: Enter an incorrect password
    password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
    password_field.send_keys("wrongpassword")  

    # Step 3: Click the login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()

    # Expected result: Check if the error message is displayed
    error_message = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']"))
    )

    # Validate if the error message matches the expected output
    assert "Invalid credentials" in error_message.text, "Error message not as expected"

    # If the error message is displayed, the test is successful
    print(f"{test_case_id}: {test_objective} - Passed")
    
except AssertionError as ae:
    print(f"{test_case_id}: {test_objective} - Failed. Assertion Error: {str(ae)}")
except Exception as e:
    print(f"{test_case_id}: {test_objective} - Failed. Error: {str(e)}")
finally:
    # Close the browser
    driver.quit()




"""
Test case ID:TC_PIM_01

Test objective:
Add a new employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser
Steps:
1.Go to PIM Module from the left pane in the web page.
2.Click on Add and add new employee details in the page
3.Fill in all the personal details of the employee and click save

Expected Result:
The user should be able to add new employee in the PIM and should see a message successful employee addition.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Set up credentials and WebDriver
username = "Admin"
password = "admin123"  
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Initialize WebDriver 
driver = webdriver.Chrome()

try:
    # Step 1: Open the login page
    driver.get(url)
    driver.maximize_window()
    
    # Step 2: Log in with ESS-User Account
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    
    # Step 3: Wait for the PIM module to be visible and navigate to it
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"))
    ).click()

    # Step 4: Click on "Add" to add a new employee
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))
    ).click()
    
    # Step 5: Fill in the employee details
    first_name = "John"
    middle_name = "A"
    last_name = "Doe"
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    ).send_keys(first_name)
    driver.find_element(By.NAME, "middleName").send_keys(middle_name)
    driver.find_element(By.NAME, "lastName").send_keys(last_name)
    
    # Click save
    driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()
    
    # Step 6: Confirm success
    time.sleep(2)  
    
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Successfully')]"))
        )
        print("Test Passed: Employee was added successfully.")
    except (NoSuchElementException, TimeoutException):
        print("Test Failed: Success message not found.")
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()



"""
Test case ID:TC_PIM_02

Test objective:
Edit an existing employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser
Steps:
1.Go to PIM Module from the left pane in the web page.
2.From the existing list of Employees in the PIM Module.
edit the employee information of the employee and save it.

Expected Result:
The user should be able to edit an existing employee information in the PIM and should see a message successful employee details addition.


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up credentials and WebDriver
username = "Admin"
password = "admin123"  
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the login page
    driver.get(url)
    driver.maximize_window()
    
    # Step 2: Log in with ESS-User Account
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    
    # Step 3: Wait for the PIM module to be visible and navigate to it
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"))
    ).click()

    # Step 4: Select an employee from the list (e.g., the first employee)
    employee_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-table-card'])[1]"))
    )
    employee_card.click()

    # Step 5: Click the Edit button to modify employee details
    edit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Edit']"))
    )
    edit_button.click()
    
    # Step 6: Modify employee details (e.g., first and last names)
    first_name_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    )
    first_name_field.clear()
    first_name_field.send_keys("EditedFirstName")

    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.clear()
    last_name_field.send_keys("EditedLastName")

    # Step 7: Save the updated details
    save_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']"))
    )
    save_button.click()
    
    # Step 8: Confirm the success message appears
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Successfully Saved')]"))
        )
        if success_message:
            print("Test Passed: Employee details were edited successfully.")
    except (NoSuchElementException, TimeoutException):
        print("Test Failed: Success message not found.")
        
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()



"""

Test case ID:TC_PIM_03

Test objective:
Delete an existing employee in the PIM Module

Precondition:
 1.A valid ESS-User Account to login to be available
2.A orangeHRM 3.0 site is launche on compatible browser

Steps:
1.Go to PIM Module from the left pane in the web page.
2.From the existing list of Employees in the PIM Module.delete an existing employee.

Expected Result:
The user should be able to delete an existing employee information in the PIM and should see a message successful deletion.


"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Set up credentials and WebDriver
username = "Admin"
password = "admin123"
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Open the login page
    driver.get(url)
    driver.maximize_window()
    
    # Step 2: Log in with ESS-User Account
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys(username)
    
    # Input password and log in
    driver.find_element(By.NAME, "password").send_keys(password + Keys.RETURN)
    
    # Step 3: Navigate to the PIM module
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']"))
    ).click()

    # Step 4: Select an employee from the list (e.g., the first employee)
    employee_card = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='oxd-table-card'])[1]"))
    )
    employee_card.click()

    # Step 5: Click the Delete button
    delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Delete']"))
    )
    delete_button.click()

    # Step 6: Confirm deletion in the pop-up modal
    confirm_delete_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Yes, Delete')]"))
    )
    confirm_delete_button.click()
    
    # Step 7: Confirm the success message appears
    success_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'Successfully Deleted')]"))
    )
    
    # Check if success message is displayed
    if success_message:
        print("Test Passed: Employee was deleted successfully.")
        
except NoSuchElementException as nse:
    print(f"Test Failed: Element not found. {str(nse)}")
except TimeoutException as te:
    print(f"Test Failed: Operation timed out. {str(te)}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
