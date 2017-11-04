import sys,bisect

def sieve(n):
    """
    Sieve of Eratosthenes to determine prime numbers less than n
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

    return primes

def next_char(chars):
    if chars[2] == 'Z':
        if chars[1] == 'Z':
            return chr(ord(chars[0])+1)+"AA"
        else:
            return chars[0]+chr(ord(chars[1])+1)+"A"
    else:
        return chars[0:2]+chr(ord(chars[2])+1)

def main():
    primes = sieve(10000)
    prime_len = len(primes)

    for line in sys.stdin:
        chars,num = line.split()
        if line.strip() == 'END 0000':
            return
        index = bisect.bisect_left(primes,int(num))
        index = -1 if index == prime_len else index
        if index == -1:
            chars = next_char(chars)
            index = 0
        next_p = primes[index]
        print (chars+" "+str(next_p).zfill(4))

if __name__ == '__main__':
    main()
