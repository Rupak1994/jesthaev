import random
import re
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Set up the ChromeDriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Define the email validation function
def is_valid_email(email):
    try:
        # Improved email pattern
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(email_pattern, email))
    except Exception as e:
        print(f"Error in email validation: {e}")
        return False

# Define the phone number validation function
def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$', phone))

# Open the website
driver.get("https://www.mindrisers.com.np/contact-us")
driver.maximize_window()

# Set the scroll parameters
target_y = 6000
scroll_distance = 1000
current_y = 0

# Loop for scrolling
while current_y < target_y:
    driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
    current_y += scroll_distance
    time.sleep(0.25)

# Interact with the web elements
try:
    first_name_field = driver.find_element(By.XPATH, "//input[@placeholder='Name']")
    email_field = driver.find_element(By.XPATH, "//input[@placeholder='Email']")
    phone_field = driver.find_element(By.XPATH, "//input[@placeholder='Phone']")
except Exception as e:
    print(f"Error locating elements: {e}")
    driver.quit()
    exit()
def generate_random_email():
    domain="test.com"
    email_length=8
    random_string=''.join(random.choice(string.ascii_lowercase)for _ in range(email_length))
    email = random_string+ "@" + domain
    return email
def generate_random_name():
    return ''.join(random.choices(string.ascii_letters,k=5))
def generate_random_phone():
    ph_number= "98"+''.join(random.choices(string.digits,k=8))
    return ph_number


# Invalid email examples (for testing purposes)
# email = "john123"
# email = "ram@@123gmail.com"
# email = "ram@gmail..com"

# Valid email
first_name = generate_random_name()
email = generate_random_email()
phone = generate_random_phone()

# Clear and fill the first name field
first_name_field.clear()
first_name_field.send_keys(first_name)
time.sleep(0.75)

# Validate the email
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")

# Clear and fill the email field
email_field.clear()
email_field.send_keys(email)
time.sleep(0.75)

# Validate the phone number
if not phone:
    print("Phone cannot be empty")
else:
    if is_valid_phone(phone):
        print("Valid phone number")
    else:
        print("Invalid phone number")

# Clear and fill the phone field
phone_field.clear()
phone_field.send_keys(phone)
time.sleep(0.75)

# Close the driver instance
driver.quit()
print(" validation completed successfully!")

