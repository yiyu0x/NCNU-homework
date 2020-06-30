import socket, sys

host = 'midterm.ncnu.net'
port = 1061
MAX_BYTES = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( (host, port) )

message = '105213029'
data = message.encode('UTF-8')
sock.send(data)

data = sock.recv(MAX_BYTES)
message = data.decode('UTF-8')
print("Receiving:", message)

sock.close()