cases = int(raw_input())
word1 = []
word2 = []
for i in range(0, cases):
    a, b = raw_input().split()
    word1.append(a)
    word2.append(b)

for j in range(0, cases):
    a = list(word1[j])
    b = list(word2[j])
    test = len(list(set(a) & set(b)))
    if test is len(word1[j]) and len(word2[j]):
        print "YES"
    else:
        print "NO"
