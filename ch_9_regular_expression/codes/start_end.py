"""
'^' > match must occur at the beginning of the search text
'$' > at the end of the string
"""

import re
from helper_function import safe_search

whole_string_is_num = re.compile(r'^\d+$')
print(safe_search(whole_string_is_num, '123456789'))
print(safe_search(whole_string_is_num, '123456dfe789'))

# Matchig on word boundary

word_boundary = re.compile(r'\bcat.*?\b')
"""Matches a word that begin with 'cat' followed by any other characters up to next word boundary"""
text = "The cat found a catapult catalog in the catacombs."
print(safe_search(word_boundary, text))

"""
'\\B' matches anything that is not a word boundary
"""

pattern = re.compile(r'\Bcat\B')
print(pattern.findall('certificate'))
print(pattern.findall('catastrophe'))


