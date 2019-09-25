# Engineering 42 Python Basics

This repo contains basics for python.
The course will cover the following:

1) SET UP
2) Data types
    1) Strings
    2) Integers
    3) Float
    4) Boolean
    5) Dates and Times
    6) Lists
    7) Dictionaries
3) Control Flow
    1) IF
    2) FOR loops
    3) WHILE loops
4) Functions (Some TDD as well)
    1) DRY
    2) TDD
5) OOP
    1) OOP
    2) Four Pillars
    3) External Packages
6) Files and error handling
7) SQL
8) JSON
9) HTTP & APIs
10) Build API with FLASK

## Git, GitHub and documentation. 

### String
- Define using ' ' & " "
- They are a list of characters

### Int, Floats
- Numbers and decimals
- You can perform arithmetic and comparison operations on them.
 
### List
- Defined with [ ]

        list = [item1, item2, item3, ..., itemN]
- Add at the end of the list using .append

        list.append(<thing to add>)
- Add in a certain index position using .insert(position_index, string_to_add)

        list.insert(<position>, <thing to insert>)

### Dictionary
- Defined using 

        my_dictionary = { 'key1' : value1,
                       'key2' : value2,
                       ...
                       'keyN' : valueN
         }
- You can add using 

        my_dictionary {'key' : item(string/integer etc)}
        
- You can access it using its key 
        
        my_dictionary['key'] --> <item for that key> 

## IF, FOR and WHILE loops - control flow

### IF statements

- Controls what the code is going to do depending on the result of the evaluations that return True or False.

- It returns something or runs a block of code depending on these boolean results.

- Syntax:
        
        if <condition1>:
            <if condition1 is true, execute this code>
        elif <condition2>:
            <if condition1 is not true but condition2 is, execute this code>
        elif <condition3>:
            <you can do any number of elif statements to provive alternative conditions to execute different codes>
            ...
        else:
            <else provides the final alternative statement, that executes if none of the if/elif conditions are true>
            <It needs no condition, because it is a last resort>
            
### FOR loops

- Iterates over a set of values in an input to perform blocks of code multiple times for each different iteration.

- Great for repeating processes over multiple organised data points.

- Syntax:

        for <placeholder> in <iterable>:
            <block of code that gets run each iteration, i.e. for each placeholder value in the iterable given>
            
- Good for performing various actions on lists and dictionary forms of data.

### While loops

- Keeps looping and iterating the whole time a condition is being met, and will only stop when that condition is met, or it comes to a BREAK statement.

- Syntax:
        
        1.    
            while <condition>:
                <block to execute>
    OR:

        2.
            while <condition>:
                <block to execute>
                if <condition>:
                    break

