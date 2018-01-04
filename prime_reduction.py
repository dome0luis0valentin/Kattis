import sys,math

def sieve(n):
    """
    Sieve of Eratosthenes, return primes less than n
    """
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

    return primes,mark

def prime_red(n,primes):
    count_a = 0
    while(True):
        count_a += 1
        new = 0
        sqrt_n = int(math.sqrt(n))
        for p in primes:
            if (p > sqrt_n or n==1):
                break
            count = 0
            while n%p == 0:
                n = n/p
                count += 1
            if count != 0:
                new += p*count
        if n!=1 and new !=0:
            new += n
        if new == 0:
            break
        n = new

    print n,count_a

def main():
    primes,mark = sieve(int(math.sqrt(10**9))+1)
    n = int(sys.stdin.readline().strip())
    while (n!=4):
        prime_red(n,primes)
        n = int(sys.stdin.readline().strip())
if __name__ == '__main__':
    main()
