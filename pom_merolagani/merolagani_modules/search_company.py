import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Search_company:
    def __init__(self, driver):
        self.driver = driver
        self.search_field=(By.XPATH,"//input[@id='ctl00_AutoSuggest1_txtAutoSuggest']")
        self.submit_search=(By.XPATH,"//a[@id='ctl00_lbtnSearch']//span[@class='icon-search']")
        self.news=(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkNewsTab']")

    def open_page(self, url):
        self.driver.get(url)

    def search_company(self, search):
        search_bar = self.driver.find_element(*self.search_field)
        search_bar.send_keys(search)
        search_bar.send_keys(Keys.RETURN)
        # self.driver.find_element(*self.search_field).send_keys(search)

    def click_search(self):
        self.driver.find_element(*self.submit_search).click()

    def click_news(self):
        news_element = self.driver.find_element(*self.news)

        # Wait for the element to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(news_element)
        )

        # Scroll to the element to make it visible
        self.driver.execute_script("arguments[0].scrollIntoView();", news_element)

        # Add a small delay to ensure the page has scrolled
        time.sleep(1)

        # Click the element after scrolling
        ActionChains(self.driver).move_to_element(news_element).click().perform()

    # def next_page(self):
    #     while True:
    #         # Check if 'Next' button is available and click it
    #         try:
    #             next_button = WebDriverWait(self.driver, 10).until(
    #                 EC.element_to_be_clickable((By.LINK_TEXT, "Next"))  # Adjust selector based on the website
    #             )
    #             next_button.click()  # Click the "Next" button
    #             time.sleep(3)  # Wait for the next page to load
    #         except:
    #             print("No more pages.")
    #             break

    def next_page(self):
        pages_visited = 0  # Initialize the counter for pages visited

        while pages_visited < 2:  # Loop until we visit 2 pages
            try:
                # Check if 'Next' button is available and click it
                next_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.LINK_TEXT, "Next"))  # Adjust selector if necessary
                )
                next_button.click()  # Click the "Next" button
                time.sleep(3)  # Wait for the next page to load

                # Increment the pages visited counter after each successful click
                pages_visited += 1
            except Exception as e:
                print("No more pages or error:", e)
                break  # Exit the loop if no more pages or error occurs