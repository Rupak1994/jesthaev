from selenium.webdriver.common.by import By

class aboutyourself:
    def __init__(self,driver):
        self.driver=driver
        self.fullname_textbox=(By.XPATH,"//input[@id='fullname']")
        self.phone_textbox=(By.XPATH,"//input[@id='phone']")
        self.email_textbox = (By.XPATH,"//input[@id='email']")
        self.hobby_textbox = (By.XPATH,"//input[@id='hobby']")
        self.submit_btn= (By.XPATH,"//button[normalize-space()='Submit']")
    def open_page(self,url):
        self.driver.get(url)
    def enter_fullname(self,fullname):
        self.driver.find_element(*self.fullname_textbox).send_keys(fullname)
    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)
    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)
    def enter_hobby(self,hobby):
        self.driver.find_element(*self.hobby_textbox).send_keys(hobby)
    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()