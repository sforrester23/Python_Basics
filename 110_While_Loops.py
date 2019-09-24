# While loops

# Keeps looping and iterating the whole time a condition is being met, and will only stop when that condition is met, or it comes to a BREAK statement.

# Syntax
# while <condition>:
    # Block

# while <condition>:
    # Block
    # if <condition>:
        # BREAK

# import time
# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1
#     time.sleep(3)

# while True:
#     print('WAAAHHHH')
#     if counter > 10:
#         break
#     counter += 1


# while True:
#     print('What up Jigglypuff? ')
#     user_input= input().lower()
#     if user_input = 'exit':
#         break
#     elif user_input == 'cute':
#         print('AAAHH Jigglypuff... <3')
#     else:
#         print('JIGGLYYYYPUUUUUUFFFFFF!!!!')

# user_input_2 = 'empty'
# while user_input_2 != 'exit':
#     print('What up Jigglypuff? ')
#     user_input_2 = input().lower()
#     if user_input_2 == 'cute':
#         print('AAAHH Jigglypuff... <3')
#     elif user_input_2 == 'oioi':
#         print('JIGGLYYYYPUUUUUUFFFFFF!!!!')

cars = ['Car', 'Volvo', 'Ferrari', 'Skoda', 'Lambo']
#
# counter = 0
# while True:
#     print(cars[counter])
#     if counter == len(cars)-1:
#         break
#     else:
#         counter += 1

counter = 0
max_length = len(cars)
while counter < max_length:
    print(counter + 1, '--', cars[counter])
    counter += 1