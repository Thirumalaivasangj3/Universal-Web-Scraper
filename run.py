import re
from scraper.universal_scraper import scrape_any_site

def clean_filename(url):
    url = re.sub(r"https?://", "", url)
    url = re.sub(r"[^a-zA-Z0-9]", "_", url)
    return url.strip("_")[:50]  # Limit filename length

if __name__ == "__main__":
    url = input("🔗 Enter a website URL to scrape: ").strip()
    if not url.startswith("http"):
        url = "https://" + url

    filename = clean_filename(url) + ".json"
    output_file = f"output/{filename}"

    scrape_any_site(url, output_file)
