# Accept paraeters in a function
def get_initial(name): 
    # name is the parameter
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
    # Here we have a second parameter that may not always be true. In the code would be get_initial(first_name, False) to use the else
# To set a default value for a parameter -
def get_initial(name, force_uppercase = True):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial
# THen when calling the function, if the second value is not included it will use the default.
# If using positional notation, they values have to be in the same order as the parameters.
# If using named notation it doesn't matter. In the above example, calling the function with named notation would look like...
first_name = input('Enter your first name: ')
first_name_initial = get_initial(force_uppercase=True, name=first_name)
# named notation makes the code more readable, especially if there are errors

