import os, sys


def draw_dir(dir):
	print(dir)
	scan_dir(dir, -1, '', dir)

def scan_dir(dir, deep=0, fn='', start=''):
	if os.path.isdir(dir):
		if start != dir:
			print('|   '*(deep) + '|')
			print('|   '*deep + '+---' + os.path.basename(dir))
		for filename in os.listdir(dir):
			fullpath = os.path.join(dir, filename)
			scan_dir(fullpath, deep + 1, filename)
	else:
		print('|   '*(deep) + '|')
		print('|   '*(deep) + '+---' + fn)


draw_dir(sys.argv[1])
