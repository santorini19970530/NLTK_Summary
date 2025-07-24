# Higher-order functions, map, filter, lambda, and flexible function interfaces

words = ['cat', 'dog', 'fish', '123', '']

# Map: get length of each word
lengths = list(map(len, words))
print('Lengths:', lengths)

# Filter: only alphabetic words
alpha_words = list(filter(lambda w: w.isalpha(), words))
print('Alphabetic words:', alpha_words)

# Named arguments, *args, and **kwargs
def repeat(msg='<empty>', num=1):
    return msg * num

print('Repeat:', repeat('Hi', 3)) 