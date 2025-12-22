
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']


"""
Sorts a list of Monty Python members' full names by their last name.

This script demonstrates two equivalent methods of sorting names:
1. Using a lambda function to sort by last name (surname)
2. Using a named function (sort_names) to achieve the same result

The sort_names function splits a full name string by spaces and returns the 
list of name components, which Python's sort() uses to sort by the last 
element (surname) when used as a key function.

Variables:
    monty_python (list): List of full names of Monty Python comedy troupe members

Functions:
    sort_names(name): Splits a name string by spaces and returns a list of 
                      name components for sorting purposes

Example Output:
    Names sorted alphabetically by surname (Chapman, Cleese, Gilliam, Idle, Jones, Palin)
"""

def sort_names(name):
    return name.split(' ')
monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)
monty_python.sort(key= sort_names)
print(monty_python)
