from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json
import os
import time

def scrape_any_site(url, output_path):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print(f"🌐 Scraping: {url}")
        driver.get(url)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(("tag name", "body"))
            )
        except:
            print("⚠️ Page load timeout")

        time.sleep(2)
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract tables
        tables = soup.find_all("table")
        output_data = []

        for table in tables:
            headers = []
            rows_data = []

            header_row = table.find("tr")
            if header_row:
                headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

            for row in table.find_all("tr")[1:]:
                cells = [td.get_text(strip=True) for td in row.find_all("td")]
                if cells:
                    if headers and len(headers) == len(cells):
                        row_dict = dict(zip(headers, cells))
                    else:
                        row_dict = {"column_" + str(i): val for i, val in enumerate(cells)}
                    rows_data.append(row_dict)

            if rows_data:
                output_data.extend(rows_data)

        # Fallback to text if no table
        if not output_data:
            text_content = soup.get_text(separator="\n", strip=True)[:3000]
            output_data = text_content

        # Save raw data only (no metadata)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Data saved to {output_path}")

    except Exception as e:
        print(f"❌ Scraping failed: {e}")
    finally:
        driver.quit()
