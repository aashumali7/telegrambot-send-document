import time
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Selenium Chrome options setup
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

dropdown_element = driver.find_element(By.ID, 'lst_caseS')
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('WP - WRIT PETITION')

dropdown_element = driver.find_element(By.ID, 'txtyear')
dropdown = Select(dropdown_element)
dropdown.select_by_visible_text('2022')

# Find the captcha image element
captcha_img = driver.find_element(By.ID, 'cp')
captcha_img.screenshot('captcha.png')

# Use pytesseract to extract text from the captcha image
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
try:
    captcha_text = pytesseract.image_to_string(Image.open('captcha.png')).strip()
    if captcha_text:
        print("Captcha text:", captcha_text)
        # Find the captcha input field
        captcha_input = driver.find_element(By.ID, 'code')
        # Fill in the captcha number
        captcha_input.send_keys(captcha_text)
    else:
        print("Failed to extract captcha text.")
except Exception as e:
    print("Error:", e)

# Wait for a while for manual verification
time.sleep(10)

# Close the browser
driver.quit()
