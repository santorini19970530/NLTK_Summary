# Program decomposition, assertions, and safe file handling

def lexical_diversity(text):
    return len(set(text)) / len(text)

# Assertion for testing
assert lexical_diversity(['a', 'b', 'a']) == 2/3

# Safe file handling
with open('file.txt', 'w') as f:
    f.write('Hello, world!\n')

with open('file.txt') as f:
    data = f.read()
    print('File contents:', data) 