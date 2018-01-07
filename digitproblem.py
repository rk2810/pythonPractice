N, x = map(int,raw_input().split())
array = list(str(N))
for i in range(0, x):
    if array[i] != 9:
        array[i] = 9
    else:
        array[i + 1] = 9
print("".join(str(x) for x in array))
