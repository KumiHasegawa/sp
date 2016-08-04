import os
import sys

def dirpath(fn):
	argc = len(sys.argv)
	if argc == 2:
		f = sys.argv[1]
		if os.path.exists(f) == False:
			sys.exit("ldir: %s: No such file or directory" % (sys.argv[1]))
	elif argc == 1:
		f='.'
	else:
		sys.exit("usage: ldir [file]")
	return f

fn = ""
flists = os.listdir(dirpath(fn))
for i in flists:
	print i
