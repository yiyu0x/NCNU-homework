import os


def scan_dir(dir):
	if os.path.isdir(dir):
		for filename in os.listdir(dir):
			fullpath = os.path.join(dir, filename)
			yield from scan_dir(fullpath)
	else:
		yield dir


for fn in scan_dir("../"):
	print(fn, os.path.getsize(fn))