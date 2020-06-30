import argparse, zmq, time

def server(host = '127.0.0.1', port = 1060):
    if host =='': host = '*'
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.bind(url)
    for i in range(10):
        time.sleep(0.5)
        msg = "Broadcast {}".format(i+1)
        print(msg)
        req = socket.send_string(msg)
    socket.send_string("EOF")

def client(host, port):
    if host =='': host = '*'
    url = "tcp://{}:{}".format(host, port)
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect(url)
    #socket.setsockopt_string(zmq.SUBSCRIBE,'')
    # Without this filter, all messages will be excluded.
    # If the filter string is '', all messages are received.
    # If the filter string is 'a', all messages with prefix 'a' are received.
    # If you run setsockopt() again to add another prefix 'b',
    # messages begins with 'a' or 'b' will be received.

    while True:
        time.sleep(1)
        msg = socket.recv_string();
        print("Message: %s" % msg)
        if msg == "EOF":
            break

if __name__ == '__main__':
    choices = {'client': server, 'server': client}
    parser = argparse.ArgumentParser(description='ZeroMQ Pub/Sub')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)