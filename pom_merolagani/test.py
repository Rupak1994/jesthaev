from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import pytest
import time

from pom_merolagani.merolagani_modules.home_page import Homepage
from pom_merolagani.merolagani_modules.language_select import Language
from pom_merolagani.merolagani_modules.create_free_account import register
from pom_merolagani.merolagani_modules.login import login
from pom_merolagani.merolagani_modules.search_company import Search_company
from pom_merolagani.merolagani_modules.help import Help
from pom_merolagani.merolagani_modules.contact_us import Contact_us

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.close()

# Test for home page
def test_homepage(driver):
    home = Homepage(driver)
    home.open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(3)
    actual_title=driver.title
    expected_title=("merolagani - Nepal Stock Exchange (NEPSE) News, Live Trading, Live Floorsheet, "
                    "Indices, Company Announcements and Reports, Market Analysis, Online Portfolio Tracker, "
                    "Watchlist, Alerts, Investor Forum")
    if actual_title == expected_title:
        print("title check pass")
    else:
        print("title check fail")
    home.hover_market()
    time.sleep(2)

# Test for language select
def test_language(driver):
    language = Language(driver)
    language.open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(1)
    result = language.toggle_language()
    print(result)
    time.sleep(2)

# Test for register new user
def test_register(driver):
    Register = register(driver)
    Register.Open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(2)
    Register.open_registerpage()
    time.sleep(2)
    Register.enter_phone("1110261003")
    time.sleep(2)
    Register.click_register()
    time.sleep(2)
    Register.enter_otp(6785)
    time.sleep(2)
    Register.enter_pincode(1111)
    time.sleep(2)
    Register.conform_pincode(1111)
    time.sleep(2)
    Register.click_submit()
    time.sleep(2)
    try:
        # Wait until the alert element is present
        alert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )

        # Check if the alert text is as expected
        alert_text = alert.text
        expected_text = "Sorry, OTP Code is incorrect. Please recheck OTP code and try again."

        if expected_text in alert_text:
            print("entered otp is incorrect please check!!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# Test login
def test_login(driver):
    Login = login(driver)
    Login.Open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(2)
    Login.open_loginpage()
    time.sleep(2)
    Login.enter_phone(9810261003)
    time.sleep(2)
    Login.enter_pin(1234)
    time.sleep(2)
    Login.click_eye_btn()
    time.sleep(2)
    Login.click_login()
    time.sleep(2)
    actual_title = driver.title
    expected_title="MeroLagani Dashboard"
    if actual_title==expected_title:
        assert True
        print("dashboard is opened. test successful")
    else:
        print("test fail")
        assert False
    Login.click_logout()
    time.sleep(2)

# Test search
def test_search(driver):
    search = Search_company(driver)
    search.open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(2)
    search.search_company("NICA")
    time.sleep(2)
    search.click_search()
    time.sleep(2)
    search.click_news()
    time.sleep(2)
    search.next_page()
    time.sleep(2)

# Test for video tutorial
def test_help(driver):
    help = Help(driver)
    help.open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(2)
    help.open_videotutorial()
    time.sleep(2)
    help.open_portfoliotutorial()
    time.sleep(2)

# Test for contact_us
def test_contactus(driver):
    contact_us = Contact_us(driver)
    contact_us.open_page("https://merolagani.com/Index.aspx")
    driver.maximize_window()
    time.sleep(2)
    contact_us.click_contactus()
    time.sleep(2)
    contact_us.enter_name("test")
    time.sleep(1)
    contact_us.enter_mobile("test11")
    time.sleep(1)
    contact_us.enter_email("test@test.com")
    time.sleep(1)
    contact_us.enter_message("i am test123")
    time.sleep(1)
    # contact_us.click_submit()
    # time.sleep(1)
    contact_us.click_reset()
    time.sleep(1)