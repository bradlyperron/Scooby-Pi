import socket
import sys
import multiprocessing
import struct

def tcp_server_main(vin,amp):
    print("server starting")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
    except socket.error:
        print("Failed to connect")
        sys.exit()

    print("Socket Created")

<<<<<<< HEAD
    server_address = ('192.168.0.16', 8888) #specify host and port 
=======
    server_address = ('172.29.30.168', 5005) #specify host and port 
>>>>>>> 67b737a3c6a9599f92bcb8a979505d0c07564a2a

    try:
        s.bind(server_address)
    except socket.error:
        print("Binding failed")
        sys.exit()

    print("Socked has been bounded")

    s.listen(2)

    print("Socket is ready")

    conn, addr = s.accept()

    print("Connected with {} : {}".format(addr[0], str(addr[1])))
    
    while True:
        volts = str(vin.value)
        amps = str(amp.value)
        request = conn.recv(1024).decode()
        if request == "voltage":
            conn.sendall(volts.encode()) # send all data in one packet
        elif request == "current":
            conn.sendall(amps.encode())
        elif request:
            print("invalid request")
        else:
            break
    conn.close() #close connection
    s.close() #close socket
    print("server stopping")
