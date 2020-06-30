# ch02_time.py
# Time Server

import socket, sys
import datetime
MAX_BYTES = 1024

def server(host, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()

    print("Listening at", listeningSock.getsockname())
    while True:
        sock, sockname = listeningSock.accept()
        s = datetime.datetime.now().strftime("%a %b %d %H:%M:%S %Y\n")
        sock.send( s.encode('UTF-8') )
        sock.close()

    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    msg = sock.recv(MAX_BYTES).decode('UTF-8')
    print(msg)

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
