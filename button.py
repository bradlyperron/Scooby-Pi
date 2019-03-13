import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    button = GPIO.input(10)
    
    if button == True:
        time.sleep(1)
        if button == True:
            with open("/home/pi/Documents/programs/rpi-programs/button_log.txt","a") as logf:
                logf.write("%s" % datetime.now())
                logf.write("\tbutton shutdown\n")
            os.system("shutdown now -h")
    time.sleep(1)
