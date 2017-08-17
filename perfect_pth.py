import sys,math
from fractions import gcd

def sieve(n):
    mark = [True for i in xrange(n+1)]
    p=2
    while(p*p <= n ):
        if (mark[p] == True):
            for i in xrange(2*p,n+1,p):
                mark[i] = False
        p +=1

    primes = []
    for i in xrange(2,len(mark)):
        if mark[i]:
            primes.append(i)

    return mark,primes

def max_power(n,primes):
    sqrt_n = int(math.sqrt(abs(n)))
    pow_gcd = 0
    for p in primes:
        if p > sqrt_n:
            break
        if n%p == 0:
            count = 0
            while n%p == 0:
                n /= p
                count += 1
            pow_gcd = gcd(pow_gcd,count)

    if pow_gcd==0:
        return 1
    if n < 0:
        while pow_gcd % 2 == 0:
            pow_gcd /= 2
    return pow_gcd

def main():
    limit = int(math.sqrt(2147483647))+1
    mark,primes = sieve(limit)
    for n in sys.stdin:
        n = int(n.strip())
        if n==0:
            break
        print int(max_power(n,primes))

if __name__ == '__main__':
    main()
