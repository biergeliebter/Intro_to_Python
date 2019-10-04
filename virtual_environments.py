# Creating a virtual environment
# By default, python installs packages globally. Version managment can become a challenge
# so virtual environments can be used to contain and manage package collections.
# A virtual environment is really just a folder behind the scenes with all the code needed to run the application.

# Creating a virtual enviornment...
# Install the virtual environment.
# Command: pip install virtualenv
# This installs this globally. :)
# Then create the environment
#Windows:
# Command: python -m venv <folder_name>
# Mac/Linux (bash)
# Command: virtualenv <folder_name>
# Then activate the environment
# Windows - from cmd.exe:
# Command: <folder_name>\Scripts\Activate.bat
# Powershell
# Command: <folder_name>\Scripts\Activate.ps1
# bash shell
# Command: . ./<folder_name>/Scripts/activate
# Mac/Linux (bash)
# Command: <folder_name>/bin/activate

# Then to install packages into a virtual environment, the commands are the same as you would do it globally.
