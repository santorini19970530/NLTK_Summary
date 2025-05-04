# distribution of word length

from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

# some word comparison operators

print(f"\nWords ending with \'ableness\' in text1 \n{sorted(w for w in set(text1) if w.endswith('ableness'))}")

print(f"\nWords containing \'gnt\' in text4 \n{sorted(term for term in set(text4) if 'gnt' in term)}")

print(f"\nWords having initial capital letters and remaining small letters in text6 \n{sorted(item for item in set(text6) if item.istitle())}")

print(f"\nWords those in fact digits in sent7 \n{sorted(item for item in set(sent7) if item.isdigit())}")

'''
# exercises
sorted(w for w in set(text7) if '-' in w and 'index' in w)
sorted(wd for wd in set(text3) if wd.istitle() and len(wd) > 10)
sorted(w for w in set(sent7) if not w.islower())
sorted(t for t in set(text2) if 'cie' in t or 'cei' in t)
'''
