from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# Install and use Microsoft Edge WebDriver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))



website_url = "https://www.mindrisers.com.np/"
driver.get(website_url)
time.sleep(3)

actual_title = driver.title
expected_title = "Best IT Training Institute in kathmandu, Nepal | Mindrisers Institute of Technology"

if actual_title == expected_title:
    print("Title check passed")
else:
    print("Title check failed")

driver.quit()
