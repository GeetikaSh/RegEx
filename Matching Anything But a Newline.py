'''
Your task is to write a regular expression that matches only and exactly strings of form: abc.efg.hij.klm
'''
regex_pattern = r"^[^\n]{3}\.[^\n]{3}\.[^\n]{3}\.[^\n]{3}$"

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
