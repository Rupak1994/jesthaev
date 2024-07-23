from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
website_url = "https://www.mindrisers.com.np/"
driver.get(website_url)
driver.maximize_window()
time.sleep(3)
# calculate page height
pg_ht = driver.execute_script("return document.body.scrollHeight")
# scroll down the content
scroll_speed = 300
scroll_iteration = int(pg_ht/scroll_speed)
for _ in range(scroll_iteration):
    driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    time.sleep(0.1)
web_title = driver.title
print(f"scroll iteration::{scroll_iteration}")
print(f"website title:{web_title}")
print("code run successfully")
driver.quit()
