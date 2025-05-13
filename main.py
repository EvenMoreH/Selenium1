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

driver.get("https://temperature.fastools.xyz/")

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "temperature"))
)

# finding element using by looking for ID attribute
input_element = driver.find_element(By.ID, "temperature")
input_element.clear()
input_element.send_keys("240")

time.sleep(0.2)
# finding element using XPATH by looking for hx-get attribute
button_element = driver.find_element(By.XPATH, "//button[@hx-get='/CK']")
button_element.click()

time.sleep(0.2)
button_element = driver.find_element(By.XPATH, "//button[@hx-get='/CF']")
button_element.click()

time.sleep(0.2)
button_element = driver.find_element(By.XPATH, "//button[@hx-get='/KC']")
button_element.click()

time.sleep(0.2)
button_element = driver.find_element(By.XPATH, "//button[@hx-get='/KF']")
button_element.click()

time.sleep(0.2)
button_element = driver.find_element(By.XPATH, "//button[@hx-get='/FC']")
button_element.click()

time.sleep(0.2)
button_element = driver.find_element(By.XPATH, "//button[@hx-get='/FK']")
button_element.click()

time.sleep(1)
# finding element using XPATH by looking for buttons that contain text 'Reset'
button_element = driver.find_element(By.XPATH, "//button[contains(text(),'Reset')]")
button_element.click()

time.sleep(5)
driver.quit()