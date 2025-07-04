from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_search_product():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)  
    driver.get("https://automationexercise.com/")

    
    try:
        driver.find_element(By.ID, "dismiss-button").click()
    except:
        pass

    
    assert "Automation Exercise" in driver.title

   
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(2)

    assert "Features Items" in driver.page_source
    driver.quit()
