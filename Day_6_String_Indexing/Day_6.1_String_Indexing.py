
# 6.1 string Indexing

'''
Definition: A string is a sequence of characters enclosed within single quotes (' ') or double quotes (" ").

In Python, a String is a sequence of characters enclosed within quotation marks. It is used to store text-based data.

A string can contain:
- Alphabets (A–Z, a–z)
- Numbers (0–9)
- Special characters (@, #, $, %)
- Spaces
- Symbols

String indexing example

Python Strings: Indexing and Slicing
In Python, Indexing and Slicing are used to access individual characters or a group of characters from a string.

Let's understand both concepts step by step.

1. String Indexing

Definition: Indexing is the process of accessing an individual character from a string using its position number.

Python supports two types of indexing:

1.1 Positive Indexing
1.2 Negative Indexing


1.1 Positive Indexing

Positive indexing starts from 0 (left to right).

Forward Indexing         0  1  2  3  4  5
                         P  Y  T  H  O  N
Backword indexing       -6 -5 -4 -3 -2 -1


1.2 Negative Indexing

Negative indexing starts from -1 (right to left).

2. String Slicing

Definition: Slicing is the process of extracting a specific portion or range of characters from a string.

string[start : stop : step]

start	: Starting index (included)
stop	: Ending index (excluded)
step	: Number of positions to skip

2.1 Basic Slicing
2.2 Slicing Without Start Index
2.3 Slicing Without Stop Index
2.4 Slicing With Negative Indexing
2.5 Slicing With Step
2.6 Reverse a String

'''
# Example :Consider a material code used in SAP MM.

material_code = "MAT-100125"

# Access individual characters
print(material_code[0])

# Extract material category
print(material_code[0:3])

# Extract material number
print(material_code[4:])

# Reverse material code
print(material_code[::-1])





# Name="Anil"
# print(Name[0])

# #6.2 string Indexing

Name="Hello Python"
print(Name)
print(Name[0])
print(Name[1])
print(Name[2])
print(Name[3])

# #6.3 string Indexing

# Name="Anil"
# print(Name[-4:])
# print(Name[-1])
# print(Name[-2])
# print(Name[-3])
# print(Name[-4])

#6.3 string Indexing
# Name="Samsung Ultra Pro 2026"
# print(Name[-4:])
# print(Name[:7])
# print(Name[0:7])
# print(Name[-1])
# print(Name[-2])
# print(Name[-3])
# print(Name[-4])
