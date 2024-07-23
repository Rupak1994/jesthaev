# automation for firefox browser
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
website_url = "https://www.mindrisers.com.np/"
driver.get(website_url)
time.sleep(3)
actual_title = driver.title
expected_title = "Best IT Training Institute in kathmandu, Nepal | Mindrisers Institute of Technology"
if (actual_title == expected_title):
    print("title check pass")
else:
    print("title check fail")
driver.quit()