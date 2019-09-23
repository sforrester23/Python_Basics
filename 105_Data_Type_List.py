# Lists
# A list keeps objects in order of index
# Defined by [ ]

# example of a list
crazy_ex_partners = ['Carolina', 'Json', 'Arthur', 'LANA!']

# Print and show type (Read All)
print(crazy_ex_partners)
print(type(crazy_ex_partners))

# Get a particular record out of the list (Read one)
print(crazy_ex_partners[0]) # the 0th entry is the first one
print(crazy_ex_partners[-1]) # -1 is the final entry (one before the first one)

# Edit an entry in a specific index (Re-assign an index)
crazy_ex_partners[3]='LANAAA!!! (...) DANGERZONE!!!' # Re-assigns the third index point
print(crazy_ex_partners[3])

# Add someone to the list (Create one)
print(crazy_ex_partners)
crazy_ex_partners.append('Cyril Figgis')
print(crazy_ex_partners)

# Insert in index specific location
crazy_ex_partners.insert(3, 'Mallory')
print(crazy_ex_partners)

# Remove someone from the list (Destroy one)
crazy_ex_partners.remove('Json')
print(crazy_ex_partners)

# Remove using index
crazy_ex_partners.pop() #removes last entry in the list
crazy_ex_partners.pop(2) #removes the number two entry in the list (change the number to remove from different indexed positions)

# What happens when we have thousands and thousands of data points?
# IF, FOR and WHILE loops!

# Mixed data & lists
    # Lists can have many data types
hybrid_list=['This is a string', 12, 66, 'hello', [1,2,3]] # list of lists are viable too!




