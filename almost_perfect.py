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
    sum_of_divisors = {1:1}
    for i in range(2,len(mark)):
        if mark[i]:
            primes.append(i)
            sum_of_divisors[n] = n+1

    return mark,primes,sum_of_divisors


def bisect(n,p):
    count = 0
    while n%p == 0:
        count += 1
        n /= p
    return count,n

def sum_divisors(n,primes,sum_of_divisors,p_m):
    if n in sum_of_divisors:
        return sum_of_divisors[n]

    sqrt_n = int(math.sqrt(n))
    for p in primes:
        if p>sqrt_n:
            break
        if n%p == 0:
            count,rest = bisect(n,p)
            s_r = sum_divisors(rest,primes,sum_of_divisors,p_m)
            sum_of_divisors[n] = ((p**(count+1) - 1)/(p-1))*s_r
            return sum_of_divisors[n]
    return n+1

def main():
    limit = int(math.sqrt(10**9))
    p_m, primes, sum_of_divisors = sieve(limit)

    for n in sys.stdin:
        n = int(n.strip())
        sum_d = sum_divisors(n,primes,sum_of_divisors,p_m)
        diff = abs(sum_d-n-n)
        print n,
        if diff == 0:
            print "perfect"
        elif diff <= 2:
            print "almost perfect"
        else:
            print "not perfect"

if __name__ == '__main__':
    main()
