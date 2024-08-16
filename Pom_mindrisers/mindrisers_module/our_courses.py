import time
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class Our_courses:
    def __init__(self, driver):
        self.driver = driver

    def Open_ourcoursespage(self,url):
        self.driver.get(url)

    def scroll_page(self,driver):
        wait = WebDriverWait(driver, 10)
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)
        # qa_course_link= wait.until(EC.presence_of_element_located(By.XPATH,"//h3[@class='sub-header title-space-md text-expanded'][normalize-space()='Quality Assurance Training in Nepal']"))
        # qa_course_link.click()

