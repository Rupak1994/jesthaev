# import pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()

def test_google_search(driver):
    url= "https://www.google.com/"
    driver.get(url)
    search_box= driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search_box.send_keys("mindrisers.com.np")
    driver.maximize_window()
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    first_link= driver.find_element(*(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    first_link.click()
    time.sleep(4)
    print("2nd pytest successfull")


