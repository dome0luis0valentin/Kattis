import sys
def choose(n,r):
    ans = 1
    for i in xrange(r):
        ans *= (n-i)
        ans /= (i+1)
    return ans

def catalan(n):
    cats = [1]
    for i in xrange(1,n+1):
        cats.append(((4*i-2)*cats[-1])/(i+1))
    return cats

def main():
    lines = int(sys.stdin.readline().strip())
    cats = catalan(5000)
    for n in sys.stdin:
        print cats[int(n.strip())]

if __name__ == '__main__':
    main()
