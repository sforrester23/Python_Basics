# Functions

# Functions are like machines!
# They take in arguments (optional)
# They have a block of code to run
# They output (return) something (optional)

# They need to be called to be executed

# Syntax:

# Running and calling a function
def full_name():
    print('hey, Zeus')

full_name()

# Good practices include
    # Good naming, following convention
    # Humans understand names and are descriptive
    # Lower case and separated with _ (underscore)
    # They should be atomic (listed as small as possible to still work)
    # This makes them testable
    # Reduces technical debt
    # Comments when appropriate
    # DO NOT PRINT IN FUNCTIONS: use *RETURN*

# Functions allow us to be DRY - don't repeat yourself

# Aim for cleaner, dryer and maintainable/testable code

def return_hey_to_Zeus():
    return('Hey_Zeus')

def return_full_name(first_name, last_name):
    return first_name + ' ' + last_name

# OR

def return_full_name(first_name, last_name):
    full = first_name + ' ' + last_name
    return full

# This is the basis for all tests
# Set up (give controlled inputs)
# Assertion (check for expected outcomes)
# Feed back output to our users 
print(return_full_name('Sam', 'Forrester') == 'Sam Forrester')






