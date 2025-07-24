## Detailed Summary for NLTK Book Chapter 2: Accessing Text Corpora and Lexical Resources

### 2.1 Accessing Text Corpora
- A text corpus is a large, structured collection of texts. NLTK provides access to many corpora, such as the Gutenberg, Brown, Reuters, and Inaugural Address corpora.
- Corpora can be categorized by genre or topic, and some categories may overlap (e.g., Brown corpus genres, Reuters topics).
- Key NLTK corpus functions:
```python
# Get words from a corpus or file
nltk.corpus.gutenberg.words('austen-emma.txt')
# Get sentences from a corpus or file
nltk.corpus.gutenberg.sents('austen-emma.txt')
# Get raw text as a string
nltk.corpus.gutenberg.raw('austen-emma.txt')
# List available files and categories
nltk.corpus.gutenberg.fileids()
nltk.corpus.brown.categories()
```
- Example: Analyzing sentence lengths in Shakespeare's Macbeth using `sents()` and finding the longest sentence.
```python
# Find the longest sentence in Macbeth
macbeth_sentences = nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt')
longest_len = max(len(s) for s in macbeth_sentences)
longest_sent = max(macbeth_sentences, key=len)
```
- Example: Using `concordance()` to find all occurrences of a word in a text (after converting to `nltk.Text`).
```python
# Find all occurrences of a word in a text
macbeth_text = nltk.Text(nltk.corpus.gutenberg.words('shakespeare-macbeth.txt'))
macbeth_text.concordance('sleep')
```
- Practical: Summarizing statistics for each text (average word length, sentence length, vocabulary size).
```python
# Summarize statistics for each text in Gutenberg corpus
for fileid in nltk.corpus.gutenberg.fileids():
    num_chars = len(nltk.corpus.gutenberg.raw(fileid))
    num_words = len(nltk.corpus.gutenberg.words(fileid))
    num_sents = len(nltk.corpus.gutenberg.sents(fileid))
    vocab = set(w.lower() for w in nltk.corpus.gutenberg.words(fileid))
    print(fileid, int(num_chars/num_words), int(num_words/num_sents), int(len(vocab)/num_words))
```

### 2.2 Conditional Frequency Distributions
- Conditional frequency distributions (CFDs) are collections of frequency distributions, each for a different condition (e.g., genre, year, or category).
- Key NLTK class: `nltk.ConditionalFreqDist`.
- CFDs are useful for comparing word usage across genres or time periods.
- Example: Comparing modal verbs (can, could, may, might, must, will) in different genres of the Brown corpus.
```python
import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)
```
- Example: Tracking the frequency of words like "america" and "citizen" in U.S. presidential inaugural addresses over time, and plotting trends.
```python
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen'] if w.lower() == target
)
cfd.plot()
```

### 2.3 More Python: Reusing Code
- For longer programs, use a text editor and save code in `.py` files, importing as needed.
- Python functions allow code reuse and organization. Methods are functions associated with objects (e.g., `word.isalpha()`).
- Example: Defining a custom pluralization function in a separate file and importing it for use.
```python
# In text_proc.py
def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'

# In another script
from text_proc import plural
plural('berry')
```
- Use `help(obj)` in the interpreter to get documentation for any object.
```python
help(str)
help(nltk.corpus.gutenberg.words)
```

### 2.4 Lexical Resources
- WordNet is a semantically-oriented dictionary of English, organized into synonym sets (synsets) and a network of lexical relations (hypernyms, hyponyms, antonyms, etc.).
- Key NLTK module: `nltk.corpus.wordnet`.
- Example: Exploring synsets, definitions, and relationships in WordNet.
```python
from nltk.corpus import wordnet as wn
wn.synsets('car')
wn.synset('car.n.01').definition()
wn.synset('car.n.01').hypernyms()
```
- NLTK provides access to other lexical resources:
  - CMU Pronouncing Dictionary (`nltk.corpus.cmudict`): Word pronunciations and stress patterns.
  - Names corpus (`nltk.corpus.names`): Lists of male and female names.
  - Stopwords corpus: Common words to filter out in analysis.
- Example: Finding unusual words in a text by comparing to a standard English wordlist.
```python
import nltk
from nltk.corpus import words
text_vocab = set(w.lower() for w in nltk.corpus.gutenberg.words('austen-sense.txt'))
english_vocab = set(w.lower() for w in words.words())
unusual = text_vocab - english_vocab
```
- Example: Calculating the fraction of content words (non-stopwords) in a corpus.
```python
from nltk.corpus import stopwords
stopwords_list = set(stopwords.words('english'))
words_in_text = [w.lower() for w in nltk.corpus.gutenberg.words('austen-emma.txt')]
content = [w for w in words_in_text if w not in stopwords_list]
print('Fraction of content words:', len(content) / len(words_in_text))
```
- Example: Analyzing name endings and their gender associations, and plotting results.
```python
from nltk.corpus import names
import nltk
cfd = nltk.ConditionalFreqDist(
    (name[-1], gender)
    for gender in ['male', 'female']
    for name in names.words(gender + '.txt')
)
cfd.plot()
```
- Example: Working with word pronunciations, stress patterns, and grouping by phonetic features.
```python
from nltk.corpus import cmudict
d = cmudict.dict()
d['blog']
# Find all words with a single syllable
one_syllable_words = [w for w, pron in d.items() if len([ph for ph in pron[0] if ph[-1].isdigit()]) == 1]
```

### 2.5 Summary
- NLTK makes it easy to access and analyze a wide range of text corpora and lexical resources.
- Python programming skills (functions, methods, imports) are essential for effective NLP work.
- Lexical resources like WordNet and CMUdict provide rich data for linguistic analysis, including semantic relationships and phonetic information.
- Practical skills include using corpus readers, frequency distributions, and writing reusable code for text analysis.

### 2.6 Exercises and Applications
- Practice loading and exploring different corpora (Gutenberg, Brown, Reuters, Inaugural, Webtext, Chat).
- Compare word usage across genres, time periods, or categories using CFDs.
- Write and import custom functions for text processing (e.g., pluralization, lexical diversity).
- Explore WordNet for synonyms, definitions, and semantic relationships.
- Analyze name data, stopwords, and word pronunciations.

---

## Chapter 2 Code Files

Below are the code examples for this chapter. Each filename links to the corresponding Python script in the `chapter02_programs` directory:

- [02_01.py](../chapter02_programs/02_01.py): Explore the Gutenberg corpus and concordances.
- [02_02.py](../chapter02_programs/02_02.py): Analyze Gutenberg texts, sentence lengths, and summary statistics.
- [02_03.py](../chapter02_programs/02_03.py): Access web and chat text corpora.
- [02_04.py](../chapter02_programs/02_04.py): Explore the Brown corpus by category and file.
- [02_05.py](../chapter02_programs/02_05.py): Study stylistics and modal verbs in the Brown corpus using frequency distributions.
- [02_06.py](../chapter02_programs/02_06.py): Work with the Reuters corpus and its categories/files.
- [02_07.py](../chapter02_programs/02_07.py): Analyze the Inaugural Address corpus and plot word frequencies over time.
- [02_08.py](../chapter02_programs/02_08.py): Use a custom pluralization function from an imported module.
- [02_09.py](../chapter02_programs/02_09.py): Find unusual words and compute content word fractions.
- [02_10.py](../chapter02_programs/02_10.py): Compare male and female names and plot name endings.
- [02_11.py](../chapter02_programs/02_11.py): Work with the CMU Pronouncing Dictionary and analyze word pronunciations and stress.
- [text_proc.py](../chapter02_programs/text_proc.py): Custom function for pluralizing English words.
