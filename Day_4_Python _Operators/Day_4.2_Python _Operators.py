

# # # Python _Operators

# #1.Arithmatic Operator

# Example 1.1 

# Here we defined two variables to do some operations

# a= 12
# b = 24

# print("Addition of Numbers:",a+b)            # Addition
# print("Substraction of Numbers:",a-b)        # Substraction
# print("Multiplication of Numbers:",a*b)      # multiplication
# print("Division of two Numbers: ",a/b)       # Division
# print("Power of two Numbers:",a**b)          # power/Exponant


#2. Comparision Operator

# N1=35
# N2=42
# N3=15
# print("The less than value is :",N1<N2)
# print("Greater than value is : ",N3>N2)
# print("The Value comparision is :",N1==N2==N3)  # Find out equal 

# print(N1!=N2) # Not equal to sign 


# 3. Assignment Operator

# value=50
# print("The Value is :",value)

# # value=value-10 this is the actual calculation write in the following line with shortcut way

# value-=10   #subtraction and assign
# print(value)

# 4. Logical operator (and,or,not)

# x1=12
# x2=23
# x3=15
# x4=26
# print("And result is :",x1<x3 and x2>x4) #AND Condition for condition should be true 
# print("And result is :",x1<x3 and x2<x4) #AND Condition
# print("or result is :",x1<x2 or x3<x4)  #OR Condition

# Not : Reverses the result

# Example 1

# x = True
# print(not x)  # It reverse the result


# age = 16

# if not age >= 18:
#     print("You are not eligible to vote.")


# #5. Identity operator : is,is not

# m1=100
# m2=100
# print(m1 is m2)

# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)      # True
# print(a is b) # False :The is operator checks whether both variables refer to the same object in memory here is different.
# print(a is not b)  # True



#6. Membership Operators : in

print("Chech e s in te Mango :",'e'in 'mango')
print("Chech a s in te Mango :",'a'in 'mango')
