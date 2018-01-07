cases = int(raw_input())
product = 1
int_list = [int(x) for x in raw_input().split()]
for i in range(0, cases):
    product = product * int(int_list[i]) % ((10**9) + 7)
print product
