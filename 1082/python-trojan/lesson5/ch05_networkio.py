import socket, struct, sys

def server(host, port):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()
    while True:
        sock, sockname = listeningSock.accept()
        s = NetworkIO(sock)
        while True:
            data = s.nbyte_to_data()
            if not data:
                break
            print('receive', data, 'from', sockname)
        sock.close()

    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )
    s = NetworkIO(sock)
    sock.send(s.data_to_nbyte(b'NCNU'))
    sock.send(s.data_to_nbyte('Happy Birthday'))
    sock.send(s.data_to_nbyte(5201314))
    sock.send(s.data_to_nbyte(3.1415926535) )

    sock.close()

class NetworkIO:
    def __init__(self, sock):
        self.handle = sock
    
    def read_handle(self, n):
        return self.handle.recv(n)    
    
    def write_handle(self, d):
        return self.handle.send(d)    
    
    def data_to_nbyte(self, n):

        if isinstance(n, int):      
            if n < (1<<8):      
                tag = b'B'
            elif n < (1<<16):   
                tag = b'H'
            elif n < (1<<32):   
                tag = b"L"
            else:               
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
        raise TypeError('Invalid type: ' + str(type(n)))
    
    def nbyte_to_data(self):
        size_info = { 'B':1, 'H':2, 'L':4, 'Q':8, 'd':8 }
    
        btag = self.read_raw(1)        
        if not btag:
            return None
        else:
            tag = btag.decode('UTF-8')
    
        if tag in size_info:                
            size    = size_info[tag]
            bnum    = self.read_raw(size)   
            result  = struct.unpack('!' + tag, bnum)[0] 
        elif tag in "sc":
            size    = self.nbyte_to_data()  
            if size >= 65536:
                raise ValueError('length too long: ' + str(size))
            bstr    = self.read_raw(size)   
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

