import socket, struct, sys

def data_to_nbyte(n):
    if isinstance(n, int):      # type(n) == int
        if n < (1<<8):      # 0~255
            tag = b'B'
        elif n < (1<<16):   # 256~65535
            tag = b'H'
        elif n < (1<<32):   # 65536~4294967295
            tag = b"L"
        else:               # 4294967296~
            tag = b'Q'
        result = tag + struct.pack('!' + tag.decode(), n)
               # 相當於 struct.pack('!B', n)
        return result
    elif isinstance(n, bytes):
        result = b's' + data_to_nbyte(len(n)) + n
        return result
    elif isinstance(n, str):
        n = n.encode('UTF-8')
        result = b'c' + data_to_nbyte(len(n)) + n
        return result
    elif isinstance(n, float):
        tag = b'd'
        result = tag + struct.pack('!' + tag.decode(), n)
        return result
    raise TypeError('Invalid type: ' + str(type(n)) )

def nbyte_to_data(sock):
    size_info = { 'B':1, 'H':2, 'L':4, 'Q':8, 'd':8 }

    btag = sock.recv(1)         # 先讀 1 byte
    if not btag:
        return None
    else:
        tag = btag.decode('UTF-8')

    if tag in size_info:                # 根據 B, H, L, Q
        size    = size_info[tag]
        bnum    = sock.recv(size)       # 再讀 1, 2, 4, 8 bytes
        result  = struct.unpack('!' + tag, bnum)[0] 
    elif tag in "sc":
        size    = nbyte_to_data(sock)   # recursive 讀出 size
        if size >= 65536:
            raise ValueError('length too long: ' + str(size))
        bstr    = sock.recv(size)       # 再讀 size 個 bytes
        if tag == 's':
            result  = bstr
        else:
            result = bstr.decode('UTF-8')
    else:
        raise TypeError('Invalid type: ' + tag)
    return result

def server(host, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()

    while True:
        sock, sockname = listeningSock.accept()
        while True:
            data = nbyte_to_data(sock)
            if not data:
                break
            if type(data) == int:
                data = 'int ' + str(data)
            elif type(data) == str:
                data = 'str ' + '\'' + data + '\''
            elif type(data) == float:
                data = 'float ' + str(data)
            elif type(data) == bytes:
                data = 'bytes ' + str(data)
            print('receive', data, 'from', sockname)
        sock.close()

    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    sock.send( data_to_nbyte(b'NCNU') )
    sock.send( data_to_nbyte('Happy Birthday') )
    sock.send( data_to_nbyte(5201314) )
    sock.send( data_to_nbyte(3.1415926535) )

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

if __name__ == "__main__":
    main()

