
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://sagar-test-qa.vercel.app/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
username= driver.find_element(*(By.XPATH,"//input[@id='username']"))
password= driver.find_element(*(By.XPATH,"//input[@id='password']"))
username.send_keys("thao")
password.send_keys("1234")
click_me= driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']"))
click_me.click()

alert= driver.switch_to.alert
time.sleep(2)

alert.accept()
time.sleep(2)
driver.close()
driver.quit()
print("click event")

