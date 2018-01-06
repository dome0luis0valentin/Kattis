import sys,math

def sieve(n):
    mark = [True for i in range(n+1)]
    p=2
    primes = []
    while(p*p <= n ):
        if (mark[p] == True):
            for i in range(2*p,n+1,p):
                mark[i] = False
        p +=1
    for i in xrange(2,n+1):
        if mark[i]:
            primes.append(i)

    return primes

def phi(n,primes):
    phi_final = 1
    for p in primes:
        if n==1:
            break
        if n%p == 0:
            curr_phi = 1
            while(n%p == 0):
                n /= p
                curr_phi *= p
            curr_phi = (curr_phi - curr_phi/p)
            phi_final *= curr_phi
    if n > 1:
        return phi_final*(n-1)
    return phi_final

def exponial(n,m,primes):
    if m == 1:
        return 0
    if n<=5:
        return reduce(lambda a,b : pow(b,a,m), xrange(1,n+1))
    phi_m = phi(m,primes)
    z = exponial(n-1,phi_m,primes) + phi_m
    return pow(n,z,m)

def main():
    n,m = [int(i) for i in sys.stdin.readline().split()]
    primes = sieve(int(math.sqrt(m))+1)
    print exponial(n,m,primes)

if __name__ == '__main__':
    main()
