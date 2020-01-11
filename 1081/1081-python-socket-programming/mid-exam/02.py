'''
=====================================================================\n
1. The server is listening at exam.ipv6.club.tw:8565 with UDP.\n
2. If a client sends a string of student ID (actually, a bytes array,\n   
such as b"106321033") to the server, the server will reply a\n   
message.\n
3. If the student ID belongs to a student enrolled to this class,\n   
the server will reply the name of the student.\n
=====================================================================\n
'''
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'105213029', ('exam.ipv6.club.tw', 8565))
data, addr = sock.recvfrom(2048)
text = data.decode('utf-8')
print('Received: {} from {}'.format(text, addr))
