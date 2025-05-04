# concordance : shows every occurrance of a given word, together with the same context

from nltk.book import *

print(f'\nShow all of the occurrances of word \'monstrous\' in text1')
print(text1.concordance("monstrous"))

print(f'\nShow all of the occurrances of word \'affection\' in text2')
print(text2.concordance("affection"))
