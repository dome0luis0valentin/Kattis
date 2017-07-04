import sys
n,k = [int(i) for i in sys.stdin.readline().split()]
if 2**k >= n:
    print "Your wish is granted!"
else:
    print "You will become a flying monkey!"
