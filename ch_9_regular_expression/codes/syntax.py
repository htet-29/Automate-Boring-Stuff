import re

# Regular Expression Example 
# phone_num_pattern_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
# match_obj = phone_num_pattern_obj.search('My number is 415-555-4242.')
# print(match_obj.group())

# Grouping with Parentheses
# phone_re = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phone_re.search('My number is 414-555-4242.')
# print(mo.group(1))
# print(mo.group(2))
# print(mo.group())
# print(mo.groups())

# Using Escape Character
# pattern = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
# mo = pattern.search("My phone number is (415) 555-4242.")
# print(mo.group(1))
# print(mo.group(2))

# Matching Characters from Alternate Groups
# pattern = re.compile(r'Cat(erpiller|astrophe|ch|egory)')
# match = pattern.search('Catch me if you can.')
# print(match.group())
# print(match.group(1))

# Returning All Matches
# findall() doesn't overlap matches
# pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# matches = pattern.findall('Cell: 515-555-9999 Work: 212-555-0000')
# print(matches)






