from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url="https://www.mindrisers.com.np/contact-us/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

# name= driver.find_element(By.XPATH,"//input[@name='name']")
name= driver.find_element(*(By.XPATH,"//input[@placeholder='Name']"))
# email=driver.find_element(By.XPATH,"//input[@name='email']")
email=driver.find_element(By.XPATH,"//input[@placeholder='Email']")

# ph= driver.find_element(By.XPATH,"//input[@name='mobile_no']")
ph= driver.find_element(By.XPATH,"//input[@placeholder='Phone']")

subject= driver.find_element(By.XPATH,"//input[@name='subject']")
anyqueries= driver.find_element(By.XPATH,"//textarea[@name='message']")

name.send_keys("rupak")
email.send_keys("xyz@email")
ph.send_keys("980000000")
subject.send_keys("qa course")
anyqueries.send_keys("i am intersted in your qa program. ")
# blog=driver.find_element(By.XPATH,"//*[@id='navbar']/div/div/div/ul[2]/li[1]/a")
# blog.click()
time.sleep(5)
driver.close()


