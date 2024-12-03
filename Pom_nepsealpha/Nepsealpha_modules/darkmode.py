from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Darkmode:
    def __init__(self, driver):
        self.driver = driver
        self.dark_mode_xpath = "//i[@class='fa fa-moon-o']"
        self.light_mode_xpath = "//i[@class='fa fa-lightbulb-o']"

    def open_page(self, url):
        self.driver.get(url)

    def toggle_dark_mode(self):
        try:
            dark_mode_button = self.driver.find_element(By.XPATH, self.dark_mode_xpath)
            dark_mode_button.click()
            return "Dark mode activated"
        except Exception:
            try:
                light_mode_button = self.driver.find_element(By.XPATH, self.light_mode_xpath)
                light_mode_button.click()
                return "Dark mode deactivated"
            except Exception as e:
                return f"button not found: {e}"
