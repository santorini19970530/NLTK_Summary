# distribution of word length

from nltk.book import *
import matplotlib.pyplot as plt

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

fdist = FreqDist(len(word) for word in text1)

print(fdist)

print(f'\nThere are total {fdist.N()} samples (words)\n')

print(f'\nThe most frequently long word length is {fdist.max()}\n')

# most_common() - sort the freq records by count descending order (from most appeared length to the least, but more than zero count)

# keys() - sort the freq records by word length ascending order (from shortest to longest)

# sorted_fdist = sorted(fdist.items(), key=lambda item: item[1], reverse=True)
    # this sort the frqu records by word length descending order (from longest to shortest)

for length, count in fdist.most_common():
    print(f"Length {length}: {count}")

print(f'\nFrequency table for word length\n{fdist.tabulate()}\n')

fdist.plot(50)

plt.show()
