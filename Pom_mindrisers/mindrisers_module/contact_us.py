# import time
# from selenium.webdriver.common.by import By
#
# class contact_us :
#     def __init__(self, driver):
#         self.driver = driver
#         self.name_textbox = (By.XPATH, "//input[@placeholder='Name']")
#         self.email_textbox = (By.XPATH, "//input[@placeholder='Email']")
#         self.phone_textbox = (By.XPATH, "//input[@placeholder='Phone']")
#         self.subject_textbox = (By.XPATH, "//input[@placeholder='Subject']")
#         self.queries_textbox = (By.XPATH, "//textarea[@placeholder='Queries']")
#         self.submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")
#
#     def Open_page(self, url):
#         self.driver.get(url)
#
#     def enter_name(self,name):
#         self.driver.find_element(*self.name_textbox).send_keys(name)
#
#     def enter_email(self,email):
#         self.driver.find_element(*self.email_textbox).send_keys(email)
#
#     def enter_phone(self, phone):
#         self.driver.find_element(*self.phone_textbox).send_keys(phone)
#
#     def enter_subject(self, subject):
#         self.driver.find_element(*self.subject_textbox).send_keys(subject)
#
#     def enter_queries(self, queries):
#         self.driver.find_element(*self.queries_textbox).send_keys(queries)
#
#     def click_submit(self):
#         self.driver.find_element(*self.submit_btn).click()

from selenium.webdriver.common.by import By

class contact_us:
    def __init__(self, driver):
        self.driver = driver
        self.name_textbox = (By.XPATH, "//input[@placeholder='Name']")
        self.email_textbox = (By.XPATH, "//input[@placeholder='Email']")
        self.phone_textbox = (By.XPATH, "//input[@placeholder='Phone']")
        self.subject_textbox = (By.XPATH, "//input[@placeholder='Subject']")
        self.queries_textbox = (By.XPATH, "//textarea[@placeholder='Queries']")
        self.submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")

    def Open_page(self, url):
        self.driver.get(url)

    def scroll_to_element(self, element):
        # Scroll the page until the specified element is in view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def enter_name(self, name):
        name_element = self.driver.find_element(*self.name_textbox)
        self.scroll_to_element(name_element)
        name_element.send_keys(name)

    def enter_email(self, email):
        email_element = self.driver.find_element(*self.email_textbox)
        self.scroll_to_element(email_element)
        email_element.send_keys(email)

    def enter_phone(self, phone):
        phone_element = self.driver.find_element(*self.phone_textbox)
        self.scroll_to_element(phone_element)
        phone_element.send_keys(phone)

    def enter_subject(self, subject):
        subject_element = self.driver.find_element(*self.subject_textbox)
        self.scroll_to_element(subject_element)
        subject_element.send_keys(subject)

    def enter_queries(self, queries):
        queries_element = self.driver.find_element(*self.queries_textbox)
        self.scroll_to_element(queries_element)
        queries_element.send_keys(queries)

    def click_submit(self):
        submit_element = self.driver.find_element(*self.submit_btn)
        self.scroll_to_element(submit_element)
        # submit_element.click()
