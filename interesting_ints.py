import sys,bisect

def extend_gcd(a,b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return x, y

def reduce_fib(a,b):
    while (a<0 or b<0 or b<a):
        a,b = b,a+b

    while b>=a and a>0:
        a,b = b-a,a
    #print "->",b, a+b
    return b,a+b

def process(xo,yo,a,b):
    t = ((xo*-1)/b) + 1
    x,y = xo + t*b, yo - t*a
    return x,y

def main():
    fib_seq = [1,1]
    while fib_seq[-1] < 10**9:
        fib_seq.append(fib_seq[-1]+fib_seq[-2])
    sys.stdin.readline()
    for n in sys.stdin:
        n = int(n.strip())
        max_i = bisect.bisect_left(fib_seq,n)
        a,b = 1,n-1
        for i in xrange(max_i):
            x,y = extend_gcd(fib_seq[i],fib_seq[i+1])
            x *=n
            y *=n
            a_,b_ = process(x,y,fib_seq[i],fib_seq[i+1])
            a_,b_ = reduce_fib(a_,b_)

            if(b,a)>(b_,a_):
                a,b = a_,b_

        print a,b


if __name__ == '__main__':
    main()
