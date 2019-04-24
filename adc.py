import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np

def adc_main(vin,amp,prim_amp):
    print("adc starting")
    # (R1 + R2)/R2

    resistor_ratio = 4.9305

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)

    # Create single-ended input on channel 0
    chan0 = AnalogIn(ads, ADS.P0) #voltage
    chan1 = AnalogIn(ads, ADS.P1) #primary amp
    chan2 = AnalogIn(ads, ADS.P2) #secondary amp

    a_offset = 2.558
    pa_offset = 2.540
    scale = 0.04
    while True:
        #calculate input voltage and amps
        vin.value = chan0.voltage*resistor_ratio
        i=0
        prim_amp_val = [0]*5
        amp_val = [0]*5

        for i in range(5):
            prim_amp_val[i] = (chan1.voltage-pa_offset)/scale
            amp_val[i] = (chan2.voltage-a_offset)/scale
            time.sleep(0.5)

        amp.value = np.average(amp_val)
        prim_amp.value = np.average(prim_amp_val)
        print("v: {}, a: {}, pa: {}".format(vin.value,amp.value,prim_amp.value))

    print("adc stopping")
