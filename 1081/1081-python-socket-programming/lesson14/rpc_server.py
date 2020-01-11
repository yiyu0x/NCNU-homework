def f(a, b):
    return a + b

from xmlrpc.server import SimpleXMLRPCServer
loc = '10.106.39.83'
server = SimpleXMLRPCServer((loc, 1060))
server.register_function(f)
server.serve_forever()
