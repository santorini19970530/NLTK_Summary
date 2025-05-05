# brown corpus

from nltk.corpus import brown

print(f'Categories of Brown Corpus \n{brown.categories()}\n')

print(f'Words in news category \n{brown.words(categories = 'news')}\n')

print(f'Words in cg22 category \n{brown.words(fileids = 'cg22')}\n')

print(f'Sentences of words in news, editorial and reviews categories \n{brown.sents(categories = ['news', 'editorial', 'reviews'])}')
