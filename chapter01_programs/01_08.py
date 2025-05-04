# count : count number of occurrances of a word in text

from nltk.book import *

print(f'\ntext3 length is {len(text3)}')

print(f'\ntext3 is having {len(set(text3))} vocabularies (individual words)')

# calculate lexical richness of text

lexical_richness = len(set(text3)) / len(text3)

print(f'\nLexical richness = no. of distinct words / no. of words =\n{lexical_richness}')

word = 'a'
print(f'\noccurrances percentage of word \'{word}\' in text4 = \n{100 * text4.count(word) / len(text4)}')

# setting up functions can reduce repeated operations

def lexical_diversity(text):
    return len(set(text)) / len(text)


def percentage(count, total):
    return 100 * count / total

print(lexical_diversity(text3))

print(lexical_diversity(text5))

print(percentage(4, 5))

print(percentage(text4.count('a'), len(text4)))
