# Strings Methods

'''
String Methods in Python :

In Python, string methods are built-in functions used to perform different operations on strings,
such as changing uppercase to lowercase, removing spaces, replacing characters, searching for text, 
and splitting strings.

A string is a sequence of characters enclosed within
single quotes (' '), double quotes (" "), or triple quotes (''' ''').

Ex.

name = "anil gavand"

1. Case Conversion Methods
These methods are used to change the case of characters in a string.
Method	Description	Example
upper()	Converts all characters to uppercase	"anil".upper()
lower()	Converts all characters to lowercase	"ANIL".lower()
capitalize()	Capitalizes the first character	"anil gavand".capitalize()
title()	Capitalizes the first letter of each word	"anil gavand".title()
swapcase()	Converts uppercase to lowercase and vice versa	"AnIl".swapcase()


1. Case Conversion Methods:

These methods are used to change the case of characters in a string.

Method	Description	Example

1.1 upper() :	Converts all characters to uppercase	
1.2 lower()	:   Converts all characters to lowercase	
1.3 capitalize() :	Capitalizes the first character	
1.4 title()	: Capitalizes the first letter of each word	
1.5 swapcase() :	Converts uppercase to lowercase and vice versa	


2. Removing Spaces Methods

These methods remove unwanted spaces from strings.

Method	Description

2.1 strip()	 :  Removes spaces from both sides
2.2 lstrip() :	Removes spaces from the left side
2.3 rstrip() :	Removes spaces from the right side

3. Searching Methods

These methods help find characters or words inside a string.

Method	Description

3.1 find()	: Returns the index of the first occurrence; returns -1 if not found
3.2 rfind()	: Returns the index of the last occurrence; returns -1 if not found
3.3 index()	: Returns the index; raises an error if not found
3.4 rindex() :	Returns the last index; raises an error if not found
3.5 count() :	Counts occurrences of a substring
3.6 startswith() :	Checks whether a string starts with specified text
3.7 endswith()	: Checks whether a string ends with specified text

4. Replacing Methods

Method	Description

4.1 replace() :	Replaces a specified substring with another substring

5. Splitting and Joining Methods

Method	Description

5.1 split()     : Splits a string into a list
5.2 rsplit()    : Splits from the right side
5.3 splitlines():	Splits a string at line breaks
5.4 join() :	Joins elements of an iterable into a string


6. Checking Methods (Boolean Methods)

These methods return either True or False.

Method	Description

6.1 isalnum()	Checks whether all characters are letters or numbers
6.2 isalpha()	Checks whether all characters are alphabets
6.3 isdigit()	Checks whether all characters are digits
6.4 isdecimal()	Checks whether all characters are decimal characters
6.5 isnumeric()	Checks whether all characters are numeric
6.6 islower()	Checks whether all cased characters are lowercase
6.7 isupper()	Checks whether all cased characters are uppercase
6.8 istitle()	Checks whether the string follows title case
6.9 isspace()	Checks whether all characters are whitespace
6.10 isascii()	Checks whether all characters are ASCII

7. String Formatting Methods

Method	Description

7.1 format()	:   Inserts values into placeholders
7.2 format_map():	Formats a string using a mapping such as a dictionary

8. Other Important String Methods

Method	Description

8.1 center() :	Aligns text in the center
8.2 ljust()	 :  Aligns text to the left
8.3 rjust()	 :  Aligns text to the right
8.4 zfill()	 :  Adds zeros to the beginning
8.5 expandtabs() :	Replaces tab characters with spaces
8.6 encode()	 :  Encodes a string into bytes
8.7 maketrans()	 :  Creates a translation mapping
8.8 translate()	 :  Translates characters using a mapping

'''


















# #Example 1. Removing Spacea from Leading and trailing

# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Remove Spaces output : ",Text.strip())

#Eaxmple 2. Upper Letters

# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Remove Spaces output : ",Text.strip())
# print("Upper Letter output:",Text.upper())

#Here we used strip function otherwise it leading and trailing space is remain same as pe the
# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.upper().strip())

# #or
# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.upper()
#                                 .strip())

# strip = All Space from left and right removing.
# rsrtip = Space from right side removing.
# lstrip = Space from left side removing.

#Eaxmple 3. Proper Letters

# Text="     hello python learners   "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.title()
#                                 .strip())

#Eaxmple 4. Lowers Letters

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.lower()
#                                 .strip())

# #Eaxmple 5. replace Word

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Replace Python Word by SQL:",Text.replace("Python","SQL")
#                                 .strip())

# #Eaxmple 6.Count occurance of word

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Replace Python Word by SQL:",Text.replace("Python","SQL")
#                                 .strip())
# print("Count of O is:",Text.count("o"))

# #Eaxmple 7.Start with some Word

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Replace Python Word by SQL:",Text.replace("Python","SQL")
#                                 .strip())
# print("Count of O is:",Text.count("o"))
# print("Start with Word ?:",Text.strip().startswith("Hello")) #Here we used strip function to remove space before the word.

# # #Eaxmple 8.Data is Numeric

# mobile="9823565726"
# print("Data is numeric ?:",mobile.isnumeric())
# mobile1=" Masters in data science"
# print("Data is numeric ?:",mobile1.isnumeric())

# #Eaxmple 9.Split function used

# Word="Welcome to goa Sinhgam"
# print("Word is as per following:",Word.split())
# Joined_Text="".join(Word)
# print("Joined Texts:",Joined_Text)

# # #Eaxmple 10.Joined back with hyphen
# Word="Welcome to goa Sinhgam"
# Joined_Text="".join(Word)
# print("Joined Texts:",Joined_Text)

# ## Example .11 finding position of g
# Word="Welcome to goa Sinhgam"
# print("Find the position of g :",Word.find("g"))

## Example .12 Extract diomain

email="student@example.com"
domain = email[email.find("@")+1:]
print=("The domain Name is:",domain)


















