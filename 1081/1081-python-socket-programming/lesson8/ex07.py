import argparse, socket, threading

def worker(sock, sockname):
    print("Connecting from", sockname)
    server_1(sock)
    # socklist.append(sock)
    sock.close()

def client(host, port):
    info = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)[0]
    sock = socket.socket( *info[0:3] )
    sock.connect( info[4] )
    for i in range(3):
        n = input("? ")
        sock.send( n.encode() )
    sock.close()

def server(host, port):
    global sum
    info = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)[0]
    listeningSock = socket.socket( *info[0:3] )
    listeningSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listeningSock.bind( info[4] )
    listeningSock.listen(1)
    print("Listening at", info[4])

    socklist = []
    threadList = []
    for i in range(3):
        sock, sockname = listeningSock.accept()
        threadList.append(threading.Thread(target=worker, args=(sock, sockname)))
        threadList[-1].start()

    for thread in threadList:
    	thread.join()
    print(sum)

def server_1(s):
    global sum
    for i in range(3):
        data = s.recv(1)
        n = int(data.decode())
        print("{} + {}".format(sum, n), end='')
        sum += n
        print(" = {}".format(sum))

if __name__ == '__main__':
    global sum
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Chat over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    sum = 0
    function(args.host, args.p)
