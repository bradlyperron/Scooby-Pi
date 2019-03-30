import socket
import sys
import multiprocessing
import struct

def tcp_server_main(vin):
    print("server starting")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
    except socket.error:
        print("Failed to connect")
        sys.exit()

    print("Socket Created")

    server_address = ('192.168.0.21', 8888) #specify host and port 

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
        request = conn.recv(1024) # check if client wants data
        #print(vin.value) # voltage from adc
        if not request: # if connection is broken, break
            break
        conn.sendall(bytearray(struct.pack("f", vin.value))) # send all data in one packet

    conn.close() #close connection
    s.close() #close socket
    print("server stopping")
