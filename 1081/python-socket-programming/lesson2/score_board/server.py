import socket
import argparse
from time import sleep

MAX_BYTES = 65535

sorce_board = []

def server(port, host):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind((host, port))
	print('Listening on 127.0.0.1:{}'.format(port))
	while True:
		data, addr = sock.recvfrom(MAX_BYTES)
		text = data.decode('utf-8')
		name, score = text.split()
		# add to variable and sotring
		sorce_board.append([name, score])
		sorce_board.sort(key = lambda x: int(x[1]), reverse=True)
		# parse data to string
		tmp = [' '.join(i) for i in sorce_board]
		result = '\n'.join(tmp)
		data = result.encode()
		print(result)
		#
		print(addr)
		sock.sendto(data, addr)


def client(port, host):
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		name, score = input('Please type your name and score. --- ').split()
		text = f'{name} {score}'
		data = text.encode('utf-8')
		sock.sendto(data, (host, port))
		data, addr = sock.recvfrom(MAX_BYTES)
		print(data.decode('utf-8'))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='which host to connect')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p, args.host)