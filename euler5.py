number = 20


while True:
    for i in xrange(1, 21):
	if i == 20:
	    print number, i
	    pause = raw_input('pause')
	if (number % i) != 0:
	    if i > 18:
		print number, i
	    break
    number += 10
    
print number
pause = raw_input('pause')
