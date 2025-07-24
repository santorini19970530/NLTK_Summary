# Example: Tokenization and sentence segmentation

import nltk

sample_text = "NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces."

# Tokenize into sentences
sentences = nltk.sent_tokenize(sample_text)
print('Sentences:', sentences)

# Tokenize each sentence into words
for i, sent in enumerate(sentences):
    words = nltk.word_tokenize(sent)
    print(f'Words in sentence {i+1}:', words) 