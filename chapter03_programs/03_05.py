# Example: Regular expressions and pattern matching

import re

text = "The rain in Spain falls mainly in the plain."

# Find all words ending with 'ain'
words_ending_ain = re.findall(r'\b\w*ain\b', text)
print('Words ending with "ain":', words_ending_ain)

# Find all words that start with 'S' or 's'
words_start_s = re.findall(r'\b[Ss]\w*\b', text)
print('Words starting with S or s:', words_start_s)

# Extract all numbers (if any)
text2 = "There are 3 cats, 7 dogs, and 1 bird."
numbers = re.findall(r'\d+', text2)
print('Numbers:', numbers) 