import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np
import fileHandler
import json

def adc_main():
    print("adc starting")

    #(R1 + R2)/R2
    resistor_ratio2 = 6.02
    resistor_ratio1 = 6.0

    #Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    #Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)
    ads1 = ADS.ADS1115(i2c, address=0x49)

    #Create single-ended input on channel 1
    chan0a = AnalogIn(ads1, ADS.P0, ADS.P1) #primary battery voltage
    chan0b = AnalogIn(ads, ADS.P0) #secondary battery voltage
    chan1 = AnalogIn(ads, ADS.P1) #electronics current
    chan2 = AnalogIn(ads, ADS.P2) #motor current
    chan3 = AnalogIn(ads, ADS.P3) #actuator current

    #offsets
    electronics_amp_offset = chan1.voltage
    motor_amp_offset = chan2.voltage
    actuator_amp_offset = chan3.voltage
    electronics_scale = 0.185
    actuator_scale = 0.185
    motor_scale = 0.1

    log = {'v1':0.0,'v2':0.0,'mc':0.0,'ac':0.0,'ec':0.0}

    while True:
        #voltage
        log['v1'] = chan0a.voltage*resistor_ratio1
        log['v2'] = chan0b.voltage*resistor_ratio2

	    #current measurement arrays
        mc_vals = []
        ac_vals = []
        ec_vals = []
        
        #calculate average current
        for i in range(99):
            ec_vals.append((chan1.voltage-electronics_amp_offset)/electronics_scale)
            mc_vals.append((chan2.voltage-motor_amp_offset)/motor_scale)
            ac_vals.append((chan3.voltage-actuator_amp_offset)/actuator_scale)
            time.sleep(0.01)

        #store current values
        log['mc'] = np.average(mc_vals)
        log['ac'] = np.average(ac_vals)
        log['ec'] = np.average(ec_vals)

        #log to file
        fileHandler.write('/home/pi/logs/adc.json',json.dumps(log))

    print("adc stopping")
