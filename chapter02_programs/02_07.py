# Inaugural Address Corpus

from nltk.corpus import inaugural
import nltk
import matplotlib.pyplot as plt

print(inaugural.fileids()[:10])
print(inaugural.fileids()[-10:])

# this is in fact presidential address

print([fileid[:4] for fileid in inaugural.fileids()])

# print(inaugural.raw(fileids = '2025-Trump.txt'))

# count number of appearances of america and citizen in the presidential speeches

cfd = nltk.ConditionalFreqDist((target,fileid[:4])
                                for fileid in inaugural.fileids()
                               for word in inaugural.words(fileid)
                               for target in ['america', 'citizen']
                                              if word.lower().startswith(target))

cfd.plot(title = "Counting the words america and citizen in US presidential speeches")
plt.legend(loc='upper left')
plt.figure(figsize=(10, 6))

plt.show()
