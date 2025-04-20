from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
import os
import time

def scrape_any_site(url, output_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        print(f"🌐 Navigating to {url}")
        driver.get(url)
        time.sleep(5)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # 📊 Find all tables
        tables = soup.find_all("table")
        all_tables_data = []

        for table in tables:
            headers = []
            rows_data = []

            # Try to get headers (if present)
            header_row = table.find("tr")
            if header_row:
                headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

            # Get all data rows
            for row in table.find_all("tr")[1:]:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                if cells:
                    if headers and len(headers) == len(cells):
                        row_dict = dict(zip(headers, cells))
                    else:
                        row_dict = {"column_" + str(i): val for i, val in enumerate(cells)}
                    rows_data.append(row_dict)

            if rows_data:
                all_tables_data.append({
                    "headers": headers,
                    "rows": rows_data
                })

        # 📁 Save output
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(all_tables_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Extracted {len(all_tables_data)} tables and saved to {output_path}")

    finally:
        driver.quit()
