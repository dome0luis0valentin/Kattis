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

    return primes

def find_neighbour(n,primes):
    neighbour = 1
    for p in primes:
        count = 0
        while n%p == 0:
            n = n/p
            count += 1
        if count != 0:
            neighbour *= (count**p)
        if n==1:
            return neighbour
    return neighbour

def main():
    max_n = 1
    nums = []
    for line in sys.stdin:
        n = int(line.strip())
        if max_n < n:
            max_n = n
        nums.append(n)
    primes = sieve(int(math.sqrt(max_n))+1)
    for i in nums:
        print i,find_neighbour(i,primes)

if __name__ == '__main__':
    main()
