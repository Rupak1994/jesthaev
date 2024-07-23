# automation for chrome browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
# website_url = "https://www.mindrisers.com.np/"
# driver.get(website_url)
# driver.maximize_window()
# time.sleep(3)
# actual_title = driver.title
# expected_title = "Best IT Training Institute in kathmandu, Nepal | Mindrisers Institute of Technology"
# if (actual_title == expected_title):
#     print("title check pass")
# else:
#     print("title check fail")
# driver.quit()


url="https://tax.digitalpalika.org/login/"
driver.get(url)

driver.find_element(By.ID,"username").send_keys("malikacounter5")
driver.find_element(By.ID,"password").send_keys("password")
time.sleep(5)
driver.quit()





