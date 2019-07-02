import socket
import sys
import struct
import time
import json
import fileHandler

def pi_socket_main(transducer_lock,adc_lock):
    print("server starting")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
    except socket.error:
        print("Failed to connect")
        sys.exit()

    print("Socket Created")


    #specify host and port
    host = '138.68.225.132'
    port = 5050
    #host = 'localhost'
    s.connect((host, port))
    print("connected to {} on port {}".format(host, port))
    #---Legend---#
    #------------#
    #---1 = v1---#
    #---2 = v2---#
    #---3 = ac---#
    #---4 = mc---#
    #---5 = ec---#
    #------------#
    
    def getJson (filename,value,lock):
        
        try:
            data = fileHandler.read('/home/pi/logs/{}.json'.format(filename))
            data = json.loads(data)
            return data[value]
        except:
            return 0.0
        
    while True:
        v1 = "{0:.2f}".format(getJson('adc','v1',adc_lock))
        v2 = "{0:.2f}".format(getJson('adc','v2',adc_lock))
        mc = "{0:.2f}".format(getJson('adc','mc',adc_lock))
        ac = "{0:.2f}".format(getJson('adc','ac',adc_lock))
        ec = "{0:.2f}".format(getJson('adc','ec',adc_lock))
        dpt = getJson('transducer','depth',transducer_lock)
        tmp = getJson('transducer','temperature',transducer_lock)
        dtime = getJson('transducer','time',transducer_lock)
        data = [v1,v2,ac,mc,ec,dpt,tmp,dtime]

        pkt = ''
        i = 0
        for i in range(len(data)):
            #package data with format [type,data]
            #might need to change comma deliminator
            pkt += (str(i+1) + ',' + str(data[i]) + ";")
        #print(pkt)
        #send encoded data
        s.sendall(pkt.encode())
        time.sleep(1)
    s.close() #close socket
    print("server stopping")
