import socket, sys
import threading

MAX_BYTES = 1024

def sender(sock):
    while True:
        try:
            msg = input()
            if msg == 'oo':
                sock.send(b'0x1')
                return
            else:
                sock.send( msg.encode('UTF-8') )
        except:
            exit()

def receiver(sock):
    while True:
        try:
            data = sock.recv(MAX_BYTES)
            if data == b'0x1':
                sock.close()
                return
            else:
                print( data.decode('UTF-8') )
        except:
            exit()

def server(host, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listeningSock.bind( (host, port) )
    listeningSock.listen()
    print("Listening at", listeningSock.getsockname())

    sock, peername = listeningSock.accept()
    s = threading.Thread(target = sender, args=(sock,))
    r = threading.Thread(target = receiver, args=(sock,), daemon=True)
    s.start()
    r.start()
    s.join()
    # r.join()
    sock.close()
    listeningSock.close()
    print('bye')

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )
    print("Connecting from", sock.getsockname(), "to", sock.getpeername())

    s = threading.Thread(target = sender, args=(sock,))
    r = threading.Thread(target = receiver, args=(sock,), daemon=True)
    s.start()
    r.start()
    s.join()
    # r.join()
    sock.close()
    print('bye')

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

if __name__ == "__main__":
    main()

