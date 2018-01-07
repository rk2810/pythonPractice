x = int(input())
binary = []


def calc():
    week = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    for k in range(0,7):
        if binary[k] is 0:
            if binary[k-1] is not 1:
                pass
            else:
                print week[k-1]
    binary[:] = []

for i in range(0,x):
    z = int(input())
    for j in range(0,7):
        bin = int(input())
        binary.append(bin)
        calc()
