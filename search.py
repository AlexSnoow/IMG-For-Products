# search.py
import requests
from bs4 import BeautifulSoup

def search_images(query):
    url = f"https://www.bing.com/images/search?q={query}&form=HDRSC2&first=1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
