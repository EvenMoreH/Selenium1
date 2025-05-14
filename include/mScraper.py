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
from gpuPriceCheck import *

def morele_scrape(gpu_model):
    # setting up path for chromedriver.exe
    chrome_service = Service(executable_path="webdriver/chromedriver.exe")

    # setting up options to use headless browser to leverage dev tools
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=3840,2160")

    # setting up driver to make actual actions in the browser
    driver = webdriver.Chrome(service=chrome_service, options=options)
    # driver = webdriver.Chrome(service=chrome_service)

    wait = WebDriverWait(driver, 5)

    driver.get("https://www.morele.net/")

    input_element = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    input_element.clear()
    input_element.send_keys(f"{gpu_model}" + Keys.ENTER)

    category_element = wait.until(
        EC.presence_of_element_located((By.ID, "12"))
    )
    category_element.click()

    dropdown_element = wait.until(
        EC.element_to_be_clickable((By.ID, "sortBy"))
    )
    dropdown_element.click()

    sort_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(normalize-space(text()), 'Cena - od najniższej')]"))
    )
    driver.execute_script("arguments[0].click();", sort_element)

    time.sleep(5)

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M")
    date = datetime.now().strftime("%d-%m-%Y")
    folder = os.path.join("gpu_snapshots", date)
    os.makedirs(folder, exist_ok=True)
    filename = f"morele_{gpu_model}_{timestamp}.webp"
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

def main():
    morele_scrape("5080")

if __name__ == "__main__":
    main()