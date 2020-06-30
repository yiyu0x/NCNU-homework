import socket, sys, struct

def nbyte_to_data(sock):
    size_info = { 'B':1, 'H':2, 'L':4, 'Q':8 }

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

def recv_something():
    MAX_BYTES = 1024
    data = sock.recv(MAX_BYTES)
    message = data
    print("Receiving:", message)
    return message

host = 'midterm.ncnu.net'
port = 1064

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( (host, port) )

Filename = ''
Filesize = 0
File_content = b''

for i in range(3):
    for counter in range(3):
        data = nbyte_to_data(sock)
        if not data:
            break
        if isinstance(data, str):
            Filename = data
        elif isinstance(data, int):
            Filesize = data
        elif isinstance(data, bytes):
            File_content = data

    with open(Filename, "wb+") as f:
        f.write(File_content)

sock.close()