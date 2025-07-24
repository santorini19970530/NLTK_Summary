# Sequence operations, zipping, sorting, and generator expressions

words = ['I', 'turned', 'off', 'the', 'spectroroute']
tags = ['noun', 'verb', 'prep', 'det', 'noun']

# Pair words with tags
pairs = list(zip(words, tags))
print('Pairs:', pairs)

# Sorting words by length
sorted_words = sorted(words, key=len)
print('Sorted by length:', sorted_words)

# Generator expression for word lengths
lengths = (len(w) for w in words)
print('Word lengths:', list(lengths)) 