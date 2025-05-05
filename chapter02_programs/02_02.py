# show all of the information in gutenberg text

from nltk.corpus import gutenberg   # shorten the commands by this import
import pandas as pd

# The raw() function gives us the contents of the file without any linguistic processing.
macbeth_raws = gutenberg.raw('shakespeare-macbeth.txt')

# The sents() function divides the text up into its sentences, where each sentence is a list of words
macbeth_sentences = gutenberg.sents('shakespeare-macbeth.txt')

print(macbeth_raws)
print(macbeth_sentences)
print(macbeth_sentences[1116])

longest_len = max(len(s) for s in macbeth_sentences)
print([s for s in macbeth_sentences if len(s) == longest_len])

# list out all of the information of each gutenberg texts

'''
# this is original code, i put the information into dataframe for the ease of print
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(word.lower() for word in gutenberg.words(fileid)))

    print(f'{round(num_chars/num_words)}\t{round(num_words/num_sents)}\t{round(num_words/num_vocab)}\t{fileid}')
'''

df = pd.DataFrame(columns = ['fileid', 'Avg. Word Length', 'Avg. Sentence Length', 'Avg. appearances of vocab in text']);

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(word.lower() for word in gutenberg.words(fileid)))

    df.loc[len(df)] = [fileid, round(num_chars/num_words), round(num_words/num_sents), round(num_words/num_vocab)]

print(df)
