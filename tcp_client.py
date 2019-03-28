import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
except socket.error:
    print("Failed to connect")
    sys.exit()

print("Socket Created")

server_address = ('localhost',8888) # specify host and port 
(host, port) = server_address

s.connect(server_address) # connect socket to port where server is listening

print("Socket Connected {} to using IP {}".format(host, port))

message = "ayy lmao"

try:
    s.sendall(message.encode())
except socket.error:
    print("Did not send successfully")
    sys.exit()

print("Message Sent Successfully")

reply = s.recv(4096)

print(reply.decode())

print("closing socket")
s.close()