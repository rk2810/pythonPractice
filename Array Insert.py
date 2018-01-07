array_bound, queries = map(int, raw_input().split())
array = map(int, raw_input().split())


def operate():
    value = 0
    query = map(int, raw_input().split())
    if query[0] is 1:
        index1 = int(query[1])
        index2 = int(query[2])
        array[index1] = index2
        print array

    elif query[0] is 2:
        index1 = int(query[1])
        index2 = int(query[2])
        for i in range(index1, index2+1):
            value = value + array[i]
        print value

for j in range(0, queries):
    operate()
