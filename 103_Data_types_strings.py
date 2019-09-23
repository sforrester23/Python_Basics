# Strings
# Strings are a list of characters that are put together
# Defined by '' or ""
#

# my_string='Amazing spicy tacos'
# print(my_string) #print it
# print(type(my_string))  #what type is it?

# Join strings/
first_name = 'Boris'
last_name = 'Becker'
print(first_name[0]) #prints the first letter of the string 'first_name'
# String IS a LIST of characters, so it behaves like a list.

# Concatenating 3 strings
full_name = first_name + ' ' + last_name
print(full_name)
print('String', 14)

# Interpolation
name= 'Rachel'
welcome_message = "hey there, how you doin'? XD XD XP LOL RAWR"
print(f"hey there, {name}, how you doin'? XD XD XP LOL RAWR")
# in front of the string, add an f
# then you can use {} to interpolate python variables inside


# Useful methods for strings
my_string = '  Hello this is an amazing string!   '
print(my_string.count('i')) #counts number of letter i's (4)
print(my_string.count(' ')) #counts number of spaces (10)
# This is a method, a function acts on a method.

# Length: find the length function
print(len(my_string)) # prints the length of the string (37)
# This is not a method, it is a function. You cannot use the .method syntax for it.

# Strip
# Removes the blank spaces at the beginning and the end
print(my_string.strip())

# Upper/Lower
# Changes the string to upper/lower case
print(my_string.lower())
print(my_string.upper())

# Capitalize
# Puts a capital letter at the start of each sentence
print(my_string.strip().capitalize())

# Replace
# .replace(arg_int, arg_two)
print(my_string.replace('an', 'THE'))

# Split
# .split(arg) --> LIST
print(my_string.split(' '))
print(type(my_string.split(' '))) #it is a list type

