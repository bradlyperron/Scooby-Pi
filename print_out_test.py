import time as t

def print_main(volt1,volt2,actuator_amp,motor_amp):
    print("{:>3}\t{:>3}\t{:>3}\t{:>3}".format('V1','V2','AA','AM'))
    while True:
        print("{:>3.1f}\t{:>3.1f}\t{:>3.1f}\t{:>3.1f}".format(volt1.value,volt2.value,actuator_amp.value,motor_amp.value))
        t.sleep(10)