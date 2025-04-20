🌐 Universal Web Scraper
A powerful Python web scraping tool that extracts structured table data from any website, including JavaScript-rendered pages.
🚀 Features

Universal Compatibility: Scrapes tables from any website, including dynamic JS content
Smart Output: Automatically saves structured data as JSON files
Seamless Operation: Headless browser mode for background operation
Intelligent Naming: Generates filenames based on URL structure
Easy Integration: Simple CLI interface for quick adoption
Error Resilient: Robust handling of missing elements and malformed HTML

📦 Installation
Prerequisites

Python 3.8 or higher
Chrome or Firefox browser (for Selenium)
git for cloning the repository

Setup
Follow these steps to set up the Universal Web Scraper:
Linux/MacOS
# Clone repository
git clone https://github.com/your-username/universal-webscraper.git
cd universal-webscraper

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

Windows
# Clone repository
git clone https://github.com/your-username/universal-webscraper.git
cd universal-webscraper

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

Verifying Installation
To confirm the setup, run:
python run.py --help

This should display the CLI help message with available options.
Troubleshooting Installation

Error: chromedriver not found: Ensure Chrome is installed, and webdriver-manager is correctly installed (pip install webdriver-manager).
Error: Python version too old: Verify Python version with python --version. Upgrade to 3.8+ if needed.
Permission issues: On Linux/Mac, try sudo pip install -r requirements.txt or use --user flag.

🕹️ Usage
Basic Usage
Run the scraper and enter the target URL when prompted:
python run.py

🔗 Enter website URL to scrape: https://example.com/data-table

Scraped data will be saved to:
output/example_com_data-table.json

Advanced Options
# Run in headless mode (no browser window)
python run.py --headless

# Specify output directory
python run.py --output custom_output_dir

🐍 Using as a Python Module
You can import and use the UniversalScraper class in your Python scripts for programmatic scraping.
Example
from scraper.universal_scraper import UniversalScraper

# Initialize scraper
scraper = UniversalScraper(headless=True)

# Scrape a URL
url = "https://example.com/data-table"
table_data = scraper.scrape(url)

# Save to JSON
scraper.save_to_json(table_data, output_dir="output")

# Close browser
scraper.close()

print(f"Data saved to output/example_com_data-table.json")

📋 Sample Output
The scraper extracts table data and saves it as a structured JSON file. Below is an example output from scraping a table on https://example.com/data-table:
[
  {
    "row_1": {
      "Name": "John Doe",
      "Age": "30",
      "Occupation": "Engineer"
    },
    "row_2": {
      "Name": "Jane Smith",
      "Age": "25",
      "Occupation": "Designer"
    },
    "row_3": {
      "Name": "Bob Johnson",
      "Age": "45",
      "Occupation": "Manager"
    }
  }
]

This JSON represents a table with three rows and three columns, automatically extracted and formatted for easy use.
🧪 Running Tests
To run the test suite in the tests/ directory:
python -m unittest discover tests

Ensure all dependencies are installed before running tests.
📂 Project Structure
universal-webscraper/
├── run.py                 # Main entry point
├── requirements.txt       # Dependency list
├── scraper/
│   ├── __init__.py
│   ├── universal_scraper.py  # Core scraping logic
│   └── utils.py          # Helper functions
├── output/                # Generated JSON files
├── tests/                 # Test cases
└── venv/                  # Virtual environment

🛠️ Dependencies

Selenium: For JavaScript rendering
BeautifulSoup: For HTML parsing
Webdriver-manager: For managing browser drivers

📅 Roadmap

[x] Basic table extraction
[x] JSON output
[ ] CSV/Excel export functionality
[ ] Batch URL processing
[ ] Enhanced error handling
[ ] GUI interface (Tkinter/Flask)
[ ] API integration

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the project
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

⚠️ Disclaimer
This tool is for educational purposes only. Always check a website's robots.txt and terms of service before scraping, and respect rate limits.
👨‍💻 Author
Thirumalaivasan GJ

GitHub Profile
✉️ Email: your.email@example.com

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
