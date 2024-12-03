import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Our_courses:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.XPATH,"//input[@name='searchTerm']")
        self.search_btn = (By.XPATH,"//button[@class='btn-simple']")
        self.qa_link = (By.XPATH,"//h3[@class='sub-header title-space-md text-expanded'][normalize-space()='Quality Assurance Training in Nepal']")

    def Open_ourcoursespage(self,url):
        self.driver.get(url)

    def scroll_page(self,driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

    def search_courses(self, search):
        search_bar = self.driver.find_element(*self.search_box)
        search_bar.send_keys(search)

    def click_search(self):
        # Click the search button with WebDriverWait to ensure it's clickable
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_btn)
        )
        search_button.click()
        time.sleep(5)
        # Wait for the QA link to be clickable and scroll into view
        qa_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.qa_link)
        )
        # Use ActionChains to move to the element and click it
        actions = ActionChains(self.driver)
        actions.move_to_element(qa_link).click().perform()  # Perform the click after moving to the element

        time.sleep(2)  # Adjust time if necessary, based on page load time
        self.scroll_page(self.driver)
