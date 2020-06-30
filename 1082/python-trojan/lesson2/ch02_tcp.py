# ch02_tcp.py
# Transmission Control Protocol (TCP)

import socket, sys
MAX_BYTES = 1024

def server(host, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()

    print("Listening at", listeningSock.getsockname())
    
    sock, sockname = listeningSock.accept() # 有這行才完成 3-way handshaking.
    
    data = sock.recv(MAX_BYTES)
    message = data.decode('UTF-8')
    print("Receiving", message, "from", sockname)
    sock.close()

    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    message = 'HELLO'
    data = message.encode('UTF-8')
    sock.send(data) # 將資料寫進 OS 緩衝區，UDP 並沒有緩衝區概念
    # OS 有空就會把資料從緩衝區送到 server 端

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
