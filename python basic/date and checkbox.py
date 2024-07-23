# automation for chrome browser
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://demoqa.com/automation-practice-form/"
driver.get(url)
driver.maximize_window()
# calculate page height
pg_ht = driver.execute_script("return document.body.scrollHeight")
# scroll down the content
scroll_speed = 300
scroll_iteration = int(pg_ht/scroll_speed)
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
time.sleep(0.4)

fname= driver.find_element(By.XPATH,"//input[@id='firstName']")
lname=driver.find_element(By.XPATH,"//input[@id='lastName']")
email=driver.find_element(By.XPATH,"//input[@id='userEmail']")
gender=driver.find_element(By.XPATH,"//label[normalize-space()='Male']")
mobile=driver.find_element(By.XPATH,"//input[@id='userNumber']")
# dob= driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']")
dob= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='dateOfBirthInput']")))
subject= driver.find_element(By.XPATH,"//input[@id='subjectsInput']")
hobies=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Sports']")))
# picture=
# cur_address=
# state_city=
fname.send_keys("ram")
lname.send_keys("kc")
email.send_keys("rt@xyz.com")
gender.click()
mobile.send_keys("12333")
dob.send_keys("12/04/2024")
time.sleep(3)
subject.send_keys("math")
driver.execute_script("arguments[0].click();", hobies)
time.sleep(5)
driver.quit()

