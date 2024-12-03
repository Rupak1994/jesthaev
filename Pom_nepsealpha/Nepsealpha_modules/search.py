import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class Search_company:
    def __init__(self, driver):
        self.driver = driver
        self.search_field=(By.XPATH,"//input[@id='__stock_symbol_search']")
        self.submit_search=(By.XPATH,"//input[@id='searchBtn']")

    def open_page(self, url):
        self.driver.get(url)

    def search_company(self, search):
        search_bar = self.driver.find_element(*self.search_field)
        search_bar.send_keys(search)
        search_bar.send_keys(Keys.RETURN)

    def click_search(self):
        self.driver.find_element(*self.submit_search).click()

    def scroll_page(self, driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

