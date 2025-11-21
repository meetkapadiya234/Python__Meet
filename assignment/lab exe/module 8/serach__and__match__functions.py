# Example of search and match functions using re module in Python

import re

# Input string
text = "Python programming is fun and powerful."

# Word to search
word = "fun"

# Using re.search() to find the word
if re.search(word, text):
    print(f"The word '{word}' was found in the string.")
else:
    print(f"The word '{word}' was not found in the string.")

# /// Using re.match() to check if the word matches at the beginning

import re

# Input string
text = "Python programming is fun."

# Word to match at the beginning
word = "Python"

# Using re.match() to check if the word matches at the start
if re.match(word, text):
    print(f"The word '{word}' matches at the beginning of the string.")
else:
    print(f"The word '{word}' does not match at the beginning of the string.")


