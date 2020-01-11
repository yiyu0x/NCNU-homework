import socket
import ssl
import sys
import re

website = ['www.google.com',
'www.apple.com',
'www.aws.com']

if len(sys.argv) != 2:
    host = 'www.ipv6.club.tw'
else:
    host = sys.argv[1]
port = socket.getservbyname('https')
address = (host, port)
context = ssl.create_default_context()
with socket.create_connection(address) as sock:
    with context.wrap_socket(sock, server_hostname=host) as ssock:
        # print(ssock.version())
        # cert = ssock.getpeercert()
        # print(cert)     
        #ssock.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
        msg = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(host)
        ssock.sendall( msg.encode() )
        #print(ssock.recv(1024).decode().split("\r\n"))
        data = ssock.recv(1024).decode()
        # print(data)
        result = re.findall("Server: (.*)\r", data)
        if result:
            print(result)
        print(data)
        
#cert = ssl.get_server_certificate(address)
#print(cert)     # This one is also called "certificate", but is
                # different from the one above.
