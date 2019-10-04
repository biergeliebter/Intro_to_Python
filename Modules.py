# Importing a module
# Import module as namespace
import helpers
helpers.display('Not a warning')

# Import all into current namespace
from helpers import *
display('Not a warning')

# Import specific items into current manespace
from helpers import display
display('Not a warning')

# Packages are published collections of modules
# Do an internet search for Python Package Index

# installing packages
# You have to use pip
# Install an individual package - command is: pip install colorama
# Install from a list of packages - command is: pip install -r requirements.txt
# Then in requirements.txt is a list of packages you will be using, ie. colorama