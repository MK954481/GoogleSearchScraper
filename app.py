from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# specify the query you want to search for
query = "House with no mirrors"

# initialize the web driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# navigate to Google
start = time.time()
driver.get("https://www.google.com")

# find the search box and enter the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(query)
search_box.submit()

# wait for the page to load
driver.implicitly_wait(10)

# get the page source
page_source = driver.page_source

# parse the page source using Beautiful Soup
soup = BeautifulSoup(page_source, "html.parser")

# Find the first five search result elements
results = soup.find_all("div", class_="g")[:5]

# Loop through the search results
for result in results:
    heading = result.find("h3").text
    description = result.find(
        "div", class_="VwiC3b yXK7lf MUxGbd yDYNvb lyLwlc lEBKkf")
    if description:
        description = description.text
    else:
        description = "Description not found"
    href = result.find("a")["href"]
    print(f"Heading: {heading}")
    print(f"Description: {description}")
    print(f"Href: {href}\n")

end = time.time()
print("Time taken to scrape the results: ", end-start, " ms")
# close the web driver
driver.quit()
