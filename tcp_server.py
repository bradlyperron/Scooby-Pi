import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create ipv4 tcp socket
except socket.error:
    print("Failed to connect")
    sys.exit()

print("Socket Created")

server_address = ('localhost',8888) #specify host and port 

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
    data = conn.recv(1024) # recieve 1 kb of data at a time
    print("OK. {}".format(data.decode())) # print decoded data in string form
    if not data: # if connection is broken, break
        break
    conn.sendall(data) # send all data in one packet

conn.close() #close connection
s.close() #close socket