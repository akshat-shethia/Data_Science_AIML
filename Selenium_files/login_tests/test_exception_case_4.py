from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


class TestExceptionCase1:
    @pytest.mark.exception
    @pytest.mark.invisibility
    def test_exception_case_1(self):
        driver = webdriver.Chrome()
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Finding the add button
        add_button = driver.find_element(
            By.XPATH, "/html//button[@id='add_btn']")
        add_button.click()

        # Adding a custom wait for the success message
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.invisibility_of_element_located(
            (By.ID, "instructions"))), "Instruction text element is still present!"
