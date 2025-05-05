# compare male and female names

from nltk.corpus import names
import nltk
import matplotlib.pyplot as plt

names = nltk.corpus.names

print(names.fileids())

male_names = names.words('male.txt')
female_names = names.words('female.txt')

common_names = [word for word in male_names if word in female_names]

print(common_names[10:])

# count number of appearances of america and citizen in the presidential speeches

cfd = nltk.ConditionalFreqDist((fileid, name[-1])
                                for fileid in names.fileids()
                               for name in names.words(fileid))

cfd.plot()

plt.show()
