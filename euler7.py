def IsPrime(x):
    test_number = 1
    numbers = []
    if test_number >= x:
        return False
    while test_number <= x:
        result = x % test_number
        if result == 0 and test_number != 1.0 and test_number != x:
            return False
        if test_number == x:
            return True
        test_number += 1

number = 2
primes = []

while len(primes) < 10001:
    if IsPrime(number) == True:
	primes.append(number)
	print len(primes)
    number += 1
    
print primes[10000]
