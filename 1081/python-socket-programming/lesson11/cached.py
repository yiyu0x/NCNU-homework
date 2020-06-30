import memcache
mc = memcache.Client(['127.0.0.1', '10.106.29.93'], debug = True)
for i in range(6):
    mc.set(chr(65+i), 'OOXX')
    #sprint(mc.get('hi'))