# $Revision: 1.1 $
# -*- coding: UTF-8 -*-
import argparse, socket
import threading
import json
import signal
BUFSIZE = 80
EOF = 'oo'
REGISTRAR_PORT = 12345
THREAD_RUN = True
class Receiver(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        global THREAD_RUN
        while True:
            try:
                data = self.sock.recv(BUFSIZE)
                if data == b'':
                    raise 'error'
                print("💻:", data.decode('UTF-8'))
            except:
                print('\nOther side closed connection.')
                THREAD_RUN = False
                break


class Sender(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        self.sock = sock
    def run(self):
        global THREAD_RUN
        while True:
            if not THREAD_RUN:
                break
            try:
                msg = input('👦:')
            except KeyboardInterrupt:
                print('Ctrl - C!!!')
            else:
                self.sock.send( msg.encode('UTF-8') )
            

def registrar(host, _):
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind((host, REGISTRAR_PORT))
    listeningSock.listen(1)
    print("Im registrar, listening on", listeningSock.getsockname() )
    
    registTab = {}

    # sock, sockname = listeningSock.accept()
    while True:
        sock, sockname = listeningSock.accept()
        dataType = sock.recv(1)
        print(f'debug:{dataType}')
        if dataType == b'\x01': # regist server user
            host, port, name = json.loads(sock.recv(BUFSIZE).decode('UTF-8'))
            registTab[name] = (host, port)
            print(f">> Server '{name}', {host}:{port} was registered.")
        if dataType == b'\x02': # inquery registrar table
            sock.send(json.dumps(registTab).encode('UTF-8'))
        if dataType == b'\x03': # server user close
            name = sock.recv(BUFSIZE).decode('UTF-8')
            print(f'Server "{name}" exit.')
            del registTab[name]

def registUser(host, port, sock):
    name = input('Please input your name... ')
    msg = (host, port, name)
    sock.send( b'\x01' + json.dumps(msg).encode('UTF-8') )
    return name

def server(host, port):
    
    listeningSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listeningSock.bind( (host, port) )
    
    try:
        sockReg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockReg.connect( (host, REGISTRAR_PORT) )
    except:
        print("Connect to rigistrar error!")
        exit()

    name = registUser(host, port, sockReg)
    try:
        listeningSock.listen(1)
        sock, addr = listeningSock.accept()
        
        sender = Sender(sock)
        receiver = Receiver(sock)
        sender.start()
        receiver.start()    

    except:
        print('\nserver side exit.\n')
        sockReg = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockReg.connect( (host, REGISTRAR_PORT) )
        sockReg.send( b'\x03' + name.encode('UTF-8'))
    

def inquery(sock):
    sock.send( b'\x02') # inquery
    data = json.loads( sock.recv( BUFSIZE ).decode('UTF-8') )

    # show users list
    item = 0
    localDic = {}
    for name, socket in data.items(): 
        item += 1
        localDic[item] = [name, socket]
        host, port = socket
        print(f'{item:<2}. {name:<7} -> {host}:{port}')

    userID = int(input('Please choose the user number you want to chat... '))
    # print(f'debug: The User you chose is -> {localDic[userID][0]}')
    return localDic[userID][0], localDic[userID][1][0], localDic[userID][1][1]

def client(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect( (host, REGISTRAR_PORT) )
    except:
        print('Connect to rigistrar error!')
        exit()

    server_name, server_host, server_port = inquery(sock) # return the target socket
    sock.close()

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect( (server_host, server_port) )
    except:
        print(f'Connect to {server_name}-server error!')
        exit()

    print(f'Successful connected to {server_name}')
    

    
    try:
        sender = Sender(sock)
        receiver = Receiver(sock)
        sender.start()
        receiver.start()
    except KeyboardInterrupt:
        sock.send( b'\x00')
        print('Client Side exit.')  
        exit()


if __name__ == '__main__':
    choices = {'client': client, 'server': server, 'registrar': registrar}
    parser = argparse.ArgumentParser(description='Chat over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
