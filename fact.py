x = 1
N = int(input())
if N is 0:
    print 1
else:
    for i in range(1, N+1):
        x = x * i
print "Factorial of " + str(N) + " is " + str(x)
