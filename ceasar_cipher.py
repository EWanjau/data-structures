#!/usr/bin/python3

def greet(name, location):
    print('Hello {}:'.format(name))
    print('There is my name')
    print('Do I hear you Over in {}'.format(location))


# positional arguments, assign the data to variable automatically how they are ordered
greet("Rungiri", "Wamuti")
# Keyword arguments, specify what data goes to what variable
greet(name="Erasto", location="Rungiri")
