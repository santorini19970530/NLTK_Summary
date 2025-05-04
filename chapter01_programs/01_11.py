# fine-grained selection of words

from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

# count each of the vocabs in text1 and then list out those having more than 15 characters

vocabularies = set(text1)

long_words = [word for word in vocabularies if len(word) > 15]

print(f'\nWords having more than 15 characters in text1: \n{sorted(long_words)}')

# sort out words having character length more than 7 and appeared in text5 more than 7 times

fdist5 = FreqDist(text5)

selected_long_words = sorted(word for word in set(text5) if (len(word) > 7 and fdist5[word] > 7))

print(f'\nWords having more than 7 characters and appeared more than 7 times in text5 : \n{selected_long_words}')
