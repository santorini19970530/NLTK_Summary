# Example: Extracting and cleaning HTML text using BeautifulSoup

import urllib.request
from bs4 import BeautifulSoup
import nltk

# Download HTML from a web page (replace with your URL)
url = 'http://www.nltk.org/'
response = urllib.request.urlopen(url)
html = response.read().decode('utf8')

# Extract text from HTML
soup = BeautifulSoup(html, 'html.parser')
raw_text = soup.get_text()

# Tokenize the cleaned text
tokens = nltk.word_tokenize(raw_text)

print('First 20 tokens:', tokens[:20]) 