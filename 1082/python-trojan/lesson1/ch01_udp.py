import socket, sys
MAX_BYTES = 1024

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( (host, port) )
    data, sockname = sock.recvfrom(MAX_BYTES)
    message = data.decode('UTF-8')
    print("Receiving", message, "from", sockname)

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = '105213029'
    data = message.encode('UTF-8')
    sock.sendto(data, (host, port))
    
    # 點名
    # data, sockname = sock.recvfrom(MAX_BYTES)
    # print(data.decode())
    
    

def main():
    if len(sys.argv) != 4:
        print("Usage: ch01_udp.py {server|client} host port")
    else:
        host = sys.argv[2]
        port = int(sys.argv[3])
        if sys.argv[1] == "server":
            server(host, port)
        elif sys.argv[1] == "client":
            client(host, port)
        else:
            print("Usage: ch01_udp.py {server|client} host port")

main()
