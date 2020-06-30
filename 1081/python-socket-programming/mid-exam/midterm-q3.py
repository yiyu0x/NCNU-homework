import socket, struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('exam.ipv6.club.tw', 5588))
reply = sock.recv(500)
res = struct.unpack('!HHHH', reply)
print('The server said:', res)
sock.close()

for port in res:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('exam.ipv6.club.tw', port))
	reply = sock.recv(500)
	res = struct.unpack('!H', reply)
	print(f'Receiving {res[0]} from exam.ipv6.club.tw:{port}')
	sock.close()
