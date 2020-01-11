import argparse, socket
import hashlib

BUFSIZE = 1024
def server(host, port, file_name):

    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen(1)
    print("Listening at", listeningSock.getsockname() )
    print("Waiting to accept a new connection")

    sock, sockname = listeningSock.accept()
    print("We have accepted a connection from ", sockname)
    print("Socket name: ", sockname)
    print("Socket peer: ", listeningSock.getsockname() )
   
    raw_data = b''
    f = open(file_name, "wb")
    while True:
        data = sock.recv(BUFSIZE)
        if not data: 
            break   
        raw_data += data

    f.write(raw_data)
    f.close()
    file_size = len(raw_data)
    print("A {}-byte file is saved as \"{}\" .".format(file_size, file_name))
    sock.send(bytes(str(file_size), 'utf-8'))
    sock.close()
    print("Reply sent, socket closed")

def client(host, port, path):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )
    print('Connected to', sock.getpeername() )

    f = open(path, "rb")
    data = f.read()
    sock.sendall(data)
    sock.shutdown(socket.SHUT_WR)
    f.close()
    
    file_size = sock.recv(4).decode('utf-8')
    print(f"The server said The file size is {file_size} bytes.")

    h = hashlib.sha256()
    with open(path, 'rb') as afile:
        buf = afile.read()
        h.update(buf)
    print("[SHA256]", h.hexdigest())

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    parser.add_argument('file', help='the file that your want to send over tcp or save.')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.file)