import socket              
import struct
import threading

s = socket.socket()     
host = socket.gethostname() 
port = 12345             
s.bind((host, port))     
s.listen(6)     

player_list = {}

def hander_connect2(c, player_name, player_list):
    p1_host, p1_port = struct.unpack('20sI', c.recv(64))
    p1_host = p1_host.decode()
    player_list[player_name] = (p1_host.rstrip('\x00'), p1_port)

def hander_connect1(c, player_name, player_list):
    competitor = c.recv(128).decode()
    print(f'[New Game] {player_name} vs. {competitor}')
    c.send(struct.pack('20sI', player_list[competitor][0].encode(), player_list[competitor][1]))
    del player_list[competitor]

def get_online_player(player_list):
    # print('[debug] get_online_player', player_list)
    if player_list == {}:
        return 'none'
    res = 'Online player list:'
    index = 0
    for player_name in player_list:
        res += '\n' + f'{str(index + 1):2}. ' + player_name
        index += 1
    return res + '\n'

while True:
    c, addr = s.accept()    
    player_name = c.recv(1024).decode()
    c.send(f'Welcome [{player_name}]\n'.encode())
    print(f'New player [{player_name}] coming in...')
    c.send((get_online_player(player_list)).encode())
    opt = c.recv(4)
    if opt == b'\x01':
        t = threading.Thread(target=hander_connect1, args=(c, player_name, player_list))
        t.start()
    elif opt == b'\x02':
        t2 = threading.Thread(target=hander_connect2, args=(c, player_name, player_list))
        t2.start()
c.close()
