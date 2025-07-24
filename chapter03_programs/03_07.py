# Example: Segmentation and evaluation

import nltk

text = "This is a sentence. Here is another one! And a third? Yes."

# Sentence segmentation
sentences = nltk.sent_tokenize(text)
print('Sentences:', sentences)

# Word segmentation for each sentence
for i, sent in enumerate(sentences):
    words = nltk.word_tokenize(sent)
    print(f'Words in sentence {i+1}:', words)

# Evaluation: count number of sentences and words
num_sentences = len(sentences)
num_words = sum(len(nltk.word_tokenize(sent)) for sent in sentences)
print(f'Number of sentences: {num_sentences}')
print(f'Total number of words: {num_words}') 