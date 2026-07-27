# 🛒 E-commerce Data Extractor (Helion Scraper)

> A lightweight, fast, and automated web scraper built to extract product information (titles and prices) from a paginated e-commerce website.

🚀 Business Value

This tool was built to solve a common e-commerce problem: wasting time on manual data entry.
Instead of spending hours manually copying competitor prices or supplier catalogs, this script does it in seconds and delivers a clean, ready-to-use dataset.

# ✨ Features

 - **Automated Pagination:** Navigates through multiple pages of the store automatically (e.g., handles 40+ pages in one run).

 - **Data Cleaning:** Strips hidden HTML characters, extra spaces, and newlines to ensure high data quality.

 - **Direct CSV Export:** Saves the final dataset directly into a structured .csv file, perfectly formatted for Excel, Shopify, WooCommerce, or any ERP system.

 - **Anti-Blocking Measures:** Uses custom User-Agent headers to simulate real browser traffic and prevent basic bot-blocking.

# 🛠️ Technology Stack

**Language:** Python 3.14

**Core Libraries:**

**requests** (HTTP requests handling)

**BeautifulSoup4** (HTML parsing and data extraction)

**csv** (Data formatting and export)

# 💻 How it works

The script accesses the target e-commerce category URL.

It iterates through all available pages automatically.

It extracts the raw HTML, locates the product containers, and isolates titles and prices.

It cleans the text and streams it line-by-line into ksiazki_helion.csv.

# 🚀 Quick Start

To run this script locally:

1. Clone the repository.
``` bash
git clone https://github.com/Twój-Nick/web-automation-tools.git
```
2. Navigate to the project folder:
``` bash
cd web-automation-tools
```
3. Install required dependencies:
``` bash
pip install requests beautifulsoup4
```

Run the script:
``` bash
python moj_scraper.py
```

5. Check the project directory – the generated ksiazki_helion.csv dataset will be ready for use.

⚠️ Disclaimer

This repository is for educational and portfolio purposes. Web scraping should be done ethically and in accordance with the target website's robots.txt policies.