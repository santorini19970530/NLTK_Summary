## Summary for NLTK Book Chapter 1

1. Texts are represented in Python using lists: `['Monty', 'Python']`.
   We can use indexing, slicing, and the `len()` function on lists.

2. A word "token" is a particular appearance of a given word in a text.
   A word "type" is the unique form of the word as a particular sequence of letters.
   We count word tokens using `len(text)` and word types using `len(set(text))`.

3. We obtain the vocabulary of a text `t` using `sorted(set(t))`.

4. We operate on each item of a text using `[f(x) for x in text]`.

5. To derive the vocabulary, collapsing case distinctions and ignoring punctuation, we can write `set(w.lower()` for `w` in text `if w.isalpha())`.

6. We process each word in a text using a `for` statement, such as `for w in t:` or `for word in text:`.
   This must be followed by the colon character and an indented block of code, to be executed each time through the loop.

7. We test a condition using an `if` statement: `if len(word) < 5:`.
   This must be followed by the colon character and an indented block of code, to be executed only if the condition is true.

8. A frequency distribution is a collection of items along with their frequency counts (e.g., the words of a text and their frequency of appearance).

9. A function is a block of code that has been assigned a name and can be reused.
   Functions are defined using the def keyword, as in `def mult(x, y):`.
   `x` and `y` are parameters of the function, and act as placeholders for actual data values.

10. A function is called by specifying its name followed by zero or more arguments inside parentheses, like this: `texts()`, `mult(3, 4)`, `len(text1)`.
