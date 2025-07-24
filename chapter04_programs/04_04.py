# Function definitions, docstrings, and lexical diversity calculation

def lexical_diversity(text):
    """Calculate lexical diversity of a text."""
    return len(set(text)) / len(text)

sample_text = ['the', 'cat', 'sat', 'on', 'the', 'mat']
print('Lexical diversity:', lexical_diversity(sample_text))

# Using help() and docstrings
help(lexical_diversity) 