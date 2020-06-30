import socket

MAX_BYTES = 1024
host = 'midterm.ncnu.net'
port = 1065

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect( (host, port) )

dic = {}

raw = ''
while True:
    data = sock.recv(MAX_BYTES)
    if not data: break
    raw += data.decode('ASCII')

raw = raw.split('\n')
del raw[-1]
for ele in raw:
	fruit, amount = ele.split()
	if fruit in dic:
		dic[fruit] += int(amount)
	else:
		dic[fruit] = int(amount)

for key in sorted(dic.keys()):  
     print(key, dic[key]) 
sock.close()  