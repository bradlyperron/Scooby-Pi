import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# (R1 + R2)/R2
resistor_ratio = 4.94 

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)

# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}".format('raw', 'v'))

while True:
    #input voltage to voltage divider
    vin = chan0.voltage*resistor_ratio
    print("{:>5}\t{:>5.3f}".format(chan0.value, chan0.voltage*resistor_ratio))
    time.sleep(0.5)