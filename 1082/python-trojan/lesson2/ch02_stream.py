# ch02_stream.py
# Demonstrate that TCP is stream-based instead of message-based

import socket, sys
MAX_BYTES = 1024

def server(host, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()

    print("Listening at", listeningSock.getsockname())
    sock, sockname = listeningSock.accept()
    sock.send( b'A' )
    sock.send( b'B' )
    sock.send( b'C' )
    sock.send( b'D' )
    sock.send( b'EFGHIJKL' )
    sock.close()

    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    for i in range(3):
        data = sock.recv(4)
        print(data)

    sock.close()

def main():
    msg = "Usage: %s {server|client} host port" % sys.argv[0]
    if len(sys.argv) != 4:
        print(msg)
    else:
        host = sys.argv[2]
        port = int(sys.argv[3])
        if sys.argv[1] == "server":
            server(host, port)
        elif sys.argv[1] == "client":
            client(host, port)
        else:
            print(msg)

main()
