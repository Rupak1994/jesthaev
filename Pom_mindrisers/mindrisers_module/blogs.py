import time
# from selenium.webdriver.common.by import By

class Blogs :
    def __init__(self, driver):
        self.driver = driver
        # self.blog_qa= (By.XPATH,"/html/body/div[1]/div/div[2]/div[3]/section[1]/ul/li[8]")

    def Open_page(self, url):
        self.driver.get(url)

    def scroll_page(self, driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

    # def click_QA(self):
    #     self.driver.find_element(*self.blog_qa).click()



