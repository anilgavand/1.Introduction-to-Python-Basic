
# 3. Introduction to Data Types in Python

# Data types tells python what kind of information is stored in a variable.
# Data type define the type of value a variable can hold and determines the how python will process ,store and manipulate the data.

'''
Ex:
Variable Name: Sugar
Variable Value: 10  

Sugar in meter ?
milk in cm ?
To undertand this we used data types.
'''

# Python has following data types:

# 1. Text Type: 

# 1.1 string (str) : Its a sequence of characters enclosed in single or double quotes.Example: "Hello", 'Python', "1234"

#2. Numeric Types: 

# 2.1 Integer (int) : It represents whole numbers without a decimal point. Example: 10, -5, 0
# 2.2 Float (float) : It represents real numbers with a decimal point. Example: 10.5, -3.14, 0.0
# 2.3 Complex (complex) : It represents numbers with a real and an imaginary part. Example: 3+4j

# 3. Sequence Types:  

# 3.1 List (list) : It is an ordered collection of items enclosed in square brackets. Example: [1, 2, 3], ['apple', 'banana', 'cherry']
# 3.2 Tuple (tuple) : It is an ordered collection of items enclosed in parentheses. Example: (1, 2, 3), ('apple', 'banana', 'cherry')
# 3.3 Range (range) : It is a sequence of numbers. Example: range(5), range(1, 11) Example: range(2, 5) 

# 4. Mapping Type:

# 4.1 Dictionary (dict) : It is an unordered collection of key-value pairs enclosed in curly braces. Example: {'name': 'John', 'age': 30}

# 5. Set Types:

# 5.1 Set (set) : It is an unordered collection of unique items enclosed in curly braces. Example: {1, 2, 3}, {'apple', 'banana', 'cherry'}
# 5.2 Frozen Set (frozenset) : It is an immutable version of a set. Example: frozenset({1, 2, 3}), frozenset({'apple', 'banana', 'cherry'})



# 6. Boolean Type

# 6.1 Boolean (bool) : It represents one of two values: True or False. Example: True, False   

# 7.None Type

# 7.1 None (NoneType) : It represents the absence of a value or a null value. Example: None


'''

Functions Used in Data Types:

1. type() : This function is used to check the data type of a variable.
2. isinstance() : This function is used to check whether a variable is of a specific data type or not.
3. id() : This function is used to get the memory address of a variable.
4. len() : This function is used to get the length of a variable.

Conversion Functions:

1. str() : This function is used to convert a variable to a string data type.
2. int() : This function is used to convert a variable to an integer data type.
3. float() : This function is used to convert a variable to a float data type.
4. complex() : This function is used to convert a variable to a complex data type.
5. list() : This function is used to convert a variable to a list data type.
6. tuple() : This function is used to convert a variable to a tuple data type. 
7. set() : This function is used to convert a variable to a set data type.
8. dict() : This function is used to convert a variable to a dictionary data type.
9. frozenset() : This function is used to convert a variable to a frozenset data type.
10. bool() : This function is used to convert a variable to a boolean data type.
11. None() : This function is used to convert a variable to a None data type.
12. eval() : This function is used to evaluate a string as a python expression and return the result.


'''


# Difference between list data type and list function:
# - List data type is a built-in data structure in Python used to store multiple items in a single variable.
# - list() function is used to create a new list object.