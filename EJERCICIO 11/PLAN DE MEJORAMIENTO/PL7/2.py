#crear un programa que haga de contador y cuando llegue a cierto numero el codigo vuelva a empezar a desarrollarse
x = 0

while x < 10:
	x += 1
	if x == 5 or x == 7:
		continue
	print(x)
