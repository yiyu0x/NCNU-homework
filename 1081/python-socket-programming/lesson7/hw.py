import argparse, socket, struct, ssl

def client(host, port=1060, cafile):
    purpose = ssl.Purpose.SERVER_AUTH
    context = ssl.create_default_context(purpose, cafile=cafile)
    context.check_hostname = False

    

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))

    ssock = context.wrap_socket(sock, server_hostname=host)

    data = ssock.recv(8)
    num = struct.unpack('>HHHH', data) # bug endian
    print(num)
    sock.close()


if __name__ == '__main__':
    choices = {'client': client}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-c', metavar='cafile', default=None,
                        help='run as client: path to CA certificate PEM file')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.c)