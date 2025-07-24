# Example: Reading and tokenizing text from a local file

import nltk

# Read the contents of a local file (replace 'sample.txt' with your file)
with open('sample.txt', encoding='utf8') as f:
    raw_text = f.read()

# Tokenize the text into words
words = nltk.word_tokenize(raw_text)

# Tokenize the text into sentences
sentences = nltk.sent_tokenize(raw_text)

print('First 10 words:', words[:10])
print('First 2 sentences:', sentences[:2]) 