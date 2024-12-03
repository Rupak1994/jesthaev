from selenium.webdriver.common.by import By

class Language:
    def __init__(self, driver):
        self.driver = driver
        self.english_xpath = "//span[@class='glyphicon glyphicon-one-fine-white-dot']"
        self.nepali_xpath = "//span[@class='glyphicon glyphicon-one-fine-white-dot']"

    def open_page(self, url):
        self.driver.get(url)

    def toggle_language(self):
        try:
            english_button = self.driver.find_element(By.XPATH, self.english_xpath)
            english_button.click()
            return "language set to english"
        except Exception:
            try:
                nepali_button = self.driver.find_element(By.XPATH, self.nepali_xpath)
                nepali_button.click()
                return "language set to nepali"
            except Exception as e:
                return f"button not found: {e}"

