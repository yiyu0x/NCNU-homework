import win32api

previous_status = {"CapsLock": 0, "NumLock": 0, "Scroll Lock": 0}

while True:
    status = {}
   
    for k, v in {"CapsLock": 0x14, "NumLock": 0x90, "Scroll Lock": 0x91}.items():
        status[k] = win32api.GetKeyState(v) & 1
    current_status = status
    
    if current_status != previous_status:
        previous_status = current_status
        for k, v in current_status.items():
            print("{}: {}\t".format(k, "ON" if v else "OFF"), end='')
        print()
