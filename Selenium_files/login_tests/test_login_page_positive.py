from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import pytest


class TestPositiveScenarios:

    @pytest.mark.positive  # Marking the positive test
    @pytest.mark.login  # Marking the login test
    def test_positive_login(self):
        driver = webdriver.Chrome()
        # Wait for 5 seconds before opening the webpage
        time.sleep(1)
        # Accessing the website
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Wait for 1 seconds before closing the webpage
        time.sleep(1)

        # Type username of student in the username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Same for the password field
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys("Password123")

        # Selecting the button
        submit_button_locator = driver.find_element(
            By.XPATH, "/html//button[@id='submit']")
        submit_button_locator.click()  # no commands are required inside

        # Checking if the url matches https://practicetestautomation.com/logged-in-successfully/
        # driver can be assumed to be the current website itself
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Checking if the new page contains the word congratulations
        congratulations_locator = driver.find_element(
            By.XPATH, "//div[@id='loop-container']//article//h1[@class='post-title']")
        actual_text = congratulations_locator.text
        assert actual_text == "Logged In Successfully"

        # Checking for logout button
        logout_locator = driver.find_element(
            By.XPATH, "/html//div[@id='loop-container']/div/article//a[@href='https://practicetestautomation.com/practice-test-login/']")
        assert logout_locator.is_displayed()

        time.sleep(1)
        # Clicking the logout button
        logout_clicker = driver.find_element(
            By.XPATH, "/html//div[@id='loop-container']/div/article//a[@href='https://practicetestautomation.com/practice-test-login/']")
        logout_clicker.click()
