from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
website_url="https://www.youtube.com/"
driver.get(website_url)
time.sleep(3)
driver.quit()