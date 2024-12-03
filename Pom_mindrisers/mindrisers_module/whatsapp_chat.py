import time
from selenium.webdriver.common.by import By


class chat:
    def __init__(self, driver):
        self.driver = driver
        self.whatsapp = (By.XPATH,"//img[@alt='WhatsApp Icon']")
        self.msg_box = (By.XPATH,"//input[@id='userMessage']")
        self.send_msg = (By.XPATH,"/html[1]/body[1]/div[1]/div[2]/div[2]/div[2]/form[1]/button[1]/*[name()='svg'][1]/*[name()='path'][1]")


    def open_page(self, url):
        self.driver.get(url)

    def open_chat(self):
        self.driver.find_element(*self.whatsapp).click()
        time.sleep(1)
        self.driver.find_element(*self.msg_box).click()
        time.sleep(1)

    def start_chat(self,msg):
        self.driver.find_element(*self.msg_box).send_keys(msg)

    def send_message(self):
        self.driver.find_element(*self.send_msg).click()