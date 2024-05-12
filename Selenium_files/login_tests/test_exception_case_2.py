from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestExceptionCase1:
    @pytest.mark.exception
    def test_exception_case_1(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Finding the add button
        add_button = driver.find_element(
            By.XPATH, "/html//button[@id='add_btn']")
        add_button.click()

        # Adding a custom wait for the success message
        wait = WebDriverWait(driver, 10)
        second_row = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']"))
        )

        second_row.send_keys("Hi This is Akshat!")

        # Pressing the save button
        save_button = driver.find_element(
            By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")
        save_button.click()

        # Verifying the Success Message
        success_message = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "/html//div[@id='confirmation']")))
        assert success_message.is_displayed(), "There was no success message displayed"
