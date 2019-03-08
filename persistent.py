import sys

def get_to(n):
    if n<10:
        return n

    prime_fact = [0,0,0,0]
    primes = [2,3,5,7]
    for i in xrange(4):
        p = primes[i]
        while n%p == 0:
            n = n/p
            prime_fact[i] +=1

    if n!=1:
        return False

    final = dict(zip(primes,prime_fact))
    # 8's
    final[8] = final[2]/3
    final[2] = final[2]%3
    # 9's
    final[9] = final[3]/2
    final[3] = final[3]%2
    #6's
    if final[3]>=1 and final[2]>=1:
        final[6] = 1
        final[3] = final[3]-1
        final[2] = final[2]-1
    #4's
    final[4] = final[2]/2
    final[2] = final[2]%2

    #now arrange answer
    result = ""
    for i in sorted(final.keys()):
        result += str(i)*final[i]

    return result

def main():
    for line in sys.stdin:
        n = int(line.strip())
        if n == -1:
            return

        if n<10:
            print 10+n
        elif n>=10:
            val = get_to(n)
            if val and val != "":
                print val.strip()
            else:
                print "There is no such number."

if __name__ == '__main__':
    main()
