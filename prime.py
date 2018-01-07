num = input()
numbers = []
for num in range(0, num):
    if num > 1:
        for i in range(2, num):
            if (num % i) is 0:
                break
        else:
            numbers.append(num)
print(" ".join(str(x) for x in numbers))
