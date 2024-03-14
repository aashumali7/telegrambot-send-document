from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

# Set up Chrome WebDriver service
webdriver_service = Service('./chromedriver.exe')

# Create a Chrome WebDriver instance with the defined service and options
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Navigate to the webpage
driver.get('https://mphc.gov.in/case-status')

# Find the element by ID and interact with it
input_element = driver.find_element(By.ID, 'txtnoS')  # Use By.ID to locate element
input_element.send_keys('1234')

print('text of the element:', input_element.text)

time.sleep(20)

# Close the browser
driver.quit()
