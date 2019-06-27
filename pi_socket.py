import socket
import sys
import multiprocessing
import struct
import time
import json

def pi_socket_main(volt1,volt2,motor_amp,actuator_amp,electronics_amp):
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
        with open('/home/pi/logs/{}.json'.format(filename),'r') as f:
            dict = json.loads(f.read())
            return dict[value]

    while True:
        v1 = str(volt1.value)
        v2 = str(volt2.value)
        mc = str(motor_amp.value)
        ac = str(actuator_amp.value)
        ec = str(electronics_amp.value)
        dpt = getJson('transducer','depth')
        tmp = getJson('transducer' ,'temperature')
        dtime = getJson('transducer' ,'time')
        data = [v1,v2,ac,mc,ec,dpt,tmp,dtime]

        pkt = ''
        i = 0
        for i in range(len(data)):
            #package data with format [type,data]
            #might need to change comma deliminator
            pkt += (str(i+1) + ',' + str(data[i]) + ";")
        print(pkt)
        #send encoded data
        s.sendall(pkt.encode())
        time.sleep(1)
    s.close() #close socket
    print("server stopping")
