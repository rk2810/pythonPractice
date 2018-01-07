inputs= int(input())


def calc():
    a, k, n = map(int, raw_input().split())
    dad = k * (n - 1)
    total = a + dad
    print total

for i in range(0, inputs):
    calc()
