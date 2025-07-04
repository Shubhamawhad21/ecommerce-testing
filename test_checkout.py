from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_checkout_page():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://automationexercise.com/")

    driver.execute_script("window.scrollBy(0, 800);")
    driver.find_element(By.XPATH, "(//a[@class='btn btn-default add-to-cart'])[1]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//u[text()='View Cart']").click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "check_out").click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)

    print("Current Page Title:", driver.title)

    assert "Login" in driver.page_source or "Account" in driver.page_source

    driver.quit()
