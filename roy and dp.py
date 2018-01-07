L = int(input())      # Length of Image
N = int(input())      # Number of images
W = []      # Width matrix
H = []      # Height Matrix
for i in range(0,N):
    a, b = raw_input().split(" ")
    W.append(a)
    H.append(b)

for j in range(0, N):
    if int(W[j]) < L or int(H[j]) < L:
        print "UPLOAD ANOTHER"
    elif int(W[j]) > int(H[j]) or int(W[j]) < int(H[j]):
        print "CROP IT"
    else:
        print "ACCEPTED"
