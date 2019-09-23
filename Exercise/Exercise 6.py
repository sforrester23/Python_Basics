# Assignment for post class

# Exercise 2 homework

# Define an empty dictionary: name_dict = {}
story_dictionary={}

# prompt user for a story
# It should have:
    # Hero, beginning, middle, end
    # 2 other things you define to be part of the story
    # Add each response to the dictionary under an appropriate key
print('Hello there fine user! Let\'s make a story!')
story_beginning = input('How should our wonderful story begin?: ')
story_beginning = story_beginning.capitalize()
story_middle = input('What should be in the middle of our story?: ')
story_end = input('And finally, how should our wonderful story end?: ')
hero = input('So, who is the hero of our story?: ')
hero = hero.capitalize()
extra_1 = input('Is there anything extra you\'d like to add about the story?: ')
extra_2 = input('One last chance, add something else important to know about the story!: ')

story_dictionary['Beginning'] = story_beginning
story_dictionary['Middle'] = story_middle
story_dictionary['Ending'] = story_end
story_dictionary['Hero'] = hero
story_dictionary['Extra information 1'] = extra_1
story_dictionary['Extra information 2'] = extra_2

# Print out the dictionary information in an ordered way so we can read the story.
print('So, this is how the story goes!: {}, {}, {}.'.format(story_dictionary['Beginning'],story_dictionary['Middle'], story_dictionary['Ending']))
print('The hero of our story is {}! You\'d also like us to know that {} and {}.'.format(story_dictionary['Hero'], story_dictionary['Extra information 1'], story_dictionary['Extra information 2']))