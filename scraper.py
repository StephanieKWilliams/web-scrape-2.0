import requests
from bs4 import BeautifulSoup
import json
import logging
import time

# Set up logging
logging.basicConfig(filename='scraping.log', level=logging.INFO)

# Define the URL to scrape
URL = 'http://ipasafrica.com/'

try:
    # Fetch the web page
    response = requests.get(URL)
    response.raise_for_status() # Raises an HTTPError if the HTTP request returned an unsuccessful status code
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching the webpage: {e}")
    exit()

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store the scraped data
data = []

# Scrape all text content from the webpage
for text in soup.stripped_strings:
    data.append(str(text))

# Save the data to a JSON file with proper formatting and indentation
with open('data.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

logging.info('Scraping completed and data saved to data.json')
