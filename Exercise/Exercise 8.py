# POPTOC

# Multiples of 3 are POP
# Multiples of 5 are TOC
# Multiples of 3 AND 5 are POPTOC

## Show count up to the number inputted

while True:
    number = int(input('Please insert a number: '))
    if number%3 == 0:
        if number%5 == 0:
            print('That number is POPTOC!')
        else:
            print('That number is POP!')
    elif number%5 == 0:
        print('That number is TOC!')
    else:
        print('This number is neither POP nor TOC...')
        break
