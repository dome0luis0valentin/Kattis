import sys,time

def n_catalans(n):
    fact = [1]
    for i in xrange(1,2*n+1):
        fact.append(fact[-1]*i)

    ans = 0
    for i in xrange((n+1)/2):
        # using the identity that choose(2n,n)= (2n!)/(n!)**2
        ans += 2*(fact[2*i]/((fact[i]**2)*(i+1))*fact[2*(n-i)]/((fact[n-i]**2)*(n-i+1)))

    ans += (fact[n]/((fact[n/2]**2)*(n/2+1)))**2 if n%2 == 0 else 0
    return ans

def main():
    s = time.time()
    n = int(sys.argv[1])
    print  n_catalans(n)
    print time.time()-s


if __name__ == '__main__':
    main()
