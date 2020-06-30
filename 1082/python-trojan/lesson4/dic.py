dic = {}
while True:

	try:
		key, value = input().split()
	except Exception as e:
		break

	value = int(value)
	if key not in dic.keys():
		dic[key] = value
	else:
		dic[key] += value

for key, value in dic.items():
	print(key, value)