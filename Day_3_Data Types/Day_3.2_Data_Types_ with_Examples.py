
#Task 1_ String

# We have to assign customer Name as Martin and Print it with Data type

# Customer_Name="Martin"
# print("Customer Name is:",Customer_Name)
# print("Customer Data Type is:",type(Customer_Name))
# print(isinstance(Customer_Name,str))
# print("id(Customer_Name):",id(Customer_Name))
# print(len(Customer_Name))


#Task 2_Numerical Data type 

# 2.1 Integer Complete Number  

# Overall_Rating=4
# Performance_Index=8
# print("The overall rating is",type(Overall_Rating))
# print("The Performance Index is",type(Performance_Index))


# # Task 2.2_ Float decimal number

# Overall_Rating=4.89
# Performance_Index=8.43
# print("The overall rating is",type(Overall_Rating))
# print("The Performance Index is",type(Performance_Index))


# #Task 2.3 Complex number  
  
# a=3+4j  # where j is the imaginary part of the complex number
# b=5+6j
# addition=a+b

# print("Print Data Type",type(a))
# print("Print Data Type",type(b))
# print("The addition of complex number is",addition)

##3 Boolean Data : it represents one of two values: True or False. Example: True, False

# Amount_Paid=True
# Amount_Pending=False

# print("The Current status is",type(Amount_Paid))
# print("Final conclusion",type(Amount_Paid))


# #Task_4.Sequence_List

# 4.1 List

# cities_in_india=["MUBAI","PUNE","DELHI","PATNA"]
# states_code=[1,2,3,4]

# print(cities_in_india)
# print(type(cities_in_india))
# print(states_code)
# print(type(states_code))



# #4.2 Tuple : which is not changeable or immutable 

# Dimentions=(1920,2008,2026)
# print("The Dimentions is",Dimentions)
# print(type(Dimentions))


# # #4.3 Range

# Exampls: 01 

# num1=range(5)       # In this case, the range will start from 0 and end at 4 (5-1)
# num2=range(1,11)    # In this case, the range will start from 1 and end at 10 (11-1)
# num3=range(2,10,2)  # In this case, the range will start from 2 and end at 8 (10-1) with a step of 2
# print(list(num1))
# print(list(num2))   # Here we use list() function to convert the range object to a list .
# print(list(num3))

# print(type(num1))
# print(type(num2))
# print(type(num3))

# #Now we are printing Days 1 to 31

# days=range(1,32)    # Step is 1 by default, so we can omit it. The range will start from 1 and end at 31 (32-1)
# print("The days are",days)
# print(type(days))
# print(list(days))


# 3.5 Mapping Type

#3.5.1 Dict_Dictonary  

# Student={
#     "Name":"Martin",
#     "Age":25,
#     "City":"Berlin",
#     "Country":"Germany",
#     "Education":"Masters",
#     "Domain":"Data Science",}

# print("Student Details as per Following =",Student)
# print(type(Student))

#3.6_Set types

# 3.6.1 Set

# numbers={1,2,2,3,4,4,4,5,6,7,8,9}   
# print("Numbers as per Followings =",numbers)
# print(type(numbers))  #repeated values are not allowed in set data type.

# 3.6.2 Frozen Set

# a = frozenset([1, 2, 3])
# b = frozenset([3, 4, 5])

# print(a | b) # Here repeated values are not allowed in frozenset data type. It will print only unique values.


# #3.7 None type

remark=None  # to take response from user we can use input() function. 
print("The remark is =",remark)
print(type(remark))  #If user does not give any response then it will be None type.

