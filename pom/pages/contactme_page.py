from selenium.webdriver.common.by import By

class contactme:
    def __init__(self,driver):
        self.driver=driver
        self.yourname_textbox=(By.XPATH,"//input[@id='name']")
        self.youremail_textbox = (By.XPATH,"//input[@id='email']")
        self.message_textbox = (By.XPATH,"//textarea[@id='message']")
        self.sendmessage_btn= (By.XPATH,"//button[normalize-space()='Send Message']")
    def open_page(self,url):
        self.driver.get(url)
    def enter_name(self,fullname):
        self.driver.find_element(*self.yourname_textbox).send_keys(fullname)
    def enter_email(self,email):
        self.driver.find_element(*self.youremail_textbox).send_keys(email)
    def enter_message(self,msg):
        self.driver.find_element(*self.message_textbox).send_keys(msg)
    def click_sendmsg(self):
        self.driver.find_element(*self.sendmessage_btn).click()