import socket
import sys
import struct
import time
import json
import fileHandler

def pi_socket_main(volt1,volt2,motor_amp,actuator_amp,electronics_amp,transducer_lock):
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
    
    def getJson (filename,value):
        
        try:
            data = fileHandler.read('/home/pi/logs/{}.json'.format(filename),transducer_lock)
            data = json.loads(data)
            return data[value]
        except:
            return 0.0
        
    while True:
        v1 = "{0:.2f}".format(volt1.value)
        v2 = "{0:.2f}".format(volt2.value)
        mc = "{0:.2f}".format(motor_amp.value)
        ac = "{0:.2f}".format(actuator_amp.value)
        ec = "{0:.2f}".format(electronics_amp.value)
        dpt = getJson('transducer','depth')
        tmp = getJson('transducer','temperature')
        dtime = getJson('transducer','time')
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
