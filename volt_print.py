import datetime as dt
import time as t
from pathlib import Path

def volt_main(volt1,volt2):
    print("{:>3}\t{:>3}".format('primary','secondary'))
    while True:
        print("{:>3.1f}\t{:>3.1f}".format(volt1.value,volt2.value))
        t.sleep(5)

