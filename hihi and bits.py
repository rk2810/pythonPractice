for _ in range(input()):
    x = bin(input())
    x = x[2:]
    x = list(x)
    for i in range(len(x)-1, -1, -1):
        if x[i] is "0":
            x[i] = "1"
            break
    p = "".join(x)
    print int(p, 2)
