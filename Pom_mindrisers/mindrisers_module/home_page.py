import time
from selenium.webdriver.common.by import By


class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.close_img=(By.XPATH,"//span[@class='absolute right-0 top-0 flex h-[28px] w-[28px] -translate-y-1/2 translate-x-1/2 cursor-pointer items-center justify-center rounded-full bg-red-400 font-bold text-white md:h-[32px] md:w-[32px] ']")

    def open_page(self, url):
        self.driver.get(url)

    def scroll_page(self,driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)

    def static_image(self):
        self.driver.find_element(*self.close_img).click()
