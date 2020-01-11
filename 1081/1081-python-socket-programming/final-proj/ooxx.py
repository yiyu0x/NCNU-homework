import socket               
import struct
import random

def is_win(board, sign):
    if board[0] == board[1] == board[2] == sign:
        return True
    if board[3] == board[4] == board[5] == sign:
        return True
    if board[6] == board[7] == board[8] == sign:
        return True
    if board[0] == board[3] == board[6] == sign:
        return True
    if board[1] == board[4] == board[7] == sign:
        return True
    if board[2] == board[5] == board[8] == sign:
        return True
    if board[0] == board[4] == board[8] == sign:
        return True
    if board[2] == board[4] == board[6] == sign:
        return True
    return False

def show_info(board=None):
    if board is None:
        print(
        '''
                          0 | 1 | 2
                          ---------
                          3 | 4 | 5
                          ---------
                          6 | 7 | 8
        ''')
    else:
        print(
        '''
                          {:2} | {:2}| {:2}
                          ------------
                          {:2} | {:2}| {:2}
                          ------------
                          {:2} | {:2}| {:2}
        '''.format(board[0], board[1], board[2], board[3], board[4],
                    board[5], board[6], board[7], board[8]))

def move(board, sign, pos=None):
    if pos is not None:
        board[pos] = sign
    else:
        while True:
            try:
                position = int(input(f'[Your tern] You are {sign} player, input position...'))
                if board[position] in ['O', 'X']:
                    raise Exception('This position has value, try other position.')
                if 0 <= position <= 8:
                    board[position] = sign
                    return position
                else:
                    raise ValueError('Please input number 0 ~ 8.')
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)

def new_game(host, port, player_name, competitor_name):
    board = [str(num) for num in range(0, 9)]
    competitor_sock = socket.socket()
    competitor_sock.connect((host, port))
    competitor_sock.send(player_name.encode())
    print(f'Player [{competitor_name}] playing with you...')
    show_info()
    while True:
        print(f'[{competitor_name} tern] Please waiting...')
        pos = int(competitor_sock.recv(4).decode())
        move(board, 'O', pos)
        show_info(board)
        if is_win(board, 'O'):
            print(f'[{competitor_name}] Win!!!')
            break       
        my_pos = move(board, 'X')
        show_info(board)
        competitor_sock.send(str(my_pos).encode())
        if is_win(board, 'X'):
            print(f'[You({player_name})] Win!!!')
            break
def new_game_p2(player_sock, player_name):
    board = [str(num) for num in range(0, 9)]
    competitor_name = player_sock.recv(64).decode()
    print(f'Player [{competitor_name}] playing with you...')
    show_info()
    while True:
        my_pos = move(board, 'O')
        show_info(board)
        player_sock.send(str(my_pos).encode())
        if is_win(board, 'O'):
            print(f'[You({player_name})] Win!!!')
            break
        print(f'[{competitor_name} tern] Please waiting...')
        pos = int(player_sock.recv(4).decode())
        move(board, 'X', pos)
        show_info(board)
        if is_win(board, 'X'):
            print(f'[{competitor_name}] Win!!!')
            break

def waiting(s, player_name):
    print('Please waiting for other player...') 
    p1 = socket.socket()
    host = socket.gethostname()
    port = random.randint(10000,65535)
    while True:
        try:
            p1.bind((host, port))
        except Exception as e:
            print(e)
            port = random.randint(10000,65535)
        break
    p1.listen(1)
    data = struct.pack('20sI', host.encode(), port)
    s.send(data)
    c, addr = p1.accept()
    new_game_p2(c, player_name)

def main():
    s = socket.socket()        
    host = socket.gethostname() 
    port = 12345              

    player_name = input('What is your name? ')
    s.connect((host, port))
    s.send(player_name.encode())
    print(s.recv(64).decode()) # Welcome MSG

    online_player_str = s.recv(128).decode()
    if online_player_str != 'none':
        print(online_player_str)
    while True:
        try:
            if online_player_str == 'none':
                print('Waiting list is empty.')
                opt = 2
            else:
                opt = int(input('Do you want to chose player [1] or waiting for challenge [2] ? '))
            
            if opt not in [1, 2]:
                raise Exception('Please input (1) or (2).')
            break
        except Exception as e:
            print(e)
    if opt == 1:
        s.send(b'\x01')
        competitor = input('Which player you want to playing with (name)? ') 
        s.send(competitor.encode())
        p1_host, p1_port = struct.unpack('20sI', s.recv(64))
        p1_host = p1_host.decode()
        new_game(p1_host.rstrip('\x00'), p1_port, player_name, competitor)
    elif opt == 2:
        s.send(b'\x02')
        waiting(s, player_name)
    s.close()

main()