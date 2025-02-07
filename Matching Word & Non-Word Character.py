```
Matching Digits & Non-Digit Characters: 
You have a test string s . Your task is to match the pattern xxxXxxxxxxxxxxXxxx
Here x denotes any word character , and X denotes any non-word character.

\w: used for word characters that are alphnumeric characters, i.e 0-9, a-z, A-Z
\W: used for non word characters.
```

Regex_Pattern = r"[\w]{3}[\W]{1}[\w]{10}[\W]{1}[\w]{3}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())
