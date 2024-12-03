from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys

class register :
    def __init__(self, driver):
        self.driver = driver
        self.firstname_textbox = (By.XPATH, "//input[@placeholder='First Name']")
        self.lastname_textbox = (By.XPATH, "//input[@placeholder='Last Name']")
        self.email_textbox = (By.XPATH, "//input[@placeholder='Email Address']")
        self.mobile_textbox = (By.XPATH, "//input[@placeholder='98XXXXXXXX']")
        self.gender_textbox = (By.XPATH, "//select[@name='gender']")
        self.DoB_textbox = (By.XPATH, "//input[@name='dob']")
        self.password_textbox = (By.XPATH, "//div[1]//div[1]//form[1]//div[2]//div[7]")
        self.confirm_password_textbox = (By.XPATH, "//input[@name='password_confirmation']")
        self.agreement_checkbox= (By.XPATH, "//input[@id='terms-conditions-agrement']")
        self.register_btn = (By.XPATH, "//button[normalize-space()='Register']")

    def Open_page(self, url):
        self.driver.get(url)

    def enter_firstname(self,fname):
        self.driver.find_element(*self.firstname_textbox).send_keys(fname)

    def enter_lastname(self,lname):
        self.driver.find_element(*self.lastname_textbox).send_keys(lname)

    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_phone(self,ph):
        self.driver.find_element(*self.mobile_textbox).send_keys(ph)

    def select_gender(self,gender):
        dropdown = Select(self.driver.find_element(*self.gender_textbox))
        dropdown.select_by_visible_text(gender)

    def enter_dob(self,dob):
        self.driver.find_element(*self.DoB_textbox).send_keys(dob)

    # def enter_password(self, password):
    #     self.driver.find_element(*self.password_textbox).send_keys(password)

    def enter_password(self, password):
        wait = WebDriverWait(self.driver, 10)
        password_field = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))  # Update the locator
        self.driver.execute_script("arguments[0].scrollIntoView();", password_field)
        password_field.send_keys(password)

    # def enter_confirm_password(self, cpassword):
    #     self.driver.find_element(*self.confirm_password_textbox).send_keys(cpassword)

    def enter_confirm_password(self, cpassword):
        wait = WebDriverWait(self.driver, 10)
        confirm_password_field = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@name='password_confirmation']")))  # Update the locator
        self.driver.execute_script("arguments[0].scrollIntoView();", confirm_password_field)
        confirm_password_field.send_keys(cpassword)

    def click_agreement(self):
        self.driver.find_element(*self.agreement_checkbox).click()

    def click_register(self):
        self.driver.find_element(*self.register_btn).click()

