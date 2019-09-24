# Control Flow: If Statements
# Controls what the code is going to do depending on the result of the evaluations that return True or False.
# It returns something or runs a block of code depending on these boolean results.



# Syntax
# if <condition>:
    #  run this block
# elif <other condition>:
    # run that block
# else:
    # run this block instead
#
# weather = input('What\'s the weather doing? ')
#
# if 'rain'in weather:
#     print('Grab your brolly')
# elif weather == 'snowy':
#     print('Get yo boots on fam')
# else:
#     print('GET yo sunny gs bro')


age = int(input('How old are you?: '))
if age >=17:
    drivers_license = input('Do you have a driver\'s license?(Y/N): ').lower()
    if drivers_license == 'y':
        drivers_license = True
    else:
        drivers_license = False
if age >= 18:
    if drivers_license:
        print('You can vote AND drive, you lucky old chap!')
    else:
        print('You can vote but not drive...')
elif 17 <= age < 18:
    if drivers_license:
        print('You can drive but you can\'t vote')
    else:
        print('You can neither vote nor drive, unlucky mate...')
elif 16 <= age < 17:
    print('Your mates might have your back if you\'re caught drinking...')
else:
    print('You\'re way too young, go back to school!')





