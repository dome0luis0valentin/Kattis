import sys

def f(a_list,n,m):
    c,d = a_list[-2:]
    a_list = a_list[:-2]
    len_a = len(a_list)/2
    res = [[d for i in xrange(n+1)] for j in xrange(m+1)]
    for y in xrange(m+1):
        for x in xrange(n+1):
            if (x>0 and y>0):
                res[y][x] = c
                for i in (2*j for j in xrange(len_a)):
                    ai,bi = a_list[i],a_list[i+1]
                    xi,yi = x-ai, y-bi
                    if (xi > 0 and yi > 0):
                        res[y][x] += res[y-bi][x-ai]
                    else:
                        res[y][x] += d
    return res

def main():
    cases = int(sys.stdin.readline().strip())
    for case in xrange(cases):
        a_list = [int(i) for i in sys.stdin.readline().split()]
        query = [int(i) for i in sys.stdin.readline().split()]
        n,m = max(query[::2]),max(query[1::2])
        look_up = f(a_list,n,m)
        for k in (2*t for t in xrange(len(query)/2)):
            print look_up[query[k+1]][query[k]]
        print

if __name__ == '__main__':
    main()
