# Example: Stemming and word pattern extraction using regex

import re

words = ['running', 'jumps', 'easily', 'fairly', 'happily', 'cats', 'boxes', 'flies', 'crying']

# Simple regex-based stemmer (removes common suffixes)
def simple_stem(word):
    return re.sub(r'(ing|ly|ed|ious|ies|ive|es|s|ment)$', '', word)

stems = [simple_stem(w) for w in words]
print('Original words:', words)
print('Stemmed words:', stems)

# Find all words with 'y' at the end
ends_with_y = [w for w in words if re.search(r'y$', w)]
print('Words ending with y:', ends_with_y) 