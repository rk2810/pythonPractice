N = int(input())
factorial = 1
if N < 0:
    print 0
elif N is 0:
    print factorial
else:
    for i in range(1,N+1):
        factorial = factorial * i
    print factorial
