# 2.2 Variable defining rules

'''
1. Must start with a letter (a-z, A-Z) or an underscore (_).
2. Can contain letters, digits (0-9), and underscores (_).
3. Cannot start with a digit (0-9).
4. Cannot contain spaces or special characters (e.g., @, #, $, %, etc)
5. Variable names are case-sensitive, meaning that "myVariable" and "myvariable" would be considered different variables.
6. Avoid using Python reserved keywords as variable names (e.g., "if", "else", "while", etc.).
7.No spaces are allowed in variable names. Use underscores (_) to separate words if needed (e.g., "my_variable").
8. Variable names should be descriptive and meaningful to improve code readability (e.g., "employee_name" instead of "x").


'''
# Reserved Keywords in Python:

'''
In Python, Reserved Keywords are predefined words that have special meanings in the Python programming language.
These words have specific purposes and cannot be used as variable names, function names, or identifiers.

Python provides a built-in module called keyword to find all reserved keywords.

'''

#1. Find All Reserved Keywords

import keyword

print(keyword.kwlist)

# Ans: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue',
#  'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']