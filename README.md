# Regular Expression(RegEx)
A Regular Expression (Regex) is a sequence of characters that define a search pattern.\
\
![In this image a Regex Pattern is Matches with the Test String](https://s3.amazonaws.com/hr-challenge-images/13619/1449634776-aeeb4b9294-ach01_.png)\
**In this image a Regex Pattern is matched with the Test String**

## Regex Applications
Some of the common **RegEx** applications are:
- **Validation:** Example ; email, phone number, pasword strength
- **Search and Replace:** Example- finding and replacing charcters in a document.
- **Extraction Information:** Example- extacting URLs, dates, specific word from text.
- **Log file Analysis:** Example- filtering logs for specific patterns.

## RegEx Functions

* ***re***: import reodule
* ***findall()***:Returns a list containing all matches https://github.com/GeetikaSh/RegEx/blob/main/Matching%20Specific%20String
* ***search()***:Returns a Match object if there is a match anywhere in the string
* ***split()***: Returns a list where the string has been split at each match
* ***sub()***:	 Replaces one or many matches with a string\

**The Match object has properties and methods used to retrieve information about the search, and the result:**
* ***span()***: returns a tuple containing the start-, and end positions of the match.
* ***string()***: returns the string passed into the function
* ***group()***: returns the part of the string where there was a match




