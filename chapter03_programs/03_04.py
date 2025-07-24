# Example: String operations and normalization

sample = "The quick brown fox jumps over the lazy dog! 123."

# Lowercase
lower = sample.lower()
print('Lowercase:', lower)

# Remove punctuation (simple example)
import re
no_punct = re.sub(r'[^\w\s]', '', lower)
print('No punctuation:', no_punct)

# Split into words
words = no_punct.split()
print('Words:', words)

# Join words back into a string
joined = ' '.join(words)
print('Joined:', joined) 