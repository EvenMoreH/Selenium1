from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import os
import base64

# setting up path for chromedriver.exe
chrome_service = Service(executable_path="webdriver/chromedriver.exe")

# setting up options to use headless browser to leverage dev tools
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=3840,2160")

# setting up driver to make actual actions in the browser
driver = webdriver.Chrome(service=chrome_service, options=options)

wait = WebDriverWait(driver, 5)

gpu_model = input("\nWhat gpu model number to look for? (Example: 5080; 4070ti; b580; 9070xt; 7900xtx) > ")
print(f"Looking for {gpu_model}...\n")

driver.get("https://www.komputronik.pl/")

input_element = wait.until(
    EC.presence_of_element_located((By.TAG_NAME, "input"))
)
input_element.clear()

time.sleep(2)

input_element.send_keys(f"karta graficzna {gpu_model}" + Keys.ENTER)

checkbox_element = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@type='checkbox']"))
)
checkbox_element.click()

time.sleep(2)

sort_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-role='selectLabel']"))
)
driver.execute_script("arguments[0].click();", sort_element)


dropdown_option = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[normalize-space(.)='Po cenie rosnąco']"))
)
driver.execute_script("arguments[0].click();", dropdown_option)

time.sleep(5)

timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
folder = "gpu_snapshots"
filename = f"komputronik_{gpu_model}_{timestamp}.webp"
filepath = os.path.join(folder, filename)

# Use DevTools command to capture full-page screenshot
result = driver.execute_cdp_cmd("Page.captureScreenshot", {
    "captureBeyondViewport": True,
    "fromSurface": True
})

with open(filepath, "wb") as f:
    f.write(base64.b64decode(result["data"]))

print(f'\nSaving snapshot to "{filepath}"...\n')
time.sleep(1)
driver.quit()