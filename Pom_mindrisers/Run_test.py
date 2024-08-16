from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

import pytest
import time

from Pom_mindrisers.mindrisers_module.home_page import Homepage
from Pom_mindrisers.mindrisers_module.our_courses import Our_courses
from Pom_mindrisers.mindrisers_module.postplus2_page import postplus2course
from Pom_mindrisers.mindrisers_module.placement_patner import placement
from Pom_mindrisers.mindrisers_module.successful_stories import success_story
from Pom_mindrisers.mindrisers_module.blogs import Blogs
from Pom_mindrisers.mindrisers_module.contact_us import contact_us
from Pom_mindrisers.mindrisers_module.admission import admission


@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    browser = request.param
    if browser == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.implicitly_wait(2)
    yield driver
    driver.quit()

# @pytest.fixture()
# def driver():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     driver.implicitly_wait(2)
#     yield driver
#     driver.close()

# for edge browser
# def driver():
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     driver.implicitly_wait(2)
#     yield driver
#     driver.quit()

# for firefox browser
# def driver():
#     driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#     driver.implicitly_wait(2)
#     yield driver
#     driver.quit()


# test for homepage
def test_homepage(driver):
    home = Homepage(driver)
    home.open_page("https://www.mindrisers.com.np/")
    driver.maximize_window()
    time.sleep(3)
    home.static_image()
    home.scroll_page(driver)

# test for our courses page
def test_ourcouses(driver):
    ourcourses = Our_courses(driver)
    ourcourses.Open_ourcoursespage("https://www.mindrisers.com.np/courses")
    driver.maximize_window()
    time.sleep(2)
    ourcourses.scroll_page(driver)

# test for post +2 courses
def test_postcourses(driver):
    post_courses = postplus2course(driver)
    post_courses.Open_page("https://www.mindrisers.com.np/after+2-courses")
    driver.maximize_window()
    time.sleep(2)
    post_courses.scroll_page(driver)

# test for placement patner
def test_placement(driver):
    placement_patner = placement(driver)
    placement_patner.Open_page("https://www.mindrisers.com.np/placement-partner")
    driver.maximize_window()
    time.sleep(2)
    placement_patner.scroll_page(driver)

# test for successful stories
def test_successstory(driver):
    success_stories = success_story(driver)
    success_stories.Open_page("https://www.mindrisers.com.np/success-gallery")
    driver.maximize_window()
    time.sleep(2)
    success_stories.scroll_page(driver)

# test for blogs
def test_blogs(driver):
    blogs = Blogs(driver)
    blogs.Open_page("https://www.mindrisers.com.np/blogs")
    driver.maximize_window()
    time.sleep(2)
    blogs.scroll_page(driver)

# test for contact us
def test_contactus(driver):
    Contact_us = contact_us(driver)
    Contact_us.Open_page("https://www.mindrisers.com.np/contact-us")
    driver.maximize_window()
    time.sleep(2)
    Contact_us.enter_name("ram kc")
    time.sleep(2)
    Contact_us.enter_email("ram@gmail.com")
    time.sleep(2)
    Contact_us.enter_phone("9800909090")
    time.sleep(2)
    Contact_us.enter_subject("QA")
    time.sleep(2)
    Contact_us.enter_queries("i am intersted in your qa program.")
    time.sleep(2)
    Contact_us.click_submit()
    time.sleep(2)

# test for admission
def test_admission(driver):
    Admission= admission(driver)
    Admission.open_page("https://www.mindrisers.com.np/online-admission")
    driver.maximize_window()
    time.sleep(2)
    Admission.click_admissionform_btn()
    time.sleep(2)
    Admission.enter_name("test")
    time.sleep(1)
    Admission.enter_email("test@test.com")
    time.sleep(1)
    Admission.enter_phone("9800000000")
    time.sleep(1)
    Admission.enter_college("kcc")
    time.sleep(1)
    Admission.select_academic_status("Bachelor Completed/Running")
    time.sleep(1)
    Admission.select_interested_course("Quality Assurance Training in Nepal")
    time.sleep(1)
    Admission.select_preferred_schedule()
    time.sleep(2)
    Admission.select_internship_radio_button_no()
    time.sleep(2)
    Admission.enter_queries("i am intrested in your qa course")
    time.sleep(2)
    # Admission.submit_form()
    # time.sleep(1)