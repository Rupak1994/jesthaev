from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
from pom.pages.login_page import loginpage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.close()
def test_login(driver):
    login_page=loginpage(driver)
    login_page.open_page("https://tax.digitalpalika.org/login")
    driver.maximize_window()
    time.sleep(2)
    login_page.enter_username("malikacounter5")
    time.sleep(2)
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)
# @pytest.mark.parametrize("username, password", [("malikacounter5", "password"), ("user2", "password2")])
# def test_login(driver,username,password):
#     login_page = loginpage(driver)
#     login_page.open_page("https://tax.digitalpalika.org/login")
#     driver.maximize_window()
#     time.sleep(2)
#     login_page.enter_username(username)
#     time.sleep(2)
#     login_page.enter_password(password)
#     time.sleep(2)
#     login_page.click_login()
#     time.sleep(2)
#     try:
#         alert=driver.switch_to.alert
#         # alert_text= alert.text
#         alert.accept()
#         print(f"invalid username or password for {username}")
#     except:
#         time.sleep(2)
#         page_source=driver.page_source
#         if "Counter Dashbord" in page_source:
#             print(f"login successful for {username}")
#         else:
#             print(f"unexpected error or login failed for {username}")