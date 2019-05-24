import socket
import sys
import time
import struct
import msvcrt
import threading

def tcp_client_main(volt1,volt2,actuator_amp,motor_amp):
    def worker():
            
        #create socket
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
        except socket.error:
            print("Failed to connect")
            sys.exit()

        print("Socket Created")
        # specify host and port
        server_address = ('172.29.93.7',5005)
        # unpack tuple
        (host, port) = server_address
        # connect socket to port where server is listening
        s.connect(server_address) 

        print("Socket Connected {} to using IP {}".format(host, port))

        while not event.is_set():
            request = "volt1" 
            try:
                s.sendall(request.encode()) # send request in byte array
            except socket.error:
                print("Did not send successfully")
                sys.exit()

            reply = s.recv(4096) # recieve reply from server

            volt1.value = float(reply.decode()) # unpack byte array inside tuple
            time.sleep(1)

            request = "volt2" 
            try:
                s.sendall(request.encode()) # send request in byte array
            except socket.error:
                print("Did not send successfully")
                sys.exit()

            reply = s.recv(4096) # recieve reply from server

            volt2.value = float(reply.decode()) # unpack byte array inside tuple
            time.sleep(1)

            request = "actuator current"
            try:
                # send request in byte array
                s.sendall(request.encode()) 
            except socket.error:
                print("Did not send successfully")
                sys.exit()
            # recieve reply from server
            reply = s.recv(4096) 
            # unpack byte array inside tuple
            actuator_amp.value = float(reply.decode()) 
            time.sleep(1)

            request = "motor current"
            try:
                # send request in byte array
                s.sendall(request.encode()) 
            except socket.error:
                print("Did not send successfully")
                sys.exit()
            # recieve reply from server
            reply = s.recv(4096) 
            # unpack byte array inside tuple
            motor_amp.value = float(reply.decode()) 
            #print("{:>3.1f}\t{:>5.1f}".format(motor_amp.value,actuator_amp.value))
            time.sleep(1)

            reply = s.recv(4096) # recieve reply from server
            motor_amp.value = float(reply.decode()) # unpack byte array inside tuple
            time.sleep(1)

            print("closing socket") # close socket
            s.close()
            
    def flag(): 
        # wait for keyboard interrupt 'q'
        if msvcrt.getch() == b'q':
            event.set()

    event = threading.Event()

    tflag = threading.Thread(target=flag)
    tworker = threading.Thread(target=worker)

    tflag.start()
    tworker.start()
