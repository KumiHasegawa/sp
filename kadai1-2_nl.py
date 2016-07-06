import sys

argc = len(sys.argv)

if argc == 2:
	try:
		f = open(sys.argv[1], "rU")
	except IOError:
		sys.exit("nl: %s: No such file or directory" % (sys.argv[1]))
elif argc == 1:
	f = sys.stdin
else:
	sys.exit("usage: nl [file]")

i = 1
for line in f:
	if len(line) > 1:
		print i,line,
		i = i + 1
	else:
		print line,
f.close()
