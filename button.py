import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)

while True:
    button = GPIO.input(26)
    
    if button == 0:
        time.sleep(1)
        if button == 0:
            os.system("shutdown now -h")
    time.sleep(1)
