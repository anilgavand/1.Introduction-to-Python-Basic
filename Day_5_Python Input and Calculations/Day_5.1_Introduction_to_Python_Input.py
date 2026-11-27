
# Introduction to Python Input

# Input Function: In Python, the input() function is used to take input from the user during program execution.
# Ex. input()

'''
1. input() reads data entered by the user.
2. Returns data as a string.
3. Use int(), float(), etc., when numeric input is required.
4. Commonly used in interactive Python programs.

'''
# Example :1 Input as string

# name = input("Enter your name: ")
# print("Hello,", name)


# Example :2 Input as integer (Problem)

# Birth_Year=input("Enter your birth Year") # input is by default string we have to convert in string.
# print(type(Birth_Year))   # ans:<class 'str'>
# age=2026-Birth_Year    # String and integer cannot minus due to data type
# print ("Your age is :",age)

# Example :3 Input as integer (Solution)

Birth_Year=int(input("Enter your birth Year :"))  # Type casting :convert one data type to other Ex. string to integer
age=2026-Birth_Year
print ("Your age is :",age)

