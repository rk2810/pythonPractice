N, K, X = map(int, raw_input().split())
members = []
print N, K, X
for i in range(1, N + 1):
    members.append(i)
kill = X % K

