import time

class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def scroll_page(self,driver):
        pg_ht = driver.execute_script("return document.body.scrollHeight")
        scroll_speed = 50
        scroll_iteration = int(pg_ht / scroll_speed)
        for _ in range(scroll_iteration):
            driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
            time.sleep(0.1)
    #
    # from selenium.common.exceptions import NoSuchElementException
    # from selenium.webdriver.common.by import By
    #
    # def scroll_page(self, driver):
    #     stop_element_xpath = '/html/body/div[1]/div[3]/div[5]/div/div[3]/div/div/table/thead/tr[1]'
    #
    #     pg_ht = driver.execute_script("return document.body.scrollHeight")
    #     scroll_speed = 50
    #     scroll_iteration = int(pg_ht / scroll_speed)
    #
    #     for _ in range(scroll_iteration):
    #         driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
    #         time.sleep(0.1)
    #
    #         if self.is_element_in_viewport(driver, stop_element_xpath):
    #             break
    #
    # def is_element_in_viewport(self, driver, xpath):
    #     try:
    #         # Use By.XPATH instead of the deprecated method
    #         element = driver.find_element(By.XPATH, xpath)
    #         return element.is_displayed() and self.is_element_visible_in_viewport(driver, element)
    #     except NoSuchElementException:
    #         return False
    #
    # def is_element_visible_in_viewport(self, driver, element):
    #     location = element.location
    #     size = element.size
    #     viewport_size = driver.execute_script("return [window.innerWidth, window.innerHeight];")
    #
    #     return (
    #             location['y'] >= 0 and
    #             location['y'] + size['height'] <= viewport_size[1]
    #     )
