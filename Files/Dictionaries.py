# Creating a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Retrieving a value from a dictionary
print(programming_dictionary["Function"])

# Adding more items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

# Creating an empty dictionary
# Important to reset something.
empty_dictionary = {} 

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

# Loop through a dictionary
# Loop For only show us the key primarly, then we need to print the dictionary with the key:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
