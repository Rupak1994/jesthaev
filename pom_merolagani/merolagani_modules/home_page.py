import time
from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.market = (By.XPATH,"//a[normalize-space()='Market']")
        self.market_overview = (By.XPATH,"//a[normalize-space()='Market Overview']")
        self.news = (By.XPATH,"//a[@title='Market'][normalize-space()='News']")
        self.all_news = (By.XPATH,"//a[@href='/NewsList.aspx']")
        self.news_article =(By.XPATH,"//img[@alt='एनपीएलमा जनकपुरको दोस्रो जित, महंगा विदेशी खेलाडी फ्लप']")
        self.load_more = (By.XPATH,"//a[normalize-space()='Load More']")

    def open_page(self, url):
        self.driver.get(url)

    def scroll_page(self,driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

    def hover_market(self):
        self.driver.find_element(*self.market).click()
        time.sleep(2)
        self.driver.find_element(*self.market_overview).click()
        time.sleep(2)
        self.scroll_page(self.driver)
        self.driver.back()
        time.sleep(2)
        self.driver.find_element(*self.news).click()
        time.sleep(2)
        self.driver.find_element(*self.all_news).click()
        time.sleep(2)
        # Scroll until the news article is found
        found_article = False
        while not found_article:
            try:
                # Check if the news article is present
                article_element = self.driver.find_element(*self.news_article)
                if article_element.is_displayed():
                    found_article = True
                    article_element.click()
                    time.sleep(2)  # Wait for the article to load
                    self.scroll_page(self.driver)
            except:
                # If the article is not found, keep scrolling
                self.driver.find_element(*self.load_more).click()
                time.sleep(2)
                # self.scroll_page(self.driver)
                # time.sleep(2)

