import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

resistor_ratio = 5.04 


# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADC object using the I2C bus
ads = ADS.ADS1115(i2c)

ads.gain = 1
# Create single-ended input on channel 0
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)
# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

#print("{:>5}\t{:>5}\t{:>5}".format('v1','v2','v3'))
print("{:>5}".format('v'))

while True:
    #print("{:>5.3f}\t{:>5.3f}\t{:>5.3f}".format(chan0.voltage,chan1.voltage,chan2.voltage))
    print("{:>5.3f}".format(chan3.voltage))
    time.sleep(1)

