# automation for chrome browser
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# url= "https://merolagani.com/"
# driver.get(url)
# driver.maximize_window()
# time.sleep(2)
# market= driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
# market.click()
# time.sleep(2)
# indices= driver.find_element(By.LINK_TEXT,"Indices")
# indices.click()
# time.sleep(2)
# driver.quit()

# for meroshare
url= "https://meroshare.cdsc.com.np/#/login"
driver.get(url)
driver.maximize_window()
time.sleep(2)
dropdown= driver.find_element(*(By.XPATH,"/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span"))
dropdown.click()
time.sleep(2)
option_xpath="//li[contains(text(),'AAKASHBHAIRAB SECURITIES LIMITED (20600)')]"
option= WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, option_xpath)))
option.click()
time.sleep(5)
print("dropdown option selected successfully")
driver.quit()
