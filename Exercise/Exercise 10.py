# Story book!
# Create a dictionary with 3 stories inside! Like a book :)
# each story should be it's own dictionary with:
# beginning, middle, end, hero

# Iterate over the book, and print out each story! Print All of :)
# formatted of course

#hints:
    # you already built a dictionary with a story
    # You already have something to prompt user for input and build dictionaries
    # now what we want to do is create a book that holds 3 stories

# extra:
    # Create a while loop so we don't stop listening to stories unless we tell it to break!

# Define an empty dictionary to store the book
book = {
    'story_1' : {},
    'story_2' : {},
    'story_3' : {}
}

# Tell the user what's going to happen
print('We\'re going to make a book! It\'s going to be made of three separate stories. Let\'s get started...')

# define and empty dictionary called story to store the stories
story = {
    'hero' : '',
    'villain': '',
    'beginning' : '',
    'middle' : '',
    'end' : '',
    'moral' : ''
}

# Define a variable to count the number story we are on
story_number = 1 # start at story number 1
# For loop to iterate the input of the important parts of the story
for key1 in book:
    print('Let\'s make story number {} for the book!'.format(story_number))
    for key2 in story:
            story[key2] = input('What is the {} of the story? '.format(key2)).capitalize()
            book[key1][key2] = story[key2]
    story_number += 1 # increase the story number we are on by one

# Let the user know that we've created all the stories
print('Finally, that\'s all the stories made.')
# Ask the user if they would like to keep going - they will do so unless they
keep_going = input('Would you like to read some back? Type anything to continue. Type exit to leave. ').upper()

# While loop to run the whole time before we have told the programme to stop (by typing exit when prompted)
while keep_going != 'EXIT':
    # Ask them which story they'd like to read again: 1, 2 or 3
    story_to_read = int(input('Which story would you like to read back? Please enter either 1, 2 or 3: '))
    if story_to_read == 1: # Read story number 1 with correct formatting
        print('This is story number 1')
        print('{}. {}. {}.'.format(book['story_1']['beginning'], book['story_1']['middle'], book['story_1']['end']))
        print('The hero of the story was {}, while the Villain was {}.'.format(book['story_1']['hero'], book['story_1']['villain']))
        print('The moral of the story is: {}. And don\'t you forget it...'.format(book['story_1']['moral']))
    elif story_to_read == 2: # Read story number 2 with correct formatting
        print('This is story number 2')
        print('{}. {}. {}.'.format(book['story_2']['beginning'], book['story_2']['middle'], book['story_2']['end']))
        print('The hero of the story was {}, while the Villain was {}.'.format(book['story_2']['hero'], book['story_2']['villain']))
        print('The moral of the story is: {}. And don\'t you forget it...'.format(book['story_2']['moral']))
    elif story_to_read == 3: # Read story number 3 with correct formatting
        print('This is story number 3')
        print('{}. {}. {}.'.format(book['story_3']['beginning'], book['story_3']['middle'], book['story_3']['end']))
        print('The hero of the story was {}, while the Villain was {}.'.format(book['story_3']['hero'], book['story_3']['villain']))
        print('The moral of the story is: {}. And don\'t you forget it...'.format(book['story_3']['moral']))
    else: # if they haven't put 1, 2 or 3, tell the user you don't recognise the number and prompt them again if they'd like to continue.
        print('Sorry, I could not decipher which story you\'d like to read')
    # Ask the user if they'd like to continue again after reading a story, which will repeat until they exit here.
    keep_going = input('Would you like to read some back? Type anything to continue. Type exit to leave. ').upper()
