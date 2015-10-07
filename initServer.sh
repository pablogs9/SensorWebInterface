#######################################################################
### System installation script                                      ###
### Create or update a virtualenv and install all the dependecies   ###
#######################################################################

# Remove old virtualenv, if exists
rm -rf venv
# Create a new virtualenv named venv copying all executables from the system
#virtualenv --always-copy venv
# Create a new virtualenv named venv symlinking all executables from the system
virtualenv venv
# Activating the virtualenv in the terminal
source venv/bin/activate
# Install all the dependecies stored in the requeriments.txt file
pip install -r requeriments.txt
# Exits the virtualenv
deactivate
