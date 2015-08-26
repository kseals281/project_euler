squared = 0
sums = 0

for i in xrange(101):
    sums += i
sums **= 2

for i in xrange(101):
    squared += i**2

print sums - squared
