"""
Python's regular expressions are greedy by defaulf, which means that in ambiguous
situations, they will match the longest string possible.
"""

# Non-greedy (lazy) '{}?'

import re
from helper_function import safe_search


greedy_pattern = re.compile(r'(Ha){3,5}')
print(safe_search(greedy_pattern, "HaHaHaHaHa"))

lazy_pattern = re.compile(r'(Ha){3,5}?')
print(safe_search(lazy_pattern, "HaHaHaHaHa"))

# Matching Everything '.*'

name_pattern = re.compile(r'First Name: (.*) Last Name: (.*)')
text = "First Name: Al Last Name: Sweigart"
print(safe_search(name_pattern, text, 1))
print(safe_search(name_pattern, text, 2))

"""
For lazy version of this is '.*?'
"""

# Matching NewLine Characters

newline_re = re.compile(r'.*', re.DOTALL)
text = "Search the public trust.\nProtect the innocent.\nUphold the law."
print(safe_search(newline_re, text))






