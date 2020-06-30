import argparse, socket
import hashlib
import struct
import glob
import os
BUFSIZE = 1024
def server(host, port):

    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen(1)
    print("Listening at", listeningSock.getsockname() )
    print("Waiting to accept a new connection")

    sock, sockname = listeningSock.accept()
    print("We have accepted a connection from ", sockname)
    # print("Socket name: ", sockname)
    # print("Socket peer: ", listeningSock.getsockname() )
   
    raw_data = b''
    # f = open(file_name, "wb")
    while True:
        raw = sock.recv(10)
        if not raw:
            break
        file_name = struct.unpack("10s", raw)[0].decode().rstrip('\x00')
        # print(file_name)
        data = sock.recv(1024)
        # print(data)   

        if not data: 
            break   

        with open(file_name, 'wb') as f:
            f.write(data)

    # f.write(raw_data)
    # f.close()
    # file_size = len(raw_data)
    # print("A {}-byte file is saved as \"{}\" .".format(file_size, file_name))
    # sock.send(bytes(str(file_size), 'utf-8'))
    # sock.close()
    # print("Reply sent, socket closed")

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    while True:
        raw = input('ftp> ')
        if raw == 'quit':
            break

        raw = raw.split()
        cmd = raw[0]
        src = raw[1]
        dst = src if len(raw) == 2 else raw[2]
        if cmd == 'put':
            try:
                with open(src, 'rb') as f:
                    data = f.read()
                    raw = struct.pack('10s', bytes(dst, 'utf-8')) + data
                    sock.sendall(raw)
            except:
                print('Error!')

        elif cmd == 'mput':
            for name in glob.glob(src):
                try:
                    with open(name, 'rb') as f:
                        data = f.read()
                        raw = struct.pack('10s', bytes(os.path.basename(name), 'utf-8')) + data
                        sock.sendall(raw)
                except:
                    print('Error!')

    sock.shutdown(socket.SHUT_RDWR)
    # print('Connected to', sock.getpeername() )

    # f = open(path, "rb")
    # data = f.read()
    # sock.sendall(data)
    # sock.shutdown(socket.SHUT_WR)
    # f.close()
    
    # file_size = sock.recv(4).decode('utf-8')
    # print(f"The server said The file size is {file_size} bytes.")

    # h = hashlib.sha256()
    # with open(path, 'rb') as afile:
    #     buf = afile.read()
    #     h.update(buf)
    # print("[SHA256]", h.hexdigest())

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    # parser.add_argument('file', help='the file that your want to send over tcp or save.')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)