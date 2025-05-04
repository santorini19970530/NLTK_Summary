# handling collocations and bigrams - sequence of words usually stick together for a meaning

from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

# extract collocations out

print(f'\nCollocations in text4 : \n')
# collocations function prints out directly to the console when called, not returning value
text4.collocations()

print(f'\nCollocations in text8 : \n')
text8.collocations()
