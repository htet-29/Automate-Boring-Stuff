# Case-Insensitive Matching

import re
from helper_function import safe_search

pattern = re.compile(r'robocop', re.I)
text = "RoboCop is part man, part machine, all cop."
print(safe_search(pattern, text))
text2 = "ROBOCOP protects the innocent."
print(safe_search(pattern, text2))
text3 = "Have you seen robocop"
print(safe_search(pattern, text3))
