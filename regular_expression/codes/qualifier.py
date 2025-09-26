"""
Regular expression are split into two parts 
the qualifiers that dictate what characters you are trying to match
followed by the quantifiers that dictate how many characters you are trying to match
"""

# Using Character Classes '[]' and Negative Character Classes '^'

import re

vowel_pattern = re.compile(r'[aeiouAEIOU]')
vowels = vowel_pattern.findall('RoboCop eats BABY FOOD.')
print(vowels)

"""
Inside the square brackets, the normal regular expression symbols are not interpreted as such.
"""

consonant_pattern = re.compile(r'[^aeiouAEIOU]') 
consonants = consonant_pattern.findall('RoboCop eats BABY FOOD')
print(consonants)

"""
There are many shorthand character classes we can use
"""

# Matching Everything with the Dot Character

at_re = re.compile(r'.at')
ats = at_re.findall("The cat in the hat sat on the flat mat.")
print(ats)

"""
The dot character will match just one character, e.g. 'flat' matched only 'lat'
"""





