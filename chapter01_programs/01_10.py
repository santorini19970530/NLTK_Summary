# statistics function of nltk

from nltk.book import *
import matplotlib.pyplot as plt

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

# count each of the distinct vocabs in text1 and then list out the first 50 occurrances vocabs

fdist1 = FreqDist(text1)

print(fdist1)

print(f'\nThe first 50 common vocabs in text1 : \n{fdist1.most_common(50)}')

# plot the cumulative curve of distinct word counts

fdist1.plot(50, cumulative=True)

plt.show()
