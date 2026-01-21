
#! 1) Question – Match, Search, Patterns, Meta-characters & Special Sequences

#~ Topics Covered:			
#~ Match and search functions, Regular expression patterns, Meta-characters, Special sequences			

'''
Write a Python program that:			
			
1. Uses re.match() to check whether a string starts with a valid employee ID in the format EMP followed by 3 digits (e.g., EMP123)			
			
2. Uses re.search() to find the first occurrence of a valid email address in a given text			
			
3. Demonstrates the use of meta-characters (., *, +, ?) and special sequences  in the patterns			
			
4. Prints matched groups using capturing parentheses			

'''

# import re

# text="EMP123"

# result=re.match("EMP",text)

# if result:
#     print("Match found")
# else:
#     print("Match not found")
    
#--------------------------------------

# import re

# email="Please contact us at konapasaip@gmail.com for assistance."

# result=re.search(r"\w+(?=@)",email)
# if result:
#     print("Email found:", result.group())
# else:
#     print("No email found")

#--------------------------------------
# import re

# text = "User id 45 logged in at 9 am"

# patterns = {
#     r"\d+": "Matches one or more digits",
#     r"\w+": "Matches one or more word characters",
#     r"\s": "Matches a single whitespace",
#     r".+": "Matches any character except newline",
#     r"\d*": "Matches zero or more digits",
#     r"\d?": "Matches zero or one digit"
# }


# for pattern, description in patterns.items():
#     match = re.search(pattern, text)
#     if match:
#         print(f"{pattern} → {match.group()} ({description})")

#-------------------------------------
# import re

# text = "My email is test@gmail.com"

# pattern = r"(\w+)@(\w+)\.(\w+)"

# match = re.search(pattern, text)

# if match:
#     print("Full match :", match.group())
#     print("Username   :", match.group(1))
#     print("Domain     :", match.group(2))
#     print("Extension  :", match.group(3))
# else:
#     print("No match found")

#! 2)Question – Assertions & Regular Expression Modifiers

#~Topics Covered: Assertions, Regular expression modifiers

'''
Write a Python program that:		
		
1. Validates a strong password using regular expressions with the following rules:		
		
Minimum 8 characters		
		
At least one uppercase letter		
		
At least one lowercase letter		
		
At least one digit		
		
At least one special character		
		
2. Uses lookahead assertions (?=)		
		
3. Uses regular expression modifiers such as:		

re.IGNORECASE		
		
re.MULTILINE		
		
re.DOTALL		
		
4. Demonstrates how modifiers affect pattern matching with examples		
'''

# import re

# password = "9398649086@SAi"

# pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

# print("Strong Password" if re.search(pattern, password, re.IGNORECASE | re.MULTILINE | re.DOTALL) else "Weak Password")
