# Check the rating for the movies:

rating = input('What is the rating for this film?: ')
rating = rating.lower()
if rating == '18':
    print('No one younger than 18 may see this film.')
elif rating == '15':
    print('No one younger than 15 may see this film.')
elif rating == '12a':
    print('No one younger than 12 may see this film without a parent.')
elif rating == '12':
    print('No one younger than 12 may see this film.')
elif rating == 'pg':
    print('This film has a parental guidance recommendation.')
elif rating == 'universal':
    print('Anyone can watch this film!')
else:
    print('I cannot tell what the rating of this function is...')
