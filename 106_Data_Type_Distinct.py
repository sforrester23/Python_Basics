# Dictionaries
# All fun and games keeping our crazy ex list... But we also need more information.
# Introducing dictionaries!

# Dictionaries are defined by using {}.
# They are organised by keys that point to values.
# Much like looking up something on a dictionary or information about a contact on our phone.
# Thus in our phone, Filipe Paiva will hold lot's of info for this entry.
# Could be the phone number, work number, email. address and so on...

# Syntax
# dict_name = {
#       'example_key': 'value',
#       'example_key': 'value'
#       }
#
# # Defining a simply dictionary with two keys
# dictionary_crazy_exes = {
#     'Carolina': 'she was actually nice',
#     'Arthur': 'bit of a drinker'
# }
# print(dictionary_crazy_exes)
# print(type(dictionary_crazy_exes))
#
# # Accessing values - use the key!
# print(dictionary_crazy_exes['Carolina'])
# print(dictionary_crazy_exes['Arthur'])
#
# # Adding a new key, pair value
# dictionary_crazy_exes['Kyle'] = 'Likes Monster' # Adding a new key and its value automatically adds it to the dictionary
# print(dictionary_crazy_exes)
#
# # Re-assigning a value
# dictionary_crazy_exes['Kyle'] = 'Absolutely Loves Monster' # Referencing the original key when it already exists will re-assign a value
# print(dictionary_crazy_exes)
#
# # Get out all the keys
# print(dictionary_crazy_exes.keys())
#
# # Get out all of the values
# print(dictionary_crazy_exes.values())
#
# # Remove item from dictionary
# dictionary_crazy_exes.pop('Arthur') #remove entries with Key of 'Arthur'
# print(dictionary_crazy_exes)


# Better example of a dictionary

Crazy1 = {
    'Name': 'Carolina',
    'Phone': '07842715517',
    'Address': 'Location 1, at places',
    'Known places to avoid': ['Milan', 'Lisbon', 'Tavira']
}
