from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Pagination:
    def __init__(self, driver):
        self.driver = driver
        self.pagination_list = (By.CSS_SELECTOR, "ul.pagination li a")
        self.next_button = (By.CSS_SELECTOR, "li.right a")

    def get_current_page(self):
        pages = self.driver.find_elements(*self.pagination_list)
        for page in pages:
            if "selected" in page.get_attribute("class"):
                return int(page.text.strip())
        return 1  # Default to 1 if not found

    def go_to_page(self, page_number):
        pages = self.driver.find_elements(*self.pagination_list)
        for page in pages:
            if page.text.strip() == str(page_number):
                page.click()
                WebDriverWait(self.driver, 10).until(
                    EC.staleness_of(page)
                )
                return
        raise ValueError(f"Page number {page_number} not found.")

    def go_to_next_page(self):
        next_page = self.driver.find_element(*self.next_button)
        next_page.click()
        WebDriverWait(self.driver, 10).until(
            EC.staleness_of(next_page)
        )

    def has_next_page(self):
        return len(self.driver.find_elements(*self.next_button)) > 0

    def get_total_pages(self):
        pages = self.driver.find_elements(*self.pagination_list)
        return len(pages) - 2  # Exclude "..." and next button
