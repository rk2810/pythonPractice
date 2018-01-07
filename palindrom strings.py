S = str(raw_input())
rev = reversed(S)
if list(S) != list(rev):
    print "NO"
else:
    print "YES"
