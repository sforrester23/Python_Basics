# For Loops

# Syntax

# for <placeholder> in <iterable>:
    # block of code (*indented*) gets run every iteration
    # Don't forget the colon!

# cars = ['Skoda Felicia FUN', 'Fiat Panda 4x4', 'Ford Mustang', 'Corvette']
#
# for car in cars:
#     print('I want a', car)
#
# embedded_list = [['Filipe', 'Francis'], ['Moustafa', 'David', 'Jillian']]
#
# for list in embedded_list:
#     print(list)
#     for name in list:
#         print(name)

student_1 = {
    'Name' : 'Arya Stark',
    'Stream' : 'Many Faces',
    'Grade' : '10',
    'Complete Modules' : ['sword', 'augmented senses', 'no face', 'no name']
}
# number=1
# for key in student_1:
#     print(number, '-', key,': ', student_1[key])
#     number = number + 1

students_1 = {
    'Student1' : student_1,
    'Student2' : {
        'name': 'Stirling Archer',
        'stream' : 'Chaos',
        'grade' : '10',
        'complete modules' : ['danger', 'robust liver', 'mummy issues', 'espionage']
    }
}
#
# print(students_1['Student2']['name'])
# for student_key in students_1:
#     count = 1
#     print("/////////////////////")
#     for key in students_1[student_key]:
#         print(count, key, ':', students_1[student_key][key])
#         count += 1


for key1 in students_1:
    count = 1
    print('\/\/\/\/\/\/\/\/\/\/\/')
    for key2 in students_1[key1]:
        print(count, key1, ':', students_1[key1][key2])
        count += 1


