cases = int(raw_input())
word1 = []
word2 = []
diff = 0
for i in range(0, cases):
    a = raw_input()
    b = raw_input()
    word1.append(a)
    word2.append(b)

for j in range(0, cases):
    a = list(word1[j])
    b = list(word2[j])
    test = len(list(set(a) & set(b)))