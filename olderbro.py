import sys
def sieve(n):
    mark = [True for i in range(n//2 - 1)]
    p=3

    while(p*p <= n):
        if mark[(p//2) - 1]:
            for i in range(p*p,n,2*p):
                mark[i//2 - 1] = False
        p +=2

    primes = [2]
    for i in range(len(mark)):
        if mark[i]:
            primes.append(2*(i+1)+1)
    return primes

primes = sieve(int(10**4.5)+1)

def fin_field_n(n):
    original = n
    p = 0
    for i in primes:
        while (n%i == 0):
            n /= i
        if n != original:
            p = i
            break

    if n!=1:
        if p==0:
            print "yes"
        else:
            print "no"
    else:
        if p==0:
            print "no"
        else:
            print "yes"

def main():
    for i in sys.stdin:
        fin_field_n(int(i.strip()))

if __name__ == '__main__':
    main()
