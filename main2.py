from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# setting up path for chromedriver.exe
chrome_service = Service(executable_path="webdriver/chromedriver.exe")
# setting up driver to make actual actions in the browser
driver = webdriver.Chrome(service=chrome_service)

driver.get("https://qr.fastools.xyz/")

wait = WebDriverWait(driver, 3)

wait.until(
    EC.presence_of_element_located((By.ID, "url"))
)

input_element = driver.find_element(By.ID, "url")
input_element.clear()

input_element.send_keys("https://www.selenium.dev/")

button_element = driver.find_element(By.XPATH, "//button[contains(text(), 'Generate QR Code')]")
button_element.click()

button_element = driver.find_element(By.XPATH, "//button[contains(text(), 'Download QR Code')]")
button_element.click()

time.sleep(5)
driver.quit()