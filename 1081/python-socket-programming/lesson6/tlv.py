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
   
    # raw_data = b''
    while True:
        raw = sock.recv(4)
        if not raw:
            break
        file_name_len = struct.unpack('i', raw)[0]

        file_name = sock.recv(file_name_len).decode()

        data_len = struct.unpack('i', sock.recv(4))[0]
        data = sock.recv(data_len)

        with open(file_name, 'wb') as f:
            f.write(data)
        # break

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
                    dst_len = len(dst)
                    data_len = len(data)
                    
                    data = bytes('abc', 'utf-8')
                    # cut two section, avoid "struct.pack" do aligment
                    raw = struct.pack(f'I{dst_len}s', dst_len, bytes(dst, 'utf-8')) + struct.pack(f'I{data_len}s', data_len, data)
                    # print(raw)
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