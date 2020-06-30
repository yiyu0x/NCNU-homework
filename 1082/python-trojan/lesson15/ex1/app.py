import os
import json

def scan_dir(dir):
	if os.path.isdir(dir):
		for filename in os.listdir(dir):
			fullpath = os.path.join(dir, filename)
			yield from scan_dir(fullpath)
	else:
		yield dir

dic = {}
for fn in scan_dir("../"):
	print(fn)
	dic[fn] = (os.path.getsize(fn), os.path.getctime(fn))

with open('previous_status.json', 'w') as outfile:
	json.dump(dic, outfile, indent=4)
