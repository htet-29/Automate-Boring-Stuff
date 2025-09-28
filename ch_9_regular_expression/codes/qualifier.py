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

# Matching Everything with the Dot Character '.'

"""
Dot character means "any single character except the newline.
"""

at_re = re.compile(r'.at')
ats = at_re.findall("The cat in the hat sat on the flat mat.")
print(ats)

"""
The dot character will match just one character, e.g. 'flat' matched only 'lat'
"""


# Matching an Optional Pattern
# Match Zero or One Qualifiers '?'
pattern = re.compile(r'42!?')
print(pattern.search('42!'))
print(pattern.search('42'))


"""
To make multiple characters optional, place them in a a group and put '?' after the group
"""

# Matching Zero or More Qualifiers '*'

pattern = re.compile(r'Eggs\s*(and spam\s*)*')
print(pattern.search('Eggs'))
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))
print(pattern.search('Eggs and spam and spam and spam'))

# Matching One or More Qualifiers '+'

pattern = re.compile(r'Eggs\s*(and spam\s*)+')
print(pattern.search('Eggs'))
print(pattern.search('Eggs and spam'))
print(pattern.search('Eggs and spam and spam'))
print(pattern.search('Eggs and spam and spam and spam'))

# Matching a Specific Number of Qualifiers

pattern = re.compile(r'(Ha){3,4}')
print(pattern.search("HaHa"))
print(pattern.search("HaHaHa"))
print(pattern.search("HaHaHaHa"))

"""
{3,} > Three or More
{,5} > at most five 
"""
