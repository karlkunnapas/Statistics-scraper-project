# Statistics Estonia Scraper

## Description
A program that navigates to the Statistics Estonia main indicators page and
saves the names and numerical values of all main indicators to a file. Then, it asks the user
which indicator they want to know about and outputs it to the console.

As a scraper, I'm using Selenium webdriver because of my interest in it as with Selenium it is possible
to make automations where it's important to see the webpage itself.
## Requirements
- Firefox web browser
- Python 3.x
- Selenium library for Python

## Installation
1. Install Python 3 if not already installed: [Python Downloads](https://www.python.org/downloads/)
2. Install Selenium using pip:
   ```sh
   pip install selenium
   ```
3. Download and install the Firefox WebDriver (Geckodriver):
   - Download from: [Geckodriver Releases](https://github.com/mozilla/geckodriver/releases)
   - Add Geckodriver to your system PATH.

## Usage
1. Ensure Firefox and Geckodriver are properly installed.
2. Run the script:
   ```sh
   python statistics.py
   ```
3. Follow the on-screen instructions to query a specific indicator.
