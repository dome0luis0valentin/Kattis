import sys,math

def sieve(n):
    """
    Sieve of Eratosthenes to determine prime factors less than n
    """
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in range(2,len(mark)):
        if mark[i]:
            primes.append(i)
            
    return mark,primes

def main():
    n = int(sys.stdin.readline().strip())
    p_m,primes = sieve(int(math.sqrt(n)))

    for p in primes:
        if n%p == 0:
            print n - (n/p)
            return
    print n-1

if __name__ == '__main__':
    main()
