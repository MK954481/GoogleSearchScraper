# GoogleSearchScraper
This project is a script that uses Selenium and Beautiful Soup to scrape the first five search results of a query on Google. The script navigates to Google and enters the search query, waits for the page to load and then parses the page source using Beautiful Soup. It then finds the first five search result elements and extracts the heading, the description and the link of each search result.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.x
- Selenium
- webdriver-manager
- BeautifulSoup
- Chrome browser

### Installing
pip install selenium

pip install webdriver-manager

pip install beautifulsoup4

### Run
python app.py

### Replace "House with no mirrors" with your desired search query.

### Note
This code is just an example, you can use this script to scrape the results of any search query.
