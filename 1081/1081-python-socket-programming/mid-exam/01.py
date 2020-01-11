import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('exam.ipv6.club.tw', 1218))
reply = sock.recv(500).decode()
print('The server said:\n', reply)