from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='192.168.0.16')
led = LED(20, pin_factory=factory)


led.on()