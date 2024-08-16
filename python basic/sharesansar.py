import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Set up the ChromeDriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://www.sharesansar.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)

# Set the scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

# Loop for scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# market= driver.find_element(*(By.XPATH,"/html/body/div[2]/div/section[1]/div/div/div/ul/li[4]/a"))
# market.click()
# time.sleep(2)
# market_overview = driver.find_element(By.LINK_TEXT,"Market")
# market_overview= "//li[contains(text(),'Market Overview')]"
# market_overview.click()
# overview=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, market_overview)))
# overview.click()
search_company= driver.find_element(*(By.XPATH,"//input[@id='company_search']"))
search_company.send_keys("(NIMBAC) NIMB Ace Capital Limited")
time.sleep(2)
search=driver.find_element(*(By.XPATH,"//button[@id='btn_frm_company_search']"))
search.click()
search.click()
# time.sleep(3)
# # news= driver.find_element(*(By.XPATH,"//a[@id='btn_cnews']"))
# # news.click()
time.sleep(5)
driver.quit()

