# revising python list and string operations

from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

# lists of words already in the nltk.book library

print(sent1, sent2, sent3)

# concatenate the lists

print(sent1 + sent2 + sent3)

# appending word onto the list, placing on the last position

sent1.append('Some')
print(sent1)

# find the 172'nd word from text4 (index starts from 0)

print(text4[173])

# get the position of the first occurrance of the word awaken from text4

print(text4.index('awaken'))

# slicing the lists

print(text5[16715 : 16735])

print(text6[1600 : 1625])

print(text2[141525 : ])

# concatenating two strings with specified string (e.g. space)

print(' '.join(['Monty', 'Python']))

# split a string with space, gives out a list of two strings

print('Monty Python'.split())
