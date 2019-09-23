# Define the following variables
# first_name, last_name, age, eye_colour, hair_colour
first_name='Ronald'
last_name='Macdonaldz'
age=83
eye_colour='Fuschia'
hair_colour='Clown Red'

# Prompt user for input and re-assign these
first_name = input('What is your first name, young fellow? ')
last_name = input('What is your last name, old bean? ')
age = input('Brilliant, {}, and how old are you? '.format(first_name))
eye_colour = input('So, old pal, what colour eyes do you have? ')
hair_colour = input('And what lovely colour eyes you do have, my friend! What colour hair do you have? ')

# Print them back to the user as conversation
print('So, {} {}, you are {} years old! And a fine age it is. You also have {} eyes and {} hair. Fantastic stuff. You must have been shaped by the gods.'.format(first_name, last_name, age, eye_colour, hair_colour))

# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair is black

age=int(age)
year_born=(2019-age)
year_born=str(year_born)
print('As you are {}, you were born in {}! Amazing that I can work that out, hey?'.format(age, year_born))
