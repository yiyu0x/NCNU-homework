import requests

url = 'http://ns10.ipv6.club.tw/~solomon/Lang/PHP/caesar.php'
data = {'plaintext': 'YQDDKOTDUEFYME', 'key': '1'}

for offset in range(26):
	data['key'] = offset
	res = requests.post(url, data=data)	
	title_offset = len('<TITLE> Caesar Cipher </TITLE>') + 1
	print(offset, res.text[title_offset:])