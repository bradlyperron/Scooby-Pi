import time
from NMEA0183 import NMEA0183
from datetime import datetime
import json

def transducer_main():

    serial_location = '/dev/ttyUSB0'
    serial_baudrate = 4800
    serial_timeout = 5

    #Provides the required serial device info
    nmea = NMEA0183(serial_location,serial_baudrate,serial_timeout)

    #Starts the serial connection
    nmea.start()
    time.sleep(1)

    #Checks if there is a valid connection
    if nmea.exit == False:
        print('Connection!')
        log = {'depth': 0.0, 'temperature': 0.0, 'time': ''}

        while True:

            #Depth data
            log['depth'] = nmea.data_depth['meters']

            #Weather data
            log['temperature'] = nmea.data_weather['water_temp']
            
            #time
            log['time'] = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

            with open('/home/pi/logs/transducer.json','w') as f:
                json.dump(log,f,indent=4)

            time.sleep(0.1)

        #Quit the NMEA connection
        nmea.quit()

    else:
        print('No connection!')
