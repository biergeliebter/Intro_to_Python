# Ctrl+K+C to comment a line, Ctrl+K+U to uncomment a line

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello " + first_name.capitalize() + " " + last_name.capitalize())
print()
# output = "Hello, {} {}".format(first_name, last_name)
# output = "Hello, {1} {0}".format(first_name, last_name)
output = f"Hello, {first_name} {last_name}"
print(output)