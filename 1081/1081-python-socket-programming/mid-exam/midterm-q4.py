import socket, struct, multiprocessing


def job(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('exam.ipv6.club.tw', port))
	reply = sock.recv(128)
	res = struct.unpack('!H', reply)
	print(f'Receiving {res[0]} from exam.ipv6.club.tw:{port}')
	sock.close()

def main():	
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(('exam.ipv6.club.tw', 3333))
	reply = sock.recv(500)
	ports = struct.unpack('!HHHH', reply)
	print('The server said:', ports)

	procs = []
	for port in ports:
		p = multiprocessing.Process(target=job,args=(port, ))
		p.start()
		procs.append(p)

	for proc in procs:
		proc.join()
	# sock.close()

main()

# socks = []
# for port in ports:
# 	socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

# print(socks)
# for i in socks:
# 	print(i)

# for sock, port in enumerate(socks, ports):
	# print(sock, port)
	
	# sock.connect(('exam.ipv6.club.tw', port))
	# reply = sock.recv(500)
	# res = struct.unpack('!H', reply)
	# print(f'Receiving {res[0]} from exam.ipv6.club.tw:{port}')
	# sock.close()
