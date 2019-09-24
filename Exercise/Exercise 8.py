# POPTOC

# Multiples of 3 are POP
# Multiples of 5 are TOC
# Multiples of 3 AND 5 are POPTOC

## Show count up to the number inputted
play_on = input('Press ENTER to play the game, type exit to leave: ').lower()
while play_on != 'exit':
    count = 0
    number = int(input('Please insert a number: '))
    while count < number:
        count += 1
        if count%3 == 0:
            if count%5 == 0:
                print(count)
                print('That number is POPTOC!')
            else:
                print(count)
                print('That number is POP!')
        elif count%5 == 0:
            print(count)
            print('That number is TOC!')
        else:
            print(count)
            print('This number is neither POP nor TOC...')
    play_on = input('Press ENTER to play the game again, type exit to leave: ').lower()



