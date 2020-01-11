
#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# http://ipv6.ncnu.org/Course/PythonNetworkProgramming/Code/ch03_tcp_sixteen.py
# Simple TCP client and server that send and receive 16 octets

import argparse, socket

def recvall(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received'
                           ' %d bytes before the socket closed'
                           % (length, len(data)))
        data += more
    return data

def server(interface, port):
    socket_info = socket.getaddrinfo(interface, port)[1] # odd number
    # for i in socket.getaddrinfo(interface, port):
        # print(i)
    listeningSock = socket.socket(*socket_info[0:2])
    # listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # print(socket_info[4][0:2])
    listeningSock.bind(socket_info[4][0:2])
    listeningSock.listen(1)
    print('Listening at', listeningSock.getsockname())
    while True:
        print('Waiting to accept a new connection')
        sock, sockname = listeningSock.accept()
        print('We have accepted a connection from', sockname)
        print('  Socket name:', sock.getsockname())
        print('  Socket peer:', sock.getpeername())
        message = recvall(sock, 16)
        print('  Incoming sixteen-octet message:', repr(message))
        sock.sendall(b'Farewell, client')
        sock.close()
        print('  Reply sent, socket closed')

def client(host, port):
    server_port = 6667
    socket_info = socket.getaddrinfo(host, port)[1] # odd numbe
    sock = socket.socket(*socket_info[0:2])

    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print('Client has been assigned socket name', sock.getsockname())
    sock.sendall(b'Hi there, server')
    reply = recvall(sock, 50)
    print('The server said', repr(reply))
    while True:
        msg = input()
        sock.sendall(msg.encode('utf-8'))
        reply = recvall(sock, 50)
        print('The server said', repr(reply))


    sock.close()

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
