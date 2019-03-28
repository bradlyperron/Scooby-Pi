import socket
import sys
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
except socket.error:
    print("Failed to connect")
    sys.exit()

print("Socket Created")

server_address = ('localhost',8888) # specify host and port 
(host, port) = server_address # unpack tuple

s.connect(server_address) # connect socket to port where server is listening

print("Socket Connected {} to using IP {}".format(host, port))

data = "ayy lmao" # data

for i in range (10):

    try:
        s.sendall(data.encode()) # send data in byte array
    except socket.error:
        print("Did not send successfully")
        sys.exit()

    print("data Sent Successfully")

    reply = s.recv(4096) # recieve reply from server

    print(reply.decode()) # print byte array decoded in to a string
    time.sleep(1)
print("closing socket") # close socket
s.close()