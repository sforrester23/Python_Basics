# Assignment for post class

# EXERCISE 1 homework
# Use variables, print and different data types.
# Ask and store the following information in variables:
    # first_name, last_name, age, age of mother as variables and three skills in a list
first_name = input('Hello you! What is your first name again?: ') # Ask for their first name
first_name = first_name.capitalize() # Format so name starts with capital letter
last_name = input('Ah of course it\'s you! What\'s your last name?: ') # Ask for their last name
last_name = last_name.capitalize() # Format so name starts with capital letter
age = input('Lovely to meet you. How old are you these days?: ') # Ask for their age, leave it stored as a string
mothers_age = input('What a smashing age. Now, bit of a werid one, but how old is your mum these days?: ') # Ask for their mother's age, leave it stored as a string
skills=[] # Set up the skills list
skill_1 = input('Can you tell me a good skill of yours?: ') # Ask them a skill
skill_1 = skill_1.lower() # Make the skill lower case so it can be used in a sentence
skills.append(skill_1) # Add the skill to the skills list
skill_2 = input('And another skill you possess?: ') # Ask them another skill
skill_2 = skill_2.lower() # Make the skill lower case so it can be used in a sentence
skills.append(skill_2) # Add the skill to the skills list
skill_3 = input('Just one final skill you can boast please?: ') # Ask them a final skill
skill_3 = skill_3.lower() # Make the skill lower case so it can be used in a sentence
skills.append(skill_3) # Add the skill to the skills list

    # Print out the information in a formatted manner
print('OK, so {} {}, you are {} years old and your mother is {} years of age. You have a great set of skills including: {}, {} and {}.'.format(first_name, last_name, age, mothers_age, skills[0], skills[1], skills[2]))

    # Calculate age difference between repsonse and mother
age = int(age)
mothers_age = int(mothers_age)
difference_in_ages = abs(mothers_age - age)
print('Also, the difference in ages between you and your mother is {}'.format(difference_in_ages))
    # Store Skills in a list
    # print each skill in a formatted way i.e. 'your age is 3'
    # a little context text, appropriate string formatting including lower and upper case or other.

