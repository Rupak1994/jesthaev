from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time

from pom.pages.login_page import loginpage
from pom.pages.dashboard_page import Dashboardpage
from pom.pages.aboutyourself_page import aboutyourself
from pom.pages.article import articlepage
from pom.pages.contactme_page import contactme

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.close()
# def test_login(driver):
#     login_page=loginpage(driver)
#     login_page.open_page("https://tax.digitalpalika.org/login")
#     driver.maximize_window()
#     time.sleep(2)
#     login_page.enter_username("malikacounter5")
#     time.sleep(2)
#     login_page.enter_password("password")
#     time.sleep(2)
#     login_page.click_login()
#     time.sleep(2)
# parameterize concept
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
# for https://sagar-test-qa.vercel.app/
def test_login(driver):
    login_page=loginpage(driver)
    login_page.open_page("https://sagar-test-qa.vercel.app/")
    driver.maximize_window()
    time.sleep(2)
    login_page.enter_username("TestQA")
    time.sleep(2)
    login_page.enter_password("password")
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)

# for dashboard
def test_dashboardpage(driver):
    dashboard_page=Dashboardpage(driver)
    dashboard_page.open_dashboard("https://sagar-test-qa.vercel.app/dashboard.html")
    driver.maximize_window()
    time.sleep(2)
    print("congrats dashboard is open successfully")
# for aboutyourself
def test_aboutyourself(driver):
    aboutyourself_page=aboutyourself(driver)
    aboutyourself_page.open_page("https://sagar-test-qa.vercel.app/about.html")
    driver.maximize_window()
    time.sleep(2)
    aboutyourself_page.enter_fullname("ram thapa")
    time.sleep(1)
    aboutyourself_page.enter_phone("9841000000")
    time.sleep(1)
    aboutyourself_page.enter_email("test@123.com")
    time.sleep(1)
    aboutyourself_page.enter_hobby("playing football")
    time.sleep(1)
    aboutyourself_page.click_submit()
    time.sleep(1)
    print("successfully submitted yourself data")
# for article
def test_article(driver):
    article=articlepage(driver)
    article.open_article("https://sagar-test-qa.vercel.app/articles.html")
    driver.maximize_window()
    time.sleep(2)
    article.scroll_page(driver)
# for contactme
def test_contactme(driver):
    contact_me=contactme(driver)
    contact_me.open_page("https://sagar-test-qa.vercel.app/contact.html")
    driver.maximize_window()
    time.sleep(2)
    contact_me.enter_name("hari kc")
    time.sleep(2)
    contact_me.enter_email("test123@1.com")
    time.sleep(2)
    contact_me.enter_message("hello host")
    time.sleep(2)
    contact_me.click_sendmsg()
    time.sleep(1)