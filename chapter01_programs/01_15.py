# distribution of word length

from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

# some word comparison operators

print(f"\nConvert all words to upper character in text1, then count the vocabs\n")

all_upper = [word.upper() for word in text1]
all_lower = [word.lower() for word in text1]

# then there will be no double count on 'This' and 'this'

print(f"no. of words of text1 : {len(text1)}\n\
    no. of vocabs of text1 : {len(set(text1))}\n\
    no. of words of text1 after all converted into capital letters : {len(all_upper)}\n\
    no. of vocabs of text1 after all converted into small letters : {len(set(all_lower))}\n")

# chop off more words which are just non-alphabetic items

all_lower_alpha = [word.lower() for word in text1 if word.isalpha()]

print(f"no. of vocabs of text1 after all converted into small letters and remove non-alphabetic words : {len(set(all_lower_alpha))}")
