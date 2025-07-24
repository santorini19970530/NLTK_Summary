# Example: Formatting and writing results to files

import nltk
from collections import Counter

text = "NLTK makes text processing easy. NLTK is powerful and flexible."
words = nltk.word_tokenize(text.lower())

# Count word frequencies
freq = Counter(words)

# Format as a table
lines = [f"{'Word':<10}{'Count':>5}"]
for word, count in freq.items():
    lines.append(f"{word:<10}{count:>5}")

# Print the table
print('\n'.join(lines))

# Write to a file
with open('word_frequencies.txt', 'w', encoding='utf8') as f:
    f.write('\n'.join(lines))

print("Word frequencies written to 'word_frequencies.txt'") 