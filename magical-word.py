primes = [67, 71, 73, 79, 83, 97, 101, 103, 107, 109, 113]
test_cases = int(raw_input())
for i in range(0, test_cases):
    final = []
    letters = int(input())
    word = raw_input()
    words = list(word)
    for j in range(0, letters):
        z = ord(words[j])
        if z in primes:
            final.append(words[j])
        else:
            add = (min(primes, key=lambda x: abs(x-z)))
            final.append(chr(add))
            print chr(add)
    print ''.join(final)
