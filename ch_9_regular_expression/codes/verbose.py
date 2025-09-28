# Managing Complex Regexes with Verbose Mode

"""
"Verbose mode" - ignore whitespace and comments inside the regular expression string.
"""

import re

pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # Area code
    (\s|-|\.)? # Separator
    \d{3} # First three digits
    (\s|-|\.) # Separator
    \d{4} # Last four digits
    (\s*(ext|x|ext\.)\s*\d{2,5})? # Extension
    )''', re.VERBOSE)


# Combining re.IGNORECASE, re.DOTALL and re.VERBOSE

regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
