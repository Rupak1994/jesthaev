from selenium.webdriver.common.by import By

class Contact_us:
    def __init__(self, driver):
        self.driver = driver
        self.contactus_xpath = (By.XPATH,"//li[@class='mobile-d-none']//a[normalize-space()='Contact Us']")
        self.full_name = (By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtFullName']")
        self.mobile_number = (By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtMobileNo']")
        self.email = (By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_txtEmail']")
        self.message = (By.XPATH,"//textarea[@id='ctl00_ContentPlaceHolder1_txtMessage']")
        self.submit = (By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_lbtnSubmit']")
        self.reset = (By.XPATH,"//button[normalize-space()='Reset']")


    def open_page(self, url):
        self.driver.get(url)

    def click_contactus(self):
        self.driver.find_element(*self.contactus_xpath).click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def enter_name(self, name):
        phone_element = self.driver.find_element(*self.full_name)
        self.scroll_to_element(phone_element)
        phone_element.send_keys(name)

    def enter_mobile(self, ph):
        phone_element = self.driver.find_element(*self.mobile_number)
        self.scroll_to_element(phone_element)
        phone_element.send_keys(ph)

    def enter_email(self, email):
        phone_element = self.driver.find_element(*self.email)
        self.scroll_to_element(phone_element)
        phone_element.send_keys(email)

    def enter_message(self, msg):
        phone_element = self.driver.find_element(*self.message)
        self.scroll_to_element(phone_element)
        phone_element.send_keys(msg)

    def click_submit(self):
        self.driver.find_element(*self.submit).click()


    def click_reset(self):
        self.driver.find_element(*self.reset).click()
