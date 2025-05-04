# len : count length of text from start to finish, i.e. tokens

# set : extract the distinct words from the tokens that the text uses, i.e. vocabularies

from nltk.book import *

print(f'\ntext3 length is {len(text3)}')

print(f'\ntext3 is having {len(set(text3))} vocabularies (individual words)')

print(f'\nlist out vocabularies in text3 in alphaberical order:\n{sorted(set(text3))}')
