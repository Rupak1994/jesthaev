# automation for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://demoqa.com/alerts/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
click_me= driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()

alert= driver.switch_to.alert
time.sleep(2)

alert.accept()
time.sleep(2)
driver.close()
driver.quit()
print("click event")
