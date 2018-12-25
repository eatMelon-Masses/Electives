for n in range(100,1000):
	temp =str(n)
	k = int(temp[0])
	j = int(temp[1])
	i = int(temp[2])
	if n == i ** 3 + j ** 3 + k ** 3:
		print(n)
