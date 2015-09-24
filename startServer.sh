#######################################################################
### System starting script                                          ###
### Activate the virtualenv and run the two processes               ###
#######################################################################

# Activate the virtual env
source venv/bin/activate

# Remove old database and create a new one with a given schema
rm database/database.db
sqlite3 database/database.db < database/schema.sql

# Prepare the terminal to kill all jobs when system signal are receivec
# To stop all you have to press ctrl + C twice
trap 'kill $(jobs -p)' SIGINT SIGTERM

# Start a background serial service and the web service
python serialService.py &
python webService.py
