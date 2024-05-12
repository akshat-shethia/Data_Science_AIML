# import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time


class TestNegativeScenarios:
    @pytest.mark.parametrize("username_send,password_send,error_message", [("incorrectUser", "Password123", "Your username is invalid!")])
    @pytest.mark.negative
    @pytest.mark.login
    def test_negative_login(self, username_send, password_send, error_message):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-login/")

        # Username
        username = driver.find_element(
            By.XPATH, "/html//input[@id='username']")
        username.send_keys(username_send)

        # Password
        password = driver.find_element(
            By.XPATH, "/html//input[@id='password']")
        password.send_keys(password_send)

        # Submit button
        submit = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit.click()
        time.sleep(2)

        # Username invalid
        invalid = driver.find_element(By.XPATH, "/html//div[@id='error']")
        assert invalid.is_displayed(), "Error message isnt displayed"

        # Error message text
        invalid_text = driver.find_element(By.XPATH, "/html//div[@id='error']")
        assert invalid_text.text == error_message, "There was no error message received"
