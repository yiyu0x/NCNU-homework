import xmlrpc.client

loc = 'http://10.106.39.83:1060'
# server = xmlrpc.client.ServerProxy('http://localhost:1060')
server = xmlrpc.client.ServerProxy(loc)
print(server.f(10, 20, 30))
