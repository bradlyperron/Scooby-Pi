import time
from datetime import datetime
import subprocess

ethf = open("/sys/class/net/eth0/operstate","r")
state = ethf.read()
flag = False

while True:
    ethf = open("/sys/class/net/eth0/operstate","r")
    state = ethf.read()
        
    if state == "down\n":
        if flag == False:
            subprocess.call("sudo systemctl start radioroom.service", shell=True)
            #print('start radioroom\n')
            with open("/home/pi/Desktop/SPLRadioRoom/ethstate.log","a") as logf:
                logf.write("%s" % datetime.now())
                logf.write("\tstart radioroom\n")
            flag = True
        #print('down\n')
        with open("/home/pi/Desktop/SPLRadioRoom/ethstate.log","a") as logf:
            logf.write("%s" % datetime.now())
            logf.write("\tdown\n")        
    
    if state == "up\n":
        if flag == True:
            subprocess.call("sudo systemctl stop radioroom.service", shell=True)
            #print('stop radioroom\n')
            with open("/home/pi/Desktop/SPLRadioRoom/ethstate.log","a") as logf:
                logf.write("%s" % datetime.now())
                logf.write("\tstop radioroom\n")
            flag = False
        #print('up\n')
        with open("/home/pi/Desktop/SPLRadioRoom/ethstate.log","a") as logf:
            logf.write("%s" % datetime.now())
            logf.write("\tup\n")
            
    time.sleep(1)
    
