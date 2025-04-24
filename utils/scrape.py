import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.get_text()
    except:
        return "Failed to load page."
