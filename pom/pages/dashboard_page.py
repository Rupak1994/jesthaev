from selenium.webdriver.common.by import By

class Dashboardpage:
    def __init__(self,driver):
        self.driver = driver

    def open_dashboard(self,url):
        self.driver.get(url)


