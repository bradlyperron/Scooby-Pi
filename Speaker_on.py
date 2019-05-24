from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory(host='172.29.30.168')
led = LED(20, pin_factory=factory)


led.off()