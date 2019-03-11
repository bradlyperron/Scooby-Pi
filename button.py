import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    button = GPIO.input(10)
    
    if button == True:
        time.sleep(1)
        if button == True:
            os.system("shutdown now -h")
    time.sleep(1)
