from selenium import webdriver
import time

def test_homepage_loads():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    time.sleep(2)

    assert "Automation" in driver.title
    driver.quit()
