#######################################################################
### Serial reading Service                                          ###
### Reads the serial info from hardware periodically and writes it  ###
### to a existing database                                          ###
#######################################################################

import dataset
import time
import datetime
import serial

# Use dataset module to connect with the sqlite database and get the table
# object
db = dataset.connect('sqlite:///database/database.db')
table = db['data']

# # Defining properties for the serial connection
# device = serial.Serial(
#     port='/dev/ttyUSB1',
#     baudrate=9600,
#     parity=serial.PARITY_ODD,
#     stopbits=serial.STOPBITS_TWO,
#     bytesize=serial.SEVENBITS)


def readSerial():
    # # Try to open and check if it is open
    # device.open()
    # if device.isOpen():
    #     # Wait until serial device is busy
    #     while (device.inWaiting() == 0):
    #         pass
    #     # Read a line of data
    #     data = device.readline()
    #
    #     # PARSE AND RETURN YOUR DATA HERE

    # Create some fake data for testing purposes
    import random
    a = random.uniform(0, 30)
    b = random.uniform(30, 60)
    c = random.uniform(60, 100)

    # Get the date and time (with 3 decimal milliseconds)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

    # Return an dictionary with the table database schema
    return {'Period': a, 'Frequency': b, 'Pulses': c, 'timestamp': timestamp}

# Main loop will read and insert serial data in the database every 100 ms
if __name__ == "__main__":
    while True:
        table.insert(readSerial())
        time.sleep(0.1)
