import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

def adc_main(vin,amp):
    print("adc starting")
    # (R1 + R2)/R2
<<<<<<< HEAD
    resistor_ratio = 4.86 
=======
    resistor_ratio = 4.9305
>>>>>>> 67b737a3c6a9599f92bcb8a979505d0c07564a2a

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    # Create single-ended input on channel 0
    chan0 = AnalogIn(ads, ADS.P0)
    chan1 = AnalogIn(ads, ADS.P1)

    while True:
        #calculate input voltage and amps
        vin.value = chan1.voltage*resistor_ratio
        i=0
        val=[0]*5
        for i in range(5):
            val[i]=chan0.value
            time.sleep(0.5)
        vals = (val[0]+val[1]+val[2]+val[3]+val[4])/5
        amp.value = (vals-19340)/(320.0)
        time.sleep(0.5)
    print("adc stopping")
