# automation for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://demoqa.com/text-box"
driver.get(url)
driver.maximize_window()
time.sleep(2)
full_name= driver.find_element(By.XPATH,"//input[@id='userName']")
email= driver.find_element(By.XPATH,"//input[@id='userEmail']")
cur_address = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
permanent_address = driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']")
# submit_but=driver.find_element(By.ID,"submit")
submit_but= driver.find_element(By.XPATH,"//*[@id='submit']")
full_name.send_keys('rupak')
email.send_keys('roopakthapa@gmail.com')
cur_address.send_keys('bhaktapur')
permanent_address.send_keys("ktm")
submit_but.click()
time.sleep(5)
driver.close()