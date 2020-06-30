import os


def scan_dir(dir, res=[]):
	if os.path.isdir(dir):
		for filename in os.listdir(dir):
			fullpath = os.path.join(dir, filename)
			scan_dir(fullpath, res)
		return res
	else:
		res.insert(0, dir)


for fn in scan_dir("../"):
	print(fn, os.path.getsize(fn))