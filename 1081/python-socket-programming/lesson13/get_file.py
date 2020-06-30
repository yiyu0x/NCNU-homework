import socket

host = 'nkust.ipv6.club.tw'
port = 80
file = 'index.html'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

payload = 'GET / HTTP/1.1\r\nHost: nkust.ipv6.club.tw\r\n\r\n'

sock.sendall(payload.encode())
reply = sock.recv(1020)
print('The server said', repr(reply))
sock.close()