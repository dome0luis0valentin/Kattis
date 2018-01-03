import sys,math

def f(n,m,p):
    if p==0:
        return 1
    if(n<0):
        return 0
    if n < m:
        return 1
    c = 0
    for i in xrange(p+1):
        c += f(n-m**i,m,i)
    return c

def f_dp(n,m,p):
    # can optimize this by using non-negative values n-m*k, where k is a N# i
    # instead of using all non-negtive numbers <= n as table width
    table = [[0 for i in xrange(n+1)] for j in xrange(p+1)]
    table[0] = [1 for i in xrange(n+1)]
    for x in xrange(1,p+1):
        for y in xrange(n+1):
            if y < m:
                table[x][y] = 1
            else:
                for k in xrange(x+1):
                    new_n = y-m**k
                    if new_n >= 0:
                        table[x][y] += table[k][new_n]
                    else:
                        break
    return table[p][n]

def main():
    sys.stdin.readline()
    for line in sys.stdin:
        k,m,n = [int(i) for i in line.split()]
        max_p = int(math.log(n,m))
        print k,f_dp(n,m,max_p)

if __name__ == '__main__':
    main()
