import memcache
import random
import datetime

def getRfc(n):
    ''' Retrieve HTML string from the URL '''
    from urllib.request import urlopen
    from urllib.error import HTTPError
    url = "http://ftp.yzu.edu.tw/RFC/in-notes/rfc{}.txt".format(n)
    try:
        txt = urlopen(url).read().decode(errors="ignore")
    except HTTPError as err:
        txt = "{} ({})".format(err, url)
    return txt

def no_cached_get_rfc(n):
	t0 = datetime.datetime.now()
	for i in range(n):
		ran = random.randint(1, 5000)
		txt = getRfc(ran)
		print(f'Number {i + 1:<3d} and Fetch RFC {ran:<5d} ...')
	delta = datetime.datetime.now() - t0
	print(f'[No Cached] Used {delta.seconds} seconds')

def cached_get_rfc(n):
	t0 = datetime.datetime.now()
	for i in range(n):
		ran = random.randint(1, 5000)
		print(f'Number {i + 1:<3d} and Fetch RFC {ran:<5d} ...')
		# if not in cache
		if (not mc.get(str(ran))):
			txt = getRfc(ran)	
			mc.set(str(ran), txt)
	delta = datetime.datetime.now() - t0
	print(f'[Cached] Used {delta.seconds} seconds')

mc = memcache.Client(['127.0.0.1'], debug = True)
cached_get_rfc(50)
no_cached_get_rfc(50)


# mc.add('k1', 'v１') #  如果已经存在，则添加失败
# mc.replace('k1','r1') # 如果ｋｅｙ不存在，则报错
# mc.set('key0', 'fbo') # set　设置一个值，如果存在则修改
# mc.set_multi({'key0': 'fbo1', 'key1': 'fbo2'})
# mc.delete('k1')
# mc.delete_multi(['key0','key1'])