# Reuters Corpus

from nltk.corpus import reuters

fileids = reuters.fileids()

print(fileids[:10])

categories = reuters.categories()

print(categories[:10])

print(reuters.categories('training/9865')[:14])

print(reuters.categories(['training/9865', 'training/9880']))

print(reuters.fileids('barley'))

print(reuters.fileids(['barley', 'corn']))

print(reuters.words(['training/9865', 'training/9880']))

print(reuters.words(categories='barley'))

print(reuters.words(categories=['barley', 'corn']))
