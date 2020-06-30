# ch05_netapi.py
# Define a class NetAPI to utilize NetworkIO to send/recv data.
import socket, struct, sys

def server(host, port):
    typename = { int:'int', str:'str', bytes:'bytes', float:'float' }  # dict
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    listeningSock.listen()
    print("Listening at", listeningSock.getsockname())

    while True:
        sock, sockname = listeningSock.accept()
        handle = NetAPI(sock)
        while True:
            data = handle.recv_file()   # It will receive a dict (P.5-8,5-24)
            if not data:
                break
            
            fp = open(handle.savePath, "wb")
            fp.write(data[b'FILEBLCK'])
            fp.close()
            print('receive  from {}\n{}'.format(sockname, data))

        sock.close()
        
    listeningSock.close()

def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (host, port) )

    handle = NetAPI(sock)
    handle.send_file('./a.txt')

    sock.close()

def normalize_path(path):
    import re
    res = re.split(r'/|\\|:', path)
    try:
        for ele in res:
            if ele == '..':
                raise ValueError('dangerous')
    except:
        print('dangerous!')
        exit()
    return '/'.join(' '.join(res).split())

class NetAPI:
    # Constants defined in P.5-4
    FILE_TAG_SIZE       = 8
    FILE_END_TAG        = b'FILEEND0'
    FILE_NAME_TAG       = b'FILENAME'
    FILE_SIZE_TAG       = b'FILESIZE'
    FILE_CONTENT_TAG    = b'FILEDATA'
    FILE_ABORT_TAG      = b'FILEABRT'
    FILE_isBLOCK_TAG    = b'FILEBLCK'
    FILE_notBLOCK_TAG   = b'FILENBLK'

    def __init__(self, iHandle=None, oHandle=None):
        if not iHandle:
            iHandle     = b''
        if not oHandle:
            oHandle     = iHandle
        from ch05_networkio import NetworkIO
        self.iHandle    = NetworkIO(iHandle)
        self.oHandle    = NetworkIO(oHandle)
        self.savePath   = './src.txt'       # 存檔目錄
        self.maxSize    = 2147483647            # 最大檔案限制
        self.blockSize  = 4096                  # 區塊大小

    def send_tag(self, tag):    self.oHandle.write_raw(tag)
    def recv_tag(self): return self.iHandle.read_raw(self.FILE_TAG_SIZE)

    def send_data(self, data):  self.oHandle.write(data)
    def recv_data(self): return self.iHandle.read()

    def send_size(self, n):     return self.send_data(n)
    def recv_size(self):
        size = self.recv_data()
        if not isinstance(size, int):   # 檢查類別是否為 int
            raise TypeError('Invalid size type %s' % type(size))
        return size

    def send_name(self, s):     return self.send_data(s)
    def recv_name(self):
        path = self.recv_data()
        if not isinstance(path, str):   # 檢查是否為 str
            raise TypeError('Invalid size type %s' % type(path))
        return path

    def send_content(self, d):  return self.send_data(d)
    def recv_content(self):     return self.recv_data()

    def send_block(self, fd):
        while True:
            block = fd.read(4)
            if block:
                self.send_content(block)
            else:
                self.send_content(self.FILE_END_TAG)
                break

    def send_file(self, path):
        import os
        filename = path
        filesize = os.path.getsize(path)
        fd = open(path, 'rb')
        try:
            self.send_tag(self.FILE_NAME_TAG)
            self.send_name(filename)
            self.send_tag(self.FILE_SIZE_TAG)
            self.send_size(filesize)
            if filesize > 4:
                self.send_tag(self.FILE_isBLOCK_TAG)
                self.send_block(fd)
            else:
                self.send_tag(self.FILE_CONTENT_TAG)
                self.send_content(fd.read())
            self.send_tag(self.FILE_END_TAG)
            return True
        except Exception as e:
            print(str(e))
            self.send_tag(self.FILE_ABORT_TAG)
            return False

    def recv_blocks(self):
        data = b''
        while True:
            block = self.recv_data()
            if block == self.FILE_END_TAG:
                break
            else:
                data += block
            if not data:
                break
        return data

    def recv_file(self):
        result = {}
        while True:
            tag = self.recv_tag()
            if not tag or tag in [self.FILE_END_TAG, self.FILE_ABORT_TAG]: break
            if tag == self.FILE_isBLOCK_TAG:
                data = self.recv_blocks()
            else:
                data = self.recv_data()
            if not data: break
            # print(tag, data)
            if tag == self.FILE_NAME_TAG:
                result[tag] = normalize_path(data)
            else:
                result[tag] = data
        return result

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