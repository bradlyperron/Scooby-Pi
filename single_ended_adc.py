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
chan = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
# Create differential input between channel 0 and 1
#chan = AnalogIn(ads, ADS.P0, ADS.P1)

print("{:>5}\t{:>5}\t{:>5}\t{:>5}".format('raw', 'a', 'raw', 'v'))

while True:
    v = chan1.voltage*resistor_ratio
    i=0
    val=[0]*5
    for i in range(5):
        val[i]=chan.value
        time.sleep(0.5)
    vals = (val[0]+val[1]+val[2]+val[3]+val[4])/5
    amps = (vals-19080)/(530.0)
    print("{:>5.0f}\t{:>5.1f}\t{:>5.3f}\t{:>5.1f}".format(vals,amps,chan1.voltage,v))
    time.sleep(0.5)

