# CMU pronouncing dictionary for US English

from nltk.corpus import cmudict

entries = cmudict.entries()

print(len(entries))

for entry in entries[42371 : 42379]:
    print(entry)

# print out words and the middle syllable for those having three syllables, starting with P, ending with T

for word, pron in entries:
    if len(pron) == 3:
        ph1, ph2, ph3 = pron
        if ph1 == 'P' and ph3 == 'T':
            print(word, ph2, end = ' ')

print('\n')

# finds all words whose pronunciation ends with a syllable sounding like nicks

syllable = ['N', 'IH0', 'K', 'S']

print([word for word, pron in entries if pron[-4 : ] == syllable])

# finds out words having the last character n but pronounced

print([w for w, pron in entries if pron[-1] == 'M' and w[-1] == 'n'])

# finds out endings with n sound but not end with n_

print(sorted(set(w[:2] for w, pron in entries if pron[0] == 'N' and w[0] != 'n')))

# find the stress of the pronounciation
def stress(pron):
    return [char for phone in pron for char in phone if char.isdigit()]

print([w for w, pron in entries if stress(pron) == ['0', '1', '0', '2', '0']])

print([w for w, pron in entries if stress(pron) == ['0', '2', '0', '1', '0']])

# find the words starting with P and have three sounds, group the results by first and second sounds

p3 = [(pron[0]+'-'+pron[2], word)
       for (word, pron) in entries
      if pron[0] == 'P' and len(pron) == 3]

cfd = nltk.ConditionalFreqDist(p3)

for template in sorted(cfd.conditions()):
    if len(cfd[template]) > 10:
        words = sorted(cfd[template])
        wordstring = ' '.join(words)
        print(template, wordstring[:70] + "...")
