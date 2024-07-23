import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(1)
    yield driver
    driver.close()
@pytest.mark.parametrize("username,password",[
    ("TestQA","password"),#valid username and password
    ("invalid","password"),#invaid username and password
                           ])
def test_login(driver,username,password):
    driver.get("https://sagar-test-qa.vercel.app/")
    username_field= driver.find_element(By.XPATH,"//input[@id='username']")
    password_field= driver.find_element(By.XPATH,"//input[@id='password']")
    login_btn= driver.find_element(By.XPATH,"//button[normalize-space()='Login']")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_btn.click()
    try:
        alert=driver.switch_to.alert
        # alert_text= alert.text
        alert.accept()
        print(f"invalid username or password for {username}")
    except:
        time.sleep(2)
        page_source=driver.page_source
        if "Welcome to the Dashboard" in page_source:
            print(f"login successful for{username}")
    else:
        print(f"unexpected error or login failed for {username}")


