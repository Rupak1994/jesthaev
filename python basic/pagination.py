# Import the necessary modules
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the chromedriver manager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Open the website
driver.get("https://www.sharesansar.com/company/aclbsl")

driver.maximize_window()
time.sleep(2)
#locate events
events_button = driver.find_element(By.ID, "btn_cevents")
driver.execute_script("arguments[0].scrollIntoView(true);", events_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", events_button)


# Wait for the content to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "cevents"))
)

time.sleep(5)

# Function to handle pagination
def handle_pagination():
    while True:
        # Wait for the table to load
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//table"))
        )

        # Check if the "Next" button is present and clickable
        next_buttons = driver.find_elements(By.XPATH, "//a[@class='paginate_button next']")
        if next_buttons:
            next_button = next_buttons[0]
            if next_button.is_displayed() and next_button.is_enabled():
                next_button.click()
                print("Clicked the Next button to go to the next page")
                time.sleep(2)
            else:
                print("Next button is not clickable")
                break
        else:
            print("No more pages to navigate")
            break


# Call the pagination handler
handle_pagination()
# Close the driver instance
driver.quit()