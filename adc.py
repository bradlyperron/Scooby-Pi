import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def adc_main(vin):
    print("adc starting")
    # (R1 + R2)/R2
    resistor_ratio = 5.28 

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    # Create single-ended input on channel 0
    chan0 = AnalogIn(ads, ADS.P0)

    while True:
        #calculate input voltage
        vin.value = chan0.voltage*resistor_ratio
        time.sleep(0.5)
    print("adc stopping")