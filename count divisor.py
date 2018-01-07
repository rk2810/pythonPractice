L, R, K = map(int,raw_input().split())
x = 0
for i in range(L, R+1):
    if i % K is 0:
        x = x + 1
print x
