import nltk

def unusual_words(text):
    text_vocab = set(word.lower() for word in text if word.isalpha())
    english_vocab = set(word.lower() for word in nltk.corpus.words.words())
    unusual = text_vocab - english_vocab
    return sorted(unusual)

print(unusual_words(nltk.corpus.gutenberg.words('austen-sense.txt')))

print(unusual_words(nltk.corpus.nps_chat.words()))


def lexical_diversity(my_text_data):
    word_count = len(my_text_data)
    vocab_size = len(set(my_text_data))
    diversity_score = vocab_size / word_count
    return diversity_score

def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

print(content_fraction(nltk.corpus.reuters.words()))
