def f(i):
	x = 1
	loop = 1
	while (loop < 10):
		x = (x*x)+ 1
		loop = loop + 1
		if (loop == i):
			break
	return x

print(f(4))

