# Examples of value equality, object identity, and truthiness in Python

a = [1, 2, 3]
b = a
print('a == b:', a == b)  # True
print('a is b:', a is b)  # True

a = [1, 2, 3]
b = [1, 2, 3]
print('a == b:', a == b)  # True
print('a is b:', a is b)  # False

# Truthiness examples
print('bool([]):', bool([]))  # False
print('bool(""):', bool(""))  # False
print('bool([1]):', bool([1]))  # True

# Using all() and any()
print('all([True, True, False]):', all([True, True, False]))  # False
print('any([False, False, True]):', any([False, False, True]))  # True 