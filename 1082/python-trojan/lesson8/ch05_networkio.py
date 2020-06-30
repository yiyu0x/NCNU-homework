# Encapsulate nbyte_to_data(),data_to_nbyte to a class NetworkIO
import socket, struct, sys

def server(host, port):
    typename = { int:'int', str:'str', bytes:'bytes', float:'float' }  # dict
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()

    while True:
        sock, sockname = listeningSock.accept()
        handle = NetworkIO(sock)
        while True:
            data = handle.read()
            if not data:
                break
            print('receive', typename[type(data)], \
                repr(data), 'from', sockname)
        sock.close()

    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    handle = NetworkIO(sock)
    handle.write( b'NCNU') 
    handle.write( 'Happy Birthday') 
    handle.write( 5201314) 
    handle.write( 3.1415926535) 

    sock.close()

class NetworkIO:
    def __init__(self, sock):
        self.handle = sock
    def read_handle(self, n):
        return self.handle.recv(n)      # sock.recv(n)
    def write_handle(self, d):
        return self.handle.send(d)      # sock.send(d)
    def data_to_nbyte(self, n):
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
            return result
        elif isinstance(n, float):
            result = b'd' + struct.pack('!d', n)
            return result
        elif isinstance(n, bytes):
            result = b's' + self.data_to_nbyte(len(n)) + n
            return result
        elif isinstance(n, str):
            n = n.encode('UTF-8')
            result = b'c' + self.data_to_nbyte(len(n)) + n
            return result
        raise TypeError('Invalid type: ' + str(type(n)) )
    
    def nbyte_to_data(self):
        size_info = { 'B':1, 'H':2, 'L':4, 'Q':8, 'd':8 }
    
        btag = self.read_raw(1)         # 先讀 1 byte
        if not btag:
            return None
        else:
            tag = btag.decode('UTF-8')
    
        if tag in size_info:                # 根據 B, H, L, Q, d
            size    = size_info[tag]
            bnum    = self.read_raw(size)       # 再讀 1, 2, 4, 8, 8 bytes
            result  = struct.unpack('!' + tag, bnum)[0] 
        elif tag in "sc":
            size    = self.nbyte_to_data()   # recursive 讀出 size
            if size >= 65536:
                raise ValueError('length too long: ' + str(size))
            bstr    = self.read_raw(size)       # 再讀 size 個 bytes
            result  = bstr if tag == 's' else bstr.decode('UTF-8')
        else:
            raise TypeError('Invalid type: ' + tag)
        return result
    def read_raw(self, n):
        return self.read_handle(n)
    def write_raw(self, d):
        return self.write_handle(d)
    def read(self):
        return self.nbyte_to_data()
    def write(self, d):
        byte_data = self.data_to_nbyte(d)
        self.write_raw(byte_data)
    def close_handle(self):
        return self.handle

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

