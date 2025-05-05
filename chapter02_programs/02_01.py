# Gutenberg Corpus

import nltk

print(f'Small sections of Project Gutenberg electronic text archive : \n{nltk.corpus.gutenberg.fileids()}')

emma = nltk.corpus.gutenberg.words('austen-emma.txt')

print(f'\nText length of Emma by Jane Austen : {len(emma)}')

# concordance belongs to Text module of nltk but not in corpus, so need to get the Text out first

emma_text = nltk.Text(emma)

print(f'\nSentences with \'surprize\'\n')
emma_text.concordance('surprize')
