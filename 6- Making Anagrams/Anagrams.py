from collections import Counter
from string import ascii_lowercase
a = input().strip()
b = input().strip()

def number_needed(a, b):
    a_dict = Counter(a)
    b_dict = Counter(b)
    difference = 0
    for letter in ascii_lowercase:
        difference += abs(a_dict[letter] - b_dict[letter])
    return difference
print(number_needed(a, b))