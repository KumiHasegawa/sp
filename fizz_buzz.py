def fb(n):
	if n % 15 == 0:
		str = 'FizzBuzz'
	elif n % 3 == 0:
		str = 'Fizz'
	elif n % 5 == 0:
		str = 'Buzz'
	else:
		str = ''

	return str

i = 1
while i <= 20:
	print i, fb(i)
	i = i + 1
