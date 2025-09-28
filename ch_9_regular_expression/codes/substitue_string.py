import re

agent_pattern = re.compile(r'Agent \w+')
result = agent_pattern.sub('CENSORED', 'Agent Alice ontacted Agent Bob.')
print(result)
print(result)

agent_pattern = re.compile(r'Agent (\w)\w*')
result = agent_pattern.sub(r'\1****', 'Agent Alice contacted Agent Bob.')
print(result)

"""
The \1 in the regular expression string is replaced by whatever
text was matched by group 1 - that is, the (\\w) group of the regular expression
"""
