
#~  Regular Expressions in Python

''' Regular Expressions (Regex) in Python 🐍

Regular Expressions are used to search, match, and manipulate text patterns like emails, phone numbers, passwords, etc.

#& What is Regex?

A Regular Expression is a special pattern written as a string that helps you:
Find text
Validate input
Extract specific data

Replace text

Python provides the re module for regex.
'''

#& re.match() -> Matches pattern at the start

# import re
# text="python is powerful"
# result=re.match("python",text)

# if result:
#     print("match found")
# else:
#     print("match not found")
    
#& re.search() -> Searches anywhere in string

import re
text="python is dope"
result=re.search("dope",text)

# if result:
#     print("search found")
# else:
#     print("search not found")
    
#! or 

# # print(result.group())
# print(result.start()) #shows start index value
# print(result.end()) #shows end index value

    
#& re.findall() -> Returns all matches as a list

# import re

# text="apple banana apple orange"
# result=re.findall("apple",text)
# print(result)

#& re.finditer() -> Returns match objects (iterator)

# import re

# text="cat bat rat fat"

# result=re.finditer("at",text)

# for i in result:
#     print(i.start(),i.group())

#&re.sub() -> Replace text

# import re

# text="hello world"
# result= re.sub("world","saiprakash",text)
# print(result)

#! match case email example:

# email="admin@gmail.com"

# if re.match(r"[a-z A-Z]+@",email):
#     print("valid email")
    
# else:
#     print("not a valid email.")

#! full match phone number

# result=re.fullmatch(r"\d{10}","1234567890")
# print(bool(result))

print(re.search(r"\d+"," age is 24"))

print(re.search(r"a.*c","abcnmds"))

m=(re.search(r"\w+(?=@)","test@gmail.com"))
print(m.group())

#! regular expression modifiers

print(re.search("python","Python",re.I)) #ignores the case senstive



#! matching pattern with multi line

text="one\ntwo\nthree\nfour"

print(re.findall(r"^t\w+",text,re.M))
