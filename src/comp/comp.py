# The following list comprehension exercises will make use of the 
# defined Human class. 

# using math import for comp square root
import math

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [person.name for person in humans if person.name.startswith('D') ]
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [person.name for person in humans if person.name.endswith('e')]
print(b)

# Write a list comprehension that creates a list of names of everyone  
# whose name starts with any letter between 'C' and 'G' inclusive.
#['Charlie', 'Daphne', 'Eve', 'Frank', 'Glenn', 'David'])
print("Starts between C and G, inclusive:")
c = [person.name for person in humans if person.name.startswith(('C', 'D', 'E', 'F', 'G'))]
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
# [39, 42, 47, 40, 36, 28, 52, 22, 51, 41]
print("Ages plus 10:")
d = [person.age + 10 for person in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
# ['Alice-29', 'Bob-32', 'Charlie-37', 'Daphne-30', 'Eve-26', 'Frank-18', 'Glenn-42', 'Harrison-12', 'Igon-41', 'David-31']
print("Name hyphen age:")
e = [f'{person.name}-{person.age}' for person in humans]
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
# [('Alice', 29), ('Bob', 32), ('Daphne', 30), ('David', 31)]
f = [tuple([person.name, person.age]) for person in humans if person.age in range(27, 33)]
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
# [Human("ALICE", 34), Human("BOB", 37), Human("CHARLIE", 42), Human("DAPHNE", 35), Human("EVE", 31), Human("FRANK", 23), Human("GLENN", 47), Human("HARRISON", 17), Human("IGON", 46), Human("DAVID", 36)]
print("All names uppercase:")
g = [Human(person.name.upper(), person.age + 5) for person in humans]
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(person.age) for person in humans]   
#print(f'{h:2.3f}')   # TEST does not like this !!!
print(h)

print(f'This should work with python 3 env setup ')