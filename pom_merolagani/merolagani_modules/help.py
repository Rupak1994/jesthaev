from selenium.webdriver.common.by import By
import time

class Help:
    def __init__(self, driver):
        self.driver = driver
        self.help_xpath = (By.XPATH,"//button[normalize-space()='Help']")
        self.videotutorial_xpath = (By.XPATH,"//ul[@role='menu']//a[normalize-space()='Video Tutorials']")
        self.free_registration = (By.XPATH,"//a[normalize-space()='1. Free user registration']")
        self.portfolio = (By.XPATH,"//a[normalize-space()='3. How to add portfolio in merolagani ?']")

    def open_page(self, url):
        self.driver.get(url)

    def open_videotutorial(self):
        self.driver.find_element(*self.help_xpath).click()
        time.sleep(2)
        self.driver.find_element(*self.videotutorial_xpath).click()
        time.sleep(2)
        self.driver.find_element(*self.free_registration).click()
        time.sleep(5)

    def open_portfoliotutorial(self):
        self.driver.find_element(*self.portfolio).click()
        time.sleep(5)


