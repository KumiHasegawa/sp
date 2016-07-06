def fb(n):
	fizz = ["Fizz", "", ""]
	buzz = ["Buzz", "", "", "", ""]
	ret1 = n % 3
	ret2 = n % 5
	result = fizz[ret1] + buzz[ret2]
	return result

i = 1
while i <= 20:
	print i, fb(i)
	i = i + 1
