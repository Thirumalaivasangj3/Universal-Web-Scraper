# 🌐 Universal Web Scraper

A powerful web scraping tool built with Python that extracts structured table data from any website, including JavaScript-rendered pages.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-orange.svg)](https://selenium.dev)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.0+-lightgrey.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## 🚀 Features

- **Universal Compatibility**: Scrapes tables from any website, including dynamic JS content
- **Smart Output**: Automatically saves structured data as JSON files
- **Seamless Operation**: Headless browser mode for background operation
- **Intelligent Naming**: Generates filenames based on URL structure
- **Easy Integration**: Simple CLI interface for quick adoption

## 📦 Installation

### Prerequisites
- Python 3.8+
- Chrome/Firefox browser (for Selenium)

### Setup
```bash
# Clone repository
git clone https://github.com/your-username/universal-webscraper.git
cd universal-webscraper

# Create virtual environment
python3 -m venv venv

# Activate environment (Linux/Mac)
source venv/bin/activate

# Activate environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
