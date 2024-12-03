from selenium.webdriver.common.by import By

class login :
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox = (By.XPATH, "//input[@id='username']")
        self.password_textbox = (By.XPATH, "//input[@id='password']")
        self.submit_btn = (By.XPATH, "//button[normalize-space()='Sign In']")
        self.eye_button = (By.XPATH,"//div[1]//div[1]//div[1]//form[1]//div[2]//span[1]//button[1]//i[1]")

    def Open_page(self, url):
        self.driver.get(url)

    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()

    def click_eye_btn(self):
        self.driver.find_element(*self.eye_button).click()
