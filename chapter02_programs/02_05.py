# using Brown corpus to study stylistics of different kinds of passages

import nltk
from nltk.corpus import brown

news_text = brown.words(categories = 'news')

fdist = nltk.FreqDist(word.lower() for word in news_text)

modals = ['can', 'could', 'may', 'might', 'must', 'will']

print('Counts of modal words in the news categories\n')

for modal_word in modals :
    print(modal_word + ':', fdist[modal_word], end = ' ')

print('\n')

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories = genre)
)

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']

modals = ['can', 'could', 'may', 'might', 'must', 'will']

print("\nCounts of modal words in each of the categories\n")

cfd.tabulate(conditions=genres, samples=modals)
