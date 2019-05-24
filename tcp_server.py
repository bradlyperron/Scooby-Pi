import socket
import sys
import multiprocessing
import struct

def tcp_server_main(volt1,volt2,motor_amp,actuator_amp):
    print("server starting")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
    except socket.error:
        print("Failed to connect")
        sys.exit()

    print("Socket Created")


    #server_address = ('192.168.0.16', 8888) #specify host and port 

    server_address = ('172.29.93.7', 5005) #specify host and port 


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
        v1 = str(volt1.value)
        v2 = str(volt2.value)
        motor_amps = str(motor_amp.value)
        actuator_amps = str(actuator_amp.value)
        request = conn.recv(1024).decode()
        if request == "volt1":
            conn.sendall(v1.encode()) # send all data in one packet
        elif request == "volt2":
            conn.sendall(v2.encode())
        elif request == "motor current":
            conn.sendall(motor_amps.encode())
        elif request == "actuator current":
            conn.sendall(actuator_amps.encode())
        elif request:
            print("invalid request")
        else:
            break
    conn.close() #close connection
    s.close() #close socket
    print("server stopping")
