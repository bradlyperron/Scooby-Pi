import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np

def adc_main(volt1,volt2,motor_amp,actuator_amp):
    print("adc starting")

    # (R1 + R2)/R2
    resistor_ratio2 = 5.21
    resistor_ratio1 = 3.76

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)
    ads1 = ADS.ADS1115(i2c, address=0x49)

    # Create single-ended input on channel 1
    chan0 = AnalogIn(ads1, ADS.P0, ADS.P1) #primary voltage
    chan1 = AnalogIn(ads, ADS.P1) #secondary voltage
    chan2 = AnalogIn(ads, ADS.P2) #motor current
    chan3 = AnalogIn(ads, ADS.P3) #actuator current

    motor_amp_offset = 2.51
    actuator_amp_offset = 2.39 
    scale = 0.04
    while True:
        #print('ch2: {}'.format(chan2.voltage))
        #print('ch3: {}'.format(chan3.voltage))
        #calculate input voltage and amps
        volt1.value = chan0.voltage*resistor_ratio1
        volt2.value = chan1.voltage*resistor_ratio2
        i=0
        motor_amp_val = [0]*5
        actuator_amp_val = [0]*5

        for i in range(5):
            motor_amp_val[i] = (chan2.voltage-motor_amp_offset)/scale
            actuator_amp_val[i] = (chan3.voltage-actuator_amp_offset)/scale
            time.sleep(0.25)
        
        motor_amp.value = np.average(motor_amp_val)
        actuator_amp.value = np.average(actuator_amp_val)
        #print("motor amp: {}\t actuator amp: {}".format(motor_amp.value,actuator_amp.value))
        #print("motor amp: {}\t actuator amp: {}".format(chan2.voltage,chan3.voltage))
        
    print("adc stopping")
