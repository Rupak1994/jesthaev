import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Media:
    def __init__(self, driver):
        self.driver = driver
        self.news_option = (By.LINK_TEXT,"News")
        # self.news_option=(By.XPATH,"//a[@title='News'][normalize-space()='News']")
        self.announcement_option = (By.LINK_TEXT,"Announcement")
    def open_page(self, url):
        self.driver.get(url)

    def scroll_page(self,driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

    def click_news(self):
        self.driver.find_element(*self.news_option).click()

    # def click_news(self):
    #     # Wait for the link with text 'News' to be clickable
    #     news_link = WebDriverWait(self.driver, 10).until(
    #         EC.element_to_be_clickable(self.news_option)
    #     )
    #     news_link.click()

    def click_announcement(self):
        self.driver.find_element(*self.announcement_option).click()

