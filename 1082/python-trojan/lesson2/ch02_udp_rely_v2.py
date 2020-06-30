import socket, sys
MAX_BYTES = 1024

def server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.sendto( b'ABCABCABCABC', (host, port) )
    # sock.sendto( b'FGH', (host, port) )
    # sock.sendto( b'KLM', (host, port) )

    sock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( (host, port) )
    print("Listening at", sock.getsockname())

    data = sock.recvfrom(9)
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