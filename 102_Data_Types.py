# # Numerical Data types
# # Ints, long, float, complex
# # These are numerical data types that we can use numerical operators with
#
# # Int - Integers/Whole numbers
# my_int = 10
# print(my_int)
# print(type(my_int))
#
# # Complex and Long we don't use as much
# # Complex brings an imaginary component
# # Long - are integers of unlimited size (not really relevant in python 3 as INT has unlimited length)
#
# # Arithmetic Operators - Add, Subtract, Divide, Multiple
# # Exponents
# print(4+3)
# print(4-3)
# print(4/2) # Changes the data type to float
# print(4//2) # Drops the decimal / keep it as integer (not float)
# print(4*2)
# print(3**2) # Exponentials i.e. 3^2
#
# # Modulo (%) looks for the remainder of one number divided by another
# print(5%3) #=2
# print(22%3) #=1
# print(23%3) #=2
#
# # Comparison Operators
# # --> boolean value
# # == is the comparison operator, it checks if two objects are equal
# # </> is bigger than and smaller than
# # <= / >= is bigger than or equal to / smaller than or equal to
# # != is the not equal to comparison
# # is and is not
#
# my_variable_1 = 10
# my_variable_2 = 13
# print(my_variable_1 == my_variable_2) #False
# print(my_variable_1 > my_variable_2) #False
# print(my_variable_1 < my_variable_2) #True
# print(my_variable_1 >= my_variable_2) #False
# print(my_variable_1 <= my_variable_2) #True
# print(my_variable_1 is my_variable_2) #False
# print(my_variable_1 is 10) #True
# print(my_variable_2 is not 13) #False
#
# # Boolean Values
# # Defined by either true or false
# print(type(True)) #'bool'
# print(type(False)) #'bool'
# print(0 == False) #True
# print(1 == True) #False
#
# ## None
# print(None)
# print(type(None)) #'None Type'
# print(bool(None)) #False
# print(0==None) #False
# print(False == None) #False
# print(False == bool(None)) #True

# Logical AND & OR
a = True
b = False
# Using *AND*: both sides of the *and* key word must be true for it to be true, one being false will make it false
print(b and b) #False
print((1==1) and (True)) #True

# Using *OR*: only one side of the *or* keyword has to be true for the whole statement to be true, one being false will still make it true.
# Having both side of *or* as false will make the whole statement false.
print('this will print true')
print(True or False)
print(True or 1==2)
print('this will print false')
print(False or 1==2)
