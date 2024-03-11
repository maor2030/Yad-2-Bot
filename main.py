from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

import time

# Function to bypass login
def bypass_login(driver, email, password):
    # Open the login page
    driver.get("https://www.yad2.co.il/personal/my-ads")

    try:
        # Wait for the email field to be present
        email_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_field.send_keys(email)

        # Find and fill in the password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Submit the login form
        password_field.send_keys(Keys.RETURN)
    except TimeoutException:
        print("Timeout: Email field not found on the page.")


# Function to hover over the button
def hover_over_button(driver):
    # Wait for the button to be visible
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "button_default-tertiary__0G2dM"))
    )
    # Perform hover action
    ActionChains(driver).move_to_element(button).perform()

if __name__ == "__main__":
    # Set up Edge options
    edge_options = Options()
    edge_options.use_chromium = True

    # Set up the web driver for Microsoft Edge
    driver = webdriver.Edge(options=edge_options)

    # Bypass login
    email = "email"
    password = "password"
    bypass_login(driver, email, password)

    # Loop to continuously hover over the button every 5 hours
    while True:
        hover_over_button(driver)
        time.sleep(5 * 3600)  # 5 hours in seconds
