import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome()
    driver.get("https://demo.dealsdray.com/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_function_testing(setup_browser):
    driver = setup_browser
    wait = WebDriverWait(driver, 10)

    username = driver.find_element(By.XPATH, "//input[@id='mui-1']")
    username.clear()
    username.send_keys("prexo.mis@dealsdray.com")

    password = driver.find_element(By.XPATH, "//input[@id='mui-2']")
    password.clear()
    password.send_keys("prexo.mis@dealsdray.com")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)

    assert 'dashboard' in driver.current_url, "Login unsuccessful or not on the dashboard"
    print("Successfully logged in and on the dashboard")

    order = driver.find_element(By.XPATH, '//span[text()="Order"]')
    order.click()
    orders = driver.find_element(By.XPATH, '//span[text()="Orders"]')
    orders.click()

    bulk_orders = driver.find_element(By.XPATH, '//button[text()="Add Bulk Orders"]')
    bulk_orders.click()

    ch_file = driver.find_element(By.XPATH, '//input[@type="file"]')
    ch_file.send_keys("D:\\download\\demo-data.xlsx")
    time.sleep(2)

    import_file = driver.find_element(By.XPATH, '//button[text()="Import"]')
    import_file.click()
    time.sleep(2)

    validate_data = driver.find_element(By.XPATH, '//button[text()="Validate Data"]')
    validate_data.click()
    time.sleep(2)
    alert = Alert(driver)
    alert.accept()
    driver.get_screenshot_as_file("full_screen_screenshot.png")
    print("Test completed successfully")

