# Variables in Python
# A Variable is a box. You can give it a name and put stuff inside.

# Assigning a variable
# Giving box a name and putting stuff inside
box_variable = "Books and stuff"

# Printing the variable
# Looking inside the box
print(box_variable)

# Re-assigning a variable
# Variable are mutable - hence they can change/be reassigned
box_variable = "CDs and my old banjo"
print(box_variable)

# Re-re-assigning with an integer
# Variable can hold any data type inside
box_variable = 141516516161
print(box_variable)

# Important python commands/functions
# print(arguments)
print('Hello') #Printing a string
print(box_variable) #printing a variable
print('Hello', box_variable)  #Overloading with two arguments

# type(argument) displays the type of data of the object in the argument
print(type('Hello'))
print(type(14))
print(type(14.0))

variable_num = '14'
print(type(variable_num*10)) #This will be a string, because you are multiplying a string 10 times.

