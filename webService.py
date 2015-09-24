#######################################################################
### Web Service                                                     ###
### This script describes the functions that manage the main web    ###
### pages answer and the REST service for the AJAX info recovery    ###
#######################################################################

import dataset
from flask import Flask, render_template, jsonify

# Create an Flask App
app = Flask(__name__)

# Use dataset module to connect with the sqlite database and get the table object
db = dataset.connect('sqlite:///database/database.db')
table = db['data']

# Define the answer for root of the webpage
@app.route("/")
def mainView():
    return render_template('index.html')

# Define a REST interface for recovering the last N entries of the database
# in a JSON format
@app.route("/chartData/<entries>")
def chartData(entries):

    # Init the data vectors
    timestamp = ['timestamp']
    Period = ['Period']
    Frequency = ['Frequency']
    Pulses = ['Pulses']

    # Query the database with a SQL sentence: get last N entries from data table
    # and order them by the timestap
    result = db.query('''SELECT * FROM data ORDER BY strftime('%Y-%m-%d %H%M:%f',timestamp) DESC LIMIT ''' + str(entries) + ';')
    for row in result:
        # Add the info to the data vectors
        timestamp.append(row['timestamp'][11:])
        Period.append(row['Period'])
        Frequency.append(row['Frequency'])
        Pulses.append(row['Pulses'])

    # Return the result with JSON format
    return jsonify(columns=[timestamp,Period,Frequency,Pulses])

if __name__ == "__main__":
    # Run the server for any client IP and in the port 8000
    app.run(host='0.0.0.0',port=8000,debug=True)
