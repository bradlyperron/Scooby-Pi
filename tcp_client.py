import socket
import sys
import time
import struct
import msvcrt
import threading

def tcp_client_main(voltage=0.0):
    def worker():

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
        except socket.error:
            print("Failed to connect")
            sys.exit()

        print("Socket Created")

        server_address = ('192.168.0.21',8888) # specify host and port 
        (host, port) = server_address # unpack tuple

        s.connect(server_address) # connect socket to port where server is listening

        print("Socket Connected {} to using IP {}".format(host, port))

        request = "feed me seymour" 

        while not event.is_set():

            try:
                s.sendall(request.encode()) # send request in byte array
            except socket.error:
                print("Did not send successfully")
                sys.exit()

            reply = s.recv(4096) # recieve reply from server

            (voltage.value,)=(struct.unpack('f',reply)) # unpack byte array inside tuple
            #print(type(voltage))
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