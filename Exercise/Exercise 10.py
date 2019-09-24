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
book = {
    'story_1' : {},
    'story_2' : {},
    'story_3' : {}
}

print('We\'re going to make a book! It\'s going to be made of three separate stories. Let\'s get started...')

story = {
    'hero' : '',
    'villain': '',
    'beginning' : '',
    'middle' : '',
    'end' : '',
    'moral' : ''
}

for key1 in book:
    print('Let\'s make a {} for the book!'.format(key1))
    for key2 in story:
        story[key2] = input('What is the {} of the story? '.format(key2)).capitalize()
        book[key1][key2] = story[key2]

# print(book)
# print('So, this is the story we\'ve just made:')
# print('{}. {}. {}.'.format(story_1['beginning'], story_1['middle'], story_1['end']))
# print('The hero of the story was {}, while the Villain was {}.'.format(story_1['hero'], story_1['villain']))
# print('The moral of the story is: {}. And don\'t you forget it...'.format(story_1['moral']))
#
# print('Right, now that\'s one story over, let\'s do another!')
#
# story = {
#     'hero' : '',
#     'villain': '',
#     'beginning' : '',
#     'middle' : '',
#     'end' : '',
#     'moral' : ''
# }
#
# for key in story:
#     story[key] = input('What is the {} of the story? '.format(key)).capitalize()
#     story_2 = story
#
# print('So, this is the story we\'ve just made:')
# print('{}. {}. {}.'.format(story_2['beginning'], story_2['middle'], story_2['end']))
# print('The hero of the story was {}, while the Villain was {}.'.format(story_2['hero'], story_2['villain']))
# print('The moral of the story is: {}. And don\'t you forget it...'.format(story_2['moral']))
#
# print('Finally, let\'s do one more story. Last one I promise...')
#
# story = {
#     'hero' : '',
#     'villain': '',
#     'beginning' : '',
#     'middle' : '',
#     'end' : '',
#     'moral' : ''
# }
#
# for key in story:
#     story[key] = input('What is the {} of the story? '.format(key)).capitalize()
#     story_3 = story
#
# print('So, this is the story we\'ve just made:')
# print('{}. {}. {}.'.format(story_3['beginning'], story_3['middle'], story_3['end']))
# print('The hero of the story was {}, while the Villain was {}.'.format(story_3['hero'], story_3['villain']))
# print('The moral of the story is: {}. And don\'t you forget it...'.format(story_3['moral']))
#
print('Finally, that\'s all the stories made.')
keep_going = input('Would you like to read some back? (Y/N) ').upper()

while keep_going != 'N':
    story_to_read = int(input('Which story would you like to read back? Please enter either 1, 2 or 3: '))
    if story_to_read == 1:
        print('This is story number 1')
        print('{}. {}. {}.'.format(book['story_1']['beginning'], book['story_1']['middle'], book['story_1']['end']))
        print('The hero of the story was {}, while the Villain was {}.'.format(book['story_1']['hero'], book['story_1']['villain']))
        print('The moral of the story is: {}. And don\'t you forget it...'.format(book['story_1']['moral']))
    elif story_to_read == 2:
        print('This is story number 1')
        print('{}. {}. {}.'.format(book['story_2']['beginning'], book['story_2']['middle'], book['story_2']['end']))
        print('The hero of the story was {}, while the Villain was {}.'.format(book['story_2']['hero'], book['story_2']['villain']))
        print('The moral of the story is: {}. And don\'t you forget it...'.format(book['story_2']['moral']))
    elif story_to_read == 3:
        print('This is story number 1')
        print('{}. {}. {}.'.format(book['story_3']['beginning'], book['story_3']['middle'], book['story_3']['end']))
        print('The hero of the story was {}, while the Villain was {}.'.format(book['story_3']['hero'], book['story_3']['villain']))
        print('The moral of the story is: {}. And don\'t you forget it...'.format(book['story_3']['moral']))
    else:
        print('Sorry, I could not decipher which story you\'d like to read').upper()
    keep_going = input('Would you like to read some back? (Y/N) ')