import socket
import argparse

MAX_BYTES = 65535

def server(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(('127.0.0.1', port))
	print('Listening on 127.0.0.1:{}'.format(port))
	while True:
		data, addr = sock.recvfrom(MAX_BYTES)
		text = data.decode('ascii')
		print('Received: {} from {}'.format(text, addr))

def client(port):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	text = 'hello, world'
	data = text.encode('ascii')
	remote_addr = '127.0.0.1'
	sock.sendto(data, (remote_addr, port))
	print(sock.getsockname())

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)