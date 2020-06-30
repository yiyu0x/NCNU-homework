import socket, sys

MAX_BYTES = 1024
def recv_something():
	data = sock.recv(MAX_BYTES)
	message = data.decode('UTF-8')
	print("Receiving:", message)
	return message

host = 'midterm.ncnu.net'
port = 1062

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( (host, port) )

msg = recv_something()
msg = str(eval(msg)).encode('UTF-8')
sock.send(msg)

recv_something()

sock.close()