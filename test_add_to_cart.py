from selenium import webdriver
import time

def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://automationexercise.com/")
    time.sleep(2)

    driver.execute_script("window.scrollBy(0, 800);")
    time.sleep(2)
    driver.find_element("xpath", "(//a[@class='btn btn-default add-to-cart'])[1]").click()
    time.sleep(2)

    driver.find_element("xpath", "//button[text()='Continue Shopping']").click()
    time.sleep(2)

    driver.find_element("xpath", "//a[@href='/view_cart']").click()
    time.sleep(2)

    assert "Shopping Cart" in driver.page_source
    driver.quit()
