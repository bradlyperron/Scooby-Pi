import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN)

button = GPIO.input(26)

while True:
	if button == 1:
		time.sleep(1)
		if button == 1:
			os.system("shutdown now -h")
	time.sleep(1)
