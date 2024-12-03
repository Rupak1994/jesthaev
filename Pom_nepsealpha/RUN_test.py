from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import pytest
import time

from Pom_nepsealpha.Nepsealpha_modules.Home_page import Homepage
from Pom_nepsealpha.Nepsealpha_modules.login_page import login
from Pom_nepsealpha.Nepsealpha_modules.register_user import register
from Pom_nepsealpha.Nepsealpha_modules.media import Media
from Pom_nepsealpha.Nepsealpha_modules.search import Search_company
from Pom_nepsealpha.Nepsealpha_modules.darkmode import Darkmode
from Pom_nepsealpha.Nepsealpha_modules.pagination import Pagination

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    yield driver
    driver.close()

# for edge browser
# def driver():
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     driver.implicitly_wait(2)
#     yield driver
#     driver.quit()

# test for homepage
def test_homepage(driver):
    home = Homepage(driver)
    home.open_page("https://nepsealpha.com/")
    driver.maximize_window()
    time.sleep(3)
    home.scroll_page(driver)
    actual_title=driver.title
    expected_title="Share Market Newsportal | Nepse Chart | Nepal Stock Exchange | Technical & Fundamental Analysis Research Tool1"
    if actual_title==expected_title:
        assert True
        print("title check pass")
    else:
        print("title check fail")
        assert False
    # assert actual_title == expected_title, f"Title check failed: expected '{expected_title}', got '{actual_title}'"
    # print("Title check passed")

def test_login(driver):
    Login = login(driver)
    Login.Open_page("https://nepsealpha.com/login")
    driver.maximize_window()
    time.sleep(2)
    Login.enter_email("test1234@gmail.com")
    time.sleep(2)
    Login.enter_password("test123")
    time.sleep(2)
    Login.click_eye_btn()
    time.sleep(2)
    Login.click_submit()
    time.sleep(2)
    # try:
    #     error_message = WebDriverWait(driver, 10).until(
    #         EC.visibility_of_element_located(
    #             (By.XPATH, "//div[@class='invalid-feedback mb-2'], 'These credentials do not match our records.')]"))
    #     )
    #     print("Error message is displayed:", error_message.text)
    # except Exception as e:
    #     print("Error message not found:", e)
    #     driver.find_element(*(By.XPATH, "//div[@class='invalid-feedback mb-2']"))
    try:
        alert = driver.switch_to.alert
        alert.accept()
        print(f"Invalid username or password")
    except Exception:
        time.sleep(2)

        page_source = driver.page_source
        if "These credentials do not match our records." in page_source:
            print(f"Invalid credentials")
        else:
            print(f"Unexpected error or login failed")

def test_register(driver):
    Register = register(driver)
    Register.Open_page("https://nepsealpha.com/register")
    driver.maximize_window()
    time.sleep(2)
    Register.enter_firstname("rama")
    time.sleep(2)
    Register.enter_lastname("kc")
    time.sleep(2)
    Register.enter_email("test@123.com")
    time.sleep(2)
    Register.enter_phone("9800000000")
    time.sleep(2)
    Register.select_gender("Female")
    time.sleep(2)
    Register.enter_dob("01/01/1990")
    time.sleep(2)
    Register.enter_password("test123")
    time.sleep(2)
    Register.enter_confirm_password("test123")
    time.sleep(2)
    Register.click_agreement()
    time.sleep(2)
    # Register.click_register()
    # time.sleep(2)

def test_media(driver):
    media = Media(driver)
    media.open_page("https://nepsealpha.com/")
    driver.maximize_window()
    time.sleep(2)
    media.click_news()
    time.sleep(2)
    # assert "News Post" in driver.title
    # driver.close()
    media.click_announcement()
    time.sleep(2)
    # assert "Announcement List" in driver.title

def test_search(driver):
    search = Search_company(driver)
    search.open_page("https://nepsealpha.com/")
    driver.maximize_window()
    time.sleep(2)
    search.search_company("(NICA) NIC Asia Bank Ltd")
    time.sleep(5)
    # search.click_search()
    # time.sleep(2)
    search.scroll_page()

def test_darkmode(driver):
    darkmode = Darkmode(driver)
    darkmode.open_page("https://nepsealpha.com/")
    driver.maximize_window()
    time.sleep(1)
    result = darkmode.toggle_dark_mode()
    print(result)
    time.sleep(2)
    result = darkmode.toggle_dark_mode()
    print(result)
    time.sleep(2)


# def test_news(driver):
#     driver.get("https://nepsealpha.com/all-news?cid=1")
#     driver.maximize_window()
#     time.sleep(2)
def test_news(driver):
    driver.get("https://nepsealpha.com/all-news?cid=1")
    driver.maximize_window()
    time.sleep(2)

    pagination = Pagination(driver)

    # Example: Go through the first 5 pages
    for i in range(1, 6):
        pagination.go_to_page(i)
        print(f"Current Page: {pagination.get_current_page()}")

        # Add any scraping or validation logic here

        # Check if there's a next page
        if pagination.has_next_page():
            pagination.go_to_next_page()
            print(f"Navigated to Next Page: {pagination.get_current_page()}")
        else:
            print("No more pages available.")
            break

    # Print total pages
    print(f"Total Pages: {pagination.get_total_pages()}")

