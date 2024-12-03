from selenium.webdriver.common.by import By

class register:
    def __init__(self, driver):
        self.driver = driver
        self.register_page = (By.XPATH, "//a[@class='btn btn-primary btn-xs']")
        self.mobile_textbox = (By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_mobileRegistration_lblRegisterMobile']")
        self.register_btn = (By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_mobileRegistration_btnRegisterMobileSignUp']")
        self.otp_textbox = (By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_mobileRegistration_lblOtpCode']")
        self.setpincode_textbox = (By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_mobileRegistration_lblPinCode']")
        self.conformpincode_textbox = (By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_mobileRegistration_lblRePinCode']")
        self.submit_btn = (By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_mobileRegistration_btnSumbitPinCode']")

    def Open_page(self, url):
        self.driver.get(url)

    def scroll_to_element(self, element):
        # Scroll the page until the specified element is in view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def open_registerpage(self):
        self.driver.find_element(*self.register_page).click()

    def enter_phone(self,ph):
        phone_element = self.driver.find_element(*self.mobile_textbox)
        self.scroll_to_element(phone_element)
        phone_element.send_keys(ph)

    def click_register(self):
        self.driver.find_element(*self.register_btn).click()

    def enter_otp(self,otp):
        self.driver.find_element(*self.otp_textbox).send_keys(otp)

    def enter_pincode(self,pin):
        self.driver.find_element(*self.setpincode_textbox).send_keys(pin)

    def conform_pincode(self,cpin):
        self.driver.find_element(*self.conformpincode_textbox).send_keys(cpin)

    def click_submit(self):
        self.driver.find_element(*self.submit_btn).click()