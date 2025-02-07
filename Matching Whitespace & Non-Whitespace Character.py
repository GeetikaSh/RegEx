```
Matching Digits & Non-Digit Characters: 
You have a test string s . Your task is to match the pattern xxXxxXxx
Here x denotes whitespace characters, and X denotes non-white space characters.

\S is used for no white space characters
\s is used for white space characters
```

Regex_Pattern = r"[\S]{2}[\s]{1}[\S]{2}[\s]{1}[\S]{2}"	

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
