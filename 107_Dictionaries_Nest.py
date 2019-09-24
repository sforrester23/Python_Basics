# Nested lists and dictionaries

# nested_list = ['bread', 'sugar', [1, 2, 3, 4, 'spice']]
#
# print(nested_list)
# print(nested_list[0]) #outputs 'bread' as it is the first in the list
# print(nested_list[2][4]) #outputs 'spice' as it is the 5th value in the nested list, that is in the 3rd position in the actual nest.

nested_list_dictionary = ['bread', 'sugar', [1, 2, 3, 4, 'spice', {'name' : 'buttercup'}]]
print(nested_list_dictionary)
print(nested_list_dictionary[2][5]) #outputs the dictionary from the nested lists
print(nested_list_dictionary[2][5]['name']) #outputs the specific key value from the nested dictionary in the nested lists

student_1 = {
    'name' : 'Arya',
    'stream' : 'Many Faces',
    'grade' : '10',
    'complete modules' : ['sword', 'augmented senses', 'no face', 'no name']
} #Stores a list inside a dictionary

students = {
    'Students' : student_1
} #stores a dictionary inside a dictionary

students_1 = {
    'Student1' : student_1,
    'Student2' : {
        'name': 'Stirling Archer',
        'stream' : 'Chaos',
        'grade' : '10',
        'complete modules' : ['danger', 'robust liver', 'mummy issues', 'espionage']
    }
} #dictionary inside a dictionary

print(student_1)
print(students)
print(students_1['Student1']['name']) # --> Arya Stark
print(students_1['Student2']['name']) # --> Stirling Archer