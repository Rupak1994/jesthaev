import time

class articlepage:
    def __init__(self,driver):
        self.driver = driver

    def open_article(self,url):
        self.driver.get(url)
    def scroll_page(self,driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 10
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

