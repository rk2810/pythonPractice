length = int(input())
numbers = map(int, raw_input().split())
x = 0
min = min(numbers)
print min
max = max(numbers)
print max
for i in range(min, max):
    if i not in numbers:
        x = 1
        print x
if x > 0:
    print "NO"
else:
    print "YES"
