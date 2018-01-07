T = int(input())
seats = []
for i in range(0, T):
    x = int(input())
    seats.append(x)

for j in range(0, T):
    if seats[j] % 12 is 0:
        seat = seats[j] - 11
        print str(seat) + " WS"
    elif seats[j] % 12 is 1:
        seat = seats[j] + 11
        print str(seat) + " WS"
    elif seats[j] % 12 is 2:
        seat = seats[j] + 9
        print str(seat) + " MS"
    elif seats[j] % 12 is 3:
        seat = seats[j] + 7
        print str(seat) + " AS"
    elif seats[j] % 12 is 4:
        seat = seats[j] + 5
        print str(seat) + " AS"
    elif seats[j] % 12 is 5:
        seat =  seats[j] + 3
        print str(seat) + " MS"
    elif seats[j] % 12 is 6:
        seat = seats[j] + 1
        print str(seat) + " WS"
    elif seats[j] % 12 is 7:
        seat = seats[j] - 1
        print str(seat) + " WS"
    elif seats[j] % 12 is 8:
        seat =seats[j] - 3
        print str(seat) + " MS"
    elif seats[j] % 12 is 9:
        seat = seats[j] - 5
        print str(seat) + " AS"
    elif seats[j] % 12 is 10:
        seat = seats[j] - 7
        print str(seat) + " AS"
    elif seats[j] % 12 is 11:
        seat = seats[j] - 9
        print str(seat) + " MS"
    else:
        print -1
