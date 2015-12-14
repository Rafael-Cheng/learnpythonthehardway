def myfunction(n, incr):
    i = 0
    numbers = []
    while i < n:
        print "At the iop i is %d" % i
        numbers.append(i)

        i = i + incr
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
    return numbers

print "The numbers: "

numbers = myfunction(10, 2)

for num in numbers:
    print num
