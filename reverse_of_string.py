# Program to explain reverse string or sentence 
# Using for loop
# Reverse String without using reverse function

# Define a function
def reverse_for(string):
    # Declare a string variable 
    rstring = ''

    # Iterate string with for loop
    for x in string:
        # Appending chars in reverse order
        rstring = x + rstring
    return rstring

string = 'Stechies'

# Print Original and Reverse string
print('Original String: ', string)
print('Reverse String: ', reverse_for(string))
