import socket
import sys
import multiprocessing
import struct

def tcp_server_main(vin,amp,prim_amp):
    print("server starting")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
    except socket.error:
        print("Failed to connect")
        sys.exit()

    print("Socket Created")


    #server_address = ('192.168.0.16', 8888) #specify host and port 

    server_address = ('172.29.174.148', 5005) #specify host and port 


    try:
        s.bind(server_address)
    except socket.error:
        print("Binding failed")
        s.close()
        sys.exit()

    print("Socked has been bounded")

    s.listen(2)

    print("Socket is ready")

    conn, addr = s.accept()

    print("Connected with {} : {}".format(addr[0], str(addr[1])))
    
    while True:
        volts = str(vin.value)
        amps = str(amp.value)
        prim_amps = str(prim_amp.value)
        request = conn.recv(1024).decode()
        if request == "voltage":
            conn.sendall(volts.encode()) # send all data in one packet
        elif request == "current":
            conn.sendall(amps.encode())
        elif request == "prim_current":
            conn.sendall(prim_amps.encode())
        elif request:
            print("invalid request")
        else:
            break
    conn.close() #close connection
    s.close() #close socket
    print("server stopping")
