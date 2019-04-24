import socket
import sys
import time
import struct
import msvcrt
import threading

def tcp_client_main(voltage,amp,prim_amp):
    def worker():

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
        except socket.error:
            print("Failed to connect")
            sys.exit()

        print("Socket Created")

        server_address = ('172.29.174.148',5005) # specify host and port
        #server_address = ('192.168.0.16', 8888) 
        (host, port) = server_address # unpack tuple

        s.connect(server_address) # connect socket to port where server is listening
        #s.close()

        print("Socket Connected {} to using IP {}".format(host, port))

        while not event.is_set():
            request = "voltage" 
            try:
                s.sendall(request.encode()) # send request in byte array
            except socket.error:
                print("Did not send successfully")
                sys.exit()

            reply = s.recv(4096) # recieve reply from server

            voltage.value = float(reply.decode()) # unpack byte array inside tuple
            time.sleep(1)

            request = "current"
            try:
                s.sendall(request.encode()) # send request in byte array
            except socket.error:
                print("Did not send successfully")
                sys.exit()

            reply = s.recv(4096) # recieve reply from server
            amp.value = float(reply.decode()) # unpack byte array inside tuple
            #print("{:>3.1f}\t{:>5.1f}".format(amp.value,voltage.value))
            time.sleep(1)
            
            request = "prim_current"
            try:
                s.sendall(request.encode()) # send request in byte array
            except socket.error:
                print("Did not send successfully")
                sys.exit()

            reply = s.recv(4096) # recieve reply from server
            prim_amp.value = float(reply.decode()) # unpack byte array inside tuple
            #print("{:>3.1f}\t{:>5.1f}".format(amp.value,voltage.value))
            time.sleep(1)

        print("closing socket") # close socket
        s.close()
        
    def flag(): # wait for keyboard interrupt
        if msvcrt.getch():
            event.set()

    event = threading.Event()

    tflag = threading.Thread(target=flag)
    tworker = threading.Thread(target=worker)

    tflag.start()
    tworker.start()