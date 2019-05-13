import RPi.GPIO as GPIO
import time
from datetime import datetime
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(10) == False:
        os.system("shutdown now -h")
    time.sleep(5)
