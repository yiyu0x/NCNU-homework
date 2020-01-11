import argparse, socket, threading, asyncio
import signal
def get_answer(data):
    d = data.decode().upper().encode()
    return d

def client(host, port):
    info = socket.getaddrinfo(host, port, 0, socket.SOCK_STREAM)[0]
    sock = socket.socket( *info[0:3] )
    sock.connect( info[4] )
    for i in range(3):
        n = input("? ")
        sock.send( n.encode() )
    sock.close()

def server(host, port):
    loop = asyncio.get_event_loop()
    coro = asyncio.start_server(server_1, host, port)
    loop.run_until_complete(coro)
    print(f"Listening at {host} : {port}")
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print('Stopping server')
    finally:
        loop.close()

async def handle_conversation(reader, writer):
    address = writer.get_extra_info('peername')
    print('Accepted connection from {}'.format(address))
    while True:
        data = b''
        more_data = await reader.read(4096)
        if not more_data:
            if date:
                print(f'Client {address} sent {data}')
            else:
                print('Client {} closed socket normally')
            return
        data += more_data
        answer = get_answer(date)
        writer.write(answer)

async def server_1(reader, writer):
    address = writer.get_extra_info('peername')
    print('Accepted connection from {}'.format(address))
    global sum
    for i in range(3):
        data = await reader.read(4096)
        n = int(data.decode())
        print('debug:', n)
        print("{} + {}".format( sum, n), end='')
        sum += n
        print(" = {}".format(sum) )

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