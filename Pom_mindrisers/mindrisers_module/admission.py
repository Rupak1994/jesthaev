from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class admission:
    def __init__(self, driver):
        self.driver = driver
        self.fill_admission_form_btn = (By.XPATH, "//a[normalize-space()='Fill admission form']")
        self.name_textbox = (By.XPATH, "//input[@id='full_name']")
        self.email_textbox = (By.XPATH, "//input[@id='email']")
        self.phone_textbox = (By.XPATH, "//input[@id='mobile_no']")
        self.college_textbox = (By.XPATH, "//input[@id='college']")
        self.academicstatus_dropdown = (By.XPATH, "//select[@id='qualification']")
        self.intrestedcourse_dropdown = (By.XPATH, "//select[@id='course']")
        self.preferedschedule_dropdown = (By.XPATH, "//select[@id='shedule']")
        self.internship_radiobutton_no = (By.XPATH, "//input[@id='remarks-no']")
        self.queries_textbox = (By.XPATH, "//textarea[@id='question']")
        self.submit_btn = (By.XPATH, "//button[normalize-space()='Submit']")

    def open_page(self, url):
        self.driver.get(url)

    def click_admissionform_btn(self):
        self.driver.find_element(*self.fill_admission_form_btn).click()

    def enter_name(self, name):
        self.driver.find_element(*self.name_textbox).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def enter_college(self,college):
        self.driver.find_element(*self.college_textbox).send_keys(college)

    def select_academic_status(self, status):
        dropdown = Select(self.driver.find_element(*self.academicstatus_dropdown))
        dropdown.select_by_visible_text(status)

    def select_interested_course(self, course):
        dropdown = Select(self.driver.find_element(*self.intrestedcourse_dropdown))
        dropdown.select_by_visible_text(course)

    # def select_preferred_schedule(self, schedule):
    #     dropdown = Select(self.driver.find_element(*self.preferedschedule_dropdown))
    #     dropdown.select_by_visible_text(schedule)

    def select_preferred_schedule(self):
        self.driver.find_element(*self.preferedschedule_dropdown).click()
        option_xpath = "/html/body/div[1]/div/section/form/div[1]/div[7]/div/select/option[3]"
        option = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
        option.click()

    def select_internship_radio_button_no(self):
        radio_button = self.driver.find_element(*self.internship_radiobutton_no)
        if not radio_button.is_selected():
            radio_button.click()
        try:
            radio_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.internship_radiobutton_no)
            )
            if not radio_button.is_selected():
                radio_button.click()
        except Exception as e:
            print(f"An error occurred: {e}")

    def enter_queries(self, queries):
        self.driver.find_element(*self.queries_textbox).send_keys(queries)

    def submit_form(self):
        self.driver.find_element(*self.submit_btn).click()


