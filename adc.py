import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import numpy as np

def adc_main(volt1,volt2,motor_amp,actuator_amp,electronics_amp):
    print("adc starting")

    # (R1 + R2)/R2
    resistor_ratio2 = 6.02
    resistor_ratio1 = 6.0

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1115(i2c)
    ads1 = ADS.ADS1115(i2c, address=0x49)

    # Create single-ended input on channel 1
    chan0a = AnalogIn(ads1, ADS.P0, ADS.P1) #primary battery voltage
    chan0b = AnalogIn(ads, ADS.P0) #secondary battery voltage
    chan1 = AnalogIn(ads, ADS.P1) #electronics current
    chan2 = AnalogIn(ads, ADS.P2) #motor current
    chan3 = AnalogIn(ads, ADS.P3) #actuator current

    electronics_amp_offset = 0.56
    motor_amp_offset = 2.54
    actuator_amp_offset = 0.048
    electronics_scale = 0.185
    actuator_scale = 0.185
    motor_scale = 0.1

    while True:
        #calculate input voltage and current
        #print("v1 raw: {}\t v2 raw: {}".format(chan0a.voltage,chan0b.voltage))
        volt1.value = chan0a.voltage*resistor_ratio1
        volt2.value = chan0b.voltage*resistor_ratio2

	#create arrays to store current measurements
        motor_amp_val = [0]*5
        actuator_amp_val = [0]*5
        electronics_amp_val = [0]*5
        for i in range(5):
            electronics_amp_val[i] = (chan1.voltage-electronics_amp_offset)/electronics_scale
            motor_amp_val[i] = (chan2.voltage-motor_amp_offset)/motor_scale
            actuator_amp_val[i] = (chan3.voltage-actuator_amp_offset)/actuator_scale
            time.sleep(0.25)
        
        motor_amp.value = np.average(motor_amp_val)
        actuator_amp.value = np.average(actuator_amp_val)
        electronics_amp.value = np.average(electronics_amp_val)
        #print("v1: {}\t v2: {}\t ac: {}\t mc: {}\t ec: {}\t".format(volt1.value,volt2.value,actuator_amp.value,motor_amp.value,electronics_amp.value))
        
    print("adc stopping")
