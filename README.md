# GPU Price Checker 🖥️💰

A simple Python project demonstrating **Selenium** automation by scraping GPU prices from two major Polish online retailers. This tool allows the user to input a desired GPU model, fetches and sorts listings from both sites by price, and saves full-page screenshots of the results — all running **completely headless**, without opening a browser window.

---

## 📌 Project Goals

* Showcase foundational **Selenium** skills using **Python**
* Work with dynamic web content and user input
* Use **headless Chrome WebDriver** for efficient scraping
* Automate file handling and screenshot capture

---

## 🗂️ Project Structure

```

 📦Selenium Project - GPU Price Checker
 ┣ 📂gpu_snapshots
 ┃ ┗ 📂14-05-2025
 ┃ ┃ ┣ 📜komputronik_b580_14-05-2025_22-01.webp     ← Output example
 ┃ ┃ ┗ 📜morele_b580_14-05-2025_22-01.webp          ← Output example
 ┣ 📂include
 ┃ ┣ 📜kScraper.py          ← Komputronik scraper logic
 ┃ ┗ 📜mScraper.py          ← Morele scraper logic
 ┣ 📂webdriver
 ┃ ┗ 📜chromedriver.exe
 ┣ 📜.gitignore
 ┣ 📜gpuPriceCheck.py       ← Main script
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┗ 📜requirements.txt

```

---

## 🧠 How It Works

1. **User Input:**
   On running `gpuPriceCheck.py`, the script prompts for a GPU model (e.g., `4070ti`, `7900xtx`).

2. **Headless Web Scraping:**
   The entered model is searched on:

   * **Komputronik** via `kScraper.py`
   * **Morele** via `mScraper.py`
     Browsing is done in **headless Chrome** for speed and invisibility.

3. **Sorting & Screenshot:**

   * Listings are sorted by price (lowest first).
   * A full-page screenshot is taken and saved in the format:
     `gpu_snapshots/{DD-MM-YYYY}/{shop}_{gpu_model}_{HH-MM}.webp`

---

## ▶️ Running the Project

### ✅ Prerequisites

* Python 3.8+
* Google Chrome installed
* Matching version of ChromeDriver in the `webdriver/` folder

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

### ▶️ Run the Script

```bash
python gpuPriceCheck.py
```

---

## 📷 Screenshot Output

Saved to:

```
gpu_snapshots/DD-MM-YYYY/shop_gpuModel_HH-MM.webp
```

Example:

```
gpu_snapshots/14-05-2025/morele_b580_14-05-2025_22-01.webp
```

---

## 🛠 Technologies Used

* Python 3
* Selenium (Headless Chrome)
* Chrome WebDriver
* OS, DateTime
* WebP format for image storage

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 🚀 Future Improvements

* Add support for more online shops
* Output scraped results to CSV or JSON
* Add retry logic on network failure
* GUI for ease of use

---