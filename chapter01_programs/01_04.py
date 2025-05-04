# similar : list out similar words, in case a word is having many meanings

# common_contexts : list out contexts that are shared by two or more words

from nltk.book import *

print(f'\nShow all of the similiar words of \'monstrous\' in text1')
print(text1.similar("monstrous"))

print(f'\nShow all of the similar words of \'monstrous\' in text2')
print(text2.similar("monstrous"))

print(f'\nShow all of the similiar words that have common meanings of \'monstrous\' and \'very\' in text1')
print(text1.common_contexts(["monstrous", "very"]))

print(f'\nShow all of the similiar words that have common meanings of \'monstrous\' and \'very\' in text2')
print(text2.common_contexts(["monstrous", "very"]))
