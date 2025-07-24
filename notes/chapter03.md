## Detailed Summary for NLTK Book Chapter 3: Processing Raw Text

### 3.1 Accessing Text from the Web and from Disk
- Demonstrates how to read text from local files using `open()`, from the web using `urllib.request.urlopen()`, and from RSS feeds using `feedparser`.
```python
# Read text from a local file
with open('sample.txt', encoding='utf8') as f:
    raw_text = f.read()

# Read text from a web page
import urllib.request
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = urllib.request.urlopen(url)
raw = response.read().decode('utf8')

# Parse RSS feed
import feedparser
feed = feedparser.parse('http://newsrss.bbc.co.uk/rss/newsonline_world_edition/americas/rss.xml')
feed['entries'][0]['title']
```
- Covers extracting text from HTML using BeautifulSoup (`BeautifulSoup(html, 'html.parser').get_text()`) and handling different file encodings (e.g., UTF-8, Latin-1).
```python
from bs4 import BeautifulSoup
html = '<html><head><title>Test</title></head><body><p>Hello, world!</p></body></html>'
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()
```
- Introduces tokenization: splitting text into words (`nltk.word_tokenize()`) and sentences (`nltk.sent_tokenize()`).
```python
import nltk
words = nltk.word_tokenize(raw_text)
sentences = nltk.sent_tokenize(raw_text)
```
- Discusses the NLP processing pipeline: from raw text to tokens, normalization, and vocabulary extraction.
- Example: Downloading a book from Project Gutenberg, cleaning it, and preparing it for analysis.
```python
# Download and clean a book from Project Gutenberg
url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = urllib.request.urlopen(url)
raw = response.read().decode('utf8')
start_idx = raw.find('*** START OF THIS PROJECT GUTENBERG EBOOK')
end_idx = raw.find('*** END OF THIS PROJECT GUTENBERG EBOOK')
book = raw[start_idx:end_idx]
```
- Example: Using `nltk.Text` objects for further analysis and concordance.
```python
text_obj = nltk.Text(words)
text_obj.concordance('Holmes')
```

### 3.2 Strings: Text Processing at the Lowest Level
- Explains Python string operations: indexing (`s[0]`), slicing (`s[1:5]`), concatenation (`s1 + s2`), and string methods (`.lower()`, `.split()`, `.join()`, `.replace()`).
```python
s = 'Monty Python'
first_char = s[0]
substring = s[1:5]
combined = s + ' and the Holy Grail'
lowercase = s.lower()
words = s.split()
joined = ' '.join(words)
replaced = s.replace('Monty', 'Flying')
```
- Discusses Unicode and encoding issues, including reading and writing files with different encodings (`open(filename, encoding='utf8')`).
```python
with open('data.txt', encoding='utf8') as f:
    data = f.read()
with open('output.txt', 'w', encoding='utf8') as f:
    f.write(data)
```
- Shows how to process and normalize text at the character level, including counting character frequencies and visualizing them with `FreqDist`.
```python
from nltk import FreqDist
fdist = FreqDist(book)
fdist.plot(30, cumulative=False)
```

### 3.3 Regular Expressions for Detecting Word Patterns
- Introduces Python's `re` module for pattern matching and searching text.
```python
import re
# Find all words ending in 'ed'
ed_words = re.findall(r'\b\w+ed\b', raw_text)
# Find all numbers in the text
numbers = re.findall(r'\d+', raw_text)
```
- Demonstrates finding words, extracting substrings, and using regular expressions for text normalization.
- Covers meta-characters (`.`, `*`, `+`, `?`, `[]`, `()`, `|`), anchors (`^`, `$`), and grouping in regex.
- Example: Finding all words ending in "ed" or matching a specific pattern in a corpus.
- Example: Extracting numbers, email addresses, or other patterns from text.
```python
# Extract email addresses
emails = re.findall(r'[\w\.-]+@[\w\.-]+', raw_text)
```

### 3.4 Useful Applications of Regular Expressions
- Shows how to use regex for stemming (removing suffixes), searching, and extracting information from text.
- Examples include finding all vowels in a word, compressing words by removing vowels, and extracting consonant-vowel sequences from a language corpus.
```python
# Remove vowels from a word
re.sub(r'[aeiou]', '', 'beautiful')
# Find all consonant-vowel sequences
re.findall(r'[bcdfghjklmnpqrstvwxyz][aeiou]', raw_text, re.I)
```
- Example: Implementing a simple stemmer using regular expressions.
```python
# Simple regex-based stemmer
re.sub(r'(ing|ly|ed|ious|ies|ive|es|s|ment)$', '', 'processing')
```
- Example: Using regex to find all three-letter words or words with specific internal patterns.
```python
# Find all three-letter words
re.findall(r'\b\w{3}\b', raw_text)
```

### 3.5 Segmentation
- Discusses sentence segmentation using NLTK’s Punkt sentence segmenter (`nltk.sent_tokenize()`), and word segmentation using `nltk.word_tokenize()`.
```python
sentences = nltk.sent_tokenize(raw_text)
words = nltk.word_tokenize(raw_text)
```
- Explains the challenges of word segmentation in languages without explicit word boundaries (e.g., Chinese).
- Introduces algorithms for segmenting text and evaluating segmentation quality, including simulated annealing for unsupervised segmentation.
- Example: Segmenting a stream of text into words and sentences, and evaluating the segmentation.

### 3.6 Formatting: From Lists to Strings
- Covers formatting output using `str.format()`, f-strings, and the `textwrap` module for pretty-printing.
```python
# Format a string using str.format()
'Word: {}, Count: {}'.format('the', 100)
# Format a string using f-strings
word = 'the'; count = 100
f'Word: {word}, Count: {count}'
# Wrap text for display
import textwrap
wrapped = textwrap.fill('This is a very long sentence that needs to be wrapped.', width=40)
```
- Shows how to join lists into strings (`' '.join(list)`), format tables, and wrap text for display.
- Writing results to files, including tabular data and formatted text.
```python
# Write tabular data to a file
with open('results.txt', 'w', encoding='utf8') as f:
    for word, freq in [('the', 100), ('and', 80)]:
        f.write(f'{word}\t{freq}\n')
```
- Example: Tabulating word frequencies and formatting them for display or file output.

### 3.7 Exercises and Applications
- Practice extracting and cleaning text from various sources (local files, web, RSS feeds).
- Write regex patterns for different linguistic phenomena (e.g., word endings, numbers, emails).
- Implement a simple stemmer using regular expressions.
- Segment a stream of text into words and sentences, and evaluate the segmentation.
- Format and write analysis results to files for reporting or further processing.

---

## Chapter 3 Code Files

Below are the code examples for this chapter. Each filename links to the corresponding Python script in the `chapter03_programs` directory:

- [03_01.py](../chapter03_programs/03_01.py): Example code for reading and tokenizing text from a local file.
- [03_02.py](../chapter03_programs/03_02.py): Example code for extracting and cleaning HTML text using BeautifulSoup.
- [03_03.py](../chapter03_programs/03_03.py): Example code for tokenization and sentence segmentation.
- [03_04.py](../chapter03_programs/03_04.py): Example code for string operations and normalization.
- [03_05.py](../chapter03_programs/03_05.py): Example code for regular expressions and pattern matching.
- [03_06.py](../chapter03_programs/03_06.py): Example code for stemming and word pattern extraction using regex.
- [03_07.py](../chapter03_programs/03_07.py): Example code for segmentation and evaluation.
- [03_08.py](../chapter03_programs/03_08.py): Example code for formatting and writing results to files. 