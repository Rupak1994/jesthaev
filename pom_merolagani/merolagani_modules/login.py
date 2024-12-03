import time
from selenium.webdriver.common.by import By

class login :
    def __init__(self, driver):
        self.driver = driver
        self.login_page = (By.XPATH,"//span[normalize-space()='Log In']")
        self.phone_textbox = (By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_login1_txtEmail']")
        self.password_textbox = (By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_login1_txtPassword']")
        self.login_btn = (By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_login1_lbtnLogin']")
        self.eye_button = (By.XPATH,"//i[@id='eyes']")
        self.logout_btn = (By.XPATH,"//a[@class='dropdown-toggle']//span[@class='icon-user']")
        self.logout = (By.XPATH,"//ul[@class='dropdown-menu']//a[normalize-space()='Log Out']")

    def Open_page(self, url):
        self.driver.get(url)

    def open_loginpage(self):
        self.driver.find_element(*self.login_page).click()

    def enter_phone(self,ph):
        self.driver.find_element(*self.phone_textbox).send_keys(ph)

    def enter_pin(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def click_eye_btn(self):
        self.driver.find_element(*self.eye_button).click()

    def click_logout(self):
        self.driver.find_element(*self.logout_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.logout).click()
        time.sleep(2)