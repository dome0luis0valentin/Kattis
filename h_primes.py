import sys,math

def binary(arry,val):
    low,high,mid = 0,len(arry)-1,(len(arry)-1)/2
    while(high >= low):
        if arry[mid] == val:
            return mid
        elif arry[mid] > val:
            high = mid - 1
        else:
            low = mid + 1
        mid = (high+low)/2
    return mid

def sieve_hprimes(h):
    n = (h-1)/4
    mark = [True for l in xrange(n+1)]
    mark[0] = False
    i = 1
    while( 4*i*i + 2*i <= n ):
        if (mark[i] == True):
            j = 1
            k = 4*i*j + i + j #next multiple
            while (k <= n):
                mark[k] = False
                j += 1
                k = 4*i*j + i + j
        i +=1

    hprimes = []
    for i in xrange(1,len(mark)):
        if mark[i]:
            hprimes.append(4*i+1)
    return hprimes

def semiprime(h_primes,n):
    sp = [0 for i in xrange(n+1)]
    for p1 in h_primes:
        for p2 in h_primes:
            if p2*p1 >= n:
                break
            sp[p1*p2] = 1
    for i in xrange(1,n+1):
        sp[i] += sp[i-1]
    return sp


def main():
    nums = []
    max_n = 0
    for line in sys.stdin:
        n = int(line.strip())
        if n == 0:
            break
        nums.append(n)
        if n > max_n:
            max_n = n

    h_primes =  sieve_hprimes(max_n/5) # divide by first h-prime
    semi_p = semiprime(h_primes,max_n+1)
    for i in nums:
        print i,semi_p[i]

if __name__ == '__main__':
    main()
