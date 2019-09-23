# I want you to use operators to:

# Equate something
# As a user, I would like to be able to guess a number and know if I got the right number, so that I can know if I won or not.

# We should define/assign number to a variable called magic_number
magic_number = int(42)
# Ask user for his guess input
user_guess = input('What would you like to guess for your magic number? You could win £1 million! ')
user_guess = int(user_guess)
# I need to check if this number matches a magic number
result = (magic_number == user_guess)
# Need to let the user know if the response was right or not
print('Hello again, your guess at the magic number was {}.'.format(result))
